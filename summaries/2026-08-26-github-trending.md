# 🔥 GitHub 趋势速览 — 2026年8月26日（周二）

## 一句话总览

**Claude Code 插件生态全面引爆。** 今天日榜 16 个项目里有 7 个直接围绕 AI Agent / Claude Code 生态，Anthropic 同时上榜官方和社区两个插件仓库，加上 Obsidian+Claude 第二大脑、Karpathy 编程规范、Ponytail 懒狗开发哲学——Claude Code 正在从"工具"变成"平台"。OpenAI Codex 周增 1.1 万 star 稳居周榜第一，终端 AI 编程助手的战争白热化。

---

## 🚀 爆款项目 TOP 5

### 1. freestylefly/awesome-gpt-image-2
🔗 https://github.com/freestylefly/awesome-gpt-image-2
⭐ 17,806 (+1,698/天) | JavaScript

**干什么的：** GPT-Image-2 工业级提示词引擎+模板库，530+ 案例逆向工程，20+ 套模板，还提炼了 Skills 系统。

**为什么火：** GPT-Image-2 出来之后大家都在摸索怎么写好 prompt，这个项目直接把"Prompt as Code"做成了可复用的工程体系，不是简单的 prompt 集合而是带 Skills 的框架。

**对主子的价值：** 如果主子在用 GPT-Image-2 做图，这个仓库的模板和 Skills 系统可以直接拿来用。做视频选题也不错——"逆向工程 530 个案例后的提示词方法论"。

---

### 2. MadsLorentzen/ai-job-search
🔗 https://github.com/MadsLorentzen/ai-job-search
⭐ 35,279 (+1,265/天) | Python

**干什么的：** 基于 Claude Code 的本地 AI 求职框架——自动评估 JD、定制简历、写求职信、准备面试。全部在本地运行，fork 即用。

**为什么火：** 找工作是刚需，AI 辅助求职正好卡在"能大幅提升效率但大家还没用起来"的甜蜜点。Claude Code 做后端让技术人群特别买账。

**对主子的价值：** 值得关注的是它的 Claude Code 集成模式，可以学习怎么把 Claude Code 嵌入到具体工作流里。视频选题："让 AI 帮你投 100 份简历"。

---

### 3. openai/codex
🔗 https://github.com/openai/codex
⭐ 118,111 (+1,181/天, +11,424/周) | Rust

**干什么的：** OpenAI 的轻量级终端编程 agent，对标 Claude Code。

**为什么火：** 周榜第一，日增破千。OpenAI 官方下场做终端 AI 编程工具，Rust 写的，性能拉满。跟 Claude Code 的正面交锋已经开始。

**对主子的价值：** 如果主子在用 Claude Code，值得试试 Codex 做个对比。两个产品的竞争格局也是好选题。

---

### 4. basecamp/omarchy
🔗 https://github.com/basecamp/omarchy
⭐ 31,270 (+1,083/天, +4,601/周) | Shell

**干什么的：** Basecamp（DHH 的公司）出品的 Linux 发行版——"Beautiful, Modern & Opinionated"。

**为什么火：** DHH 光环加持。Basecamp 做 Linux 发行版本身就是话题，"Opinionated"意味着有强烈的设计哲学，跟 Rails 一脉相承。

**对主子的价值：** 如果主子折腾 Linux，可以关注下这个发行版的设计理念。DHH 出品通常有独到的工程哲学值得学习。

---

### 5. DietrichGebert/ponytail
🔗 https://github.com/DietrichGebert/ponytail
⭐ 111,025 (+982/天) | JavaScript

**干什么的：** AI agent 编程规范——"让你的 AI agent 像房间里最懒的高级开发者一样思考。最好的代码是你没写的代码。"

**为什么火：** 11 万 star，说明大家对 AI agent 乱写代码的问题有强烈共鸣。跟 Karpathy-skills（20 万 star）异曲同工——都是在用 CLAUDE.md / 规则文件约束 AI 行为。

**对主子的价值：** 直接用。把 ponytail 的规则文件加到你的项目里，让 AI agent 少写废代码。

---

## 📈 技术趋势洞察

### 🔴 Claude Code 生态大爆发
今天最明显的信号：Anthropic 在一天之内同时推了 `claude-plugins-official`（官方插件目录，3.4 万 star）和 `claude-plugins-community`（社区插件市场，1,750 star）。加上 `claude-obsidian`（Obsidian+Claude 第二大脑）、`andrej-karpathy-skills`（Karpathy 编程规范，20 万 star）、`ponytail`（懒狗开发哲学）——Claude Code 正在从"终端工具"升级为"开发平台"。

这跟 VS Code 当年的路径一样：先做好核心编辑器，然后靠插件生态形成护城河。

### 🟠 AI Agent 记忆/上下文管理成新赛道
- `volcengine/OpenViking`（字节跳动，周增 4,211）：Agent 自演化上下文数据库
- `akitaonrails/ai-memory`（周增 2,073）：跨 agent 厂商的长期记忆方案
- `tinyhumansai/openhuman`（日增 542）：本地优先的"个人超级智能"

Agent 没有记忆就没法真正有用。这个方向正在从"锦上添花"变成"刚需"。

### 🟡 Local-first 持续走强
- `openhuman`：本地记忆
- `AprilNEA/OpenLogi`（周增 7,648）：Rust 写的 Logitech Options+ 替代品，无账号无遥测
- `OpenLogi` 这种"用 Rust 重写臃肿商业软件"的模式越来越受欢迎

### 🔵 Rust 工具链：从"能用"到"好用"
Rust 日榜有 `openhuman`、`codex`、`OpenLogi`、`vaultwarden` 等项目。特别值得注意的是 `OpenLogi`——用 Rust 重写硬件驱动管理软件，说明 Rust 正在渗透到以前不会想到的领域。

### 🟢 AI 求职工具意外走红
`ai-job-search` 日增 1,265 star，35K 总 star。说明：1）就业市场确实紧张；2）AI 辅助工作流的"杀手级应用"可能不在编程领域而在日常刚需。

---

## 💡 值得深挖 TOP 3

### 1. anthropics/claude-plugins-community
🔗 https://github.com/anthropics/claude-plugins-community
**理由：** Claude Code 插件生态刚起步，现在进场贡献插件或学习生态架构，窗口期最好。
**建议：** clone 下来看看插件提交规范和目录结构，考虑为主子的 Hermes Agent 做几个 Claude Code 插件。

### 2. volcengine/OpenViking
🔗 https://github.com/volcengine/OpenViking
**理由：** 字节跳动出品的 Agent 上下文数据库，周增 4,211，定位"统一 Agent 记忆、知识 RAG 和 Skills"。这是 Agent 基础设施级别的项目。
**建议：** 值得 clone 试试，看看能不能整合到现有的 Agent 工作流里，替代自己写的记忆管理。

### 3. tashfeenahmed/freellmapi
🔗 https://github.com/tashfeenahmed/freellmapi
⭐ 20,261 (+500/天) | TypeScript
**理由：** 34 个免费 LLM 提供商、635 个免费模型端点，统一在 OpenAI 兼容的 `/v1` 接口后面。智能路由+自动故障转移。个人实验用太方便了。
**建议：** 开发测试时拿来做免费 API 中转，省 token 费用。

---

## 📅 周榜亮点

### 持续霸榜
- **openai/codex** — 周增 11,424，毫无悬念的周冠。终端 AI 编程赛道的第一名之争。
- **harry0703/MoneyPrinterTurbo** — 周增 9,019，AI 短视频生成工具，持续火爆。中文社区特别活跃。
- **public-apis/public-apis** — 47 万 star 的经典项目，周增 6,747，API 百科。

### 本周新晋黑马
- **AprilNEA/OpenLogi** — 周增 7,648 🚀 Rust 写的 Logitech Options+ 替代品。本地优先、无遥测、无账号。鼠标键盘玩家狂喜。
- **modular/modular** — 周增 2,354，Mojo 语言背后的 Modular 平台。Chris Lattner 的项目总算又有动静了。
- **Tencent/AI-Infra-Guard** — 周增 1,247，腾讯的 AI 红队平台，扫描 Agent/MCP/基础设施的安全漏洞。安全+AI 方向值得关注。

---

## 🎬 视频选题建议

### 选题 1：「Claude Code 插件大战——Anthropic 要建 AI 时代的 App Store？」
Anthropic 同时推官方和社区两个插件仓库，加上 Karpathy-skills（20 万 star）和 Ponytail（11 万 star），Claude Code 生态正在以肉眼可见的速度膨胀。可以做一期"Claude Code 插件生态全景"，讲清楚插件系统怎么运作、目前有什么好玩插件、对开发者意味着什么。

### 选题 2：「OpenAI Codex vs Claude Code——终端 AI 编程谁更强？」
Codex 周增 1.1 万 star 正面硬刚 Claude Code。两个都是 Rust/高性能终端工具，定位几乎完全重合。做一期横向对比评测：安装体验、代码质量、速度、价格、生态，绝对有流量。

---

## 📊 语言分布

| 语言 | 日榜数量 | 代表项目 |
|------|---------|---------|
| Python | 8 | ai-job-search, TradingAgents, claude-obsidian |
| JavaScript | 2 | awesome-gpt-image-2, ponytail |
| Rust | 3 | codex, openhuman, OpenLogi |
| TypeScript | 2 | maka, cloudflare-os |
| Go | 1 | hister |
| Shell | 1 | omarchy |

**Python 仍然是 AI 项目的首选语言，但 Rust 在基础设施/工具链方向的份额明显在涨。**

---

*报告生成时间：2026-08-26 09:00 | 数据来源：GitHub Trending*
