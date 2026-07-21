# 🔥 GitHub 趋势速览 — 2026-07-20（周日）

## 一句话总览

**"Agent Skills" 生态全面爆发。** 本周 GitHub 被 AI Agent 工具链屠榜——从 Matt Pocock 的 skills 仓库（周增 1 万+ star）到各种 Agent Skill 生成器，再到 MCP 协议相关的代码智能、语音 AI、CLI 编码 Agent，整个 AI 开发工具栈都在高速增长。另一个显著信号：**开源替代商业 SaaS** 的趋势在加速（CapCut 替代品、Semrush 替代品、自托管部署平台都上了榜）。

---

## 🚀 爆款项目 TOP 5（按日增 star 排序）

### 1. [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)
⭐ 23,173 | **+1,833/day** | Python

> 本地优先的代码智能图谱，为 MCP 和 CLI 构建代码库持久化地图，让 AI 编码工具只读取必要的上下文。

**为什么火：** 解决了 AI 编码助手在大仓库中"上下文爆炸"的核心痛点。通过构建代码依赖图谱，精准裁剪传给 LLM 的上下文窗口，实测能大幅降低 token 消耗。

**价值：** 主子日常用 AI 辅助编码，这个直接解决大项目 context 塞不下的问题。值得 clone 试试，特别是配合 MCP 使用。

### 2. [oblien/openship](https://github.com/oblien/openship)
⭐ 4,803 | **+1,641/day** | TypeScript

> 自托管部署平台。

**为什么火：** Vercel/Netlify 的开源替代品，在 AI 时代开发者对自托管的需求持续增长（数据隐私、成本控制）。日增 1,600+ 说明社区对"去平台锁定"的呼声很高。

**价值：** 如果主子有自己的项目需要部署且不想被平台绑架，值得关注。也适合做"自托管全家桶"选题。

### 3. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)
⭐ 21,829 | **+1,107/day** | TypeScript

> 免费 MIT 协议的 AI 网关：一个端点接入 268+ 供应商（50+ 免费）、500+ 模型。支持 Claude、GPT、Gemini、Kimi K3 等，带配额感知自动降级、token 压缩（节省 15-95%）、MCP/A2A 支持。

**为什么火：** 一站式 AI 模型路由+省钱方案。500+ 模型的统一接口 + 自动降级 + token 压缩，对重度 AI 用户来说是刚需。500+ 贡献者说明社区参与度很高。

**价值：** 省钱利器。如果主子每月 API 费用不低，这个网关的自动降级和压缩功能可以直接用。也适合做"AI 开发省钱指南"选题。

### 4. [every-app/open-seo](https://github.com/every-app/open-seo)
⭐ 5,850 | **+939/day** | TypeScript

> Semrush 和 Ahrefs 的开源替代品。

**为什么火：** SEO 工具一直是高收费赛道（Semrush 月费 $130+），开源替代直接戳中独立开发者和中小团队的痛点。

**价值：** 如果主子做内容/产品需要 SEO 分析，这个省下不少钱。也是"开源替代商业工具"系列的好选题。

### 5. [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
⭐ 134,710 | **+862/day** | Shell

> 一整套 AI 代理机构——从前端专家到 Reddit 社区运营，从创意注入器到现实检验官。每个 Agent 都是有人格、有流程、有交付物的专业角色。

**为什么火：** 13 万+ star 的超级项目，把"AI Agent 即员工"的理念落地成具体的 prompt+workflow 模板。Shell 脚本说明是轻量级方案，不需要复杂框架。

**价值：** 可以直接拿来用或改造成自己的 Agent 团队。适合做"用 AI 组建虚拟团队"的选题。

---

## 📈 技术趋势洞察

### 1. Agent Skills 生态爆发 🔥🔥🔥
本周最突出的信号：**"Skills" 成为 AI Agent 生态的新范式**。
- **mattpocock/skills**（周增 10,872）：Matt Pocock（TypeScript 圈大佬）分享的 Agent Skills 合集
- **Nutlope/hallmark**（周增 9,173）：反"AI 审美"的设计 Skill，给 Claude Code/Cursor/Codex 用
- **ibelick/ui-skills**（周增 1,925）：给设计工程师的 Skills
- **kangarooking/cangjie-skill**（周增 1,342）：把书籍/视频/播客蒸馏成可执行的 Agent Skills
- **tt-a1i/archify**（周增 2,102）：Agent Skill 生成架构图

**解读：** Agent 从"通用助手"进化到"专业技能包"模式。Skills = 可复用的 prompt+workflow+tool 组合，比 MCP server 更轻量，比纯 prompt 更结构化。这可能是 2026 年下半年 Agent 生态的核心范式。

### 2. CLI 编码 Agent 军备竞赛继续
- **openai/codex**（10 万 star，周增 2,448）
- **MoonshotAI/kimi-cli**（日增 410）
- **1jehuang/jcode**（日增 568，Rust）
- **openinterpreter/openinterpreter**（周增 2,644，转向 Rust）

**解读：** 终端里的编码 Agent 已经从新鲜事物变成标配工具。竞争焦点转向：语言支持广度、上下文管理、安全护栏（destructive_command_guard 就是配套产物）。

### 3. 语音 AI 三件套上榜
- **jamiepine/voicebox**（日增 821）：开源 AI 语音工作室
- **handy-computer/transcribe.cpp**（日增 395）：支持 16+ 模型家族的 STT
- **moonshine-ai/moonshine**（日增 282）：超低延迟语音交互

**解读：** 语音 Agent 从玩具走向生产级。低延迟 STT+TTS+意图识别的全栈方案开始成熟。

### 4. MCP 协议渗透率持续扩大
日榜中有 4 个项目直接提到 MCP（code-review-graph、OmniRoute、wigolo、fastmcp），说明 MCP 正在成为 AI 工具互操作的事实标准。

### 5. Rust 在 AI 工具链中的地位稳固
jcode、topcoat、destructive_command_guard、codex、openinterpreter 都用 Rust，AI 基础设施工具的"性能敏感层"正在全面 Rust 化。

---

## 💡 值得深挖 TOP 3

### 1. [code-review-graph](https://github.com/tirth8205/code-review-graph)
**建议：** clone 下来在自己的项目上跑一下。如果 context 裁剪效果好，可以整合进日常编码流程。也可以作为"MCP + 代码图谱"技术方案的参考。

### 2. [OmniRoute](https://github.com/diegosouzapw/OmniRoute)
**建议：** 认真评估作为日常 API 网关的可行性。268 个供应商 + 自动降级 + token 压缩，如果能跑稳就是大省钱。值得做个对比测试（延迟、稳定性、实际压缩效果）。

### 3. [mattpocock/skills](https://github.com/mattpocock/skills)
**建议：** 研究 Skills 的写法和结构。这是 Matt Pocock 从自己 .agents 目录拿出来的实战经验，学一下怎么写出高质量的 Agent Skill。如果主子在用 Claude Code 或 Codex，直接可以用。

---

## 📅 周榜亮点（与日榜差异）

### 持续霸榜
- **codecrafters-io/build-your-own-x**（52 万 star，周增 4,863）：永远的教育类第一
- **Shubhamsaboo/awesome-llm-apps**（12 万 star，周增 5,857）：AI 应用合集常青树

### 本周黑马
- **OpenCut-app/OpenCut**（7.6 万 star，**周增 11,676**）：开源版 CapCut，本周增 star 冠军。视频编辑工具开源化是大趋势。
- **HKUDS/Vibe-Trading**（2.5 万 star，周增 4,387）：港大出品的 AI 交易 Agent，"Vibe Trading"这个概念很新——让 AI 自己感受市场节奏做交易。
- **iOfficeAI/OfficeCLI**（2 万 star，周增 4,140）：专门为 AI Agent 设计的 Office 套件（C#），不需要安装 Office 就能读写 Word/Excel/PPT。Agent 自动化的关键基础设施。
- **Dicklesworthstone/destructive_command_guard**（5,198 star，周增 1,410）：阻止 AI Agent 执行危险命令的护栏工具，Rust 写的。Agent 安全方向的标志性项目。

---

## 🎬 视频选题建议

### 选题 1：「Agent Skills 是什么？为什么 Matt Pocock 的 Skills 仓库一周涨了 1 万 star」
**角度：** 从 mattpocock/skills、hallmark、cangjie-skill 这几个项目切入，讲清楚 Agent Skills 这个新范式——它比 MCP 轻量、比纯 prompt 结构化，是 2026 年 Agent 生态的关键拼图。可以演示怎么用 Skills 提升编码效率。

### 选题 2：「我用开源工具替代了每月 $500 的 SaaS 订阅」
**角度：** 把 OpenCut（替代 CapCut）、open-seo（替代 Semrush）、OmniRoute（替代各 API 直连）、openship（替代 Vercel）串起来，做一个"开源替代全家桶"的实操演示。省钱永远是流量密码。

---

## 📊 今日语言分布

| 语言 | 日榜项目数 | 趋势 |
|------|-----------|------|
| Python | 8 | AI/ML 主力语言，稳固 |
| TypeScript | 8 | 全栈 + AI 工具链 |
| Rust | 2 | AI 基础设施层 |
| C++ | 2 | 语音 AI 推理引擎 |
| Shell | 1 | Agent Skills 载体 |

---

*数据采集时间：2026-07-20 09:00 | 来源：GitHub Trending*
