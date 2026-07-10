# 🔥 GitHub 趋势速览 — 2026年7月10日

## 一句话总览

**AI Agent 生态大爆发。** 今天 GitHub 日榜和周榜几乎被 Agent 工具链吞没——从给 Agent 喂技能（agent-skills）、配沙箱（CubeSandbox）、写设计稿（awesome-design-md）、到多 Agent 编排（orca、herdr），整个开发工具链正在围绕"如何让 AI Agent 更好地干活"重构。Claude Code + Codex 生态是绝对主战场。

---

## 🚀 爆款项目 TOP 5

### 1. MadsLorentzen/ai-job-search
🔗 https://github.com/MadsLorentzen/ai-job-search
⭐ +3,716/天 | 周榜 +13,847 | TypeScript

**干什么：** 基于 Claude Code 的 AI 求职框架。Fork 后填入个人资料，Claude 自动评估岗位、定制简历、写求职信、模拟面试。

**为什么火：** 把求职这个高频痛点场景完全 Agent 化了。不是简单的"AI 帮你改简历"，而是完整的求职工作流——岗位匹配度评估、个性化 CV 生成、面试准备一站式搞定。日增 3700+ star 说明戳中了大量技术人的痛点。

**对主子的价值：** 值得 clone 下来研究其 Claude Code 技能编排方式，Agent 工作流设计思路可以借鉴。也是不错的视频选题——"用 AI 帮你找工作"天然有流量。

---

### 2. addyosmani/agent-skills
🔗 https://github.com/addyosmani/agent-skills
⭐ +2,554/天 | JavaScript

**干什么：** 给 AI 编程 Agent 提供生产级工程技能的集合。可以理解为 Agent 的"技能树"——教 Agent 怎么按最佳实践写代码。

**为什么火：** Addy Osmani（Google Chrome 团队大佬）背书，解决了 Agent 写代码质量差的核心问题。不是 prompt engineering，而是结构化的技能文件，让 Agent 在特定任务上达到高级工程师水平。

**对主子的价值：** 直接能用。把这些 skills 集成到日常 Agent 工作流里，代码质量会明显提升。也值得研究 skill 文件的写法来给自己的 Agent 定制技能。

---

### 3. iOfficeAI/OfficeCLI
🔗 https://github.com/iOfficeAI/OfficeCLI
⭐ +1,929/天 | C#

**干什么：** 专为 AI Agent 打造的 Office 套件。单二进制文件，不装 Office 就能读写 Word/Excel/PPT。开源免费。

**为什么火：** Agent 处理 Office 文件一直是个大坑——要么依赖 Office 安装，要么用各种不靠谱的库。这个工具把整个 Office 操作封装成 Agent 友好的 CLI，直接解决了"让 AI 处理文档"的最后一公里。

**对主子的价值：** 实用工具，收藏备用。任何需要 Agent 批量处理文档的场景都能用上。

---

### 4. VoltAgent/awesome-design-md
🔗 https://github.com/VoltAgent/awesome-design-md
⭐ +1,391/天

**干什么：** 收集各大品牌设计系统的 DESIGN.md 文件。丢一个到你的项目里，编码 Agent 就能生成风格一致的 UI。

**为什么火：** 巧妙地把设计系统"翻译"成了 Agent 能理解的结构化文档。解决了 AI 生成 UI 风格不统一的痛点——给 Agent 一份设计规范，它就知道按钮该长什么样、配色该怎么用。

**对主子的价值：** 如果主子有前端项目，直接丢一个 DESIGN.md 进去让 Agent 生成 UI，效果会比裸跑好很多。

---

### 5. asgeirtj/system_prompts_leaks
🔗 https://github.com/asgeirtj/system_prompts_leaks
⭐ +1,125/天 | 周榜 +7,149 | JavaScript

**干什么：** 从各大 AI 产品提取的系统提示词合集——Anthropic Claude 全家桶、OpenAI ChatGPT/Codex、Google Gemini、xAI Grok、Cursor、Copilot 等。持续更新。

**为什么火：** 系统提示词是 AI 产品的核心秘密，大家天然好奇。而且这些泄露对做 AI 产品的人来说是宝贵的参考资料——看看顶级产品怎么设计 prompt 的。

**对主子的价值：** 做 AI 相关内容时的绝佳素材。可以分析各家的 prompt 策略，也可以作为视频选题——"揭秘 ChatGPT/Claude 的系统提示词"。

---

## 📈 技术趋势洞察

### 🔴 AI Agent 基础设施层（爆发中）
今天最突出的信号：**Agent 工具链正在从"能用"走向"好用"**。具体表现：
- **技能系统**：agent-skills（教 Agent 怎么写代码）、dotnet/skills（.NET 专项技能）、SkillOpt（自动优化 Agent 技能）
- **沙箱/安全**：TencentCloud/CubeSandbox（Agent 专用沙箱）、pentagi（Agent 做渗透测试）
- **设计系统**：awesome-design-md + facebook/astryx = Agent 生成 UI 有了标准化方案
- **编排层**：orca（多 Agent 并行 ADE）、herdr（终端 Agent 多路复用）、alibaba/page-agent（网页内 GUI Agent）

### 🟡 Claude Code / Codex 生态（主战场）
Claude Code 和 Codex 的插件生态在快速膨胀：
- codex-plugin-cc（Codex 调用 Claude Code 审查代码）
- claude-video（让 Claude 看视频）
- DesktopCommanderMCP（给 Claude 终端控制权）
- ai-job-search、ai-berkshire 等垂直应用

### 🟢 语音/视频 AI（新热点）
- jamiepine/voicebox（+1,146/天）：开源 AI 语音工作室，克隆/转录/创作
- kyutai-labs/pocket-tts：CPU 就能跑的 TTS
- huggingface/speech-to-speech：本地语音 Agent
- browser-use/video-use：用编程 Agent 编辑视频

### 🔵 安全 + AI
- usestrix/strix（周榜 +8,370）：开源 AI 渗透测试
- vxcontrol/pentagi（+535/天）：全自主渗透测试 Agent
- 安全领域正在成为 AI Agent 的重要应用场景

### 语言热度
- **TypeScript** 依然是 Agent 工具链的主力语言
- **Rust** 在 Agent 基础设施层（沙箱、会议工具、WiFi 感知）表现抢眼
- **Python** 稳定输出 AI 工具和爬虫类项目
- **Go** 在安全工具和 MCP 服务端方面有一席之地

---

## 💡 值得深挖 TOP 3

### 1. Graphify-Labs/graphify ⭐+909/天
🔗 https://github.com/Graphify-Labs/graphify

把任意代码/文档/数据库变成可查询的知识图谱，支持 Claude Code、Codex、Cursor 等。

**理由：** 知识图谱 + Agent 的结合非常有想象力。如果能让 Agent 理解整个项目的代码图谱，上下文管理问题就解决了一大半。值得 clone 试试，看看对大型项目的实际效果。

### 2. Zackriya-Solutions/meetily 周榜 +8,885
🔗 https://github.com/Zackriya-Solutions/meetily

本地优先的 AI 会议助手：Rust 写的 Whisper 转录快 4 倍，说话人分离，Ollama 总结。100% 本地处理，零云端依赖。

**理由：** 会议记录是刚需，本地处理解决了隐私焦虑。Rust + Parakeet 的性能亮点值得研究。可以直接用，也可以拆解学习其 Rust 架构。

### 3. microsoft/SkillOpt ⭐+276/天
🔗 https://github.com/microsoft/SkillOpt

文本空间优化器，通过轨迹驱动编辑自动训练 Agent 技能，输出可部署的 `best_skill.md`。

**理由：** 微软出品，解决的是"怎么自动发现和优化 Agent 技能"这个元问题。如果好用，意味着 Agent 可以自我进化——这比手工写技能文件高了一个维度。

---

## 📅 周榜亮点

### 持续霸榜
- **ai-job-search**：周增 13,847 star，日增 3,716，还在加速。求职 AI 这个赛道的热度超出预期。
- **system_prompts_leaks**：周增 7,149，持续更新的内容自然吸引回访。

### 本周新晋黑马
- **meetily**（+8,885/周）：本地 AI 会议工具突然爆发，可能跟某个版本更新或 KOL 推荐有关。
- **usestrix/strix**（+8,370/周）：AI 渗透测试工具周增 8000+，安全 AI 赛道热度起来了。
- **OmniRoute**（+4,119/周）：免费 AI 网关，一个端点接 231+ 供应商，50+ 免费。对省钱党来说太有吸引力了。
- **ai-berkshire**（+3,757/周）：巴菲特+芒格+段永平+李录的价值投资框架，用多 Agent 做对抗性研究分析。金融 AI 的有趣尝试。

---

## 🎬 视频选题建议

### 选题 1：「我用 AI Agent 自动求职，投了 100 份简历...」
以 ai-job-search 为主角，展示 AI 自动评估岗位 → 定制简历 → 写求职信的完整流程。天然有话题性和争议性（AI 投简历算不算作弊？）。可以搭配 system_prompts_leaks 讲讲背后的 prompt 设计。

### 选题 2：「2026 年 AI Agent 工具链全景图」
从今天的 trending 里梳理出 Agent 生态全景：技能层（agent-skills）→ 设计层（design.md）→ 沙箱层（CubeSandbox）→ 编排层（orca/herdr）→ 网关层（OmniRoute）。讲清楚每个环节解决什么问题，帮观众建立全局认知。

---

*数据采集时间：2026-07-10 09:00 | 来源：GitHub Trending 日榜 + 周榜 + Python/TypeScript/Rust/Go 语言分榜*
