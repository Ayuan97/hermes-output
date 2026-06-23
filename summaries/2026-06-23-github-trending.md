# 🔥 今日 GitHub 趋势速览 — 2026-06-23

## 一句话总览

AI Agent 工具链全面爆发：从视频制作、语音克隆到代码记忆、网络安全，几乎所有热门项目都在围绕「让 Agent 更能干」这个主题。TypeScript 和 Python 依然是主战场，Rust 在基础设施层持续渗透。

---

## 🚀 爆款项目 TOP 5（按日增 Star 排序）

### 1. [OpenMontage](https://github.com/calesthio/OpenMontage) — ⭐+2,938/day
- **是什么**：开源 Agentic 视频制作系统，12 条流水线、52 个工具、500+ Agent 技能
- **为什么火**：把 AI 编程助手变成完整的视频制作工作室，打通了「想法→成片」的全链路
- **对主子的价值**：如果做视频内容，这个项目值得关注。可以作为「AI 替代传统剪辑工作流」的选题素材

### 2. [mattpocock/skills](https://github.com/mattpocock/skills) — ⭐+2,051/day
- **是什么**：Matt Pocock（TypeScript 大神）的 Claude Code 工程技能集，来自他的 `.claude` 目录
- **为什么火**：名人效应 + 实战经验，展示了专业工程师怎么给 AI Agent 编写高质量技能
- **对主子的价值**：直接 clone 学习怎么写 Agent Skills，可以迁移到自己的 Hermes 配置里

### 3. [palmier-pro](https://github.com/palmier-io/palmier-pro) — ⭐+2,463/day
- **是什么**：专为 AI 打造的 macOS 视频编辑器，原生 Swift 开发
- **为什么火**：AI 视频编辑赛道持续火热，macOS 原生体验 + AI 能力的组合有差异化
- **对主子的价值**：主子用 macOS，可以试试看和现有剪辑工具对比如何

### 4. [daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) — ⭐+1,557/day
- **是什么**：LLM 驱动的多市场股票智能分析系统，支持多源行情、实时新闻、决策看板和自动推送
- **为什么火**：零成本运行 + 自动化推送，散户和量化爱好者的刚需
- **对主子的价值**：如果对投资感兴趣可以部署一个；技术上也是 LLM + 数据管道的好案例

### 5. [codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) — ⭐+1,185/day
- **是什么**：高性能代码智能 MCP 服务器，把代码库索引成知识图谱，毫秒级查询，支持 158 种语言
- **为什么火**：解决了 AI Agent「看不懂大代码库」的痛点，单二进制零依赖，性能极强
- **对主子的价值**：强烈推荐。配合 Claude Code / Cursor 等工具，让 AI 真正理解你的项目上下文

---

## 📈 技术趋势洞察

### Agent 技能生态成为新战场
今天 trending 里至少 6 个项目直接跟 Agent Skills 相关：
- mattpocock/skills（工程技能）
- mukul975/Anthropic-Cybersecurity-Skills（817 个安全技能）
- NVIDIA/skills（NVIDIA 官方 Agent 技能）
- addyosmani/agent-skills（生产级工程技能，周榜 +5,277）
- vectorize-io/hindsight（Agent 记忆层）
- NVIDIA/SkillSpector（Agent 技能安全扫描器，周榜 +3,302）

**趋势信号**：Agent Skills 正在从「手动写 prompt」进化到「标准化技能市场」，安全性（NVIDIA SkillSpector）也开始被重视。

### AI + 创意工具链成型
- OpenMontage（视频制作）、palmier-pro（视频编辑）、voicebox（语音克隆）、heygen-com/hyperframes（HTML→视频）—— AI 创意工具从单点突破走向全链路覆盖

### MCP（Model Context Protocol）持续升温
- codebase-memory-mcp 日增 1,185 star，说明 MCP 生态的基础设施层正在快速完善

### Rust 在基础设施层稳步扩张
- turso（SQLite 兼容数据库）+540/天
- iroh（模块化网络栈）周增 1,806
- Rust 写的工具在性能敏感场景越来越受欢迎

---

## 💡 值得深挖 TOP 3

### 1. codebase-memory-mcp
- **理由**：单二进制、零依赖、毫秒级查询，直接解决 AI 编码助手的最大短板
- **建议**：clone 下来集成到日常开发流程，效果立竿见影

### 2. mattpocock/skills
- **理由**：TypeScript 领域顶级工程师的实战 Agent Skills，学习价值极高
- **建议**：研究他的技能编写模式，应用到自己的 Hermes Agent 配置中

### 3. [bytedance/deer-flow](https://github.com/bytedance/deer-flow) — ⭐+738/day
- **理由**：字节开源的长时任务 SuperAgent 框架，支持沙箱、记忆、子 Agent、消息网关，架构设计值得学习
- **建议**：适合做「企业级 AI Agent 架构」的技术选题，也可以参考其子 Agent 编排思路

---

## 📅 周榜亮点

### 持续霸榜
- **codebase-memory-mcp**：周增 7,560 star，稳居第一，说明代码库理解是真刚需
- **OpenMontage**：周增 6,089，视频制作 Agent 持续吸睛
- **penpot**：周增 2,983，开源设计工具的常青树

### 本周新晋黑马
- **[Agent-Reach](https://github.com/Panniantong/Agent-Reach)**：周增 8,108 star！给 AI Agent 一只「互联网之眼」—— 一条命令读取 Twitter、Reddit、YouTube、GitHub、B站、小红书，零 API 费用
- **[system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks)**：周增 2,612，收集了各大 AI 产品的 System Prompt（Claude、GPT-5.5、Gemini 3.5、Grok、Cursor 等），安全研究者的宝藏
- **[worldmonitor](https://github.com/koala73/worldmonitor)**：周增 2,090，AI 驱动的全球情报仪表盘，新闻聚合 + 地缘监控 + 基础设施追踪

---

## 🎬 视频选题建议

### 选题一：「AI Agent Skills 生态大爆发：从手动 Prompt 到标准化技能市场」
- **切入点**：用今天 trending 里的多个 skills 项目（mattpocock、NVIDIA、addyosmani）做对比分析
- **看点**：Agent Skills 的标准化趋势、安全性问题（SkillSpector）、以及普通人怎么上手
- **素材**：可以实际 clone 项目演示效果

### 选题二：「让 AI 看懂你的代码库：codebase-memory-mcp 深度体验」
- **切入点**：实操演示 MCP 服务器如何索引代码库、配合 AI 编码工具使用
- **看点**：性能数据（毫秒级查询）、知识图谱可视化、与传统 RAG 方案对比
- **素材**：拿一个真实项目跑一遍，展示前后对比

---

> 数据来源：GitHub Trending（日榜 + 周榜 + Python/TypeScript/Rust/Go 分语言榜）
> 采集时间：2026-06-23 09:00 CST
