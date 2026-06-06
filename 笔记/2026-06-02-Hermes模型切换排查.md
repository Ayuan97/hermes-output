# Hermes 模型切换排障记录 · 2026-06-02

## 背景

主子想把默认模型从 DeepSeek 切换到 GPT-5.5（通过 openai-codex provider）。

## 遇到的三个问题

### 问题 1：缺少 OAuth 认证

config.yaml 里写了 `model: gpt-5.5` / `provider: openai-codex`，但 Hermes 没有 openai-codex 的 OAuth token，自动 fallback 到 DeepSeek。

**解决：** 直接从 Codex CLI 的本地文件 `~/.codex/auth.json` 导入 token，跳过在线 OAuth 认证（因为 `auth.openai.com` 被墙）。

```bash
# 读取 Codex CLI 的 token
cat ~/.codex/auth.json
# 将 access_token 导入 Hermes auth.json
```

### 问题 2：Token 刷新导致 401

Codex CLI 和 Hermes 共用同一个 OAuth token。Codex CLI 刷新 token 后，旧 token 失效，Hermes 拿着旧 token 请求就返回 401。

**解决：** 每次使用前重新读取 `~/.codex/auth.json` 中的最新 token，不要缓存。

### 问题 3：Endpoint 不匹配

Token 的 JWT `aud`（audience）字段是 `api.openai.com/v1`，但 Hermes 的 openai-codex provider 默认走 `chatgpt.com/backend-api/codex`，endpoint 不匹配导致认证失败。

**解决：** 修改 auth.json 中 openai-codex credential 的 `base_url` 为 `https://api.openai.com/v1`。

```python
import json
path = "~/.hermes/auth.json"
with open(path) as f:
    data = json.load(f)
for cred in data.get("credential_pool", {}).get("openai-codex", []):
    cred["base_url"] = "https://api.openai.com/v1"
with open(path, "w") as f:
    json.dump(data, f, indent=2)
```

## 最终结果

- config.yaml: `model: gpt-5.5` / `provider: openai-codex` ✅
- auth.json: 从 Codex CLI 导入最新 token ✅
- base_url: 改为 `https://api.openai.com/v1` ✅
- 重启 Hermes 后切换到 GPT-5.5 成功

## 经验总结

1. **被墙环境的 OAuth 变通**：直接从本地已有 CLI 工具的 auth 文件导入 token
2. **共享 token 陷阱**：多个工具共享同一 OAuth token 时，刷新会导致其他工具失效
3. **JWT audience 检查**：token 的 `aud` 字段必须与请求的 endpoint 匹配
4. **Fallback 链**：Hermes 的 provider fallback 是 openai-codex → deepseek → alibaba/qwen3.7-max
