# 🔥 GitHub 趋势速览 | 2026-06-09

**一句话总览：** AI Agent 技能生态大爆发——今天 trending 前 16 里有 11 个跟 AI Agent 直接相关，"Skills"（给 Agent 装技能包）已经取代 MCP 成为新的开源范式。

---

## 🚀 爆款项目 TOP 5（日增 star 最多）

### 1. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) ⭐+3,558/天
- **是什么：** 一个 AI Agent 技能包，能自动调研 Reddit、X、YouTube、HN、Polymarket 等平台最近 30 天的信息，生成综合报告
- **为什么火：** 把"信息搜集+摘要"这个最常见的 Agent 场景做成了即插即用的 skill，零配置上手
- **对主子的价值：** 做技术趋势追踪、竞品调研的现成工具，可以直接拿来用或参考其架构做自己的调研 skill

### 2. [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) ⭐+1,729/天
- **是什么：** 基于 TurboQuant 构建的向量索引，Rust 实现 + Python 绑定
- **为什么火：** 号称在向量检索性能上有突破，Rust 底层保证速度，Python 接口降低使用门槛
- **对主子的价值：** 如果做 RAG 或语义搜索相关的项目，可以关注其 benchmark 数据

### 3. [aaif-goose/goose](https://github.com/aaif-goose/goose) ⭐+699/天
- **是什么：** 开源可扩展 AI Agent，不只是代码补全——能安装、执行、编辑、测试，支持任意 LLM
- **为什么火：** 定位 Claude Code / Cursor 的开源替代，Rust 实现性能好
- **对主子的价值：** 值得 clone 体验一下，看看跟 Hermes Agent 的差异点在哪

### 4. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) ⭐+679/天
- **是什么：** 给 AI Agent 一双"眼睛"——一个 CLI 工具让 Agent 能读取和搜索 Twitter、Reddit、YouTube、GitHub、B站、小红书，零 API 费用
- **为什么火：** 打通了 Agent 获取中文互联网信息的痛点，B站+小红书覆盖是亮点
- **对主子的价值：** 如果要做中文内容调研的 Agent，这个工具直接解决信息源问题

### 5. [refactoringhq/tolaria](https://github.com/refactoringhq/tolaria) ⭐+651/天
- **是什么：** 桌面端 Markdown 知识库管理应用
- **为什么火：** 轻量级本地知识库方案，TypeScript 实现，跨平台
- **对主子的价值：** 如果需要管理本地文档/笔记，可以试试

---

## 📈 技术趋势洞察

### 1. "AI Skills" 生态全面爆发
今天最明显的趋势：**Skills（技能包）已经取代 MCP 成为 Agent 生态的新货币**。trending 里出现了一大波 "xxx-skills"、"pm-skills"、"ui-skills"、"google/skills" 这类项目。开发者不再只是给 Agent 接工具，而是把能力封装成标准化的 skill 文件，即插即用。

### 2. Agent 信息采集工具链成型
last30days-skill、Agent-Reach 这类项目说明：**让 Agent 能"看到"互联网**是刚需。过去 Agent 只能操作代码，现在需要它能读社交媒体、搜索新闻、抓取视频内容。这个方向会持续增长。

### 3. Rust 在 AI 基础设施中加速渗透
turbovec（向量索引）、goose（AI Agent）、microsoft/pg_durable（PostgreSQL 持久执行）、sniffnet（网络监控）——Rust 在性能敏感的 AI 基础设施层越来越多。Python 做上层，Rust 做底层的分层模式正在固化。

### 4. "反 AI 味" 工具出现
周榜里的 [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)（移除 AI 写作痕迹）和 [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)（让 AI 有品味）说明：**用户开始反感 AI 生成内容的"模板味"**，"去 AI 味"本身成了一个细分赛道。

### 5. 语言热度
- **Python** 依然是 AI/Agent 项目的第一语言，今天 Python trending 里几乎全是 AI 相关
- **TypeScript** 在 Agent 前端框架（CopilotKit）和桌面应用（tolaria）上发力
- **Rust** 在底层工具链持续扩张
- **Go** 在 CLI 工具和基础设施层面稳定（trivy、rclone、d2）

---

## 💡 值得深挖 TOP 3

### 1. [chopratejas/headroom](https://github.com/chopratejas/headroom) ⭐+14,266/周
- **理由：** 周增 1.4 万 star，解决的是 LLM 调用中 token 浪费的痛点——压缩工具输出、日志、RAG chunk，减少 60-95% token 用量
- **建议：** 如果主子有 LLM 应用在跑，token 成本高的话这个值得集成。可以先看看它的压缩策略是否适合自己的场景

### 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) ⭐+11,747/周
- **理由：** 周增 1.17 万 star（没错，就是我们自己）。说明 Hermes Agent 的"技能系统"理念正在被社区认可
- **建议：** 持续关注社区反馈，Skills 生态的爆发对我们是利好

### 3. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) ⭐+7,597/周
- **理由：** "给 AI 好品味"——一个 skill 文件就能让 AI 输出不再无聊泛泛，周增 7.6k star
- **建议：** 可以直接装到 Hermes Agent 试试效果，或者参考其 prompt 设计思路优化自己的输出风格

---

## 📅 周榜亮点

### 持续霸榜
- **microsoft/markitdown**（+11,177/周）：文件转 Markdown 工具，微软出品，持续火热
- **harry0703/MoneyPrinterTurbo**（+5,574/周）：AI 一键生成短视频，中文社区长期热门
- **mvanhorn/last30days-skill**：日榜第一，周榜也在前三

### 本周新晋黑马
- **chopratejas/headroom**：LLM token 压缩工具，周增 1.4 万，直接空降周榜第一
- **affaan-m/ECC**（+9,301/周）：Agent 性能优化系统，给 Claude Code/Codex 加技能、记忆、安全层
- **pbakaus/impeccable**（+3,736/周）：让 AI Agent 擅长设计的"设计语言"skill 文件
- **can1357/oh-my-pi**（+1,952/周）：终端 AI 编码 Agent，主打 hash 锚定编辑和 LSP 支持

---

## 🎬 视频选题建议

### 选题 1：「AI Agent 技能系统大爆发：Skills 为什么取代了 MCP？」
- **切入点：** 从今天 trending 里十几个 skills 相关项目切入，讲解 Agent 技能生态的演进——从 function calling → MCP → Skills 的三代范式变迁
- **素材：** last30days-skill、google/skills、pm-skills、taste-skill 等实际案例
- **时长预估：** 10-15 分钟

### 选题 2：「给你的 AI 装上互联网之眼：Agent-Reach 实测」
- **切入点：** 实测 Agent-Reach 这个工具，演示如何让 AI Agent 一键读取 Twitter、B站、小红书等平台内容，零 API 费用
- **素材：** 实际演示 CLI 操作，对比传统 API 方案的成本和复杂度
- **时长预估：** 8-12 分钟

---

## 📊 完整数据附录

### 日榜 TOP 16（全语言）
| # | 项目 | 日增⭐ | 语言 | 简介 |
|---|------|--------|------|------|
| 1 | mvanhorn/last30days-skill | +3,558 | Python | AI Agent 跨平台调研技能包 |
| 2 | RyanCodrai/turbovec | +1,729 | Python | Rust 向量索引 + Python 绑定 |
| 3 | roboflow/supervision | +1,288 | Python | 计算机视觉工具库 |
| 4 | aaif-goose/goose | +699 | Rust | 开源可扩展 AI Agent |
| 5 | Panniantong/Agent-Reach | +679 | Python | Agent 互联网信息采集 CLI |
| 6 | refactoringhq/tolaria | +651 | TypeScript | Markdown 知识库桌面应用 |
| 7 | TapXWorld/ChinaTextbook | +592 | Roff | 中国教材 PDF 合集 |
| 8 | google/skills | +461 | Python | Google 产品 Agent 技能包 |
| 9 | CopilotKit/CopilotKit | +378 | TypeScript | Agent 前端框架 + AG-UI 协议 |
| 10 | luongnv89/claude-howto | +312 | Python | Claude Code 可视化教程 |
| 11 | santifer/career-ops | +308 | JS | AI 求职系统 |
| 12 | openai/plugins | +296 | JS | OpenAI 插件集合 |
| 13 | ibelick/ui-skills | +261 | TypeScript | 设计工程师技能包 |
| 14 | MemPalace/mempalace | +170 | Python | 开源 AI 记忆系统 |
| 15 | phuryn/pm-skills | +164 | — | PM 技能市场 100+ 技能 |
| 16 | Andyyyy64/whichllm | +143 | Python | 本地 LLM 硬件适配测评 |

### 周榜 TOP 18
| # | 项目 | 周增⭐ | 语言 | 简介 |
|---|------|--------|------|------|
| 1 | chopratejas/headroom | +14,266 | Python | LLM token 压缩工具 |
| 2 | microsoft/markitdown | +11,177 | Python | 文件转 Markdown |
| 3 | NousResearch/hermes-agent | +11,747 | Python | 可成长 AI Agent |
| 4 | affaan-m/ECC | +9,301 | JS | Agent 性能优化系统 |
| 5 | Leonxlnx/taste-skill | +7,597 | Shell | 让 AI 有品味 |
| 6 | mvanhorn/last30days-skill | +6,616 | Python | 跨平台调研技能包 |
| 7 | harry0703/MoneyPrinterTurbo | +5,574 | Python | AI 一键生成短视频 |
| 8 | lfnovo/open-notebook | +3,891 | TypeScript | 开源 NotebookLM |
| 9 | pbakaus/impeccable | +3,736 | JS | 设计语言 skill |
| 10 | Panniantong/Agent-Reach | +3,006 | Python | Agent 信息采集 |
| 11 | Open-LLM-VTuber/Open-LLM-VTuber | +2,528 | Python | 本地 LLM VTuber |
| 12 | supermemoryai/supermemory | +2,434 | TypeScript | AI 时代记忆引擎 |
| 13 | can1357/oh-my-pi | +1,952 | TypeScript | 终端 AI 编码 Agent |
| 14 | revfactory/harness | +1,553 | HTML | Agent 团队元技能 |
| 15 | hardikpandya/stop-slop | +1,498 | — | 去 AI 味 skill |
| 16 | openai/plugins | +899 | JS | OpenAI 插件 |
| 17 | aquasecurity/trivy | +919 | Go | 容器安全扫描 |
| 18 | phuryn/pm-skills | +640 | — | PM 技能市场 |
