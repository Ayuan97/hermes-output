# 🔥 今日 GitHub 趋势速览（2026-06-13）

## 一句话总览

**AI Agent 技能生态全面爆发**——今天 trending 榜单被 "agent skills" 类项目屠榜，从工程技能、产品管理技能到"给 AI 培养品味"的技能包，开发者正在疯狂构建 Agent 的能力层。同时 Apple 官方开源的容器工具一天涨了 3500+ star，成为现象级项目。

---

## 🚀 爆款项目 TOP 5（日增 star 最多）

### 1. apple/container ⭐+3,504/day
- **链接**：https://github.com/apple/container
- **语言**：Swift
- **干什么**：Apple 官方开源的 Linux 容器工具，用轻量虚拟机在 Mac 上跑 Linux 容器，专为 Apple Silicon 优化
- **为什么火**：Apple 终于亲自下场做容器了！不用再折腾 Docker Desktop，原生 Swift 实现，性能和集成度直接拉满。这相当于 Apple 对 Docker 说"我自己来"
- **对主子的价值**：⭐⭐⭐⭐⭐ 如果用 Mac 开发，这是 Docker 的终极替代方案，必须关注

### 2. addyosmani/agent-skills ⭐+2,656/day
- **链接**：https://github.com/addyosmani/agent-skills
- **语言**：Shell
- **干什么**：给 AI 编码 Agent 提供生产级工程技能包，涵盖代码质量、测试、调试等最佳实践
- **为什么火**：Addy Osmani（Google Chrome 团队大佬）出品，直接给 Agent 喂"工程素养"，解决 Agent 写代码质量不稳定的核心痛点
- **对主子的价值**：⭐⭐⭐⭐ 如果在用 Claude Code / Codex 等编码 Agent，直接装上提升代码质量

### 3. obra/superpowers ⭐+1,275/day
- **链接**：https://github.com/obra/superpowers
- **语言**：Shell
- **干什么**：一套 Agentic 技能框架 + 软件开发方法论，给 Agent 注入系统化的开发能力
- **为什么火**：不是简单的 prompt 集合，而是一套完整的 Agent 工作方法论。跟 agent-skills 形成互补
- **对主子的价值**：⭐⭐⭐⭐ 值得 clone 下来研究其技能组织方式，可能对 Hermes Agent 的技能设计有启发

### 4. msitarzewski/agency-agents ⭐+1,026/day
- **链接**：https://github.com/msitarzewski/agency-agents
- **语言**：Shell
- **干什么**：一个完整的 AI 代理机构——从前端专家到 Reddit 社区运营，每个 Agent 都是带个性的专家
- **为什么火**：把 Agent 做成了"团队"的概念，每个 Agent 有专业分工和人格设定，不再是万能但平庸的通用 Agent
- **对主子的价值**：⭐⭐⭐⭐ 思路很好，可以参考其 Agent 角色设计来做视频选题

### 5. phuryn/pm-skills ⭐+827/day
- **链接**：https://github.com/phuryn/pm-skills
- **语言**：Markdown
- **干什么**：产品经理技能市场，100+ Agentic 技能/命令/插件，覆盖从发现到策略、执行、发布、增长全流程
- **为什么火**：Agent 技能的"应用商店"模式开始出现，PM 领域先落地了
- **对主子的价值**：⭐⭐⭐ 可以借鉴这种技能组织方式，但 PM 领域跟技术内容关系不大

---

## 📈 技术趋势洞察

### 1. Agent Skills 生态大爆发 🔥🔥🔥
今天最明显的方向：**Agent 从"能用"走向"好用"的关键一步是技能包**。agent-skills、superpowers、pm-skills、taste-skill（周榜 +8,651/week）、last30days-skill（周榜 +12,257/week）——开发者正在疯狂给 Agent "装技能"。这说明 Agent 基础能力已经不是瓶颈，**差异化来自技能层**。

### 2. Token 效率成为刚需
- **headroom**（周榜 +10,184/week）：压缩工具输出/日志/RAG 内容，减少 60-95% token
- **context-mode**（TypeScript 日榜）：上下文窗口优化，减少 98% 工具输出
- **LMCache**：LLM 的 KV Cache 加速层

Token 成本是 Agent 落地的最大障碍之一，这类工具会越来越重要。

### 3. AI Agent 可观测性工具兴起
- **agentsview**（Go 日榜 +530/day）：编码 Agent 的本地会话分析工具
- **abtop**（Rust 日榜 +65/day）：Agent 的 "htop"，监控 Claude Code / Codex 的 token、上下文窗口、速率限制

Agent 跑起来之后怎么监控、怎么优化，正在成为新的工具赛道。

### 4. 语言热度变化
- **Shell** 语言的 trending 项目激增——大量 agent skill 包是用 Markdown/Shell 组织的
- **Swift** 因 Apple/container 重回聚光灯
- **Rust** 持续在工具链领域发力（cc-switch、abtop、helix-db、pgdog）
- **Python** 依然是 AI/ML 的绝对主力

---

## 💡 值得深挖 TOP 3

### 1. apple/container
**理由**：Apple 官方出品，3,504 star/天的增长速度说明这是真需求。原生 Swift 实现 + Apple Silicon 优化，可能是 Docker Desktop 的终结者。
**建议**：主子是 Mac 用户的话，建议 clone 下来跑一下，评估是否能替代日常 Docker 用法。如果好用，这是个绝佳的视频选题——"Apple 官方容器工具 vs Docker Desktop"。

### 2. mvanhorn/last30days-skill（周榜冠军）
**链接**：https://github.com/mvanhorn/last30days-skill
**理由**：一周涨 12,257 star，跨 Reddit、X、YouTube、HN、Polymarket 等平台做研究并综合总结。本质上是一个"AI 研究助手技能"。
**建议**：这个项目的架构思路值得学习——怎么让 Agent 有效聚合多源信息。可以整合到 Hermes Agent 的技能库里做信息聚合。

### 3. farion1231/cc-switch（Rust 日榜 +872/day）
**链接**：https://github.com/farion1231/cc-switch
**理由**：跨平台桌面 All-in-One 助手，支持 Claude Code、Codex、OpenCode、Gemini CLI 和 Hermes Agent。一个工具管所有 AI 编码助手。
**建议**：直接跟 Hermes Agent 相关！建议关注其对 Hermes Agent 的集成方式，看看有什么可以反哺的功能。

---

## 📅 周榜亮点

### 持续霸榜
- **apple/container**：日榜 +3,504，周榜 +7,781，持续高热
- **phuryn/pm-skills**：日榜 +827，周榜 +4,839，Agent 技能市场的标杆

### 本周新晋黑马
- **mvanhorn/last30days-skill**（+12,257/week）：跨平台研究 Agent 技能，周榜冠军
- **chopratejas/headroom**（+10,184/week）：LLM token 压缩工具，解决真实痛点
- **Leonxlnx/taste-skill**（+8,651/week）：给 AI 培养"品味"，拒绝平庸输出，概念新颖
- **Panniantong/Agent-Reach**（+5,364/week）：让 Agent 能读 Twitter/Reddit/YouTube/B站/小红书，零 API 费用
- **lfnovo/open-notebook**（+3,848/week）：开源 NotebookLM 替代品，功能更灵活

---

## 🎬 视频选题建议

### 选题 1：「Apple 官方出手！开源容器工具能否干掉 Docker？」
- 切入点：apple/container 一天 3500 star 的现象级事件
- 内容：跟 Docker Desktop 做对比测试，展示 Apple Silicon 原生优势
- 受众：Mac 开发者、容器用户
- 热度预估：⭐⭐⭐⭐⭐（Apple + 开源 + 替代 Docker，三重流量密码）

### 选题 2：「AI Agent 的技能革命：从通用助手到专家团队」
- 切入点：agent-skills、superpowers、agency-agents、taste-skill 集体屠榜
- 内容：拆解 Agent Skills 生态，展示怎么给 Agent 装技能、技能包的设计模式
- 受众：AI 开发者、Agent 爱好者
- 热度预估：⭐⭐⭐⭐（技术深度 + 实操性强）
