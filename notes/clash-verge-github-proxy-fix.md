# Clash Verge TUN 模式导致 GitHub SSL 连接失败

**日期：** 2026-07-15  
**环境：** macOS, Clash Verge (verge-mihomo), TUN mode (gvisor stack), mixed-port: 7897

## 问题现象

- `curl https://github.com` 报 `SSL_ERROR_SYSCALL`
- `curl https://api.github.com` 同样 SSL 握手失败
- `ping github.com` 正常（解析到 198.18.0.18，即 Clash 的 fake-ip）
- Google 等其他 HTTPS 站点正常
- Python urllib / requests 均报 SSL EOF 错误

## 排查过程

1. **确认 DNS 正常**：github.com 解析到 198.18.0.18（Clash fake-ip 段）
2. **确认系统代理正常**：127.0.0.1:7897，浏览器可以正常访问 GitHub
3. **检查 Clash 节点健康度**：发现代理选择器指向的节点 `alive=False`
   - CreamData AnyTLS 的多国节点大量 offline
   - 日本/台湾节点全部 `alive=False`
   - 加拿大节点 `alive=True`
4. **确认 TUN 模式配置**：
   - TUN enabled, gvisor stack, auto-route
   - dns-hijack: any:53
   - sniffer enabled with parse-pure-ip

## 根因

Clash Verge 的代理选择器（Selector）指向了一个 `alive=False` 的死节点。
TUN 模式下，所有流量（包括 curl/Python 的 HTTPS 请求）被透明代理到该死节点，
导致 TCP 连接建立后 TLS 握手阶段被远端断开（SSL_ERROR_SYSCALL / EOF）。

浏览器不受影响是因为浏览器走了系统 HTTP 代理（127.0.0.1:7897），
代理内部的 fallback 机制会切换到可用节点。

## 解决方法

通过 Clash API 切换代理选择器到存活节点：

```bash
# 查看代理组和节点状态
curl -s --unix-socket /tmp/verge/verge-mihomo.sock   http://localhost/proxies | jq '.proxies | keys'

# 切换到存活节点
curl -s --unix-socket /tmp/verge/verge-mihomo.sock   -X PUT http://localhost/proxies/<GROUP_NAME>   -d '{"name": "<ALIVE_NODE>"}'
```

或直接在 Clash Verge GUI 中手动切换代理组到可用节点。

## 经验教训

- TUN 模式比系统代理模式更"透明"但也更"脆弱"——它不走 fallback，直接用选择器的当前节点
- `SSL_ERROR_SYSCALL` 在 TUN 环境下大概率是代理节点问题，不是目标站点的 SSL 问题
- 排查优先级：节点健康度 → 代理组选择器 → TUN 配置 → DNS 配置
