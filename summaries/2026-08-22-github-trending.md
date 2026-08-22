# 🔥 GitHub 趋势速览 — 2026年8月22日（周六）

## 一句话总览

**今天 GitHub 被「AI Agent 技能/工具链」生态彻底占领。** 从 Agent 技能集、Agent 记忆系统、Agent 安全审计到 Agent 插件规范——至少 8 个 trending 项目直接围绕「让 AI 编程助手更强」展开。与此同时，Rust 本地优先工具、Mojo 语言生态和 AI 短视频生成也在持续爆发。

---

## 🚀 爆款项目 TOP 5

### 1. mattpocock/skills — ⭐+3,362/天（总 229K）
🔗 https://github.com/mattpocock/skills

**是什么：** TypeScript 之父 Matt Pocock 公开的 AI 编程 Agent 技能集，直接从他的 `.agents` 目录提取，覆盖「真正的工程师」日常开发场景。

**为什么火：** Matt Pocock 本人在 TS 社区的影响力 + 实用性极强的 skills 模板。大家发现 Claude Code / Codex 的效果差距就在 skills 配置上，这个项目相当于「学霸的笔记公开了」。

**对主子的价值：** 直接 clone 下来挑适合自己工作流的 skills 用，或者作为写自己 skills 的参考模板。

---

### 2. AprilNEA/OpenLogi — ⭐+1,380/天（总 12.9K）
🔗 https://github.com/AprilNEA/OpenLogi

**是什么：** 用 Rust 写的罗技 Options+ 本地替代品。支持鼠标按键重映射、DPI 调节、SmartShift 配置，走 HID++ 协议，不需要登录账号，不收集遥测数据。

**为什么火：** 罗技 Options+ 一直被人吐槽又卡又要联网，Rust 原生替代方案 + 本地优先 + 无遥测，戳中了所有痛点。

**对主子的价值：** 如果用罗技鼠标，可以直接换这个。Rust 写的，性能好还不烦人。

---

### 3. harry0703/MoneyPrinterTurbo — ⭐+1,201/天（总 113K）
🔗 https://github.com/harry0703/MoneyPrinterTurbo

**是什么：** 输入主题/关键词，AI 大模型 + 自动化工作流一键生成高清短视频。中文项目，国内热度极高。

**为什么火：** 短视频赛道的 AI 自动化刚需，113K 星说明一切。持续霸榜。

**对主子的价值：** 做视频内容的利器，可以研究它的工作流设计思路，或者直接用来批量生成内容。

---

### 4. mahlernim/google-timeline-visualizer — ⭐+1,053/天（总 2.2K）
🔗 https://github.com/mahlernim/google-timeline-visualizer

**是什么：** Kotlin 写的 Google 位置历史（Timeline）数据可视化工具，把你一年的出行轨迹变成漂亮的可视化图表。

**为什么火：** Google Timeline 即将关闭/迁移的传闻让很多人开始导出自己的数据，这个项目正好解决了「导出来之后怎么看」的问题。

**对主子的价值：** 有趣的数据可视化项目，可以把自己的出行数据玩一玩。Kotlin 写的，Android 友好。

---

### 5. santifer/career-ops — ⭐+921/天（总 67K）
🔗 https://github.com/santifer/career-ops

**是什么：** 开源 AI 求职工具——自动扫描招聘网站、用 A-F 评分体系给岗位打分（1.0-5.0）、定制简历、追踪申请进度。跑在本地 AI 编程 CLI 里（Claude Code、Codex 等）。

**为什么火：** 就业市场卷 + AI Agent 能自动化求职流程 = 精准戳中痛点。直接在终端里跑，不需要额外 SaaS。

**对主子的价值：** 虽然主子可能不需要找工作，但这个项目展示了 AI Agent 如何端到端解决复杂流程问题，架构设计值得参考。

---

## 📈 技术趋势洞察

### 1. AI Agent 技能/工具链生态大爆发 🔥🔥🔥

今天最显著的趋势。以下项目全部围绕「让 AI 编程 Agent 更好用」：

| 项目 | 方向 | 日增 |
|------|------|------|
| mattpocock/skills | Agent 技能集 | +3,362 |
| obra/superpowers | Agent 开发方法论 | +790 |
| affaan-m/ECC | Agent 性能优化系统 | +357 |
| cursor/plugins | Cursor 插件规范 | +388 |
| ruvnet/ruflo | Agent 多智能体编排 | +140 |
| apache/maka | Agent 工作空间（Apache 孵化） | +148 |
| Tencent/AI-Infra-Guard | AI 红队安全审计 | +434 |

**结论：** AI 编程不再是「谁的模型好」的竞赛，而是「谁的 Agent 生态好」的竞赛。技能集、插件、记忆系统、安全审计——一个完整的 Agent 工具链生态正在成型。

### 2. Rust 持续渗透桌面工具

OpenLogi（鼠标驱动）、ai-memory（Agent 记忆）、nautilus_trader（交易引擎）、Switchyard（LLM 路由）——Rust 正在从系统层走向「替代 Electron/Python 桌面工具」的阶段。

### 3. Mojo 语言有了重量级项目

modular/modular（Mojo 语言本体）日增 913，周增 1,643。28K 星说明 Mojo 不再是玩具，开始有真实的社区和生态。

### 4. 本地优先（Local-first）成为主流叙事

OpenLogi（无遥测）、Apache Maka（本地 Agent 工作空间）、career-ops（本地运行）、google-timeline-visualizer（本地可视化）——「不联网也能干活」成了卖点。

### 5. 语言热度

- **Python**：依然是 AI 项目的绝对主力语言
- **Rust**：桌面工具 + 基础设施层增长强劲
- **TypeScript**：Agent 插件/生态层的主力
- **Go**：偏基础设施和代理网关
- **Kotlin**：偶有亮点（Timeline 可视化）
- **Mojo**：开始进入 trending 常客行列

---

## 💡 值得深挖 TOP 3

### 1. cursor/plugins（⭐+388/天）
🔗 https://github.com/cursor/plugins

**理由：** Cursor 正式发布插件规范，意味着 Cursor 生态要开放了。这可能会改变 AI 编辑器的竞争格局——从「比模型」变成「比插件生态」。

**建议：** 详细看看插件 spec，考虑是否能为主子的工具链写个插件。

### 2. volcengine/OpenViking（⭐+3,033/周）
🔗 https://github.com/volcengine/OpenViking

**理由：** 字节跳动火山引擎出品的「AI Agent 自进化上下文数据库」——统一 Agent 记忆、知识 RAG 和技能系统。周增 3K+，说明企业级 Agent 基础设施需求很大。

**建议：** 研究架构设计，看看怎么做 Agent 的长期记忆和技能管理。

### 3. cactus-compute/needle（⭐+2,985/周）
🔗 https://github.com/cactus-compute/needle

**理由：** 14MB 的基础模型，专门给手机、可穿戴设备、智能家居和机器人用。端侧 AI 的重要进展。

**建议：** 关注端侧部署场景，如果在做 IoT 或边缘计算，这个值得 clone 试试。

---

## 📅 周榜亮点

### 持续霸榜
- **harry0703/MoneyPrinterTurbo**：周增 10,470，总 113K，AI 短视频赛道的绝对王者
- **public-apis/public-apis**：周增 10,990，总 468K——这个老牌项目还在涨，说明 API 集合类资源永远有需求

### 本周新晋黑马
- **cordiverse/cordis**（周增 3,614）：「时空可组合性元框架」，TypeScript 写的，概念比较新
- **cathrynlavery/diagram-design**（周增 8,457）：38 种编辑级图表模板，专为 Claude Code/Codex 设计的 HTML+SVG 方案，不用 Mermaid
- **basecamp/omarchy**（周增 2,565）：Basecamp 创始人 DHH 搞的「有态度的现代 Linux」发行版
- **NVIDIA-NeMo/Switchyard**（周增 642）：NVIDIA 的 LLM 路由中间件，兼容 OpenAI/Anthropic API，做模型切换和成本优化
- **akitaonrails/ai-memory**（周增 2,404）：Rust 写的 Agent 长期记忆方案，支持跨 Agent 工具交接

---

## 🎬 视频选题建议

### 选题 1：「AI Agent 技能大战：谁的 Claude Code/Codex 配置最强？」
把 mattpocock/skills、obra/superpowers、affaan-m/ECC、cursor/plugins 这几个项目串起来讲，对比不同大牛的 Agent 技能配置思路，展示实际效果差异。这个选题时效性强，流量潜力大。

### 选题 2：「不用罗技官方软件！Rust 写的 OpenLogi 体验」
OpenLogi 作为 Rust 替代商业驱动软件的典型案例，可以做一个「安装 → 配置 → 对比 Options+」的实测视频，受众面广（罗技鼠标用户多），而且能带出 Rust 生态的优势。

---

## 📊 各语言日榜精华速查

### Python
| # | 项目 | 日增 | 亮点 |
|---|------|------|------|
| 1 | MoneyPrinterTurbo | +1,201 | AI 短视频生成 |
| 2 | Tencent/AI-Infra-Guard | +434 | AI 红队安全平台 |
| 3 | PostHog | +335 | 自驱产品平台 |
| 4 | mukul975/Anthropic-Cybersecurity-Skills | +243 | 817 个安全技能集 |
| 5 | MadsLorentzen/ai-job-search | +223 | AI 求职框架 |

### TypeScript
| # | 项目 | 日增 | 亮点 |
|---|------|------|------|
| 1 | diegosouzapw/OmniRoute | +768 | 340 个 AI 提供商的统一网关 |
| 2 | makeplane/plane | +579 | 开源 Jira/Linear 替代 |
| 3 | cursor/plugins | +388 | Cursor 插件规范 |
| 4 | garrytan/gstack | +192 | Garry Tan 的 Claude Code 配置 |
| 5 | n8n-io/n8n | +193 | 工作流自动化 |

### Rust
| # | 项目 | 日增 | 亮点 |
|---|------|------|------|
| 1 | AprilNEA/OpenLogi | +1,380 | 罗技驱动替代 |
| 2 | akitaonrails/ai-memory | +467 | Agent 长期记忆 |
| 3 | nautechsystems/nautilus_trader | +300 | 量化交易引擎 |
| 4 | aaif-goose/goose | +113 | 开源 AI Agent |
| 5 | oven-sh/bun | +89 | JS 运行时 |

### Go
| # | 项目 | 日增 | 亮点 |
|---|------|------|------|
| 1 | Wei-Shaw/sub2api | +673 | API 订阅统一中转 |
| 2 | JuliusBrussee/caveman | +590 | Claude Code token 优化（砍 65%） |
| 3 | agent-substrate/substrate | +243 | Agent 核心系统 |
| 4 | alibaba/open-code-review | +102 | 阿里级代码审查 |
| 5 | microsoft/TypeScript | +65 | TS 本体（Go 编译） |

---

*数据采集时间：2026-08-22 09:00 | 来源：GitHub Trending*
