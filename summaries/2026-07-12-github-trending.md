# 🔥 今日 GitHub 趋势速览 — 2026年7月12日（周日）

## 一句话总览

**AI Agent 工具链全面爆发。** 今天 GitHub 被 Claude/Copilot 生态的 MCP 服务器、Agent Skills 框架、AI 安全工具屠榜了。"给 AI 编程助手加技能"已经成了一个独立的赛道，从底层 runtime（Bun 日增 658 星）到上层 skill 库（Google Stitch Skills 日增 340 星）全在涨。最炸裂的是 obra/superpowers 这个 agentic 框架，日增 740 星，总星标已超 25 万。

---

## 🚀 爆款项目 TOP 5

### 1. wonderwhy-er / DesktopCommanderMCP
🔗 https://github.com/wonderwhy-er/DesktopCommanderMCP
⭐ 7,776 (+909/day) | TypeScript

**一句话：** 给 Claude 装一个"桌面指挥官"——终端控制、文件搜索、diff 编辑，一个 MCP 服务器搞定。

**为什么火：** 解决了 Claude Code 的核心痛点——不能直接操作本地文件系统和终端。开发者需要让 AI 能"看到"和"操作"他们的开发环境，这个工具补上了这个缺口。周榜也上了（+1,451/week），说明不是昙花一现。

**对主子的价值：** 如果主子在用 Claude Code 做开发，这个 MCP server 几乎是必装的。可以直接 clone 试一下。做视频选题也不错——"让 Claude 真正控制你的电脑"。

---

### 2. malisper / pgrust
🔗 https://github.com/malisper/pgrust
⭐ 2,062 (+774/day) | Rust

**一句话：** 用 Rust 重写的 PostgreSQL，已通过 100% 的 Postgres 回归测试。

**为什么火：** 这是一个大胆到近乎疯狂的项目——用 Rust 从零实现 PostgreSQL。能通过全部回归测试说明兼容性已经做到了生产级。Rust 社区对此类"用 Rust 重写经典基础设施"的项目一直热情高涨（类似 Firecracker、ripgrep 的路线）。

**对主子的价值：** 目前还不适合生产使用，但值得关注其发展。如果未来成熟了，对数据库性能和安全性要求高的场景会有大用。做技术视频选题很棒——"PostgreSQL 的 Rust 版来了"。

---

### 3. obra / superpowers
🔗 https://github.com/obra/superpowers
⭐ 252,458 (+740/day) | Shell

**一句话：** Agentic Skills 框架 + 软件开发方法论，号称"真正能用的 AI 编程助手工作流"。

**为什么火：** 25 万星标说明这已经不是一个普通项目了，而是一种运动。它提供了一套结构化的方法论，让 AI Agent 在写代码时不再是"聊天机器人"，而是一个有系统思维的开发者。

**对主子的价值：** 强烈建议 clone 下来研究其方法论。不管用不用 Claude，这套"agentic development"的思路对任何 AI 辅助编程都有参考价值。

---

### 4. oven-sh / bun
🔗 https://github.com/oven-sh/bun
⭐ 94,568 (+658/day) | Rust

**一句话：** 用 Rust 写的超快 JavaScript 运行时 + 打包器 + 测试运行器 + 包管理器，四合一。

**为什么火：** Bun 一直在稳步增长，今天突然爆发可能是新版本发布或者某项重大功能更新。9.4 万星说明它已经从"挑战者"变成了"主流选择"。

**对主子的价值：** 如果还在用 Node.js + npm + Jest 的组合，值得试试 Bun 一站式搞定。速度提升非常明显。

---

### 5. google-labs-code / stitch-skills
🔗 https://github.com/google-labs-code/stitch-skills
⭐ 7,065 (+340/day) | TypeScript

**一句话：** Google Labs 出品的 Agent Skills 库，专为 Stitch MCP 服务器设计，遵循 Agent Skills 开放标准。

**为什么火：** Google 官方下场做 Agent Skills，说明这个方向被大厂认可了。"开放标准"这几个字很关键——意味着不同 AI 编程工具之间可以共享技能。

**对主子的价值：** 如果主子在搭建自己的 AI Agent 工作流，这套 Skills 可以直接用。也值得研究其标准规范，看看 Agent Skills 的生态怎么建。

---

## 📈 技术趋势洞察

### 🔴 AI Agent 工具链 = 今天的绝对主角
- **MCP 服务器**持续井喷：DesktopCommanderMCP、Chrome DevTools MCP、Stitch MCP
- **Agent Skills 生态**正在成型：Google Stitch Skills、superpowers、claude-skills（345个技能）
- **Agent 多路复用**：herdr（终端 agent 复用器）、orca（并行 agent 舰队 ADE）
- **AI 网关/路由**：OmniRoute 一个端点连 231+ 个 AI 供应商

### 🟢 Rust 基建化加速
- pgrust（Rust 重写 Postgres）、Bun（Rust 写 JS 运行时）、CubeSandbox（腾讯的 AI Agent 沙箱）
- 趋势：越来越多关键基础设施在用 Rust 重写，从数据库到运行时到安全沙箱

### 🟡 安全 + AI 交叉升温
- usestrix/strix（AI 渗透测试，周增近 5000 星）
- pentagi（全自动 AI 渗透测试 Agent）
- microsoft/agent-governance-toolkit（Agent 治理工具包）

### 🔵 C++ 意外回春
- 今天日榜有 5 个 C++ 项目：Catch2、abseil-cpp、meshoptimizer、asio、nasa/fprime
- 可能和嵌入式/游戏/高性能计算领域的某个动态有关

### 语言热度分布（日榜 24 个项目）
- TypeScript: 8 个（33%）
- C++: 5 个（21%）
- Python: 3 个
- Rust: 3 个
- Go: 1 个
- JavaScript: 2 个
- Shell: 1 个
- C: 1 个

---

## 💡 值得深挖 TOP 3

### 1. 🎯 asgeirtj / system_prompts_leaks
🔗 https://github.com/asgeirtj/system_prompts_leaks
⭐ 56,236 (+7,731/week)

**理由：** 一周涨了 7700+ 星，提取了 Claude、ChatGPT、Google 等大模型的系统提示词。这个仓库本身就是一座金矿——研究各家 AI 的 system prompt 设计思路，对做 AI 产品的人太有价值了。

**建议：** 立刻 clone，仔细研读各家 prompt 设计。适合做视频——"揭秘各大 AI 的系统提示词"。

---

### 2. 🎯 usestrix / strix
🔗 https://github.com/usestrix/strix
⭐ 40,558 (+4,987/week) | Python

**理由：** 开源 AI 渗透测试工具，能自动发现并修复应用漏洞。周增近 5000 星说明安全 + AI 的需求极大。4 万星说明社区认可度很高。

**建议：** 可以在隔离环境里 clone 试试，看看它到底能发现什么漏洞。对安全领域感兴趣的可以做视频。

---

### 3. 🎯 bradautomates / claude-video
🔗 https://github.com/bradautomates/claude-video
⭐ 7,557 (+4,399/week) | Python

**理由：** 让 Claude 能"看视频"——下载、抽帧、转录、喂给 Claude。多模态 AI 工作流的实用工具，一周涨 4400 星。

**建议：** 直接 clone 试试，用 /watch 命令让 Claude 分析视频。对做视频内容分析或自动字幕的需求很有用。

---

## 📅 周榜亮点

### 🏆 持续霸榜
- **obra/superpowers** — 日榜 +740，周榜也在前列，agentic 框架的统治地位
- **JuliusBrussee/caveman** — "原始人风格 Claude 技能"，通过减少 65% token 来省钱，8.8 万星（周增 4696）。创意满分

### 🐴 本周新晋黑马
- **Zackriya-Solutions/meetily** — AI 会议助手，一周 +8,579 星，Rust 写的实时转录 + Ollama 摘要。隐私优先的路线很受欢迎
- **iOfficeAI/OfficeCLI** — 专门为 AI Agent 设计的 Office 套件（Word/Excel/PPT），一周 +6,549 星。AI Agent 开始入侵办公自动化了
- **facebook/astryx** — Facebook 开源的 Agent-ready 设计系统，一周 +2,779 星

### ⚡ 值得注意的周榜项目（日榜没出现的）
- **openai/codex-plugin-cc** — 在 Claude Code 里用 Codex 来 review 代码或分配任务（+4,030/week）。OpenAI 和 Anthropic 的工具开始互相嵌入了
- **alibaba/page-agent** — 阿里巴巴的浏览器内 GUI Agent，用自然语言控制网页界面（+3,317/week）
- **ruvnet/RuView** — 用 WiFi 信号做空间感知/生命体征监测，无需摄像头（8 万星，+3,720/week）。黑科技

---

## 🎬 视频选题建议

### 选题 1：「AI Agent 技能大爆发：从 MCP 到 Skills，开发者工具链正在被重塑」
**素材：** DesktopCommanderMCP + Google Stitch Skills + superpowers + caveman + claude-skills
**角度：** 2026 年 AI 编程助手已经不是"一个聊天框"了，而是一个有技能系统、有 MCP 协议、有 Agent 框架的完整生态。通过演示几个热门 MCP server 和 Agent Skills，展示这个新世界的全貌。

### 选题 2：「系统提示词泄露大全：看看 Claude、GPT-5、Gemini 背后都写了什么」
**素材：** system_prompts_leaks 仓库（5.6 万星）
**角度：** 逐个解读各大 AI 的 system prompt 设计，分析其设计思路的异同。这类"揭秘向"内容天然有流量属性。

---

*数据采集时间：2026-07-12 09:00 | 数据来源：GitHub Trending*
