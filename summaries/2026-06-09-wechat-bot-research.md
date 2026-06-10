# 微信群机器人方案调研报告

> 调研日期：2026-06-09
> 调研目的：监控主子的某几个微信群，群里有问题时由 AI 自动回复

---

## 核心结论

**腾讯对个人微信第三方接入限制极严**，这不是技术问题，是腾讯封堵的问题。个人微信群自动回复这条路基本被堵死。

---

## 市面方案对比

| 方案 | Star | 群聊支持 | 稳定性 | 风险 |
|------|------|---------|--------|------|
| **CowAgent** (原chatgpt-on-wechat) | 45.2k | ❌ 个人微信群不支持 | - | - |
| **ChatGPT-On-CS** | 4.1k | ✅ 支持@机器人 | 中 | 商业产品 |
| **wechatbot-webhook** | 2.2k | 有限 | 差（2天掉线） | 已归档 |
| **ComWeChatRobot** | 1.8k | ✅ | 中 | 仅Windows+封号风险 |
| **Wechaty** | 22.8k | ✅ | 中 | 需付费puppet |

---

## 关键发现

### CowAgent（最活跃的开源项目，45.2k star）
- 微信（个人）：✅ 文本/图片/文件/语音，**群聊列为空**
- 企微智能机器人：✅ 全功能，**包括群聊**
- 飞书/钉钉：✅ 全功能，**包括群聊**

### Hermes 当前 iLink Bot 接入情况
- iLink bot 是独立身份（如 `8572f761f905@im.bot`），**不是主子的微信号**
- 普通微信群**邀请不进去**
- iLink **不传递群消息**给网关（腾讯限制）
- 当前配置 `WEIXIN_GROUP_POLICY=disabled`

---

## 可行方案

### 方案1：企业微信群（最推荐）⭐

**优势：**
- 官方 API，稳定可靠
- WebSocket 实时连接，无需公网端口
- `group_policy` 支持 `open`/`allowlist`/`disabled`
- 支持 per-group 白名单，精细控制
- 支持图片、文件、语音、视频

**前提条件：**
1. 企业微信组织账号（免费注册）
2. 在企业微信后台创建 AI Bot

**配置步骤：**
```bash
# 1. 运行设置向导，扫码创建 Bot
hermes gateway setup
# 选择 WeCom，扫码登录

# 2. 配置群白名单（.env）
WECOM_GROUP_POLICY=allowlist
WECOM_GROUP_ALLOWED_USERS=group_id_1,group_id_2

# 3. 启动网关
hermes gateway
```

**群 ID 获取方式：**
- 网关日志会打印收到的群消息，包含 group_id
- 或在企业微信后台查看

### 方案2：飞书群/钉钉群
- 官方支持，稳定
- CowAgent 支持扫码一键接入

### 方案3：基于 web 微信（不推荐）
- wechatbot-webhook 等
- 两天掉一次线，已停止维护

### 方案4：PC 微信 hook（高风险）
- ComWeChatRobot 等
- 仅 Windows，有封号风险

---

## 建议

**推荐走企业微信群路线。** 个人微信群监控真的没法做，腾讯把这条路堵死了。如果主子已经有企业微信账号，可以直接配置 Hermes 的 WeCom 适配器。
