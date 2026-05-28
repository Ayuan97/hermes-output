# Hermes 配置与技能精简记录（2026-05-28）

## 一、回复风格修正

今天确认并修正了一个回复问题：虽然系统要求全程简体中文，但之前回复里保留了太多英文清单和英文标题。

后续规则：

- 说明、判断、分类、建议优先中文。
- 英文只保留必要技术标识符：命令、路径、URL、API 名、模型名、技能原名。
- 技能名第一次出现时加中文解释，例如「代理浏览器技能（`agent-browser`）」。
- 不直接粘贴大段英文工具输出，先理解后用中文总结。
- 发出前自检：一整句几乎全英文时，改成中文表达。

主子也要求回复尽量简洁：普通问题直接给结论和关键操作，除非要求详细展开。

## 二、技能精简

主子判断很多内置技能用不上后，今天执行了技能精简。

### 精简前

- 总数：101 个
- 内置：90 个
- 本地：10 个
- 社区安装：1 个

### 精简后

- 总数：63 个
- 内置：54 个
- 本地：9 个
- 社区安装：0 个

共移除 38 个低频或依赖外部服务的技能。

### 移除清单

- `parallel-deep-research`
- `minecraft-modpack-server`
- `pokemon-player`
- `openhue`
- `godmode`
- `ai-digital-human-video`
- `ascii-art`
- `ascii-video`
- `baoyu-article-illustrator`
- `baoyu-comic`
- `comfyui`
- `design-md`
- `humanizer`
- `ideation`
- `manim-video`
- `p5js`
- `pixel-art`
- `pretext`
- `songwriting-and-ai-music`
- `touchdesigner-mcp`
- `gif-search`
- `heartmula`
- `songsee`
- `spotify`
- `audiocraft-audio-generation`
- `dspy`
- `evaluating-llms-harness`
- `huggingface-hub`
- `llama-cpp`
- `obliteratus`
- `segment-anything-model`
- `serving-llms-vllm`
- `weights-and-biases`
- `airtable`
- `linear`
- `teams-meeting-pipeline`
- `polymarket`
- `research-paper-writing`

### 备份和归档

完整备份：

```text
/Users/administer/.hermes/backups/skills-before-prune-20260528-004220.tar.gz
```

移出技能归档：

```text
/Users/administer/.hermes/skill-archive/.removed-by-agent/20260528-004220
```

如果以后发现误删，可以从归档恢复。

## 三、界面清爽 + 高推理配置

主子要求「界面清爽一点，但推理强度改成高」，已修改并验证配置。

当前配置：

```yaml
agent.reasoning_effort: high
agent.verbose: false
display.tool_progress: new
display.tool_preview_length: 0
display.cleanup_progress: true
display.show_reasoning: false
display.show_cost: false
agent.gateway_notify_interval: 300
```

含义：

- 默认推理强度：高。
- 工具进度：只显示新动作。
- 工具内容预览：关闭。
- 思考内容：不展示。
- 费用：不展示。
- 任务完成后清理进度消息：开启。
- 长任务提醒：每 300 秒一次。
- verbose：关闭。

执行过的配置命令：

```bash
hermes config set agent.reasoning_effort high
hermes config set display.tool_progress new
hermes config set display.tool_preview_length 0
hermes config set display.cleanup_progress true
hermes config set display.show_reasoning false
hermes config set display.show_cost false
hermes config set agent.gateway_notify_interval 300
hermes config set agent.verbose false
```

随后执行了网关重启：

```bash
hermes gateway restart
```

重启后确认 gateway 服务已加载，新进程 PID 当时为 `69544`，日志路径：

```text
/Users/administer/.hermes/logs/gateway.log
```

## 四、保留方向

精简后保留更贴近主子工作流的方向：

- 编码：Claude Code、Codex、调试、测试、代码审查。
- Hermes 配置和技能市场。
- GitHub / GitLab 工作流。
- Telegram / gateway / 自动化相关。
- 浏览器和 macOS 后台操控。
- 文档、OCR、PPT、Notion、Google Workspace。
- 公司日报。
- 架构图、信息图、设计草图。
- 搜索研究和社区研究。
