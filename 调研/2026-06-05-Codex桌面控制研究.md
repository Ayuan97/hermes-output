# OpenAI Codex CLI 桌面控制 / Computer Use 调研报告

> 调研日期：2026-06-05

## 一、Codex CLI 的桌面控制能力概览

**Codex CLI 本身不内置桌面控制功能。** 它是一个终端里的编码 agent，核心能力是代码编辑、shell 命令执行、文件操作。桌面/GUI 自动化通过以下三种机制实现：

### 1. Codex Desktop 的内置 Computer Use 插件（官方）
Codex Desktop（桌面版）内置了一组 `openai-bundled` 插件：
- **`browser@openai-bundled`** — 内置浏览器控制
- **`computer-use@openai-bundled`** — 桌面截图 + 鼠标/键盘操作
- **`chrome@openai-bundled`** — 通过 Chrome 扩展配对控制浏览器
- **`latex@openai-bundled`** — LaTeX 渲染

**macOS 上的问题：** 官方 Computer Use 插件在 macOS 上不如 Windows 成熟，且经常出现 "unavailable" 的问题。

### 2. 官方 Skills 系统（Playwright 为主）
OpenAI 官方在 `github.com/openai/skills` 维护了一组 curated skills：
- **`playwright`** — CLI-first 浏览器自动化，通过 `playwright-cli` 驱动真实浏览器
- **`playwright-interactive`** — 通过 `js_repl` 维持持久 Playwright 会话，适合迭代式 UI 调试
- **`screenshot`** — OS 级截图工具

### 3. 社区插件生态

**macOS 方案：**
- **`macuse-mcp`** — MCP server，直接控制 Calendar/Mail/Notes 等 Mac 原生应用 + Computer Use
- **`background-computer-use`** — MCP server，后台驱动 macOS 应用，不抢焦点，支持 ghost cursor
- **`computer-use-plugin`**（dnakov）— Claude Code 插件，macOS 桌面控制

## 二、核心技术栈

| 技术层 | 工具/方法 | 说明 |
|--------|----------|------|
| 浏览器自动化 | Playwright | 官方推荐 |
| 桌面截图 | screencapture (macOS) | screenshot skill |
| 鼠标/键盘 | CGEvent / AX API | 社区插件 |
| UI 元素识别 | macOS Accessibility | 社区插件 |
| 协议层 | MCP (Model Context Protocol) | 统一接口 |

## 三、推荐方案：background-computer-use

GitHub: `Panchangam18/background-computer-use`

核心优势：
- **后台操控不抢焦点** — 你继续用电脑，agent 在后台干活
- **Ghost cursor 可视化** — 半透明幽灵光标，能看到 agent 在哪点击
- **Accessibility API 优先** — 比坐标点击可靠 10 倍
- **多 agent 锁机制** — 多个 agent 共享一台 Mac 时自动串行化
- **一次配置，所有 MCP 客户端通用**

## 四、与 Claude Code 的对比

| 维度 | OpenAI Codex | Claude Code |
|------|-------------|-------------|
| 官方 Computer Use | Codex Desktop 内置插件（Windows 优先） | Anthropic 原生 Computer Use API |
| 浏览器自动化 | Playwright skill（js_repl） | Playwright / MCP 浏览器插件 |
| 原生桌面控制 | 弱，依赖社区插件 | 更成熟 |
| 后台操作 | 官方不支持 | background-computer-use 可后台操控 |

## 五、最佳实践

1. 使用 `playwright-interactive` 而非普通 `playwright`（持久化会话）
2. 优先用 Accessibility API / UI Automation 而非坐标点击
3. 使用 observe→act→observe 循环（每次操作后截图验证）
4. Ghost Cursor 可视化（操作时能看到 agent 在哪里点击）
5. 后台操作不抢焦点
6. 多 Agent 桌面锁（flock 文件锁机制）
