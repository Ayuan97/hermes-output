# 🔥 GitHub 趋势速览 — 2026年8月29日（周六）

## 一句话总览

**AI Agent 生态全面爆发。** 今天的 GitHub Trending 被 Claude Code 插件、Agent Skills、编码代理工具屠榜了。Anthropic 官方下场建了插件目录和社区市场，OpenAI Codex（Rust 终端代理）周增 9000+ star，Cursor 也开放了插件规范。"Agent Skills" 正在成为新的开源协作范式。

---

## 🚀 爆款项目 TOP 5

### 1. [tt-a1i/archify](https://github.com/tt-a1i/archify) ⭐ +4,562/天
**一句话：** AI Agent 的画图神器——自动生成架构图、流程图、时序图、数据流图，输出自包含 HTML，带动画效果。

**为什么火：** 解决了"AI 生成的图表又丑又难验证"的痛点。自包含 HTML 意味着零依赖、可分享、可版本控制。Agent Skill 格式让它能直接塞进 Claude Code / Cursor 里用。

**对主子的价值：** 直接 clone 试用。做技术内容时画架构图效率能翻几倍，也可以做视频演示"AI 一键出架构图"。

---

### 2. [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) ⭐ +3,829/天
**一句话：** 浏览器里的间谍卫星模拟器——但数据是真的。3D 地球上的实时开源空间情报。

**为什么火：** "间谍卫星"这个概念太抓眼球了。用的是真实开源卫星数据，3D 地球渲染，开源且完全在浏览器运行。这种"看起来很机密但其实开源"的项目天然自带传播力。

**对主子的价值：** 绝佳视频选题！"我用开源数据造了个间谍卫星"——标题就值百万播放。

---

### 3. [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) ⭐ +1,687/天（周榜 +12,877）
**一句话：** GPT-Image2 工业级提示词引擎，530+ 案例逆向工程 + 20+ 套工业模板，把提示词当代码写。

**为什么火：** 中文社区出品，持续更新，把提示词工程做成了可复现、可版本管理的"代码"。GPT-Image2 发布后需求暴涨。

**对主子的价值：** 收藏备用。做 AI 图像相关视频时可以直接拿模板演示，省时省力。

---

### 4. [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) ⭐ +1,396/天
**一句话：** 让你的 AI 代理像最懒的高级工程师一样思考——最好的代码就是不写的代码。

**为什么火：** 击中了"AI 写太多代码"的痛点。不是让 AI 多写，而是让 AI 学会克制、复用、做减法。理念新颖，讨论度高。

**对主子的价值：** 理念值得关注。如果你用 AI 编码时觉得它"话太多代码太啰嗦"，这个项目提供了一套系统性的解决方案。

---

### 5. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) ⭐ +1,144/天
**一句话：** 全球首个开源 AI 视频制作系统——12 条生产线、100+ 工具、700+ Agent Skill 文件，把编码助手变成视频制作工作室。

**为什么火：** 开源 + Agent 驱动 + 视频制作，三个热词叠满。不是简单的"AI 生成视频"，而是完整的视频制作工作流（剪辑、配音、特效、渲染）。

**对主子的价值：** 值得深挖。如果能跑通，可以大幅降低视频制作成本。也是很好的视频选题："用 AI 做 AI 的视频"。

---

## 📈 技术趋势洞察

### 今天涨的最猛的方向：
1. **AI Agent 插件/Skills 生态** 🔥🔥🔥 — archify、scientific-agent-skills、Claude plugins、Cursor plugins、VoltAgent/awesome-agent-skills… Agent Skills 正在标准化，"写一个 Skill 就能让所有 AI 编辑器获得新能力"这个模式跑通了。
2. **终端编码代理** — OpenAI Codex（Rust 写的，周增 9000+）持续霸榜。终端 + AI = 最纯粹的编码体验。
3. **免费 LLM 访问** — freellmapi（34 个免费供应商聚合）、free-claude-code（13 亿免费 token）。说明大家对付费 API 的怨念很深。
4. **本地优先（Local-first）** — OpenLogi（罗技驱动的 Rust 替代品）、openhuman（个人 AI 大脑）、Apache Maka（本地优先 AI 工作空间）。数据不出本地的需求在增强。

### 新范式信号：
- **"Agent Skill" 作为新的开源单元** — 不再是 "库/框架"，而是 "Skill"。一个 Skill 文件就能让 Claude Code、Cursor、Codex 都获得新能力。这比 npm 包还轻量。
- **AI 代理的"克制"哲学** — ponytail 代表的方向：AI 不是写越多越好，而是学会不写。
- **逆向工程类项目的复兴** — Ghidra（NSA 出品）重回趋势，可能与近期安全事件有关。

### 语言热度：
- **Python** 依然是 AI 项目首选
- **TypeScript** 在工具链/基础设施层占比很高
- **Rust** 在终端工具领域强势（Codex、OpenLogi、dbx）
- **Go** 在网络/基础设施（Tailscale、路由）

---

## 💡 值得深挖 TOP 3

### 1. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) + [claude-plugins-community](https://github.com/anthropics/claude-plugins-community)
**理由：** Anthropic 官方下场建了插件目录（官方 + 社区两个仓库）。这意味着 Claude Code 的插件生态正式起步，而且是官方认证的。值得研究插件规范，抢占早期生态位。
**建议：** 研究插件规范，看看能不能给 Hermes 写个 Claude Code 插件。

### 2. [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) ⭐ +574/天
**理由：** JetBrains 出的"帮 AI 写现代 Go 代码"的指南。说明连 JetBrains 都在专门为 AI 编码代理优化代码规范和上下文了——这个方向很新。
**建议：** 收藏，把里面的规范整合进自己的 AI 编码 prompt 里。

### 3. [tailscale/tailcat](https://github.com/tailscale/tailcat) ⭐ +965/天
**理由：** Tailscale 出品的"netcat 替代品"，走 Tailscale 数据平面但不依赖控制平面。对于需要安全内网穿透的场景非常实用。
**建议：** 试试替代 nc 做内网调试，安全又方便。

---

## 📅 周榜亮点

### 持续霸榜：
- **freestylefly/awesome-gpt-image-2** — 周增 12,877 ⭐，GPT-Image2 提示词库持续火爆
- **openai/codex** — 周增 9,109 ⭐，Rust 终端代理热度不减
- **tt-a1i/archify** — 周增 11,099 ⭐，Agent 画图工具稳居前列

### 本周新晋黑马：
- **[basecamp/omarchy](https://github.com/basecamp/omarchy)** — Basecamp 出的"漂亮现代有主见的 Linux"，Shell 项目周增 5,942。Basecamp（DHH 的公司）出品必有话题。
- **[MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)** — 跑在本地的 AI 求职框架，基于 Claude Code，自动评估职位、定制简历。周增 4,828。
- **[AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi)** — Rust 写的罗技 Options+ 替代品。罗技用户积怨已久。周增 4,825。
- **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** — 免费用 Claude Code/Codex/Pi，13 亿+ 免费 token。周增 4,769。

---

## 🎬 视频选题建议

### 选题 1：「开源间谍卫星：我用浏览器监控了整个地球」
用 [gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) 做演示。标题自带流量，"间谍""卫星""开源"都是关键词。可以讲讲开源卫星情报（OSINT）的背景，演示 3D 地球上的实时数据，讨论隐私和安全的边界。

### 选题 2：「Agent Skills：10 行文件让所有 AI 编辑器获得新能力」
对比演示 archify（画图）、scientific-agent-skills（科研）在 Claude Code、Cursor、Codex 中的效果。讲解 "Agent Skill" 这个新范式为什么可能比传统 npm 包更有影响力。顺便介绍 Anthropic 刚建的官方插件目录。

---

## 📊 完整日榜数据

| # | 项目 | 语言 | 日增⭐ | 简介 |
|---|------|------|--------|------|
| 1 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | JS | +4,562 | Agent 画图技能（架构/流程/时序图） |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | JS | +3,829 | 浏览器间谍卫星模拟器 |
| 3 | [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) | JS | +1,687 | GPT-Image2 工业级提示词引擎 |
| 4 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JS | +1,396 | 让 AI 像懒高级工程师一样思考 |
| 5 | [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | Python | +1,144 | 开源 AI 视频制作系统 |
| 6 | [tailscale/tailcat](https://github.com/tailscale/tailcat) | Go | +965 | netcat over Tailscale |
| 7 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Python | +720 | AI 科学家技能库（163 个技能） |
| 8 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | Python | +703 | AI 工程从零开始教程 |
| 9 | [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines) | Go | +574 | 帮 AI 写现代 Go 的规范 |
| 10 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | TS | +433 | 34 个免费 LLM 供应商聚合 |
| 11 | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | +457 | Anthropic 官方 Claude 插件目录 |
| 12 | [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) | Python | +326 | 截图转代码 |
| 13 | [cursor/plugins](https://github.com/cursor/plugins) | TS | +246 | Cursor 插件规范和官方插件 |
| 14 | [marin-community/marin](https://github.com/marin-community/marin) | Python | +236 | 基础模型研发开源框架 |
| 15 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | TS | +202 | 零服务器代码智能引擎 |
| 16 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | Java | +191 | NSA 逆向工程框架 |
| 17 | [swoole/typephp](https://github.com/swoole/typephp) | PHP | +188 | 编译 PHP 为原生二进制 |
| 18 | [google/googletest](https://github.com/google/googletest) | C++ | +156 | Google 测试框架 |
| 19 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | TS | +67 | Chrome DevTools for 编码代理 |
| 20 | [livekit/agents](https://github.com/livekit/agents) | Python | +22 | 实时语音 AI 代理框架 |

---

*报告由奴才自动生成 | 2026-08-29 09:00*
