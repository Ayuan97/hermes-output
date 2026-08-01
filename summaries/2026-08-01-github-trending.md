# 🔥 GitHub 趋势速览 — 2026-08-01

## 一句话总览

**Agent Skills 生态全面爆发。** 今天的 GitHub Trending 被 AI Agent 技能（Skills）类项目屠榜了——从安全研究、量化交易、代码审查到知识蒸馏，几乎每个垂直领域都在长出自己的 "Claude Code Skill"。微软 AI 入门课单日 +1,592 星，持续霸榜。

---

## 🚀 爆款项目 TOP 5

### 1. microsoft/AI-For-Beginners
- **链接**: https://github.com/microsoft/AI-For-Beginners
- **是什么**: 微软出品的 12 周 24 课时 AI 入门课程，Jupyter Notebook 驱动
- **⭐ 55,325 (+1,592/天)**
- **为什么火**: 全球 AI 学习热潮持续，这套课程免费、系统、有微软背书，适合从零基础到中级开发者。最近可能因为暑期学习季+AI 热潮叠加爆发
- **跟主子有关吗**: ⭐⭐⭐⭐⭐ 适合做"微软免费 AI 课值不值得刷"的视频选题，也可以推荐给社区学习者

### 2. different-ai/openwork
- **链接**: https://github.com/different-ai/openwork
- **是什么**: Claude Cowork（Claude Code 的协作功能）的开源替代品，基于 opencode 构建
- **⭐ 19,508 (+806/天)** | TypeScript
- **为什么火**: Claude Code 用户越来越多，但 Cowork 是付费功能。这个项目让不想付钱或想自托管的团队有了替代方案
- **跟主子有关吗**: ⭐⭐⭐⭐ 如果团队在用 Claude Code 协作，值得 clone 试试。也可以做"Claude Cowork 开源替代"的评测视频

### 3. paperswithbacktest/awesome-systematic-trading
- **链接**: https://github.com/paperswithbacktest/awesome-systematic-trading
- **是什么**: 量化交易/系统化交易的一站式资源集合——库、策略、书籍、教程、博客
- **⭐ 11,758 (+763/天)** | Python
- **为什么火**: 量化交易+AI 结合热度持续走高，加上最近市场波动，散户和机构都在找系统化方法
- **跟主子有关吗**: ⭐⭐⭐ 如果对量化交易感兴趣，这是一个很好的起点。适合做"量化交易入门资源"视频

### 4. mvanhorn/last30days-skill
- **链接**: https://github.com/mvanhorn/last30days-skill
- **是什么**: AI Agent 技能——让 Agent 自动在 Reddit、X、YouTube、Hacker News、Polymarket 和全网搜索某个话题，然后生成综合摘要
- **⭐ 56,232 (+658/天)** | Python
- **为什么火**: 解决了"如何让 AI Agent 做深度调研"的核心痛点。一个技能就能替代手动刷 10 个平台
- **跟主子有关吗**: ⭐⭐⭐⭐⭐ 直接可用！装上这个 skill，让 Agent 每天帮你做行业调研

### 5. 1jehuang/jcode
- **链接**: https://github.com/1jehuang/jcode
- **是什么**: "最省内存的评测工具"——Rust 编写的代码评测 harness
- **⭐ 14,616 (+527/天)** | Rust
- **为什么火**: 用 Rust 重写传统评测工具，内存占用极低，适合资源受限环境
- **跟主子有关吗**: ⭐⭐⭐ 技术亮点明确（Rust + 极致优化），适合做技术深度视频

---

## 📈 技术趋势洞察

### 🔴 正在涨的方向

1. **Agent Skills 生态爆发**
   - 日榜：reverse-skill（安全）、last30days-skill（调研）、cangjie-skill（知识蒸馏）
   - 周榜：mattpocock/skills（+11,622/周）、book-to-skill（+4,603/周）、i-have-adhd（+5,133/周）
   - 趋势：几乎每个垂直领域都在长出自己的 Agent 技能包，"Skills" 正在成为新的 npm packages

2. **AI 工具民主化 / 开源替代**
   - openwork（替代 Claude Cowork）、OmniRoute（290+ AI 供应商统一网关）、earendil-works/pi（Agent 工具集）
   - 趋势：大厂付费功能 → 开源平替的速度越来越快

3. **Rust 工具链持续走强**
   - jcode（评测）、tuicr（代码审查 TUI）、openai/codex（终端编码 Agent）
   - 趋势：Rust 在开发者工具领域的渗透率还在提高

4. **语音 AI 崛起**
   - huggingface/speech-to-speech（+1,275/天）、microsoft/VibeVoice（+1,222/周）
   - 趋势：语音 Agent 从实验走向实用

### 🟡 语言/框架热度变化

| 语言 | 趋势 | 代表项目 |
|------|------|----------|
| Python | 稳定热门 | AI Skills、量化交易、语音 AI |
| TypeScript | 持续走强 | 开源替代品、项目管理、Agent 平台 |
| Rust | 加速增长 | 开发者工具、TUI、性能关键场景 |
| Go | 稳健 | AI 网关、Agent 平台、安全工具 |

---

## 💡 值得深挖 TOP 3

### 1. mvanhorn/last30days-skill
**理由**: 直接解决"如何让 AI Agent 做全网调研"的问题。装上就能用，每天自动跑一遍行业动态。
**建议**: clone 下来装上，跑一个"AI Agent 框架对比"的调研报告试试效果。

### 2. different-ai/openwork
**理由**: Claude Cowork 的开源替代品，如果团队有协作需求但不想付 Anthropic 的钱，这是目前最好的选择。
**建议**: 做个评测视频，对比 openwork vs Claude Cowork vs Cursor 协作功能。

### 3. huggingface/speech-to-speech
**理由**: 本地语音 Agent，完全离线，开源模型驱动。语音 AI 是下一个大风口。
**建议**: clone 试试本地跑语音对话的效果，如果能用，做个"本地语音 Agent 搭建指南"视频。

---

## 📅 周榜亮点

### 持续霸榜
- **microsoft/AI-For-Beginners**: 周榜同样热门，AI 学习需求持续
- **deepfakes/faceswap**: 老项目但热度不减，deepfake 技术关注度依然高

### 本周新晋黑马
1. **mattpocock/skills** (+11,622/周) — Matt Pocock 的 Agent Skills 合集，"Skills for Real Engineers"，直接从他自己的 .agents 目录公开
2. **block/buzz** (+10,558/周) — Block（原 Square）出品的"蜂群思维"沟通平台，Rust 编写
3. **alibaba/open-code-review** (+4,746/周) — 阿里巴巴开源的代码审查工具，混合架构（确定性流水线 + LLM Agent），在阿里内部大规模验证过
4. **diegosouzapw/OmniRoute** (+7,701/周) — 免费 MIT AI 网关：一个端点，290+ 供应商（90+ 免费），500+ 模型，兼容 Claude Code/Codex/Cursor 等所有主流工具
5. **koala73/worldmonitor** (+4,657/周) — 实时全球情报仪表盘，AI 驱动的新闻聚合 + 地缘政治监控 + 基础设施追踪

---

## 🎬 视频选题建议

### 选题 1：「Agent Skills 生态大爆发：2026 年最火的 AI 开发范式」
**切入点**: 从 last30days-skill、cangjie-skill、mattpocock/skills 切入，讲清楚什么是 Agent Skills、怎么用、为什么突然爆发。可以现场演示装一个 skill 做调研。
**素材**: last30days-skill 跑一个调研报告、cangjie-skill 蒸馏一本书

### 选题 2：「Claude Cowork 开源替代品实测：openwork 到底行不行」
**切入点**: Claude Code 用户越来越多，协作功能是付费的。openwork 号称是开源替代品，日增 800+ star。实测对比功能差异。
**素材**: openwork 安装演示、与 Claude Cowork 功能对比、团队协作场景测试

---

## 📊 完整数据

### 日榜 TOP 12

| # | 项目 | 语言 | ⭐ 总数 | 今日增长 | 简介 |
|---|------|------|---------|----------|------|
| 1 | [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | Jupyter | 55,325 | +1,592 | 微软 AI 入门课 |
| 2 | [openwork](https://github.com/different-ai/openwork) | TypeScript | 19,508 | +806 | Claude Cowork 开源替代 |
| 3 | [awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading) | Python | 11,758 | +763 | 量化交易资源合集 |
| 4 | [last30days-skill](https://github.com/mvanhorn/last30days-skill) | Python | 56,232 | +658 | Agent 全网调研技能 |
| 5 | [jcode](https://github.com/1jehuang/jcode) | Rust | 14,616 | +527 | 最省内存的评测工具 |
| 6 | [reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | PowerShell | 10,726 | +335 | 安全研究/逆向工程技能 |
| 7 | [tuicr](https://github.com/agavra/tuicr) | Rust | 2,157 | +335 | Vim 键位代码审查 TUI |
| 8 | [kaneo](https://github.com/usekaneo/kaneo) | TypeScript | 5,093 | +194 | 开源项目管理工具 |
| 9 | [faceswap](https://github.com/deepfakes/faceswap) | Python | 56,991 | +93 | Deepfake 换脸工具 |
| 10 | [ESP32-Bit-Pirate](https://github.com/geo-tp/ESP32-Bit-Pirate) | C++ | 5,006 | +83 | ESP32 硬件黑客工具 |
| 11 | [chatwoot](https://github.com/chatwoot/chatwoot) | Ruby | 35,125 | +35 | 开源客服系统 |
| 12 | [copilot-sdk](https://github.com/github/copilot-sdk) | Java | 10,137 | +7 | GitHub Copilot Agent SDK |

### 周榜 TOP 18（日榜未覆盖的）

| # | 项目 | 语言 | 本周增长 | 简介 |
|---|------|------|----------|------|
| 1 | [skills](https://github.com/mattpocock/skills) | Shell | +11,622 | Matt Pocock 的 Agent Skills |
| 2 | [buzz](https://github.com/block/buzz) | Rust | +10,558 | Block 团队沟通平台 |
| 3 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | TypeScript | +7,701 | 免费 AI 网关，290+ 供应商 |
| 4 | [i-have-adhd](https://github.com/ayghri/i-have-adhd) | Python | +5,133 | ADHD 友好的 Agent 输出 |
| 5 | [open-code-review](https://github.com/alibaba/open-code-review) | Go | +4,746 | 阿里开源代码审查工具 |
| 6 | [worldmonitor](https://github.com/koala73/worldmonitor) | TypeScript | +4,657 | 全球情报仪表盘 |
| 7 | [book-to-skill](https://github.com/virgiliojr94/book-to-skill) | Python | +4,603 | 技术书 PDF 转 Agent 技能 |
| 8 | [pi](https://github.com/earendil-works/pi) | TypeScript | +4,571 | AI Agent 工具集 |
| 9 | [airi](https://github.com/moeru-ai/airi) | TypeScript | +3,125 | 自托管 AI 伴侣 |
| 10 | [Instatic](https://github.com/CoreBunch/Instatic) | TypeScript | +2,866 | Webflow 开源替代品 |
| 11 | [editor](https://github.com/pascalorg/editor) | TypeScript | +2,863 | 3D 建筑编辑器 |
| 12 | [GeoLibre](https://github.com/opengeos/GeoLibre) | TypeScript | +2,765 | 云端原生 GIS 平台 |
| 13 | [Kronos](https://github.com/shiyu-coder/Kronos) | Python | +1,939 | 金融市场语言基础模型 |
| 14 | [text-to-cad](https://github.com/earthtojake/text-to-cad) | JavaScript | +1,901 | CAD/CAE/CAM Agent 技能 |
| 15 | [t3code](https://github.com/pingdotgg/t3code) | TypeScript | +1,488 | 编码工具 |
| 16 | [VibeVoice](https://github.com/microsoft/VibeVoice) | Python | +1,222 | 微软开源语音 AI |

### 语言日榜亮点

**Python**: speech-to-speech (+1,275)、book-to-skill (+601)、cangjie-skill (+320)
**TypeScript**: openwork (+806)、airi (+356)、chrome-devtools-mcp (+318)
**Rust**: jcode (+527)、tuicr (+335)、Handy 语音转文字 (+294)
**Go**: multica (+274)、IRIS 终端补全 (+113)、new-api (+110)
