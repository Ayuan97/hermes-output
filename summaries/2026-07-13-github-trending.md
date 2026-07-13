# 🔥 GitHub 趋势速览 — 2026年7月13日（周一）

## 一句话总览

> 今天 GitHub 被 **AI Agent 基础设施**全面占领：从 Agent 安全护栏、MCP 服务器、Agent 多路复用器，到 Claude Code 生态的各种插件和 token 压缩工具——我们正身处 "Agent 基建" 时代。另外 AI 量化交易和 Rust 重写经典软件也在持续火热。

---

## 🚀 爆款项目 TOP 5（按日增 star 排序）

### 1. HKUDS/Vibe-Trading ⭐+768/天（总 20,561）
🔗 https://github.com/HKUDS/Vibe-Trading

**是什么：** 港大开源的"氛围交易" AI 代理，用 LLM 做量化交易决策。

**为什么火：** 把 Vibe Coding 的概念延伸到金融交易领域，让不懂编程的人也能用自然语言描述交易策略。AI + 量化的组合永远是流量密码。

**跟主子有啥关系：** 如果对 AI 量化感兴趣，这个项目值得 clone 下来研究它的 Agent 架构和策略编排方式。不过实盘需谨慎。

---

### 2. malisper/pgrust ⭐+518/天（总 2,472）
🔗 https://github.com/malisper/pgrust

**是什么：** 用 Rust 重写的 PostgreSQL，已通过 100% 的 Postgres 回归测试。

**为什么火：** Rust 重写经典 C 项目的趋势又添重磅选手。Postgres 是最关键的数据库之一，能用 Rust 完全兼容地重写，技术含量极高。性能提升和内存安全是核心卖点。

**跟主子有啥关系：** 如果关注数据库技术或 Rust 生态，这是里程碑级别的项目。即使不直接用，看看它的架构设计也很有启发。

---

### 3. anthropics/claude-cookbooks ⭐+459/天（总 48,415）
🔗 https://github.com/anthropics/claude-cookbooks

**是什么：** Anthropic 官方出品的 Claude 使用示例合集，各种 notebook 和 recipes。

**为什么火：** Claude 生态持续扩大，官方 cookbook 是学习最佳实践的第一入口。Claude Code 火了之后更多人想找"怎么用好 Claude"的参考。

**跟主子有啥关系：** 直接能用。找灵感、学 prompt 技巧、了解 Claude 最新能力，都值得翻翻。

---

### 4. Dicklesworthstone/destructive_command_guard ⭐+444/天（总 2,912）
🔗 https://github.com/Dicklesworthstone/destructive_command_guard

**是什么：** 用 Rust 写的 Agent 安全护栏，拦截 AI 代理执行的危险 git/shell 命令。

**为什么火：** AI Agent 越来越能干，但也越来越容易干坏事（`rm -rf`、`git push --force`）。这个项目精准解决了"让 Agent 干活但别把家拆了"的痛点。

**跟主子有啥关系：** **强烈推荐**。如果日常用 Claude Code/Codex 等 Agent 编程工具，装上这个能避免很多悲剧。Rust 写的，性能没话说。

---

### 5. Shubhamsaboo/awesome-llm-apps ⭐+408/天（总 118,553）
🔗 https://github.com/Shubhamsaboo/awesome-llm-apps

**是什么：** 100+ 可以直接运行的 AI Agent 和 RAG 应用合集，clone 即用。

**为什么火：** 11.8 万 star 的常青项目，持续更新中。"能跑起来的 demo"比什么都值钱。

**跟主子有啥关系：** 找项目灵感、快速原型验证的宝库。需要某个功能的 Agent？先来这里看看有没有现成的。

---

## 📈 技术趋势洞察

### 🔴 爆涨方向

- **AI Agent 安全/治理**：destructive_command_guard（护栏）、CubeSandbox（沙箱）、strix（渗透测试）——Agent 越强，安全需求越大
- **Claude Code 生态爆发**：cookbooks、templates、skills（345 个技能包）、caveman（token 压缩 65%）、claude-video（让 Claude 看视频）——Claude Code 已经形成了一个完整的插件经济
- **AI 量化交易**：Vibe-Trading + ai-hedge-fund 双双上榜，"用 AI 炒股"的需求永远不缺关注者
- **Agent 多路复用/编排**：herdr（终端 Agent 多路复用器）、orca（并行 Agent 舰队）、background-agents——从单个 Agent 到 Agent 集群管理

### 🟡 持续热门

- **Rust 重写一切**：pgrust（Postgres→Rust）、destructive_command_guard、RuView（WiFi 感知）
- **MCP 协议生态**：DesktopCommanderMCP、chrome-devtools-mcp——MCP 已成 Agent 工具接入的事实标准
- **AI 网关/路由**：OmniRoute（231+ 提供商、50+ 免费）——"用最少的钱调最多的模型"

### 🟢 值得关注的新信号

- **token 优化成为独立赛道**：caveman 一周涨了近 4000 star，核心就一个：压缩 token 省钱。说明 AI 使用成本已经是开发者核心痛点
- **"离线/本地优先"回归**：meetily（100% 本地 AI 会议纪要）、project-nomad（离线生存电脑）——隐私和离线能力重新被重视

---

## 💡 值得深挖 TOP 3

### 1. 🛡️ destructive_command_guard
**理由：** 解决 AI Agent 编程中最容易被忽视但后果最严重的问题——安全防护。Rust 写的，轻量高效。
**建议：** 立刻 clone 装上，配置到你的 Agent 工作流里。花 10 分钟可能救你 10 小时。

### 2. 🪨 JuliusBrussee/caveman（周榜 +3,992）
**理由：** "能用 caveman 语法为啥要多说话"——用石器时代的说话方式压缩 65% token。简单粗暴有效。
**建议：** 加到你的 Claude Code skills 里，立刻省 token 省钱。值得研究它的压缩策略能否应用到其他 Agent 场景。

### 3. 📊 HKUDS/Vibe-Trading
**理由：** 港大出品，把"Vibe Coding"理念带入量化交易，架构清晰，适合作为 Agent 编排的学习案例。
**建议：** 不建议直接实盘用，但值得 clone 下来研究它的多 Agent 协作和策略编排模式。

---

## 📅 周榜亮点（vs 日榜差异）

### 持续霸榜
- **awesome-llm-apps**（118K star）和 **home-assistant**（89K star）稳如磐石
- **system_prompts_leaks** 周涨 7,155 star，"偷看 AI 系统提示词"的需求持续火爆

### 本周黑马
- **Zackriya-Solutions/meetily**（周涨 7,440）：100% 本地运行的 AI 会议纪要助手，Rust 加持的 Parakeet/Whisper 转录，比云端方案快 4 倍。隐私第一。
- **iOfficeAI/OfficeCLI**（周涨 6,978）：专为 AI Agent 打造的 Office 套件（Word/Excel/PPT），单二进制、不需要装 Office。Agent 自动化办公的利器。
- **stablyai/orca**（周涨 4,481）：并行 Agent 舰队管理 ADE，桌面端+移动端都能用。
- **usestrix/strix**（周涨 4,143）：开源 AI 渗透测试工具，自动发现并修复漏洞。安全领域的新星。

---

## 🎬 视频选题建议

### 选题 1："AI Agent 安全防护指南——别让 AI 把你的代码删了"
**切入点：** 从 destructive_command_guard 出发，演示 AI Agent 可能造成的危险操作，然后展示如何用护栏工具防护。可以顺带讲 CubeSandbox（沙箱）和权限控制。实用性极强，每个用 Agent 编程的人都需要。
**预估热度：** ⭐⭐⭐⭐⭐（痛点明确，受众广）

### 选题 2："省 65% 的 AI 账单——Caveman 和 Token 压缩的黑科技"
**切入点：** 从 caveman 的"原始人说话法"切入，讲解 token 优化原理，演示实际省了多少 token/多少钱。然后延伸到 OmniRoute 的智能路由和免费模型接入。开发者最关心的成本话题。
**预估热度：** ⭐⭐⭐⭐⭐（省钱 = 流量密码）

---

## 📊 语言热度快照

| 语言 | 趋势 | 代表项目 |
|------|------|----------|
| Python | 🟢 稳定热门 | AI Agent、量化交易、Home Assistant |
| TypeScript | 🟢 强劲 | MCP 生态、Agent 编排、前端工具 |
| Rust | 🔴 爆涨 | pgrust、Agent 安全、性能工具 |
| Go | 🟡 平稳 | 基础设施、网络工具、安全 |
| C# | 🟡 偶现亮点 | PS5 模拟器 sharpemu、OfficeCLI |

---

*报告生成时间：2026-07-13 09:00 | 数据来源：GitHub Trending*
