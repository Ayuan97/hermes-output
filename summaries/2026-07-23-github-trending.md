# 🔥 GitHub 趋势速览 — 2026年7月23日

## 一句话总览

**AI Agent "技能（Skills）"生态大爆发。** 今天日榜和周榜被 Agent 技能框架、AI 网关代理、代码智能工具三类项目屠榜了。开发者已经从"怎么用 Agent"进化到"怎么让 Agent 更好用"——技能注入、上下文优化、多模型路由成为核心战场。

---

## 🚀 爆款项目 TOP 5

### 1. koala73/worldmonitor ⭐+4,139/天
🔗 https://github.com/koala73/worldmonitor

**是什么：** 实时全球情报仪表盘，用 AI 做新闻聚合、地缘政治监控和基础设施追踪。

**为什么火：** TypeScript 全栈，界面酷炫，把原本要付费的 OSINT 工具做成了开源。日增 4000+ star 说明大家对"信息聚合+AI 分析"类产品有刚需。

**跟主子的关系：** 值得 clone 跑起来看看，情报监控类产品的架构设计可以参考。也可以做视频——"开源版 CIA 情报面板长啥样"。

---

### 2. bojieli/ai-agent-book ⭐+3,297/天
🔗 https://github.com/bojieli/ai-agent-book

**是什么：** 《深入理解 AI Agent：设计原理与工程实践》开源书，含全书正文、PDF 和配套代码。

**为什么火：** 中文社区出的，系统化讲 Agent 设计原理的书本身就稀缺，还直接开源了。日增 3000+ 说明国内开发者对 Agent 底层原理的求知欲很强。

**跟主子的关系：** **必读。** 这是目前最系统的 Agent 工程化中文资料，可以整合到自己的知识体系里。做视频选题也绝佳——"开源了一本 Agent 教科书，我来拆解"。

---

### 3. diegosouzapw/OmniRoute ⭐+1,651/天
🔗 https://github.com/diegosouzapw/OmniRoute

**是什么：** 免费开源 AI 网关，一个端点接入 268+ 提供商、500+ 模型（Claude/GPT/Gemini/Kimi/DeepSeek 全覆盖），支持 Claude Code、Codex、Cursor 等所有主流编码工具。自带配额感知自动降级和 token 压缩（省 15-95%）。

**为什么火：** 解决了每个 AI 开发者的痛点——模型多、接口乱、费用高。500+ 贡献者说明社区驱动力极强。

**跟主子的关系：** 直接能用。如果主子在用多个 AI 模型做开发，OmniRoute 可以统一接口、省钱、自动降级。强烈建议试试。

---

### 4. oblien/openship ⭐+1,302/天
🔗 https://github.com/oblien/openship

**是什么：** 自托管部署平台，TypeScript 写的。

**为什么火：** Vercel/Netlify 的开源替代品。自托管需求越来越强（数据隐私、成本控制），又一个新玩家入场。

**跟主子的关系：** 如果主子有自己的服务器想部署项目又不想依赖第三方平台，可以关注。

---

### 5. tirth8205/code-review-graph ⭐+882/天
🔗 https://github.com/tirth8205/code-review-graph

**是什么：** 本地优先的代码智能图谱，给 MCP 和 CLI 用的。构建代码库持久化地图，让 AI 编码工具只读必要的上下文，在代码审查和大型仓库场景下显著减少 token 消耗。

**为什么火：** 精准命中"AI 编码工具的上下文窗口不够用"这个痛点。周榜 5,639 star 说明不是昙花一现。

**跟主子的关系：** 如果主子在用 Claude Code 或类似工具处理大型代码库，这个工具能直接提升效率和省钱。

---

## 📈 技术趋势洞察

### 🔥 方向一：Agent Skills 生态爆发

周榜被 Skills 相关项目屠了：
- **mattpocock/skills** — 周增 10,282 star，直接来自 .agents 目录的实战技能
- **Nutlope/hallmark** — 周增 8,471，反 AI 套话的设计技能
- **ibelick/ui-skills** — 周增 2,206，设计工程师的技能库
- **ComposioHQ/awesome-claude-skills** — Claude Skills 资源大全

**趋势判断：** "给 Agent 写技能"已经从小众玩法变成主流开发模式。Agent 不再是一个黑盒，而是可以像插件一样加载各种专业技能。这个范式会持续演化。

### 🔥 方向二：AI 网关/代理层

- OmniRoute（268+ 提供商）、grok2api（Grok 多账号网关）、sub2api（订阅统一接入）
- **痛点：** 模型碎片化严重，开发者需要一个统一入口

### 🔥 方向三：代码智能与 Agent 编码工具

- code-review-graph、jcode（Rust 写的 Agent 编码框架，日增 502）、pi（Agent 工具包，日增 919）
- Facebook 也下场了：astryx（开源设计系统，Agent-ready）
- 阿里巴巴的 open-code-review 也上榜了

### 语言热度
- **TypeScript** 依然统治前端和 Agent 工具链层
- **Rust** 在 Agent 基础设施层持续发力（jcode、dioxus、dbx）
- **Python** 在 AI/ML 研究侧稳如泰山
- **Go** 在 DevOps 和网关层依然是首选

---

## 💡 值得深挖 TOP 3

### 1. bojieli/ai-agent-book 📚
**理由：** 中文社区出品的 Agent 系统化教材，直接开源了全书。这种质量的内容在中文技术圈极其稀缺。
**建议：** 下载 PDF 通读，可以做 2-3 期视频选题。

### 2. OmniRoute 🔀
**理由：** 解决实际问题、社区活跃度高、直接能用。
**建议：** clone 下来跑一下，看看能不能替换掉主子现在的多模型管理方案。

### 3. earendil-works/pi 🤖
**理由：** AI Agent 工具包，统一 LLM API + Agent 循环 + TUI + 编码 Agent CLI。周增 4,060，TypeScript 日榜 919。是一个完整的 Agent 开发框架。
**建议：** 值得 clone 试玩，对比一下跟其他 Agent 框架的差异，适合做技术对比视频。

---

## 📅 周榜亮点

### 持续霸榜
- **mattpocock/skills** — 周增 10,282，绝对王者。Matt Pocock 的 .agents 技能库直接成了标杆
- **OpenCut-app/OpenCut** — 周增 7,394，开源 CapCut 替代品，视频编辑赛道的搅局者

### 本周新晋黑马
- **Robbyant/lingbot-map** — 周增 4,250，从流数据重建 3D 场景的前馈基础模型。3D 重建 + AI 的结合是个新方向
- **iOfficeAI/OfficeCLI** — 周增 3,579，C# 写的 Office 套件，专门给 AI Agent 读写 Word/Excel/PPT 用的，不需要安装 Office。Agent 自动化办公的新拼图
- **HKUDS/DeepTutor** — 周增 3,030，终身个性化辅导系统，港大出品

### 日榜有但周榜没的（说明今天刚爆）
- **Apollo-11 源码**（chrislgarry/Apollo-11）— 日增 768，经典老项目又火了一波
- **schollz/croc** — 日增 739，跨机器文件传输，Go 写的，老牌工具持续有需求
- **dottxt-ai/outlines** — 日增 364，LLM 结构化输出，Python 圈的老熟人

---

## 🎬 视频选题建议

### 选题 1：「2026 年，AI Agent 的技能生态已经卷成这样了」
**角度：** 从 mattpocock/skills（周增 1 万）、hallmark、ui-skills 这几个项目切入，讲"Agent Skills"这个新范式。演示如何给自己的 Agent 注入技能，对比不同技能框架的优劣。观众是 AI 开发者，热度正好。

### 选题 2：「开源了一本 AI Agent 教科书，我来替你们读」
**角度：** bojieli/ai-agent-book 日增 3000+，中文社区出品。拆解书里的核心观点，结合实际代码演示。这种"帮你读技术书"的内容形式天然有完播率。

---

*数据采集时间：2026-07-23 09:00 CST | 数据来源：GitHub Trending*
