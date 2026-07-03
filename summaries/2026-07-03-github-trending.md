# 🔥 GitHub 趋势速览 — 2026年7月3日（周五）

## 📌 一句话总览

**AI Agent 生态全面爆发。** 今天 GitHub Trending 日榜 17 个项目里有 **14 个直接跟 AI Agent 相关**——从技能框架、记忆系统、多路复用器到垂直领域 Agent（交易、渗透测试、招聘、视频剪辑），已经不是"AI Agent 很火"的问题了，是整个开源社区都在围着 Agent 转。

---

## 🚀 爆款项目 TOP 5

### 1. msitarzewski/agency-agents ⭐+3,032/day
🔗 https://github.com/msitarzewski/agency-agents

**一句话说清楚：** 一个完整的 AI 代理公司模板——前端开发、Reddit 运营、产品经理等各种专业 Agent，每个都有独立人设、流程和交付物。

**为什么火：** 不是又一个 Agent 框架，而是一套可以直接用的 Agent "人设模板"。解决了"怎么让 Agent 像专家一样干活"的痛点，Shell 脚本就能跑。

**对主子的价值：** 直接拿来当 Hermes Agent 的 skills 模板用。做视频选题也不错——"用 AI 搭建一家完整的公司"。

---

### 2. usestrix/strix ⭐+2,137/day（周榜 ⭐+4,743）
🔗 https://github.com/usestrix/strix

**一句话说清楚：** 开源 AI 渗透测试工具，自动发现并修复应用漏洞。

**为什么火：** 把安全测试 Agent 化了。以前需要安全专家干的活，现在 AI Agent 自动扫描+修复。Python 写的，门槛低。

**对主子的价值：** 安全方向值得关注，可以给自己项目跑一遍。视频选题："让 AI 黑客攻击你的代码会怎样"。

---

### 3. HKUDS/Vibe-Trading ⭐+939/day
🔗 https://github.com/HKUDS/Vibe-Trading

**一句话说清楚：** 港大出品，你的个人 AI 交易 Agent。

**为什么火：** 学术背景（港大）+ 实用场景（量化交易）。"Vibe-Trading"这个名字很潮，把 vibe coding 延伸到了交易领域。

**对主子的价值：** 如果有量化交易兴趣，这是目前最火的开源方案。但金融领域风险大，建议先看看论文和方法论再决定。

---

### 4. JuliusBrussee/caveman ⭐+926/day
🔗 https://github.com/JuliusBrussee/caveman

**一句话说清楚：** Claude Code 技能——通过"原始人说话方式"省掉 65% 的 token。

**为什么火：** "why use many token when few token do trick" 🪨。名字搞笑，效果实在。解决了一个真痛点——AI 编码工具 token 消耗太高。用极度精简的 prompt 格式让 Claude 照样干活。

**对主子的价值：** 立刻能用！装到 Claude Code 里省 token 省钱。做视频选题也很有趣——"教 AI 说原始人话省 65% 成本"。

---

### 5. hasaneyldrm/exercises-dataset ⭐+938/day
🔗 https://github.com/hasaneyldrm/exercises-dataset

**一句话说清楚：** 433 个健身动作的完整数据集——名称、目标肌群、器材、教学、动画视频全有。

**为什么火：** 健身 + 开源数据，两个热门领域交叉。数据结构清晰，做健身 App 或者 AI 健身教练可以直接用。

**对主子的价值：** 今天唯一的非 AI 项目进 TOP 5，说明数据类项目依然有需求。如果有健身 App 想法可以直接 clone。

---

## 📈 技术趋势洞察

### 🔥 最热的方向

1. **AI Agent 基础设施层**——不再是"做一个 Agent"，而是"做 Agent 的生态"：
   - **技能规范**：[agentskills/agentskills](https://github.com/agentskills/agentskills)（Agent Skills 标准化文档）
   - **记忆系统**：[topoteretes/cognee](https://github.com/topoteretes/cognee)（周榜 ⭐+4,531，给 Agent 持久记忆）
   - **多路复用**：[ogulcancelik/herdr](https://github.com/ogulcancelik/herdr)（Rust 写的终端 Agent 多路复用器）、[stablyai/orca](https://github.com/stablyai/orca)（并行 Agent 的 IDE）
   - **互联网接入**：[Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)（周榜 ⭐+8,265，让 Agent 能读 Twitter/Reddit/YouTube/B站/小红书）

2. **Claude Code / Codex 生态工具**——围绕 AI 编码工具的"周边经济"：
   - [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) — 省 token
   - [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) — Claude Code 里调 Codex
   - [affaan-m/ECC](https://github.com/affaan-m/ECC) — Agent harness 性能优化
   - [obra/superpowers](https://github.com/obra/superpowers) — Agent 技能框架

3. **垂直领域 Agent 井喷**——Agent 从通用走向专业：
   - 安全：[usestrix/strix](https://github.com/usestrix/strix)（渗透测试）
   - 交易：[HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)（量化交易）
   - 招聘：[interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent)（简历评估）
   - 视频：[browser-use/video-use](https://github.com/browser-use/video-use) + [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)（视频制作）
   - 求职：[santifer/career-ops](https://github.com/santifer/career-ops)（AI 求职系统）

### 📊 语言/框架热度

| 语言 | 日榜占比 | 趋势 | 主要场景 |
|------|---------|------|---------|
| Python | 41% | 🔥 稳定热门 | AI Agent、ML、数据 |
| TypeScript | 29% | 📈 上升 | Agent 前端工具、设计系统 |
| JavaScript | 18% | ➡️ 持平 | 通用工具、技能脚本 |
| Rust | 6% | 📈 缓慢上升 | Agent 沙箱、高性能工具 |
| Shell | 6% | ⬆️ 意外上榜 | Agent 技能配置 |
| Go | — | ➡️ 稳定 | 基础设施工具 |

### 🆕 新范式信号

- **Agent Skills 标准化**：[agentskills/agentskills](https://github.com/agentskills/agentskills) 试图给 Agent 技能写规范文档，就像 OpenAPI 之于 REST API
- **Design.md 范式**：Google Labs 的 [design.md](https://github.com/google-labs-code/design.md)（周榜 ⭐+6,240）提出让 Agent 理解视觉设计规范
- **"原始人 prompt" 范式**：caveman 证明极简 prompt 也能让 AI 干活，可能是对"越复杂越好"的反叛

---

## 💡 值得深挖 TOP 3

### 1. DeusData/codebase-memory-mcp（周榜 ⭐+9,873）
🔗 https://github.com/DeusData/codebase-memory-mcp

**理由：** 把代码库索引成持久化知识图谱的 MCP 服务器，平均毫秒级索引一个仓库。C 写的，性能炸裂。

**建议：** 必须 clone 试试。给大型项目用，看看知识图谱效果如何。整合进 Hermes Agent 的代码分析能力也很有潜力。

### 2. calesthio/OpenMontage（周榜 ⭐+10,199，本周最高）
🔗 https://github.com/calesthio/OpenMontage

**理由：** 号称全球首个开源 Agentic 视频制作系统——12 条流水线、52 个工具、500+ Agent 技能。把 AI 编码工具变成视频编辑器。

**建议：** 做视频选题！这是本周 star 增长最高的项目，话题性极强。"AI 自动剪视频"是所有人关心的话题。

### 3. topoteretes/cognee（周榜 ⭐+4,531）
🔗 https://github.com/topoteretes/cognee

**理由：** 开源 AI 记忆平台，让 Agent 跨会话有持久记忆。这个方向是 Agent 从"工具"变成"同事"的关键。

**建议：** 深入研究架构设计，考虑整合进自己的 Agent 工作流。记忆系统是 Agent 产品化的核心竞争力之一。

---

## 📅 周榜亮点

### 持续霸榜
- **msitarzewski/agency-agents**：日榜 #1 + 周榜 ⭐+9,484，Agent 模板赛道绝对的王者
- **usestrix/strix**：日榜 + 周榜双上榜，AI 安全测试赛道领头羊

### 本周新晋黑马 🐴
- **calesthio/OpenMontage**（⭐+10,199/week）：开源视频制作，本周全站第一
- **DeusData/codebase-memory-mcp**（⭐+9,873/week）：代码知识图谱 MCP，技术含量最高的项目
- **Panniantong/Agent-Reach**（⭐+8,265/week）：让 Agent 读全网数据，解决 Agent "看不见互联网"的痛点
- **xbtlin/ai-berkshire**（⭐+6,989/week）：AI 价值投资框架，巴菲特+芒格方法论 + 多 Agent 并行研究
- **simplex-chat/simplex-chat**（⭐+6,376/week）：无用户标识的隐私通讯，Haskell 写的，跟 AI Agent 无关但涨得猛

### 日榜 vs 周榜差异
日榜 17 个项目里有 14 个是 Agent 相关的。周榜 23 个项目里多了几个非 Agent 项目（simplex-chat、free-for-dev、MediaCrawler），说明 Agent 热度是**最近几天集中爆发**的。

---

## 🎬 视频选题建议

### 选题 1：「2026 年 AI Agent 生态全景——从工具到同事的进化」
**素材：** 今天 trending 里 80%+ 都是 Agent 项目，做一个全景梳理。可以分成：基础设施层（记忆、技能规范、MCP）→ 工具层（多路复用器、IDE）→ 应用层（交易、安全、招聘、视频）。配合 agency-agents、cognee、OpenMontage 做实操演示。

### 选题 2：「教 AI 说原始人话，省 65% Token 钱 💰」
**素材：** 以 caveman 项目为切入点，演示安装和效果对比。可以延伸到各种 AI 编码工具的 token 优化技巧。话题轻松有趣，受众广。

---

## 📊 各语言日榜 TOP 3

### Python
1. [usestrix/strix](https://github.com/usestrix/strix) ⭐+2,137 — AI 渗透测试
2. [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) ⭐+939 — 交易 Agent
3. [browser-use/video-use](https://github.com/browser-use/video-use) ⭐+554 — Agent 视频编辑

### TypeScript
1. [facebook/react-design-system](https://github.com/facebook) ⭐+1,108 — Agent-ready 设计系统
2. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) ⭐+837 — AI 网关（231+ 提供商）
3. [yikart](https://github.com/yikart) ⭐+462 — AI 赚钱工具

### Rust
1. [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) ⭐+571 — 终端 Agent 多路复用器
2. [TencentCloud](https://github.com/TencentCloud) ⭐+314 — AI Agent 沙箱
3. [Zackriya-Solutions](https://github.com/Zackriya-Solutions) ⭐+138 — AI 会议助手

### Go
1. [yorukot](https://github.com/yorukot) ⭐+252 — 终端文件管理器
2. [ollama](https://github.com/ollama) ⭐+86 — 本地 LLM 运行器
3. [go-vikunja](https://github.com/go-vikunja) ⭐+42 — 自托管 Todo 应用

---

*报告生成时间：2026-07-03 09:00 CST*
*数据来源：GitHub Trending（日榜 + 周榜 + Python/TypeScript/Rust/Go 分语言榜）*
