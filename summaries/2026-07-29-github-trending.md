# 🔥 GitHub Trending 趋势速览 — 2026年7月29日

## 一句话总览

**AI Agent 生态全面爆发**：今天 GitHub 最突出的主题是「Coding Agent 技能生态」——从 Matt Pocock 的 Skills（周增 1.2 万星）到 book-to-skill、claude-video、ADHD-friendly agent skills，围绕 Claude/Codex Agent 的技能开发工具链正在快速膨胀。同时，开源 AI 网关、Agent 治理、本地语音 Agent 也在同步起飞。

---

## 🚀 爆款项目 TOP 5

### 1. [bradautomates/claude-video](https://github.com/bradautomates/claude-video) ⭐ +988/day
**是什么**：让 Claude 能「看」视频——自动下载、抽帧、转录，把视频内容交给 Claude 处理。
**为什么火**：解决了 Claude 无法直接处理视频的痛点，用 `/watch` 命令一行搞定，对内容创作者和研究者极其有用。
**对主子的价值**：做视频选题的神器——可以用它分析竞品视频、提取关键帧做封面参考、转录后做内容拆解。强烈推荐 clone 试试。

### 2. [moeru-ai/airi](https://github.com/moeru-ai/airi) ⭐ +797/day
**是什么**：自托管的 AI 伴侣系统（Grok Companion），支持自定义人格、记忆和情感交互。
**为什么火**：AI 伴侣赛道持续升温，这个项目主打「你拥有、你自托管」，戳中了隐私和个性化两大痛点。
**对主子的价值**：技术架构值得研究（人格系统 + 记忆层），可以做视频选题「开源 AI 伴侣到底能做到什么程度」。

### 3. [alibaba/open-code-review](https://github.com/alibaba/open-code-review) ⭐ +918/day（Go）
**是什么**：阿里开源的代码审查工具，混合架构（规则引擎 + AI），在阿里内部大规模验证过。
**为什么火**：大厂开源 + 免费 + 实战验证，Go 语言写的，性能好。解决团队代码审查效率问题。
**对主子的价值**：如果主子有团队项目，可以整合进去；也可以做一期「阿里开源的代码审查工具 vs GitHub Copilot Review」的对比视频。

### 4. [yorukot/superfile](https://github.com/yorukot/superfile) ⭐ +662/day（Go）
**是什么**：现代终端文件管理器，界面漂亮，操作流畅。
**为什么火**：终端党永远缺一个好用的文件管理器，superfile 在颜值和功能之间找到了很好的平衡。
**对主子的价值**：日常工具，装上直接用。也可以出一期「2026 年终端文件管理器横评」。

### 5. [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) ⭐ +607/day（TypeScript）
**是什么**：轻量级云原生 GIS 平台，浏览器内运行，支持地理数据可视化和分析。
**为什么火**：GIS 工具一直又重又贵，这个直接在浏览器里跑，开源免费，降低了地理数据处理的门槛。
**对主子的价值**：如果有地理数据可视化需求可以试试，技术上 WebGIS + 轻量化是个有意思的方向。

---

## 📈 技术趋势洞察

### 🔥 最火方向：AI Agent 技能生态
今天和周榜上最大的主题就是 **Coding Agent 的 Skills/Skill 生态**：
- [mattpocock/skills](https://github.com/mattpocock/skills)（周榜第一，+12,794 星）—— Matt Pocock 把自己的 `.agents` 目录开源了
- [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill)（+423/天）—— 把技术书 PDF 转成 Claude Code skill
- [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)（周增 +6,156）—— ADHD 友好的 Agent 输出技能
- [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) —— Agent 技能管理层

**判断**：Agent Skill 正在成为新的「npm 包」——开发者开始像管理依赖一样管理 Agent 技能。这是一个范式转变。

### 🔥 AI 网关大乱斗
- [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)（周增 +10,028）：MIT 协议，一个端点接入 290+ 供应商、500+ 模型
- 开源 AI 网关赛道越来越卷，免费模型聚合是核心卖点

### 🔥 Agent 治理与安全
- [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit)（+46/天）：微软出的 Agent 治理工具包，策略执行 + 零信任 + 沙箱
- [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)：英伟达出的 Agent 安全运行时
- 说明 Agent 大规模部署后，治理和安全成了刚需

### 📊 语言热度
- **Python**：依然是 AI/ML 项目的绝对主力（语音 Agent、量化交易、爬虫）
- **TypeScript**：前端/全栈工具、AI 伴侣、GIS、可视化
- **Rust**：WiFi 感知（RuView）、会议转录（Meetily）、Agent 编程语言（BAML）
- **Go**：终端工具（superfile）、企业级工具（阿里代码审查、飞书 CLI）

### 新范式：Agent 即平台
从 skills 管理、governance、memory（OpenViking）、到 coding agent toolkit（pi），整个 Agent 开发栈在快速成型。

---

## 💡 值得深挖 TOP 3

### 1. [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill)
**理由**：把 PDF 技术书变成 Agent skill，这个思路太妙了。相当于把你的知识库直接灌进 Agent。
**建议**：clone 试试，看看能不能把自己收藏的技术书转成 skill 用。也可以做一期视频。

### 2. [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)（周增 +10,637）
**理由**：《深入理解 AI Agent》开源全书 + 代码，中文作者，系统性学习 Agent 设计的最佳资源。
**建议**：下载 PDF 通读，配合代码实践。做视频系列「跟主子一起读 AI Agent 书」也行。

### 3. [koala73/worldmonitor](https://github.com/koala73/worldmonitor)（周增 +12,173）
**理由**：实时全球情报仪表盘，AI 驱动的新闻聚合 + 地缘政治监控。技术栈和产品设计都值得学。
**建议**：clone 跑一下看看效果，对了解 AI + 信息聚合的产品设计有启发。

---

## 📅 周榜亮点

### 持续霸榜
- [mattpocock/skills](https://github.com/mattpocock/skills)：周增 12,794 星，Agent Skills 赛道的现象级项目
- [schollz/croc](https://github.com/schollz/croc)：老牌文件传输工具，周增 2,488，说明基础工具永远有需求

### 本周黑马
- [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)：周增 10,028，免费 AI 网关，290+ 供应商一站式接入
- [CoreBunch/Instatic](https://github.com/CoreBunch/Instatic)：周增 2,828，开源 Webflow/Framer 替代品，Agentic 自托管视觉 CMS
- [ruvnet/RuView](https://github.com/ruvnet/RuView)：周增 5,026，用 WiFi 信号做空间感知和生命体征监测，Rust 写的，很硬核

### 日榜 vs 周榜差异
日榜偏工具类（文件管理器、代码审查、视频处理），周榜偏平台和生态类（AI 网关、Agent Skills、开源 CMS）。说明短期热点是具体工具，长期趋势是生态建设。

---

## 🎬 视频选题建议

### 选题 1：「一行命令让 Claude 看视频——claude-video 深度体验」
**角度**：演示 `/watch` 命令如何让 Claude 分析视频内容，实测用它拆解一个技术教程视频，展示抽帧 + 转录 + 分析全流程。
**热度依据**：日增 988 星，Claude 生态热度持续高涨。

### 选题 2：「Agent Skills 是什么？为什么 Matt Pocock 的 .agents 目录值 1.2 万星」
**角度**：解读 Agent Skill 生态的爆发，对比 book-to-skill、ADHD skill、OpenSpace 等项目，讲清楚「Agent 技能管理 = 新时代的包管理器」这个概念。
**热度依据**：周榜多个 Skills 相关项目同时上榜，趋势明确。

---

*报告生成时间：2026-07-29 09:00 | 数据来源：GitHub Trending*
