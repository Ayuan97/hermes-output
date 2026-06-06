# Hermes Agent Config UI 完整调研

> 调研日期：2026-06-05

## 三套配置界面

### 1. Web Dashboard（`hermes dashboard`）
最完整的 config UI，启动方式：
```bash
hermes dashboard          # http://127.0.0.1:9119
hermes dashboard --port 8080 --tui  # 自定义端口 + 浏览器内聊天
```

**Config 页面特性：**
- 表单编辑器，150+ 字段自动从 `DEFAULT_CONFIG` 发现
- 左侧分类 Tab：general / agent / terminal / display / delegation / memory / compression / security / browser / voice / tts / stt / logging / discord / auxiliary
- 字段类型自动推断：bool → toggle, 有 options 的 → dropdown, 其他 → 文本框
- 搜索功能（模糊匹配字段名、描述、分类）
- YAML 模式切换（直接编辑原始 YAML）
- 导入/导出 JSON、重置到默认值（按分类/搜索范围）
- 支持 OAuth 认证（公网上部署时自动启用）

**其他页面：**
- Status（版本、网关状态、活跃会话）
- API Keys（.env 管理，分组：LLM Provider / Tool / Messaging / Agent）
- Sessions（FTS5 全文搜索、展开消息历史、工具调用折叠）
- Logs（agent/errors/gateway，按级别/组件过滤，自动刷新）
- Analytics（Token 用量、费用、每日/每模型统计）
- Cron（创建/暂停/触发/删除定时任务）
- Skills & Toolsets（搜索、分类过滤、开关）

**REST API：** `/api/config`、`/api/config/schema`、`/api/config/defaults`、`/api/env` 等全套 CRUD

### 2. CLI 交互式 Setup Wizard（`hermes setup`）
代码在 `hermes_cli/setup.py`（3455 行），5 个模块化 section：
1. **Model & Provider** — 选 AI 提供商和模型
2. **Terminal Backend** — local/docker/ssh/modal/daytona
3. **Agent Settings** — 迭代次数、压缩、会话重置
4. **Messaging Platforms** — 连接 Telegram/Discord/Slack 等
5. **Tools** — TTS、Web Search、Image Gen 等

可单独运行某 section：`hermes setup model`、`hermes setup gateway` 等

### 3. CLI 命令行配置
```bash
hermes config           # 查看当前配置
hermes config edit      # $EDITOR 打开 config.yaml
hermes config set KEY VAL   # 设置单个值
hermes config path      # 打印配置路径
hermes config check     # 检查缺失/过时配置
hermes config migrate   # 更新配置新选项
hermes model            # 交互式模型/提供商选择器
hermes tools            # 交互式工具开关（curses UI）
```

## Config Schema 机制

**后端（`hermes_cli/web_server.py`）：**
- `_build_schema_from_config()` 遍历 `DEFAULT_CONFIG`，生成 `dot.path → field schema` 字典
- `_SCHEMA_OVERRIDES` 手动定义 dropdown 字段（terminal.backend、tts.provider、approvals.mode 等 14 个）
- `_CATEGORY_MERGE` 合并小分类（privacy→security、telegram→discord 等）
- `_CATEGORY_ORDER` 定义 Tab 排序
- `/api/config/schema` 端点返回 `{fields, category_order}`

**前端（`web/src/pages/ConfigPage.tsx`，660 行）：**
- React 组件，用 `<AutoField>` 根据 schema type 自动渲染对应控件
- `<PluginSlot name="config:top" />` 插件扩展点
- 支持 i18n（中文、日文、韩文、德文等 12 种语言）

## Display 配置体系

**`gateway/display_config.py`：**
- 4 级优先级：`per-platform override > global user > built-in platform default > built-in global default`
- 平台分级：Tier 1 (Telegram/Discord) / Tier 2 (Slack/飞书) / Tier 3 (Signal/微信) / Tier 4 (Email/SMS)
- 可配置项：tool_progress、show_reasoning、streaming、interim_assistant_messages、cleanup_progress 等

## 关键路径

| 内容 | 位置 |
|------|------|
| config.yaml | `~/.hermes/config.yaml` |
| .env (API keys) | `~/.hermes/.env` |
| Web Dashboard 前端 | `web/src/pages/ConfigPage.tsx` |
| Web Dashboard 后端 API | `hermes_cli/web_server.py` |
| Schema 构建 + overrides | `hermes_cli/web_server.py` L290-478 |
| Display 配置解析 | `gateway/display_config.py` |
| Setup Wizard | `hermes_cli/setup.py` |
| CLI 配置管理 | `hermes_cli/config.py` |
| Dashboard 认证 | `hermes_cli/dashboard_auth/` + `plugins/dashboard_auth/nous/` |
