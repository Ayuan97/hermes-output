# 🔥 GitHub 趋势速览 — 2026-07-17

## 一句话总览

今天的 GitHub 被 **AI Agent 技能（Skills）和编码助手生态** 统治了——Claude Code/Codex 的"技能包"成为新物种，同时开源替代品（OpenCut 替代 CapCut）也在猛烈爆发。

---

## 🚀 爆款项目 TOP 5（日增 Star）

### 1. OpenCut-app / OpenCut ⭐ +3,537/day
- **链接**: https://github.com/OpenCut-app/OpenCut
- **干啥的**: 开源的 CapCut 替代品，TypeScript 写的全功能视频编辑器
- **为什么火**: CapCut 商业化越来越重、功能限制越来越多，开源替代是刚需。一周涨了 8,700+ star，说明市场对免费无限制视频剪辑的需求极其旺盛
- **价值**: 如果你日常做视频，这个值得试试。开源+自托管意味着完全可控，不会被平台锁死

### 2. Nutlope / hallmark ⭐ +3,372/day
- **链接**: https://github.com/Nutlope/hallmark
- **干啥的**: 给 Claude Code / Cursor / Codex 用的「反 AI 水味」设计技能包
- **为什么火**: AI 生成的 UI 代码越来越"千篇一律"，这个 skill 专门让编码 Agent 输出更有设计感、更不像 AI 生成的界面。解决了 AI 编码工具最大的痛点之一
- **价值**: 直接 clone 到你的 `.claude/skills/` 目录就能用，立刻提升 AI 辅助编码的 UI 质量

### 3. mattpocock / skills ⭐ +2,060/day
- **链接**: https://github.com/mattpocock/skills
- **干啥的**: Matt Pocock（TypeScript 知名博主）公开的 Claude Code 技能集，直接从他的 `.claude` 目录搬出来的
- **为什么火**: 顶级开发者怎么配置 AI 编码工具，这是大家最想知道的。"偷窥大佬配置"永远有流量
- **价值**: 学习高手是怎么写 Agent 提示词和技能规则的，比自己从零摸索快 10 倍

### 4. Graphify-Labs / graphify ⭐ +1,107/day
- **链接**: https://github.com/Graphify-Labs/graphify
- **干啥的**: 把任意代码/文档/数据库/脚本变成可查询的知识图谱，支持 Claude Code、Codex、Cursor 等所有主流编码工具
- **为什么火**: 解决了 AI Agent 理解大型代码库的核心问题——用知识图谱而不是纯文本让 Agent 理解项目结构
- **价值**: 如果你维护大型项目，这个能让 AI 编码助手对你的项目理解力暴增

### 5. Shubhamsaboo / awesome-llm-apps ⭐ +923/day
- **链接**: https://github.com/Shubhamsaboo/awesome-llm-apps
- **干啥的**: 100+ 个真正能跑的 AI Agent 和 RAG 应用，clone 下来就能改
- **为什么火**: 周涨近 5000 star，持续霸榜。大家需要的是"拿来就用"的 AI 应用模板，不是论文
- **价值**: AI 应用的"菜单"，不知道做什么项目就翻这个找灵感

---

## 📈 技术趋势洞察

### 1. **Agent Skills 生态爆发** 🔥🔥🔥
今天最突出的趋势：AI 编码工具的"技能包"成为独立品类。hallmark（设计技能）、mattpocock/skills（TypeScript 技能）、ibelick/ui-skills（UI 技能）、graphify（知识图谱技能）——Agent 不再是通用工具，而是通过 Skills 变成领域专家。这跟 MCP（Model Context Protocol）的兴起是一脉相承的。

### 2. **Rust 写 Agent 工具链**
openinterpreter（开源模型的编码 Agent，661/day）、codex（OpenAI 官方轻量终端 Agent，381/day）、herdr（Agent 多路复用器）、memvid（Agent 记忆层）——Rust 正成为 AI Agent 基础设施的首选语言，因为性能和安全沙箱都很关键。

### 3. **AI + 金融交易 Agent**
HKUDS 的 Vibe-Trading 周涨 4,802 star，日增 915。个人交易 Agent 这个方向在加速，AI 直接帮你做量化交易不再是概念。

### 4. **开源替代持续升温**
- OpenCut 替代 CapCut（视频编辑）
- meetily 替代 Otter.ai/Fireflies（会议记录，本地运行，Rust+Whisper）
- OmniRoute 替代各种 AI API 付费网关（231+ 供应商，50+ 免费）

---

## 💡 值得深挖 TOP 3

### 1. **hallmark** — 直接 clone 使用
- **理由**: 立竿见影地提升 AI 编码输出的 UI 质量
- **建议**: 下载后对比一下有和没有这个 skill 的输出差异，效果好的话做个视频对比

### 2. **OpenCut** — 深度体验
- **理由**: 开源视频编辑器如果真的好用，对整个内容创作生态是颠覆性的
- **建议**: 实际用它剪一个视频，看看功能完整度和体验如何

### 3. **graphify** — 整合进你的开发流程
- **理由**: 知识图谱 + AI Agent 的组合可能是大型项目 AI 辅助编码的终极形态
- **建议**: 在你的某个项目上试试，看它生成的知识图谱质量如何

---

## 📅 周榜亮点（与日榜差异）

### 持续霸榜
- **awesome-llm-apps**: 日榜 923 / 周榜 4,902，稳定热门
- **OpenCut**: 日榜 3,537 / 周榜 8,702，持续爆发
- **build-your-own-x**: 老牌学习资源，日涨 435

### 本周新晋黑马
- **iOfficeAI/OfficeCLI** ⭐ 6,374/week: AI Agent 专用的 Office 套件（Word/Excel/PPT），不需要安装 Office 就能让 Agent 操作文档。单文件部署，C# 写的。**这个方向很新——给 Agent 造"办公软件"**
- **stablyai/orca** ⭐ 5,777/week: 并行 Agent 编排桌面（ADE），同时跑多个编码 Agent 并协调。桌面+移动端都支持
- **Zackriya-Solutions/meetily** ⭐ 3,499/week: 本地 AI 会议助手，Rust + Whisper + Ollama，完全离线，隐私友好

---

## 🎬 视频选题建议

### 1. 「Claude Code 技能包大比拼：hallmark vs mattpocock/skills vs 自己写」
三个最火的 Agent Skills 横向对比，展示同一个任务在有/没有技能包时的输出差异。观众最关心"这玩意到底有没有用"。

### 2. 「OpenCut：开源 CapCut 替代品，能替代到什么程度？」
深度体验 OpenCut，用实际剪辑任务测试功能完整度。标题可以是"CapCut 慌了吗？"——自带冲突感。

---

## 附：今日各语言 Trending 精选

**Python**: Vibe-Trading（交易Agent）、DeepTutor（AI家教）、spec-kit（规范驱动开发）、datawhalechina/hello-agents（中文智能体教程）

**TypeScript**: OpenCut（视频编辑）、opencode（开源编码Agent）、airi（AI 伴侣/虚拟人）、pi-computer-use（让AI控制你的电脑）

**Rust**: openinterpreter（开源模型编码Agent）、screenpipe（屏幕录制+Agent）、codex（OpenAI 终端Agent）、memvid（Agent 记忆层）

**Go**: google-maps-scraper（地图爬虫）、grok2api（Grok API网关）、SafeLine（自托管WAF）

---

*报告生成时间: 2026-07-17 09:00 | 数据来源: GitHub Trending*
