# 🔥 今日 GitHub 趋势速览（2025-06-24）

## 一句话总览

**AI Agent 工具链全面霸榜。** 今天 GitHub Trending 里超过 70% 的项目都跟 AI Agent 相关——Skills、插件、安全扫描、代码记忆、视频制作、语音克隆……开发者们正在疯狂给 Agent「造零件」。

---

## 🚀 爆款项目 TOP 5

### 1. [OpenMontage](https://github.com/calesthio/OpenMontage) — ⭐+3,592/day
**一句话：** 全球首个开源 AI 视频制作系统，12 条流水线、52 个工具、500+ Agent 技能。
**为什么火：** 把 AI coding assistant 变成完整的视频制作团队，从脚本到剪辑一条龙。解决了「AI 能写代码但做不了视频」的痛点。
**对主子的价值：** 强烈推荐 clone 试试，直接能用来做视频内容。非常适合做一期视频选题——「用 AI Agent 自动做视频」。

### 2. [palmier-pro](https://github.com/palmier-io/palmier-pro) — ⭐+1,630/day
**一句话：** 专为 AI 打造的 macOS 视频编辑器。
**为什么火：** 把 AI 能力直接嵌入视频编辑流程，Swift 原生 macOS 应用，体验应该很流畅。
**对主子的价值：** macOS 用户直接可用，视频制作相关项目值得关注。

### 3. [codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) — ⭐+1,300/day（周榜 ⭐+8,536/week）
**一句话：** 高性能代码知识图谱 MCP 服务器，毫秒级索引整个代码仓库，支持 158 种语言。
**为什么火：** MCP 生态的核心基础设施项目。解决了 AI Agent 理解大型代码库的痛点——不用每次重新读文件，直接查知识图谱。
**对主子的价值：** 直接有用。如果你在用 Claude Code 或 Hermes Agent 处理大项目，这个 MCP 服务器能显著提升代码理解能力。

### 4. [voicebox](https://github.com/jamiepine/voicebox) — ⭐+1,045/day（周榜 ⭐+2,883/week）
**一句话：** 开源 AI 语音工作室——声音克隆、语音输入、语音生成。
**为什么火：** 一站式语音 AI 工具，开源免费，替代 ElevenLabs 等付费方案。
**对主子的价值：** 做视频配音、播客、语音内容都能用。值得 clone 试试。

### 5. [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) — ⭐+826/day
**一句话：** 一条命令用 AI 克隆任意网站。
**为什么火：** 「给我一个 URL，AI 帮你还原整个页面」，对前端开发者和快速原型制作极有价值。
**对主子的价值：** 可以用来快速复刻参考网站、做前端原型，效率工具。

---

## 📈 技术趋势洞察

### Agent Skills / 插件生态全面爆发
- **周榜冠军 [skills](https://github.com/mattpocock/skills)**（⭐+11,784/week）：Matt Pocock 的 Claude Code 技能集，说明「给 Agent 写 Skills」已经成为新的开发范式。
- **[agent-skills](https://github.com/addyosmani/agent-skills)**（⭐+5,073/week）：Addy Osmani 的生产级 Agent 技能。
- **[claude-plugins-official](https://github.com/anthropics/claude-plugins-official)**：Anthropic 官方插件目录上线，意味着插件生态正式进入官方支持阶段。
- **[gstack](https://github.com/garrytan/gstack)**（⭐+1,011/day）：Y Combinator CEO Garry Tan 的 Claude Code 配置，23 个工具覆盖 CEO、设计师、工程经理等角色。

**信号：** Agent Skills/Plugins 正在成为像 npm 包一样的新分发单元。

### MCP 生态持续增长
- codebase-memory-mcp 周增 8,536 star，成为 MCP 生态最热项目
- AWS 官方也推出了 [agent-toolkit-for-aws](https://github.com/anthropics/agent-toolkit-for-aws)

### AI + 视频制作是新热点
- OpenMontage（视频制作 Agent）、palmier-pro（AI 视频编辑器）、[OpenCut](https://github.com/OpenCut-app/OpenCut)（开源 CapCut 替代品，周增 3,283）、[hyperframes](https://github.com/nicholasgriffintn/hyperframes)（HTML 渲染视频，⭐+753/day）
- 视频制作工具链正在被 AI 重构

### Rust 稳健上升
- [iroh](https://github.com/n0-computer/iroh)（⭐+1,531/week）：Rust 模块化网络栈，用密钥代替 IP 地址
- [turso](https://github.com/tursodatabase/turso)（⭐+698/day）：Rust 实现的 SQLite 兼容数据库
- Rust 在基础设施领域持续扩张

### 安全方向开始受关注
- [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)（⭐+1,041/day）：817 个网络安全 Agent 技能
- [SkillSpector](https://github.com/NVIDIA/SkillSpector)（⭐+2,849/week）：NVIDIA 出品的 Agent 技能安全扫描器
- Agent 安全正在成为独立赛道

---

## 💡 值得深挖 TOP 3

### 1. [codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)
**理由：** MCP 生态基础设施级项目，周增 8,536 star 不是偶然。解决了 AI 理解大型代码库的核心痛点。
**建议：** 立即 clone 试用，集成到 Hermes Agent 或 Claude Code 工作流中。

### 2. [OpenMontage](https://github.com/calesthio/OpenMontage)
**理由：** 开源 AI 视频制作系统的开创性项目，500+ Agent 技能的设计思路值得学习。
**建议：** clone 研究架构，非常适合做一期深度视频——「开源 AI 视频生产线长什么样」。

### 3. [Agent-Reach](https://github.com/Panniantong/Agent-Reach)
**理由：** 周增 6,915 star。一条命令让 Agent 能读取 Twitter、Reddit、YouTube、B站、小红书等平台内容，零 API 费用。
**建议：** 舆情监控、竞品分析、内容采集都能用，实用性极强。

---

## 📅 周榜亮点

### 持续霸榜
- **[skills](https://github.com/mattpocock/skills)**（⭐+11,784/week）：Agent Skills 赛道的标杆项目
- **[OpenMontage](https://github.com/calesthio/OpenMontage)**（⭐+9,410/week）：AI 视频赛道的当红炸子鸡
- **[codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)**（⭐+8,536/week）：MCP 基础设施

### 本周新晋黑马
- **[Agent-Reach](https://github.com/Panniantong/Agent-Reach)**（⭐+6,915/week）：Agent 互联网访问利器
- **[agent-skills](https://github.com/addyosmani/agent-skills)**（⭐+5,073/week）：Addy Osmani 的 Agent 技能集
- **[SkillSpector](https://github.com/NVIDIA/SkillSpector)**（⭐+2,849/week）：NVIDIA 的 Agent 安全扫描
- **[iroh](https://github.com/n0-computer/iroh)**（⭐+1,531/week）：Rust 去中心化网络栈
- **[flue](https://github.com/withastro/flue)**（⭐+1,489/week）：Astro 团队出的沙箱 Agent 框架

---

## 🎬 视频选题建议

### 选题 1：「给 AI Agent 写 Skills 正在成为新风口」
- 切入点：skills（周增 11,784）、agent-skills、claude-plugins-official 等项目爆发
- 内容方向：什么是 Agent Skills？跟传统插件有什么区别？普通人怎么上手？市场前景如何？
- 素材：gstack（YC CEO 的配置）、OpenMontage（500+ 技能的实战案例）

### 选题 2：「AI Agent 能刷 Twitter、逛 B站、看小红书了」
- 切入点：Agent-Reach（周增 6,915）——一条命令让 Agent 访问全网
- 内容方向：演示 Agent 如何跨平台采集信息，讨论 AI Agent 的「眼睛」和「耳朵」意味着什么
- 素材：实际演示 Agent-Reach 读取各大平台内容的过程

---

> 数据来源：GitHub Trending（2025-06-24 日榜 + 周榜）
> 生成时间：2025-06-24 09:00 CST
