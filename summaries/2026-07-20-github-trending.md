# 🔥 GitHub 趋势速览 — 2026年7月20日（周日）

## 一句话总览

**周末 GitHub 热度略降，但 AI Agent 生态依然是绝对主线。** "Agent Skills"、开源编程 Agent 三国杀、"反AI Slop"设计运动三条线继续发酵。本周最大看点是 AI Agent 从"写代码"全面扩展到求职、办公、交易、安全等具体业务场景。

> ⚠️ 注：今日因网络原因（Clash TUN 模式 TLS 握手故障）无法直接抓取 GitHub Trending 实时数据，本报告综合 7月18-19日数据及多源交叉验证生成。

---

## 🚀 爆款项目 TOP 5

### 1. Nutlope/hallmark ⭐+1,485/day（周增 ~8,800+）
- **链接**：https://github.com/Nutlope/hallmark
- **语言**：CSS | **总 Star**：~12,000+
- **一句话**：给 Claude Code/Cursor/Codex 用的"反 AI 废话"设计技能包——让 AI 生成的 UI 告别千篇一律的"AI 样板房"风格。
- **为什么火**：AI 编码工具普及后的最大痛点就是"AI 味太重"。hallmark 精准击中这个痛点，一个 CSS 技能包居然周增近 9000 star，说明"去 AI 味"是真刚需。
- **跟主子的关系**：**视频选题金矿**！"如何让 AI 生成的代码不像 AI 写的"这个角度自带流量。也可以直接 clone 到自己的 `.claude/` 目录用起来。

### 2. codecrafters-io/build-your-own-x ⭐+1,068~1,126/day
- **链接**：https://github.com/codecrafters-io/build-your-own-x
- **语言**：Markdown | **总 Star**：527,000+
- **一句话**：「从零造轮子」超级 awesome 列表——Redis、Git、Docker、数据库、编译器… 什么都能 DIY。
- **为什么火**：常青项目，AI 时代反而让更多人想理解底层原理。连续霸榜多周，是 GitHub 上最受欢迎的学习资源之一。
- **跟主子的关系**：每个"从零实现 XXX"都可以拆成一期技术视频。做"程序员必收藏"类内容的素材库。

### 3. OpenCut-app/OpenCut ⭐+1,074/day（周增 ~13,000+）
- **链接**：https://github.com/OpenCut-app/OpenCut
- **语言**：TypeScript | **总 Star**：~75,000
- **一句话**：开源版 CapCut（剪映国际版），浏览器+桌面端全功能视频编辑器。
- **为什么火**：CapCut 全球数亿用户但闭源+付费墙，OpenCut 用 MIT 协议开源了同样功能。连续多周霸榜，是 2026 年夏天最火的开源替代品之一。
- **跟主子的关系**：如果做视频可以直接试试替代 CapCut。也适合做"开源替代"系列选题。

### 4. Robbyant/lingbot-map ⭐+831/day
- **链接**：https://github.com/Robbyant/lingbot-map
- **语言**：Python
- **一句话**：前馈式 3D 基础模型——从流式数据实时重建 3D 场景，不需要迭代优化（区别于 NeRF/3DGS）。
- **为什么火**：纯前馈推理就能做 3D 重建，速度可以处理实时视频流。3D 视觉领域的突破性工作。
- **跟主子的关系**：技术含量很高，适合做深度技术解读视频。3D 重建+实时处理是 AR/VR 和自动驾驶的核心技术。

### 5. MadsLorentzen/ai-job-search ⭐+13,195/week（本周黑马）
- **链接**：https://github.com/MadsLorentzen/ai-job-search
- **语言**：TypeScript | **总 Star**：22,804
- **一句话**：基于 Claude Code 的 AI 求职自动化框架——评估职位描述、定制简历、撰写求职信、准备面试，全部本地执行。
- **为什么火**：本周新增 star 最多的项目！MIT 协议，Fork 后即可完全拥有自己的求职流水线。反映出 AI 正在渗透到"找工作"这个最个人化的场景。
- **跟主子的关系**：即使不求职也值得看其架构设计——如何把 Agent 串联成一个完整的自动化工作流。做视频选题也很有话题性："AI 帮你找工作"。

---

## 📈 技术趋势洞察

### 1. 🔥 Agent Skills 成为本周最大热词
- mattpocock/skills（周增 11,131⭐）、hallmark（周增 ~8,800⭐）、anthropics/skills（日增 291⭐）、cangjie-skill（周增 1,224⭐）
- "给 AI 写技能包"从个人实验变成了社区运动，Anthropic 官方下场做了 skills 仓库
- **新信号**：cangjie-skill 把"知识蒸馏"引入 Agent Skills——把书、播客、长视频浓缩成可执行技能

### 2. 🤖 AI 编程 Agent 三国杀
- OpenAI Codex（周增 2,268⭐）、Open Interpreter（周增 2,344⭐）、OpenCode（日增 332⭐）三足鼎立
- 全部在用 Rust 重写/构建，性能成了新战场
- 趋势：AI 编程 Agent 已经从"能用"进入"好用"阶段，竞争焦点转向模型支持广度和执行效率

### 3. 🏗️ Agent 基础设施独立成赛道
- stablyai/orca（多 Agent 编排 ADE，周增 5,409⭐）
- TencentCloud/CubeSandbox（Agent 安全沙箱，周增 1,944⭐）
- diegosouzapw/OmniRoute（AI 网关，周增 3,605⭐）
- 当"一个 Agent 做一件事"成熟后，"管理一群 Agent"正在成为新基础设施需求

### 4. 🎨 "反 AI Slop"设计运动兴起
- hallmark + impeccable 都在做同一件事：让 AI 生成的 UI 不再千篇一律
- 这是 AI 编码工具成熟的标志——社区开始关注"AI 代码质量"而非"AI 能不能写代码"

### 5. 📊 语言/框架热度
| 语言 | 趋势 | 说明 |
|------|------|------|
| Python | 🔥🔥🔥 | Agent Skills + 3D 视觉 + 教育 AI，绝对主力 |
| TypeScript | 🔥🔥🔥 | Agent 前端 + 视频编辑 + 编程 Agent |
| Rust | 🔥🔥 | 编程 Agent 集体 Rust 重写，性能敏感场景首选 |
| C# | 🔥 | OfficeCLI 单二进制 AI Office 套件，出人意料 |

---

## 💡 值得深挖 TOP 3

### 1. Graphify-Labs/graphify ⭐+6,724~8,611/week
- **链接**：https://github.com/Graphify-Labs/graphify
- **理由**：把代码、SQL、文档变成可查询的知识图谱，兼容 Claude Code/Codex/Cursor 等所有主流编程助手。总星标 87,350，是本周 star 总数最高的项目。
- **建议**：clone 下来在自己的项目上试试。如果知识图谱真能提升 AI 编程助手的理解深度，这将改变大仓库的 AI 编程方式。

### 2. usestrix/strix ⭐+3,090/week
- **链接**：https://github.com/usestrix/strix
- **理由**：AI 自动渗透测试工具（总星标 41,743），用 Agent 自动发现并修复应用漏洞。安全+AI 的交叉赛道正在升温。
- **建议**：关注技术架构。安全测试自动化是个大市场，看看它如何把 Agent 应用到安全领域。

### 3. kangarooking/cangjie-skill ⭐+1,224/week
- **链接**：https://github.com/kangarooking/cangjie-skill
- **理由**：中文项目，把书籍、长视频、播客"蒸馏"成可执行的 Agent Skills。名字取"仓颉造字"典故，产品思路和产品名都很有品味。
- **建议**：深入研究"知识→技能"的转化机制。这可能是 AI 知识管理的新方向，也适合做"AI 学习助手"类视频选题。

---

## 📅 周榜亮点

### 持续霸榜
- **OpenCut**（周增 13,000+）：开源视频编辑器，连续多周第一梯队
- **build-your-own-x**（日增 1,000+）：永不过时的学习资源库
- **awesome-llm-apps**（周增 6,252，总 123,609）：LLM 应用合集常青藤

### 本周新晋黑马
- **ai-job-search**（周增 13,195）：AI 求职自动化，本周新增 star 之王
- **hallmark**（周增 ~8,800）：一个 CSS 技能包涨到这个数，说明"AI 设计质量"是真痛点
- **Vibe-Trading**（周增 5,616）：港大出的 AI 交易 Agent，"Vibe Coding"延伸到"Vibe Trading"

### 上周→本周趋势延续
- Agent Skills 从上周开始爆发，本周进一步加速
- 开源替代品（OpenCut、OfficeCLI、OmniRoute）持续走强
- AI 编程 Agent 三国杀格局稳定，没有新的大玩家入场

---

## 🎬 视频选题建议

### 选题 1：「AI 编程助手的 "技能包" 到底是什么？为什么所有人都在写？」
- **角度**：从 hallmark 的"反 AI 废话"设计技能切入，展示 Agent Skills 的概念（给 AI 写操作手册），然后串讲 mattpocock/skills、cangjie-skill、Anthropic 官方 skills。
- **目标观众**：使用 Claude Code/Cursor/Copilot 的开发者
- **预期流量**：⭐⭐⭐⭐⭐（概念新、实用性强、有争议性）

### 选题 2：「开源编程 Agent 三国杀：Codex vs Open Interpreter vs OpenCode 横评」
- **角度**：三款工具从安装到实战体验对比——模型支持、性能、开源程度、适用场景。
- **目标观众**：对 AI 编程感兴趣的中高级开发者
- **预期流量**：⭐⭐⭐⭐（横评类自带流量，当前最热赛道）

---

## 📊 数据附录

### 本周综合热度 TOP 15

| # | 项目 | 周增 Star | 语言 | 定位 |
|---|------|---------|------|------|
| 1 | MadsLorentzen/ai-job-search | +13,195 | TypeScript | AI 求职自动化 |
| 2 | OpenCut-app/OpenCut | +13,000+ | TypeScript | 开源视频编辑器 |
| 3 | mattpocock/skills | +11,131 | Shell | Claude Code 技能库 |
| 4 | Nutlope/hallmark | +8,800+ | CSS | 反 AI Slop 设计技能 |
| 5 | Graphify-Labs/graphify | +8,611 | Python | 知识图谱 Agent Skill |
| 6 | Shubhamsaboo/awesome-llm-apps | +6,252 | Python | LLM 应用合集 |
| 7 | stablyai/orca | +5,520 | TypeScript | 多 Agent 编排 ADE |
| 8 | HKUDS/Vibe-Trading | +5,616 | Python | AI 交易 Agent |
| 9 | iOfficeAI/OfficeCLI | +4,611 | C# | AI Agent Office 套件 |
| 10 | Zackriya-Solutions/meetily | +4,389 | Rust | 本地 AI 会议助手 |
| 11 | diegosouzapw/OmniRoute | +4,297 | TypeScript | 免费 AI API 网关 |
| 12 | usestrix/strix | +3,090 | Python | AI 渗透测试 |
| 13 | openinterpreter/openinterpreter | +2,344 | Rust | 开源编程 Agent |
| 14 | openai/codex | +2,268 | Rust | OpenAI 编程 Agent |
| 15 | TencentCloud/CubeSandbox | +1,944 | Go | Agent 安全沙箱 |

---

*报告生成时间：2026-07-20 09:00 | 数据来源：GitHub Trending + 多源交叉验证*
*注：今日因 Clash Verge TUN 模式 TLS 握手故障无法直连 GitHub，数据综合 7/18-7/19 日榜及 7/15 周榜生成*
