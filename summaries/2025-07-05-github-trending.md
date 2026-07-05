# 🔥 GitHub 趋势速览 — 2025年7月5日

## 一句话总览

**AI Agent 工具链全面井喷。** 今天的 GitHub Trending 几乎被 Agent Skills、MCP 服务器、Agent 编排工具和 Claude Code 生态项目屠榜了。"Agent 基础设施"已从概念进入实用阶段。

---

## 🚀 爆款项目 TOP 5

### 1. usestrix/strix ⭐+1,904/天（周+9,362）
🔗 https://github.com/usestrix/strix

**干什么的：** 开源 AI 渗透测试工具，自动发现并修复应用安全漏洞。

**为什么火：** AI + 安全赛道的杀手级应用。把原本需要高级安全工程师干的渗透测试工作自动化了，对中小企业来说直接省掉一笔安全审计费用。

**跟主子的关系：** 如果主子有 Web 应用或 API，可以直接拿来扫一遍。也是很好的安全类视频选题——"让 AI 帮你黑自己的网站"。

---

### 2. JuliusBrussee/caveman ⭐+1,089/天
🔗 https://github.com/JuliusBrussee/caveman

**干什么的：** Claude Code 的 Skill 插件，通过"像原始人一样说话"砍掉 65% 的 token 消耗。

**为什么火：** 简单粗暴但有效。AI 编码助手最大的成本就是 token，这玩意直接帮你省钱。思路很巧妙——用精简的 prompt 模式让 Claude 理解意图但不浪费 token。

**跟主子的关系：** 如果主子日常用 Claude Code，装上直接省钱。视频选题也不错——"如何让你的 AI 编码助手省 65% 的钱"。

---

### 3. mattpocock/skills ⭐+973/天
🔗 https://github.com/mattpocock/skills

**干什么的：** Matt Pocock（TypeScript 知名教育者）分享的 Claude Code Skills 集合，来自他真实的 `.claude` 配置目录。

**为什么火：** 大佬的实战配置直接开源，质量有保证。"Skills for Real Engineers"这个标题就够吸引人——不是玩具，是真在生产环境用的。

**跟主子的关系：** 直接抄作业。看看高手怎么配置 Claude Code 的，学习 Skill 的写法，整合到自己的工作流。

---

### 4. alibaba/page-agent ⭐+742/天（周+2,484）
🔗 https://github.com/alibaba/page-agent

**干什么的：** 阿里出品的浏览器内 GUI Agent，用自然语言控制网页界面。

**为什么火：** 大厂出品 + 实用场景。能直接在网页里跑的 Agent，不依赖外部工具，对 RPA 和自动化测试场景很有价值。

**跟主子的关系：** 值得关注。可以用来做网页自动化、数据抓取、或者给现有 Web 应用加一层 AI 控制层。

---

### 5. openai/codex-plugin-cc ⭐+718/天（周+1,974）
🔗 https://github.com/openai/codex-plugin-cc

**干什么的：** OpenAI 官方出的插件，让你在 Claude Code 里直接调用 Codex 来审查代码或委派任务。

**为什么火：** OpenAI 给竞品（Claude Code）出插件，这个姿态很有意思。说明 AI 编码助手的"互操作性"正在成为趋势——不再锁定单一工具。

**跟主子的关系：** 如果同时用 Claude Code 和 Codex，装上就能让两个 AI 互相 review 代码。视频选题："让两个 AI 互相审查代码会怎样？"

---

## 📈 技术趋势洞察

### 🔥 正在涨的方向

1. **Agent Skills 标准化** — `agentskills/agentskills`（⭐+351/天）在推动 Agent Skills 开放标准，多个项目都在跟进。这意味着 Agent 的"能力插件"正在形成生态。

2. **MCP 协议遍地开花** — `DeusData/codebase-memory-mcp`（周+9,517）、`ChromeDevTools/chrome-devtools-mcp`（日+304）、`CoplayDev/unity-mcp`，MCP 已经是 AI 工具链的事实标准协议。

3. **AI 视频制作** — `browser-use/video-use`（周+4,174）和 `calesthio/OpenMontage`（周+8,447）两个视频项目同时上榜，AI 视频编辑赛道在升温。

4. **Claude Code 生态** — caveman、codex-plugin-cc、mattpocock/skills、alirezarezvani/claude-skills（337个技能）、hesreallyhim/awesome-claude-code… Claude Code 的工具生态正在快速成熟。

5. **AI 金融分析** — `ZhuLinsen/daily_stock_analysis`（周+3,842）和 `xbtlin/ai-berkshire`（周+5,984），用 AI 做投资分析的需求在爆发。

### 📊 语言热度

| 语言 | 上榜项目数 | 趋势 |
|------|-----------|------|
| Python | 最多 | Agent框架、安全、教育 |
| TypeScript | 次多 | 前端Agent、UI工具 |
| Rust | 稳定增长 | 高性能Agent、系统工具 |
| Go | 偏少 | 基础设施、DevOps |

### 💡 新范式

- **Agent 多路复用**：`herdr`（⭐+707/天）让你在终端里同时跑多个 Agent，类似 Agent 的 tmux
- **Agent 记忆持久化**：`cognee`（周+3,388）给 Agent 加长期记忆的知识图谱
- **Agent 编排桌面**：`orca`（周+3,790）提供并行 Agent 管理的桌面环境

---

## 💡 值得深挖 TOP 3

### 1. DeusData/codebase-memory-mcp（周+9,517）
**理由：** 把代码库索引成知识图谱，毫秒级查询，节省 99% token。单二进制零依赖。
**建议：** 必须试试。直接 `clone` 下来配上你的项目，看看它对代码理解和 Agent 效率的提升。

### 2. browser-use/video-use（周+4,174）
**理由：** 用编程 Agent 编辑视频，思路很新。从 browser-use 团队出品，质量有保障。
**建议：** 做视频选题的好素材。"用 AI Agent 剪视频"这个题材本身就自带流量。

### 3. ogulcancelik/herdr（日+707，周+3,506）
**理由：** 终端里的 Agent 多路复用器，Rust 写的，性能没问题。解决了同时管理多个 Agent 的痛点。
**建议：** `clone` 试试。如果你日常需要多个 Agent 并行干活，这是目前最优雅的方案。

---

## 📅 周榜亮点

### 持续霸榜
- **usestrix/strix** — 日榜周榜都是 TOP 级别，AI 安全赛道最火项目
- **DeusData/codebase-memory-mcp** — 周榜第2（+9,517），代码智能 MCP 服务器的标杆

### 本周新晋黑马
- **msitarzewski/agency-agents**（周+10,976）— "一整个 AI 代理公司"的 Agent 集合，从前端到社区运营全覆盖，本周最猛
- **calesthio/OpenMontage**（周+8,447）— 把 AI 编码助手变成视频制作工作室，52 个工具 500+ Agent Skills
- **diegosouzapw/OmniRoute**（周+4,133）— 免费 AI 网关，一个端点连 231+ 提供商，还有 token 压缩

### 日榜 vs 周榜差异
日榜偏"小工具"（caveman、skills 集合），周榜偏"大系统"（OpenMontage、OmniRoute、orca）。说明大项目需要持续关注度才能上周榜，而小工具容易一天爆火。

---

## 🎬 视频选题建议

### 选题 1：「让 AI 黑掉你的网站」
**核心：** 用 strix 对一个真实应用做渗透测试，展示 AI 安全工具的能力。
**流量点：** 安全 + AI + 实操演示，天然有戏剧性。可以加上"AI 发现了人类遗漏的漏洞"之类的 hook。

### 选题 2：「AI Agent 工具链全家桶体验」
**核心：** 把今天最火的几个 Agent 工具串起来演示——用 herdr 管理多个 Agent、page-agent 控制网页、caveman 省 token、codebase-memory-mcp 做代码记忆。
**流量点：** "2025年 AI 开发者必备工具包"，实用性强，适合做成系列。

---

## 📋 完整数据附录

### 日榜 TOP 18（全部语言）

| # | 项目 | ⭐/天 | 语言 | 简介 |
|---|------|-------|------|------|
| 1 | usestrix/strix | +1,904 | Python | AI 渗透测试 |
| 2 | JuliusBrussee/caveman | +1,089 | JS | Claude Code 省 65% token |
| 3 | mattpocock/skills | +973 | Shell | 工程师实战 Skills |
| 4 | alibaba/page-agent | +742 | TS | 浏览器 GUI Agent |
| 5 | openai/codex-plugin-cc | +718 | JS | Codex × Claude Code 联动 |
| 6 | Zackriya-Solutions/meetily | +718 | Rust | 本地 AI 会议助手 |
| 7 | ogulcancelik/herdr | +707 | Rust | Agent 多路复用器 |
| 8 | asgeirtj/system_prompts_leaks | +471 | JS | 系统提示词泄露集 |
| 9 | harvard-edge/cs249r_book | +443 | Python | ML 系统教材 |
| 10 | rommapp/romm | +398 | Python | 自托管 ROM 管理器 |
| 11 | agentskills/agentskills | +351 | Python | Agent Skills 标准 |
| 12 | ChromeDevTools/chrome-devtools-mcp | +304 | TS | Chrome DevTools MCP |
| 13 | immich-app/immich | +201 | TS | 自托管照片管理 |
| 14 | chthollyphile/folia-major | +175 | TS | 歌词动画音乐播放器 |
| 15 | alirezarezvani/claude-skills | +136 | Python | 337 个 Claude Skills |
| 16 | alirezarezvani/claude-skills | +136 | Python | Agent Skills 大合集 |
| 17 | dotnet/skills | +59 | C# | .NET Agent Skills |
| 18 | crynta/terax-ai | +62 | TS | 7MB 轻量 AI 开发环境 |

### 周榜 TOP 22

| # | 项目 | ⭐/周 | 语言 | 简介 |
|---|------|-------|------|------|
| 1 | msitarzewski/agency-agents | +10,976 | Shell | AI 代理公司 Agent 集 |
| 2 | DeusData/codebase-memory-mcp | +9,517 | C | 代码知识图谱 MCP |
| 3 | usestrix/strix | +9,362 | Python | AI 渗透测试 |
| 4 | calesthio/OpenMontage | +8,447 | Python | AI 视频制作系统 |
| 5 | xbtlin/ai-berkshire | +5,984 | Python | AI 价值投资框架 |
| 6 | simplex-chat/simplex-chat | +4,630 | Haskell | 零标识符隐私聊天 |
| 7 | browser-use/video-use | +4,174 | Python | Agent 视频编辑 |
| 8 | diegosouzapw/OmniRoute | +4,133 | TS | 免费 AI 网关 231+ 提供商 |
| 9 | stablyai/orca | +3,790 | TS | 并行 Agent 桌面 |
| 10 | ZhuLinsen/daily_stock_analysis | +3,842 | Python | LLM 股票分析系统 |
| 11 | JCodesMore/ai-website-cloner-template | +3,730 | TS | AI 网站克隆模板 |
| 12 | ogulcancelik/herdr | +3,506 | Rust | Agent 多路复用 |
| 13 | topoteretes/cognee | +3,388 | Python | Agent 记忆知识图谱 |
| 14 | alibaba/page-agent | +2,484 | TS | 浏览器 GUI Agent |
| 15 | openai/codex-plugin-cc | +1,974 | JS | Codex × Claude Code |
| 16 | Robbyant/lingbot-map | +2,065 | Python | 3D 场景重建 |
| 17 | interviewstreet/hiring-agent | +1,647 | Python | AI 简历评估 |
| 18 | logto-io/logto | +1,488 | TS | SaaS/AI 应用认证授权 |
| 19 | allenai/olmocr | +1,229 | Python | PDF 线性化工具 |
| 20 | Starmel/OpenSuperWhisper | +499 | Swift | macOS 语音转文字 |
| 21 | craft-ai-agents/craft-agents-oss | +341 | TS | Craft AI Agents |
| 22 | apache/maven | +157 | Java | Apache Maven |

---

*报告生成时间：2025-07-05 09:00 | 数据来源：GitHub Trending*
