# 🔥 GitHub 趋势速览 — 2026年7月19日（周六）

## 一句话总览

**"Agent Skills" 成了本周 GitHub 最大热词。** 从 mattpocock 的万星 skills 仓库到 Anthropic 官方 skills 仓库、从反 AI 废话的 hallmark 到把播客蒸馏成 Agent 技能的 cangjie-skill——整个社区都在给 AI 编程助手"写说明书"。与此同时，开源编程 Agent（Codex、Open Interpreter、OpenCode）集体霸榜，AI 编程工具赛道已经进入白热化。

---

## 🚀 爆款项目 TOP 5（日增 star 最多）

### 1. codecrafters-io/build-your-own-x
- **链接**：https://github.com/codecrafters-io/build-your-own-x
- **日增**：⭐+1,126/day
- **一句话**：「从零造轮子学编程」的超级 awesome 列表，覆盖 Redis、Git、Docker、数据库等几十种技术的 DIY 教程。
- **为什么火**：老项目持续更新，AI 时代大家反而更想理解底层原理。这份列表就是最好的"逆向工程学习路线图"。
- **跟主子的关系**：选题金矿。每个「从零实现 XXX」都可以拆成一期技术视频，自带高完播率属性。

### 2. Robbyant/lingbot-map
- **链接**：https://github.com/Robbyant/lingbot-map
- **日增**：⭐+831/day
- **一句话**：前馈式 3D 基础模型，从流式数据实时重建场景。
- **为什么火**：不需要迭代优化（区别于 NeRF/3DGS），纯前馈推理就能做 3D 重建，速度快到可以处理实时视频流。
- **跟主子的关系**：3D 视觉+实时重建，技术含量很高，适合做深度技术解读视频。

### 3. openinterpreter/openinterpreter
- **链接**：https://github.com/openinterpreter/openinterpreter
- **日增**：⭐+661/day（Rust 榜）| 周增 ⭐+2,344/week
- **一句话**：面向开源模型（如 Kimi K3）的编程 Agent，终端里直接跑代码。
- **为什么火**：OpenAI Codex 的开源对标产品。用 Rust 重写后性能飞升，对开源模型的支持比 Codex 更灵活。
- **跟主子的关系**：值得关注。如果你用非 OpenAI 的模型做编程，这可能是最好的终端 Agent。

### 4. SigNoz/signoz
- **链接**：https://github.com/SigNoz/signoz
- **日增**：⭐+432/day（TypeScript 榜）
- **一句话**：开源 OpenTelemetry 原生可观测性平台——日志、指标、链路追踪一把梭。
- **为什么火**：加了 MCP 支持和 AI 队友功能，从"给 DevOps 用的工具"变成了"AI Agent 也能用的诊断平台"。
- **跟主子的关系**：如果做 AI Agent 应用，可观测性是刚需。SigNoz 是目前最好的开源方案之一。

### 5. tirth8205/code-review-graph
- **链接**：https://github.com/tirth8205/code-review-graph
- **日增**：⭐+355/day
- **一句话**：本地优先的代码智能图谱，给 MCP 和 CLI 构建代码库的持久化地图，让 AI 编程工具只读需要的文件。
- **为什么火**：解决了 AI 编程助手的核心痛点——上下文爆炸。大仓库里 AI 不知道读哪些文件，这个工具帮你精准裁剪上下文。
- **跟主子的关系**：直接能用。配合 Claude Code 或 Codex 使用，大项目里能显著提升 AI 编程质量。

---

## 📈 技术趋势洞察

### 🔥 本周最热方向

1. **Agent Skills 生态大爆发**
   - mattpocock/skills 周增 11,131⭐，Nutlope/hallmark 周增 8,834⭐，anthropics/skills 日增 291⭐
   - "给 AI 写技能包"已经从个人实验变成了社区运动。Anthropic 官方下场做了 skills 仓库，等于正式认可了这个范式
   - **新信号**：cangjie-skill（周增 1,224⭐）把"知识蒸馏"概念引入 Agent Skills——把书、播客、长视频浓缩成可执行技能，这个思路很新

2. **AI 编程 Agent 三国杀**
   - OpenAI Codex（周增 2,268⭐）、Open Interpreter（周增 2,344⭐）、OpenCode（日增 332⭐）三足鼎立
   - 全都在 Rust 上重写/构建，性能成了新战场
   - anomalyco/opencode 打的是"完全开源"的牌，对标 Codex 的闭源焦虑

3. **MCP（Model Context Protocol）已成基础设施**
   - wigolo（给 AI Agent 做本地搜索/爬取，零 API 费用）、DesktopCommanderMCP、agentgateway（Agent 代理网关）都在围绕 MCP 做文章
   - MCP 从"协议"变成了"生态"，周边工具越来越多

4. **开源替代品持续涌现**
   - OpenCut（开源 CapCut，周增 13,319⭐ 本周第一）
   - SigNoz（开源 Datadog）
   - LocalAI（本地跑一切模型）
   - 趋势：每个赛道的 SaaS 都在被开源复刻

### 📊 语言/框架热度

| 语言 | 趋势 | 说明 |
|------|------|------|
| Python | 🔥🔥🔥 | Agent Skills + 3D 视觉 + AI 应用，依然是主力 |
| TypeScript | 🔥🔥🔥 | Agent 前端 + 可观测性 + 开源工具 |
| Rust | 🔥🔥 | 编程 Agent 集体 Rust 重写，性能敏感场景首选 |
| Go | 🔥 | Agent 框架 + 可观测性，稳扎稳打 |

---

## 💡 值得深挖 TOP 3

### 1. Graphify-Labs/graphify ⭐+8,611/week
- **链接**：https://github.com/Graphify-Labs/graphify
- **理由**：把代码、SQL、基础设施变成可查询的知识图谱，支持 Claude Code/Codex/Cursor 等所有主流编程助手。周增 8.6K 说明需求巨大。
- **建议**：clone 下来在自己的项目上试试，看看知识图谱能不能提升 AI 编程助手的理解深度。如果好用，可以直接整合进日常工作流。

### 2. stablyai/orca ⭐+5,520/week
- **链接**：https://github.com/stablyai/orca
- **理由**：Agent 开发环境（ADE），可以同时跑一堆并行 Agent，桌面和移动端都支持。这代表了"Agent 编排"从命令行走向可视化。
- **建议**：值得关注产品形态。多个 Agent 并行工作是未来的方向，看看它的编排 UI 怎么设计的。

### 3. iOfficeAI/OfficeCLI ⭐+4,284/week
- **链接**：https://github.com/iOfficeAI/OfficeCLI
- **理由**：第一个专门为 AI Agent 设计的 Office 套件——单二进制文件、不需要安装 Office、C# 写的。让 Agent 直接读写 Word/Excel/PPT。
- **建议**：直接能用。如果你有自动化办公的需求（批量生成报告、处理表格数据），这个工具可以让 AI Agent 直接操作 Office 文件。

---

## 📅 周榜亮点

### 持续霸榜
- **codecrafters-io/build-your-own-x**：日榜周榜双料冠军，学编程的终极资源库
- **openai/codex + openinterpreter**：编程 Agent 赛道两强，周榜稳定在 2,000+ star

### 本周新晋黑马
- **Nutlope/hallmark**（周增 8,834⭐）：给 Claude Code/Cursor/Codex 用的"反 AI 废话"设计技能——让 AI 生成的 UI 不再是千篇一律的样板房风格。这个方向很新，说明大家开始在意 AI 生成内容的"审美"了
- **HKUDS/Vibe-Trading**（周增 5,635⭐）：港大出的"Vibe 交易"Agent，把 AI 交易从量化信号变成了"感觉驱动"。名字就很有梗
- **kangarooking/cangjie-skill**（周增 1,224⭐）：中文项目，把长内容蒸馏成 Agent 技能，名字取"仓颉造字"的典故，产品思路和产品名都很有品味

---

## 🎬 视频选题建议

### 选题 1：「AI Agent 的 "技能包" 生态爆发了——Agent Skills 是什么？为什么所有人都在写？」
- **切入角度**：从 mattpocock/skills 周增 1.1 万星说起，讲清楚 Agent Skills 的概念（给 AI 编程助手写"操作手册"），然后展示 hallmark 的"反 AI 废话"技能、cangjie-skill 的知识蒸馏技能、以及 Anthropic 官方 skills 仓库。
- **为什么能火**：概念新、有争议性（AI 需要"技能包"还是应该自己学？）、实用性强（观众可以直接用起来）。

### 选题 2：「开源编程 Agent 三国杀：Codex vs Open Interpreter vs OpenCode，谁更适合你？」
- **切入角度**：三款工具横评——OpenAI 的 Codex（闭源+Rust）、Open Interpreter（开源+支持多模型）、OpenCode（完全开源）。从安装、使用体验、模型支持、性能几个维度对比。
- **为什么能火**：AI 编程助手是当前最热赛道，横评类内容自带流量，观众可以直接参考选择。

---

*数据采集时间：2026-07-19 09:00 | 数据源：GitHub Trending*
