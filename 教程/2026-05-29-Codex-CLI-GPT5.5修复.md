# Codex CLI 无法使用 gpt-5.5 的排障与修复

> 归档时间：2026-05-29 08:00 CST  
> 来源会话：`20260528_220341_347550`  
> 类型：教程类 / 排障记录

## 问题现象

本机 Codex CLI 调用失败，原因不是 OAuth 本身失效，而是命令行实际命中的 Codex CLI 版本过旧。

当时 PATH 命中的版本：

```text
/Users/administer/.nvm/versions/node/v22.22.2/bin/codex
codex-cli 0.120.0
```

Hermes / Codex 配置里默认模型是：

```text
gpt-5.5
```

旧版 Codex 报错核心含义：

```text
The 'gpt-5.5' model requires a newer version of Codex
```

## 额外排查结果

手动尝试这些模型名也不可用：

```text
gpt-5
gpt-5.1-codex
```

原因是当前使用的是 **ChatGPT OAuth 账号模式**，这些模型名在该模式下不支持，会报类似：

```text
model is not supported when using Codex with a ChatGPT account
```

## 发现的可用版本

机器里已有较新的 Codex App 内置版本：

```text
/Applications/Codex.app/Contents/Resources/codex
codex-cli 0.133.0
```

该版本可以正常跑 `gpt-5.5`。

## 修复方式

升级全局命令行版 Codex：

```bash
npm install -g @openai/codex@latest
```

升级后命令：

```text
/opt/homebrew/bin/codex
codex-cli 0.134.0
```

## 验证结果

验证命令使用默认 `gpt-5.5`，成功输出 `OK`。

验证到的关键信息：

```text
model: gpt-5.5
provider: openai
auth: ChatGPT OAuth
输出: OK
```

## 后续排查清单

如果以后再次出现 Codex 不可用，先查这几项：

```bash
which -a codex
codex --version
npm view @openai/codex version
```

重点确认：

1. PATH 是否又命中了旧的 nvm 版 `codex`。
2. `/opt/homebrew/bin/codex` 是否存在并靠前。
3. Codex CLI 是否为较新版本。
4. 当前账号是否为 ChatGPT OAuth；如果是，不要随便换成 API 侧模型名。

## 当前结论

截至 2026-05-29，命令行 `codex` 已修复到 v0.134.0，并验证可用 `gpt-5.5`。
