# Hermes 工具链精简记录

> 日期：2026-06-05

## 背景
主子决定精简 Hermes 的桌面操控工具链，只保留 `computer_use` 一个方案。

## 移除的工具

### 1. browser_* 系列（Hermes 内置浏览器）
- `browser_navigate`, `browser_click`, `browser_type` 等
- 操作：通过 `hermes config set toolsets.browser.enabled false` 禁用
- 原因：与 computer_use 功能重叠，且没有登录态

### 2. opencli（第三方 CLI 工具）
- 操作：删除二进制、node_modules、~/.opencli 配置目录、zsh 补全
- 原因：功能被 computer_use 完全覆盖

### 3. cua-driver MCP server
- 操作：从 config.yaml 的 mcp_servers 中移除
- 原因：与内置 computer_use 功能重叠

## 保留的工具
- **`computer_use`** — macOS 桌面操控唯一方案，后台运行不抢焦点

## 配置变更
- `toolsets.browser.enabled: false`
- MCP servers 中移除了 cua-driver
- 辅助 vision 模型设为 `mimo-v2-omni`（解决主模型不支持截图的问题）
