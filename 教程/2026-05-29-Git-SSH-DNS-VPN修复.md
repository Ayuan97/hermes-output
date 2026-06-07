# VPN DNS 劫持导致 Git SSH 连接失败的排障与修复

> 归档时间：2026-05-29 20:00 CST
> 来源会话：`20260529_053245_9501abb4`
> 类型：教程类 / 排障记录

## 问题现象

所有 git push 操作失败，包括：

- `hermes-output` 仓库：`ssh: connect to host github.com port 22: Connection refused`
- `hermes-agent` 仓库：`failed to push some refs`、无写权限报错

同时 AI 早报 cron（09:00）和 GitLab 日报 cron（18:00）生成的 Markdown 文件在本地 commit 成功，但 push 均失败。

## 排查过程

### 第一步：确认 SSH 密钥可用

```bash
ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=accept-new git@140.82.121.4
```
输出：`Hi Ayuan97! You've successfully authenticated` — 密钥本身是好的。

### 第二步：发现 DNS 被劫持

检查 DNS 解析：

```bash
nslookup github.com
```
结果：
```text
Server:   114.114.114.114
Address:  github.com → 198.18.0.59
```
`198.18.0.59` 是 **VPN 内部 IP**，不是 GitHub 的真实 IP。

VPN DNS（114.114.114.114）劫持了 `github.com` 域名，解析到了 VPN 内部地址，导致 SSH 连接被拒绝。

### 第三步：确认真实 IP

```bash
ssh -v -i ~/.ssh/id_ed25519 -p 22 git@140.82.121.4
```
认证成功。GitHub 官方的真实 IP 段之一是 `140.82.121.4`。

## 修复方案

### 1. 修改 `~/.ssh/config`

在文件最顶部添加：

```text
# VPN DNS hijacks github.com → use real IP
Host github.com
    HostName 140.82.121.4
    IdentityFile ~/.ssh/id_ed25519
    StrictHostKeyChecking accept-new
```

### 2. 配置 git 全局使用指定 SSH 密钥

```bash
git config --global core.sshCommand "ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=accept-new"
```

### 3. 为 hermes-output 仓库单独配置（可选）

```bash
cd ~/Desktop/go/hermes-output
git config core.sshCommand "ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=accept-new"
```

### 4. 创建 hermes-agent 的 fork

```bash
# 用 GitHub API 创建 fork
curl -X POST -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.github.com/repos/NousResearch/hermes-agent/forks
```
创建了 `Ayuan97/hermes-agent` 作为 upstream 的 fork，以获得写权限。

## 验证结果

| 操作 | 结果 |
|------|------|
| `git pull --rebase origin main` | ✅ 成功 |
| `git push --dry-run` | ✅ 成功 |
| `git ls-remote` | ✅ 成功 |
| `git push --force --dry-run` | ✅ 成功 |

## 后续影响

- **所有 cron 任务**（AI 早报、GitLab 日报、每日工作总结）现在 push 不会再因认证失败爆红
- **hermes-agent 本地开发**：远程已从上游切换到 fork，可正常推送
- **hermes-output**：SSH 配置修复后自动恢复 push 能力

## 排查清单（如果再次出现）

1. `nslookup github.com` — 检查 DNS 是否又被劫持到 `198.18.0.59`
2. `ssh -T git@github.com` — 测试 SSH 连接是否正常
3. `ssh -i ~/.ssh/id_ed25519 -p 22 git@140.82.121.4` — 绕过 DNS 直连测试
4. `cat ~/.ssh/config` — 确认 github.com Host 块还在
5. `git config core.sshCommand` — 确认 SSH 命令配置正确
