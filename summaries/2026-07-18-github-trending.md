# 🔥 GitHub Trending 每日速览 - 2026年7月18日

## 📌 一句话总览

**AI Agent 生态大爆发 + "反AI Slop"运动兴起。** 今天的 trending 被 AI Agent 工具链（MCP server、Agent Skills、多 Agent 编排）和强调设计质量的"反AI生成垃圾"项目霸榜。同时，开源替代商业工具的趋势依然强劲。

---

## 🚀 爆款项目 TOP 5

### 1. Nutlope/hallmark ⭐+1,485/天 (周增 8,075)
**链接：** https://github.com/Nutlope/hallmark  
**语言：** CSS | **总 Star：** 12,035

**是什么：** 一个专门为 Claude Code、Cursor、Codex 设计的 "Anti-AI-slop" 设计技能包。本质是一组 CSS 规则和 prompt 模板，让 AI 生成的 UI 摆脱千篇一律的"AI风格"，产出更专业的设计。

**为什么火：** AI 编码工具普及后，"AI味太重"成了普遍痛点——大家用 Claude/Cursor 写出来的界面都长得一样。hallmark 精准击中这个痛点，提供了一套"去AI味"的设计规范。

**对主子的价值：** 做视频选题绝佳！"如何让你的 AI 代码不像 AI 写的"这个角度有流量。也可以直接集成到日常开发中，提升 AI 生成代码的 UI 质量。

---

### 2. OpenCut-app/OpenCut ⭐+1,074/天 (周增 12,718)
**链接：** https://github.com/OpenCut-app/OpenCut  
**语言：** TypeScript | **总 Star：** 74,878

**是什么：** 开源版 CapCut（剪映国际版），功能完整的视频编辑工具，支持浏览器和桌面端。

**为什么火：** CapCut/剪映在全球有数亿用户，但闭源+付费墙让人不爽。OpenCut 提供了一模一样的功能但完全开源免费，自然爆火。周增 1.2 万 star 说明这是持续热度最高的项目之一。

**对主子的价值：** 如果主子做视频，可以直接试试替代 CapCut。也可以作为"开源替代"系列视频选题。技术上值得关注其 Web 端视频编辑的架构实现。

---

### 3. codecrafters-io/build-your-own-x ⭐+1,068/天
**链接：** https://github.com/codecrafters-io/build-your-own-x  
**语言：** Markdown | **总 Star：** 527,372

**是什么：** 老面孔了。一个巨大的"从零造轮子"教程合集，覆盖数据库、编译器、操作系统、AI 模型等各种技术的手写教程。

**为什么火：** 常青项目，持续霸榜。AI 时代反而让更多人想理解底层原理，"知其然更要知其所以然"的需求在增长。

**对主子的价值：** 适合推荐关注，做"程序员必收藏"类视频。自己也可以挑几个感兴趣的方向动手实践。

---

### 4. HKUDS/DeepTutor ⭐+531/天 (周增 1,801)
**链接：** https://github.com/HKUDS/DeepTutor  
**语言：** Python | **总 Star：** 27,365

**是什么：** 港大团队做的"终身个性化辅导" AI 系统。根据学生的学习进度和风格，提供定制化的辅导方案。

**为什么火：** 教育 AI 赛道持续升温。DeepTutor 不只是问答机器人，而是真正做了"个性化"和"长期记忆"——能记住你之前学了什么、哪里薄弱，然后针对性辅导。

**对主子的价值：** 教育 AI 赛道的标杆项目，值得关注技术架构。"AI + 教育"也是很好的视频选题方向。

---

### 5. PostHog/posthog ⭐+438/天
**链接：** https://github.com/PostHog/posthog  
**语言：** Python | **总 Star：** 36,192

**是什么：** 开源产品分析平台，集成了 AI 可观测性、用户行为分析、Session Replay、特性开关、A/B 测试、错误追踪等一站式工具。

**为什么火：** 最近加入了 AI Agent 可观测性功能，帮助开发者监控和调试 AI 应用。在 AI Agent 大爆发的背景下，这个功能卡位很准。

**对主子的价值：** 如果主子有 SaaS 产品或 AI 应用，PostHog 是很好的分析工具。也可以关注其 AI 可观测性的实现思路。

---

## 📈 技术趋势洞察

### 1. 🔥 AI Agent 生态全面爆发
今天的 trending 几乎被 AI Agent 相关项目屠榜：
- **MCP Server / Agent Skills：** `google-labs-code/stitch-skills`（周增 1,076）、`wonderwhy-er/DesktopCommanderMCP`（周增 1,657）
- **多 Agent 编排：** `stablyai/orca`（周增 5,409）——一个并行运行多个 AI Agent 的 ADE（Agent Development Environment）
- **Agent 工具链：** `openai/codex-plugin-cc`（周增 1,801）、`davila7/claude-code-templates`（周增 1,084）

**趋势判断：** AI Agent 从"能跑"进入"能管理"阶段。开发者不再满足于跑单个 Agent，而是需要编排多个 Agent 协作、监控 Agent 行为、复用 Agent 技能。这预示着 Agent 工程化正在加速。

### 2. 🎨 "反AI Slop"设计运动
`hallmark`（CSS 技能包，日增 1,485）和 `pbakaus/impeccable`（周增 2,331）都在做同一件事：让 AI 生成的 UI 不再千篇一律。

**趋势判断：** 这是 AI 编码工具成熟的标志。大家开始关注"AI 代码的质量"而非"AI 能不能写代码"。预计会有更多"AI 设计系统"类项目出现。

### 3. 🔓 开源替代持续加速
- **OpenCut** 替代 CapCut/剪映
- **DocuSeal** 替代 DocuSign
- **OfficeCLI** 替代 Microsoft Office（周增 4,611，C# 单二进制）
- **OmniRoute** 提供免费 AI API 网关，替代付费 AI 服务（周增 3,605）

**趋势判断：** "开源平替"是永恒主题，但今年的特点是：替代品质量越来越高，不再是"能用就行"的玩具。

### 4. 🦀 Rust 持续渗透
日榜/周榜中多个项目用 Rust 实现核心性能组件：
- `openinterpreter/openinterpreter`（Rust 实现 AI 编码 Agent）
- `RyanCodrai/turbovec`（Rust 实现的向量索引，Python 绑定）
- `oven-sh/bun`（Rust 实现的 JS 运行时，周增 1,212）
- `ogulcancelik/herdr`（Rust 实现的 Agent 多路复用器）

**趋势判断：** Rust 已经从"系统级编程"扩展到"高性能 AI 基础设施"。越来越多项目采用"Rust 核心 + Python/TS 绑定"的模式。

### 5. 📚 Agent Skills 成为新范式
`google-labs-code/stitch-skills`、`kangarooking/cangjie-skill`（周增 1,158）等项目都在做"Agent 技能包"——把特定领域的能力打包成可复用的 Agent Skills。

**趋势判断：** Agent 开发正在从"写 prompt"转向"组装技能"。这可能成为 Agent 开发的主流模式。

---

## 💡 值得深挖 TOP 3

### 1. stablyai/orca - 多 Agent 开发环境
**理由：** 周增 5,409 star，做的是"Agent Development Environment"——一个并行运行多个 AI Agent 的桌面/移动端工具。这代表了 Agent 开发的下一个形态：从单 Agent 到 Agent 舰队。  
**建议：** clone 下来体验一下，看看多 Agent 协作的 UX 设计。如果做得好，可以成为视频选题"AI 编程的未来：一个人指挥一群 Agent"。

### 2. diegosouzapw/OmniRoute - 免费 AI API 网关
**理由：** 周增 3,605 star，提供 231+ AI 提供商的统一 API（50+ 免费），支持 Claude Code、Codex、Cursor 等工具直连。还有 token 压缩功能（节省 15-95%）。  
**建议：** 立刻用起来！如果免费额度够大，可以省不少 AI API 费用。也适合推荐给观众。

### 3. kangarooking/cangjie-skill - 内容蒸馏 Agent Skills
**理由：** 周增 1,158 star，把书籍、长视频、播客等内容"蒸馏"成可执行的 Agent Skills。这个思路很新颖——把知识变成 Agent 能用的技能。  
**建议：** 深入研究其技术实现，看看如何把非结构化内容转化为 Agent 可执行的技能。"知识→技能"的转化可能是 AI 教育/知识管理的新方向。

---

## 📅 周榜亮点

### 持续霸榜项目
- **OpenCut** (周增 12,718) - 开源视频编辑器，连续多周霸榜
- **awesome-llm-apps** (周增 6,252，总 123,609) - LLM 应用合集，常青藤项目
- **build-your-own-x** (日增 1,068) - 从零造轮子教程，永不过时

### 本周新晋黑马
- **hallmark** (周增 8,075) - 本周绝对黑马，一个 CSS 技能包居然能涨这么多 star，说明"AI 设计质量"是真痛点
- **Vibe-Trading** (周增 5,616) - AI 交易 Agent，港大团队出品，"Vibe Coding"延伸到"Vibe Trading"
- **orca** (周增 5,409) - 多 Agent ADE，Agent 开发工具链的新玩家

### 日榜 vs 周榜差异
日榜更偏"新发现"（如 PrismML-Eng/Bonsai-demo、github/copilot-sdk），周榜更偏"持续影响力"（如 bun、awesome-llm-apps）。两者重合的项目（hallmark、OpenCut、DeepTutor）是真正的热门。

---

## 🎬 视频选题建议

### 选题 1：AI 代码"去味儿"指南
**角度：** 以 hallmark 和 impeccable 为切入点，讲"如何让 AI 生成的代码不像 AI 写的"。演示对比：默认 AI 生成的 UI vs 应用 hallmark 后的 UI。  
**目标观众：** 使用 Claude/Cursor/Copilot 的开发者  
**预期流量：** ⭐⭐⭐⭐⭐ （痛点明确，实用性强）

### 选题 2：一个人指挥一群 Agent - Orca 多 Agent 开发实战
**角度：** 以 orca 为工具，演示如何同时运行多个 AI Agent 协作完成一个项目。比如一个 Agent 写前端、一个写后端、一个做测试。  
**目标观众：** 对 AI 编程感兴趣的中高级开发者  
**预期流量：** ⭐⭐⭐⭐ （前沿话题，有技术深度）

---

## 📊 数据附录

### 今日完整日榜 (14 个项目)

| # | 项目 | 日增Star | 语言 | 总Star |
|---|------|---------|------|--------|
| 1 | Nutlope/hallmark | +1,485 | CSS | 12,034 |
| 2 | OpenCut-app/OpenCut | +1,074 | TypeScript | 74,878 |
| 3 | codecrafters-io/build-your-own-x | +1,068 | Markdown | 527,372 |
| 4 | HKUDS/DeepTutor | +531 | Python | 27,365 |
| 5 | PostHog/posthog | +438 | Python | 36,192 |
| 6 | openinterpreter/openinterpreter | +431 | Rust | 66,374 |
| 7 | RyanCodrai/turbovec | +280 | Python | 13,310 |
| 8 | PrismML-Eng/Bonsai-demo | +278 | Shell | 1,713 |
| 9 | github/copilot-sdk | +233 | Java | 9,795 |
| 10 | HenryNdubuaku/maths-cs-ai-compendium | +200 | TypeScript | 6,621 |
| 11 | docusealco/docuseal | +91 | Ruby | 17,844 |
| 12 | tirth8205/code-review-graph | +74 | Python | 19,757 |
| 13 | anthropics/cwc-workshops | +45 | TypeScript | 1,587 |
| 14 | protocolbuffers/protobuf | +11 | C++ | 71,540 |

### 周榜精选 (19 个项目)

| # | 项目 | 周增Star | 语言 | 总Star |
|---|------|---------|------|--------|
| 1 | OpenCut-app/OpenCut | +12,718 | TypeScript | 74,879 |
| 2 | Nutlope/hallmark | +8,075 | CSS | 12,035 |
| 3 | Shubhamsaboo/awesome-llm-apps | +6,252 | Python | 123,609 |
| 4 | HKUDS/Vibe-Trading | +5,616 | Python | 24,627 |
| 5 | stablyai/orca | +5,409 | TypeScript | 21,155 |
| 6 | iOfficeAI/OfficeCLI | +4,611 | C# | 18,832 |
| 7 | diegosouzapw/OmniRoute | +3,605 | TypeScript | 18,387 |
| 8 | ogulcancelik/herdr | +2,512 | Rust | 17,663 |
| 9 | pbakaus/impeccable | +2,331 | JavaScript | 47,644 |
| 10 | openai/codex-plugin-cc | +1,801 | JavaScript | 29,104 |

---

*报告生成时间：2026-07-18 09:00 | 数据来源：GitHub Trending*
