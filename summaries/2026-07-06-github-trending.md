# 🔥 GitHub 趋势速览 — 2026年7月6日（周一）

## 一句话总览

**AI Agent 生态大爆发。** 今天 GitHub 日榜几乎被 "AI 编程助手插件/技能包" 和 "Agent 编排工具" 垄断——Claude Code 技能包、Codex 插件、Agent 多路复用器、AI 渗透测试工具扎堆上榜。Rust 凭借本地 AI 推理场景持续吃香，自托管工具（照片管理、ROM 管理、笔记）也有稳定热度。

---

## 🚀 爆款项目 TOP 5

### 1. openai/codex-plugin-cc
- 🔗 https://github.com/openai/codex-plugin-cc
- ⭐ +1,532/天 | JavaScript
- **干什么的**：让 Claude Code 能调用 OpenAI Codex 来审查代码或委派任务，实现跨 Agent 协作。
- **为什么火**：OpenAI 官方出品，打通了 Claude Code 和 Codex 两个最热门的 AI 编程助手。开发者可以一边用 Claude Code 写代码，一边让 Codex 做 code review，双 Agent 互补。
- **对主子的价值**：如果你在用 Claude Code，这个插件值得装上试试。多一个 AI 审查环节对代码质量有帮助。也可以做视频选题——"让两个 AI 互相 review 代码会怎样？"

### 2. usestrix/strix
- 🔗 https://github.com/usestrix/strix
- ⭐ +1,114/天 | Python | 周榜 +10,338/周 🏆
- **干什么的**：开源 AI 渗透测试工具，自动发现并修复应用安全漏洞。
- **为什么火**：AI + 安全的交叉领域，自动化渗透测试一直是高价值方向。周增 1 万+ star 说明安全圈和 AI 圈同时关注。
- **对主子的价值**：安全从业者或开发者必备。可以 clone 下来对自己的项目跑一遍漏洞扫描。做视频也很有话题性——"让 AI 来黑你的网站"。

### 3. JuliusBrussee/caveman
- 🔗 https://github.com/JuliusBrussee/caveman
- ⭐ +1,052/天 | JavaScript
- **干什么的**：Claude Code 技能插件，通过"原始人式"精简表达让 token 消耗降低 65%。
- **为什么火**：直击 AI 编程的最大痛点——token 太贵。用极简语言风格压缩 prompt 体积，思路很巧妙也很搞笑。
- **对主子的价值**：立刻能用！装上就能省 token 钱。而且"AI 说原始人语"这个梗非常适合做视频，流量密码。

### 4. asgeirtj/system_prompts_leaks
- 🔗 https://github.com/asgeirtj/system_prompts_leaks
- ⭐ +981/天 | JavaScript
- **干什么的**：收集了 Anthropic Claude、OpenAI ChatGPT、Google Gemini、xAI Grok 等主流 AI 的系统提示词泄露。
- **为什么火**：人们对 AI 系统提示词的好奇心从未消退。这个仓库定期更新，覆盖最新模型（包括 ChatGPT 5.5 Thinking、Gemini 3.5 Flash 等）。
- **对主子的价值**：研究各家 AI 的系统设计思路，对自己的 prompt engineering 有参考价值。也是不错的视频素材——"各家 AI 的隐藏指令长什么样"。

### 5. alibaba/page-agent
- 🔗 https://github.com/alibaba/page-agent
- ⭐ +805/天 | TypeScript | 周榜 +3,151/周
- **干什么的**：阿里巴巴开源的网页内 GUI Agent，用自然语言控制网页界面操作。
- **为什么火**：Browser Use 概念的落地，阿里出品品质有保障。可以在浏览器内直接执行自然语言指令操控网页，适合自动化测试和 RPA 场景。
- **对主子的价值**：如果做自动化工作流或爬虫，这个库值得关注。大厂出品意味着文档和维护相对靠谱。

---

## 📈 技术趋势洞察

### 🔥 正在涨的方向

1. **AI Agent 技能/插件生态** — 日榜前 25 里有 **8 个** 是 Claude Code / Codex 的技能包或插件（claude-skills、caveman、awesome-claude-code、marketingskills、planning-with-files、codex-plugin-cc、dotnet/skills 等）。这说明 AI 编程助手已经从"能用"进入"好用"阶段，生态建设开始爆发。

2. **Agent 编排 & 多路复用** — herdr（Rust，终端 Agent 多路复用器）、gastown（Go，多 Agent 工作区管理器）、orca（多 Agent 并行 IDE）都上榜。开发者开始从"用单个 AI 助手"转向"编排一支 AI 舰队"。

3. **AI + 安全** — strix 周增万星，渗透测试自动化正在成为 AI 的杀手级应用之一。

4. **本地/隐私优先 AI** — Meetily（本地会议转录 + Ollama 总结）、RuView（WiFi 信号感知）、OpenSuperWhisper（本地语音转文字）都在强调"100% 本地处理，不需要云"。

### 📊 语言/框架热度

| 语言 | 日榜占比 | 趋势 |
|------|---------|------|
| Python | 高 | AI/ML/Agent 技能包主导 |
| TypeScript | 中高 | Agent GUI、设计系统、自托管 |
| Rust | 中 | 本地 AI 推理、系统工具 |
| Go | 低 | Agent 编排、基础设施 |
| JavaScript | 中 | 插件/技能包为主 |

### 🆕 新范式

- **"Skill.md 标准"**：多个项目提到兼容 SKILL.md 标准（类似 Agent 的 manifest），说明 Agent 技能的分发和复用正在走向标准化。
- **跨 Agent 协作**：Codex 调用 Claude Code、Claude Code 调用 Codex，Agent 之间不再是孤岛。

---

## 💡 值得深挖 TOP 3

### 1. herdr — Agent 终端多路复用器
- 🔗 https://github.com/ogulcancelik/herdr
- ⭐ +651/天 | Rust | 周榜 +3,937/周
- **理由**：用 Rust 写的终端 Agent 管理器，可以同时跑多个 AI Agent 并协调它们。随着 Agent 生态爆发，"管理多个 Agent"变成刚需。
- **建议**：clone 下来试试，特别是如果你同时在多个项目里用 AI 编程助手的话。

### 2. DeusData/codebase-memory-mcp — 代码库知识图谱 MCP
- 🔗 https://github.com/DeusData/codebase-memory-mcp
- ⭐ 周榜 +7,945/周 🏆
- **理由**：把代码库索引成持久化知识图谱，支持 158 种语言，平均仓库毫秒级索引。这是给 AI 编程助手加了"长期记忆"，解决了每次对话都要重新理解代码库的痛点。
- **建议**：强烈推荐装上。对大型项目使用 AI 编程助手的体验提升巨大。

### 3. browser-use/video-use — 用编程 Agent 编辑视频
- 🔗 https://github.com/browser-use/video-use
- ⭐ 周榜 +4,288/周
- **理由**：browser-use 团队的又一新作，让编程 Agent 能直接操作视频编辑。这是 AI Agent 从"写代码"扩展到"做内容创作"的重要一步。
- **建议**：关注 + star，等稳定了用来做视频自动化处理。

---

## 📅 周榜亮点

### 持续霸榜
- **usestrix/strix** — 周增 10,338 星，AI 安全领域现象级项目
- **DeusData/codebase-memory-mcp** — 周增 7,945 星，代码智能 MCP 服务器
- **calesthio/OpenMontage** — 周增 7,353 星，开源 Agent 视频制作系统（12 条管线、52 个工具、500+ Agent 技能）

### 本周黑马
- **msitarzewski/agency-agents** — 周增 10,637 星 🤯，一套完整的"AI 公司"代理集合——前端开发、Reddit 社区运营、创意注入、现实检查……每个 Agent 都是一个专业角色。Shell 脚本仓库能涨这么多星，说明人们对"AI 员工团队"的想象空间非常大。
- **xbtlin/ai-berkshire** — 周增 5,038 星，AI 时代的伯克希尔·哈撒韦——用 Claude Code/Codex 做价值投资研究框架，巴菲特 + 芒格 + 段永平 + 李录四大师方法论。中国开发者做的，很懂中文投资圈的需求。
- **diegosouzapw/OmniRoute** — 周增 4,411 星，免费 AI 网关，一个端点接入 231+ 供应商（50+ 免费），让 Claude Code/Codex/Cursor/Cline 接入免费的 Claude/GPT。省钱神器。

---

## 🎬 视频选题建议

### 选题 1：「让 AI 说原始人语省 65% token 钱」
- 项目：caveman（日增 1,052 星）
- 角度：实测安装 caveman 技能包前后 token 消耗对比，演示"AI 用穴居人语法说话"的搞笑效果，最后算一笔经济账。
- 流量潜力：⭐⭐⭐⭐⭐（省钱 + 搞笑 + 实用三合一）

### 选题 2：「让 AI 来黑你的网站——开源渗透测试实测」
- 项目：strix（周增 10,338 星）
- 角度：用 strix 对一个故意有漏洞的测试站点做渗透测试，展示 AI 如何发现 SQL 注入、XSS 等漏洞，并给出修复建议。
- 流量潜力：⭐⭐⭐⭐⭐（安全话题自带流量 + AI 加持）

---

## 📎 附：今日完整数据

### 日榜 TOP 22（全部语言）

| # | 项目 | 语言 | 日增⭐ | 简述 |
|---|------|------|--------|------|
| 1 | [meetily](https://github.com/Zackriya-Solutions/meetily) | Rust | +1,409 | 本地 AI 会议助手 |
| 2 | [codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | JS | +1,532 | OpenAI 官方 Claude Code 插件 |
| 3 | [system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | JS | +981 | 主流 AI 系统提示词合集 |
| 4 | [taste-skill](https://github.com/Leonxlnx/taste-skill) | JS | +863 | 让 AI 输出有品味的内容 |
| 5 | [claude-skills](https://github.com/alirezarezvani/claude-skills) | Python | +392 | 337 个 Claude Code 技能包 |
| 6 | [romm](https://github.com/rommapp/romm) | Python | +410 | 自托管 ROM 管理器 |
| 7 | [herdr](https://github.com/ogulcancelik/herdr) | Rust | +651 | 终端 Agent 多路复用器 |
| 8 | [page-agent](https://github.com/alibaba/page-agent) | TS | +805 | 阿里开源网页 GUI Agent |
| 9 | [cs249r_book](https://github.com/harvard-edge/cs249r_book) | Python | +329 | 哈佛 ML 系统教材 |
| 10 | [strix](https://github.com/usestrix/strix) | Python | +1,114 | AI 渗透测试工具 |
| 11 | [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Python | +148 | Claude Code 资源合集 |
| 12 | [marketingskills](https://github.com/coreyhaines31/marketingskills) | JS | +145 | AI Agent 营销技能包 |
| 13 | [caveman](https://github.com/JuliusBrussee/caveman) | JS | +1,052 | 省 65% token 的 Claude 技能 |
| 14 | [unity-mcp](https://github.com/CoplayDev/unity-mcp) | C# | +414 | Unity + AI 桥接 MCP |
| 15 | [astryx](https://github.com/facebook/astryx) | TS | +522 | Facebook 开源 Agent 设计系统 |
| 16 | [immich](https://github.com/immich-app/immich) | TS | +470 | 自托管照片管理 |
| 17 | [RuView](https://github.com/ruvnet/RuView) | Rust | +161 | WiFi 信号空间感知 |
| 18 | [gastown](https://github.com/gastownhall/gastown) | Go | +51 | 多 Agent 工作区管理 |
| 19 | [dotnet/skills](https://github.com/dotnet/skills) | C# | +246 | .NET AI Agent 技能包 |
| 20 | [planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Python | +66 | AI Agent 持久化规划 |
| 21 | [CodexBar](https://github.com/steipete/CodexBar) | Swift | +153 | Codex/Claude 用量统计 |
| 22 | [claude-code](https://github.com/anthropics/claude-code) | Python | +156 | Anthropic 官方 AI 编程工具 |

### Python 日榜亮点
- free-llm-api-resources（+482/天）— 免费 LLM API 资源列表
- TradingAgents（+257/天）— 多 Agent LLM 股票交易框架
- claude-video（+368/天）— 让 Claude 能看视频

### TypeScript 日榜亮点
- chrome-devtools-mcp（+252/天）— 给编程 Agent 的 Chrome DevTools MCP
- openclaw（+192/天）— 全平台个人 AI 助手
- oh-my-pi（+155/天）— 终端 AI 编程 Agent

### Rust 日榜亮点
- Handy（+161/天）— 开源离线语音转文字
- omnigraph（+58/天）— Lakehouse 原生图引擎

### Go 日榜亮点
- ntfy（+141/天）— 推送通知服务
- DeepSeek-Reasonix（+102/天）— DeepSeek 终端 AI Agent
- headscale（+63/天）— 开源 Tailscale 控制服务器

---

*报告生成时间：2026-07-06 09:00 | 数据来源：GitHub Trending*
