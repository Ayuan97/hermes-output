# 🔥 GitHub 趋势速览 | 2026-07-07（周一）

## 一句话总览

**AI Agent 技能生态大爆发** — 今天 GitHub 日榜几乎被 Claude Code / Codex 的 Skills、Plugins 和 Agent 工具链霸屏。从"给 AI 编程 Agent 装技能包"到"多 Agent 协作编排"，整个社区正在从"用 AI 写代码"快速演进到"用 Agent 管理 Agent"。Rust 在 AI 基础设施层持续崛起。

---

## 🚀 爆款项目 TOP 5（日增 star 最多）

### 1. Zackriya-Solutions/meetily ⭐+2,494/day
🔗 https://github.com/Zackriya-Solutions/meetily

**是什么：** 用 Rust 构建的开源 AI 会议助手，支持本地 Parakeet/Whisper 实时转录、说话人分离、Ollama 摘要生成。100% 本地处理，不传云端。

**为什么火：** 隐私+本地+Rust 三个关键词全踩中了。比 Zoom/Teams 的 AI 转录快 4 倍，而且完全自托管。周榜 +5,769，持续霸榜。

**对主子的价值：** 如果日常开会多，这个值得 clone 试试。macOS 和 Windows 都支持，本地跑不吃 API 费用。也可以做视频选题——"用 Rust 造一个比 Copilot 还快的会议记录器"。

---

### 2. Leonxlnx/taste-skill ⭐+1,458/day
🔗 https://github.com/Leonxlnx/taste-skill

**是什么：** 一个 Claude Code Skill，号称能给 AI 编程 Agent "注入审美"，让它不再输出千篇一律的无聊代码。

**为什么火：** 戳中了当前 AI 编程的痛点——生成的代码"能用但很丑"。通过 Skill 机制把人类的工程审美注入 Agent。

**对主子的价值：** 配合 Hermes Agent 的理念（skill 系统），非常值得研究其实现方式。看看它的 prompt 和 skill 结构怎么设计的。

---

### 3. asgeirtj/system_prompts_leaks ⭐+1,378/day
🔗 https://github.com/asgeirtj/system_prompts_leaks

**是什么：** 收集了 Anthropic Claude、OpenAI ChatGPT、Google Gemini、xAI Grok、Cursor、Copilot 等主流 AI 的系统提示词（prompt 泄露合集），持续更新。

**为什么火：** 每家出新模型，社区就扒系统提示词。这是 prompt engineering 的"逆向工程宝典"。

**对主子的价值：** 研究竞品 AI 的 prompt 设计思路。特别是 Claude Code 和 Cursor 的系统提示，对优化 Hermes Agent 的指令设计有直接参考价值。

---

### 4. addyosmani/agent-skills ⭐+1,112/day
🔗 https://github.com/addyosmani/agent-skills

**是什么：** Google Chrome 团队 Addy Osmani 出的项目——给 AI 编程 Agent 提供"生产级工程技能"集合。

**为什么火：** Addy 本人在前端工程领域的影响力巨大，这个项目相当于给 Agent 装了"高级工程师认证"。

**对主子的价值：** 直接看它的 skill 列表，挑选有用的整合到 Hermes Agent 的技能库里。

---

### 5. openai/codex-plugin-cc ⭐+906/day
🔗 https://github.com/openai/codex-plugin-cc

**是什么：** OpenAI 官方出品，让你在 Claude Code 里调用 Codex 来做代码审查或委派任务。

**为什么火：** "AI 套娃"——用一个 Agent 指挥另一个 Agent 干活。这是 Agent 协作的官方示范。

**对主子的价值：** 理解 OpenAI 对 Agent 互操作的设计思路。如果你同时用 Claude Code 和 Codex，这个插件可以直接装。

---

## 📈 技术趋势洞察

### 1. AI Agent Skill 生态爆发 🌋
日榜 16 个项目里至少 **7 个** 直接跟 "AI Agent Skill/Plugin" 相关：
- `agent-skills`（生产级技能）
- `taste-skill`（审美注入）
- `claude-skills`（345 个技能合集）
- `codex-plugin-cc`（跨 Agent 调用）
- `last30days-skill`（研究技能）
- `claude-video`（视频理解技能）
- `herdr`（Agent 多路复用）

这不再是"用 AI 写代码"的时代，而是"给 AI Agent 装技能包"的时代。就像 VS Code 的插件生态一样，Claude Code / Codex 正在建立自己的 Skill 市场。

### 2. Rust 在 AI 基础设施层持续扩张
- `meetily`（会议转录）用 Rust
- `RuView`（WiFi 感知）用 Rust
- `herdr`（Agent 多路复用）用 Rust

Rust 不再只是"系统编程语言"，它正在成为 AI 本地推理和实时处理的首选。性能+安全+本地部署需求完美匹配。

### 3. 多 Agent 编排成为新范式
- `gastown`（多 Agent 工作区管理器）
- `herdr`（Agent 多路复用器）
- `codex-plugin-cc`（Agent 间委派）
- 周榜 `orca`（并行 Agent 舰队的 ADE）

从"一个 Agent 干活"到"一群 Agent 协作"，编排层正在成为新的技术热点。

### 4. 语言热度
- **Rust**：AI 本地基础设施（3 个日榜项目）
- **JavaScript/TypeScript**：Agent Skill 和 Web Agent（主力）
- **Python**：AI 研究框架和数据管道
- **Go**：Agent 工具链和网络工具
- **Swift**：macOS 本地工具（语音/监控）

---

## 💡 值得深挖 TOP 3

### 1. 🔥 alirezarezvani/claude-skills
https://github.com/alirezarezvani/claude-skills
⭐+610/day | Python

345 个 Claude Code / Codex / Gemini CLI 技能合集，覆盖工程、营销、产品、合规、研究等方向。

**理由：** 这是一个"Agent 技能超市"，可以挑选适合主子工作流的技能直接集成。
**建议：** 浏览它的 skill 目录，把有价值的 skill 模式移植到 Hermes Agent 的 skill 系统里。

---

### 2. 🔥 firecrawl/firecrawl
https://github.com/firecrawl/firecrawl
⭐+867/day | TypeScript

Web 搜索/抓取/交互的 API，大规模数据采集利器。

**理由：** 如果主子在做 AI Agent 的数据采集管线，这个工具可以省掉大量爬虫开发时间。
**建议：** 看看能不能整合到 Hermes Agent 的数据采集流程中，替代部分 curl + 正则的方案。

---

### 3. 🔥 alibaba/zvec
https://github.com/alibaba/zvec
⭐+382/day | C++

阿里巴巴出的轻量级进程内向量数据库，主打"闪电快"。

**理由：** 本地 RAG 场景下，比 Chroma/Faiss 更轻更快。C++ 实现，进程内嵌入。
**建议：** 如果后续做本地知识库/RAG，可以 benchmark 对比一下。

---

## 📅 周榜亮点

### 持续霸榜
- **meetily**（Rust 会议助手）：周 +5,769，日 +2,494，双榜第一
- **herdr**（Agent 多路复用）：周 +4,348，日 +779，稳如老狗

### 本周新晋黑马

**usestrix/strix** ⭐+10,759/week | Python
AI 渗透测试工具，自动发现并修复应用漏洞。安全+AI 的结合引爆了关注。

**msitarzewski/agency-agents** ⭐+9,706/week | Shell
"完整的 AI 代理公司"——从前端开发到社区运营，每个 Agent 都有人设、流程和交付物。本质上是一个精心设计的 Prompt 角色库。

**JuliusBrussee/caveman** ⭐+7,780/week | JavaScript
给 Claude Code 装的"穴居人模式" Skill——用极简语言回复，省 65% token。"能用少 token 为啥用多 token？" 搞笑但实用。

**DeusData/codebase-memory-mcp** ⭐+6,309/week | C
代码智能 MCP 服务器，把代码库索引成知识图谱，158 种语言，毫秒级查询，省 99% token。

**alibaba/page-agent** ⭐+3,989/week | TypeScript
阿里出的 Web GUI Agent，用自然语言控制网页界面操作。

---

## 🎬 视频选题建议

### 选题 1：「AI Agent 的 Skill 系统：如何给你的编程 Agent 装 345 个技能」
切入点：从 claude-skills 和 agent-skills 两个项目入手，展示 AI Agent 从"裸奔"到"全副武装"的变化。对比 Hermes Agent 的 Skill 系统设计，讲清楚 Skill 生态为什么是 AI Agent 的下一个战场。

### 选题 2：「Rust 正在吃掉 AI 基础设施：从会议转录到 Agent 编排」
切入点：meetily（Rust 会议助手）+ herdr（Rust Agent 多路复用）+ RuView（Rust WiFi 感知），三个项目展示 Rust 在 AI 本地化场景的爆发。可以 benchmark 对比 Python 方案的性能差异。

---

## 📊 语言专项榜亮点

### Python 日榜
- `claude-skills`（345 技能合集）⭐+610
- `last30days-skill`（跨平台研究 Agent）⭐+458
- `claude-video`（给 Claude 看视频）⭐+427
- `TradingAgents`（多 Agent 金融交易框架）⭐+322
- `free-llm-api-resources`（免费 LLM API 资源列表）⭐+419

### TypeScript 日榜
- `firecrawl`（Web 抓取 API）⭐+867
- `alibaba/page-agent`（Web GUI Agent）⭐+892
- `OmniRoute`（免费 AI 网关，231+ 供应商）⭐+749
- `immich`（自托管照片管理）⭐+558

### Rust 日榜
- `meetily`（会议助手）⭐+2,494
- `herdr`（Agent 多路复用）⭐+779
- `RuView`（WiFi 空间感知）⭐+470
- `Handy`（离线语音转文字）⭐+84

### Go 日榜
- `gastown`（多 Agent 工作区管理器）⭐+291
- `agentsview`（Agent 会话分析/统计）⭐+247
- `ragflow`（RAG 引擎）⭐+96
- `sing-box`（通用代理平台）⭐+66

---

*数据采集时间：2026-07-07 09:00 | 数据源：GitHub Trending*
