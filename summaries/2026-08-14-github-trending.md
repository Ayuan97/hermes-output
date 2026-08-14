# 🔥 GitHub 趋势速览 — 2026年8月14日

## 一句话总览

**"Agent Skills" 生态全面爆发。** Anthropic、Google、Obsidian 创始人齐刷刷推出各自的 Agent 技能仓库，Cloudflare 直接给 Agent 发电脑，腾讯开源 Agent 记忆系统——整个 GitHub trending 被「让 AI Agent 干活」这条主线贯穿。同时端侧小模型（14MB 基础模型）和 Agent 编排框架也在快速起势。

---

## 🚀 爆款项目 TOP 5（日增 star 最多）

### 1. cathrynlavery/diagram-design — ⭐ +4,475/day
**🔗** https://github.com/cathrynlavery/diagram-design
**📝** 29 种编辑级图表模板，专为 Claude Code 设计，纯 HTML+SVG，不依赖 Mermaid。
**🔥 为什么火：** Claude Code 现在能直接生成漂亮的架构图、流程图了，不用再忍受 Mermaid 的默认样式。痛点精准——AI 生成的图表一直丑得没法直接用。
**💡 跟主子有关：** 直接能用在你的项目文档和视频脚本里。让 Claude Code 帮你画架构图，输出质量立马上一个档次。

### 2. macro-inc/macro — ⭐ +1,239/day（Rust）
**🔗** https://github.com/macro-inc/macro
**📝** 团队统一工作空间：邮件、聊天、文档、任务、Agent、电话、CRM 全整合，带共享 AI 记忆，用 @ 互相引用。
**🔥 为什么火：** 把 Notion + Slack + Linear + CRM 全捏在一起，还加了 AI 记忆层。Rust 写的性能有保障。解决的是团队工具碎片化的老大难问题。
**💡 跟主子有关：** 值得关注，这种 all-in-one + AI 记忆的产品形态可能是下一代协作工具的方向。

### 3. cactus-compute/needle — ⭐ +769/day（Python）
**🔗** https://github.com/cactus-compute/needle
**📝** 只有 14MB 的基础模型，给手机、可穿戴设备、智能家居、机器人用的。
**🔥 为什么火：** 14MB！这比大多数 app 的图标都小。端侧 AI 一直卡在模型大小上，这个项目可能突破了这个瓶颈。
**💡 跟主子有关：** 做视频选题绝佳——「14MB 的 AI 能在手机上干什么？」这个标题就很吸引人。

### 4. msitarzewski/agency-agents — ⭐ +778/day（Shell）
**🔗** https://github.com/msitarzewski/agency-agents
**📝** 一套完整的 AI 代理事务所：前端开发、Reddit 社区管理、风格注入、代码审查……每个 Agent 都是带性格和标准交付流程的专家。
**🔥 为什么火：** 不是一个工具，是一整套方法论+Agent 配置。相当于把「AI 代工厂」开源了。
**💡 跟主子有关：** 可以直接拿来组建自己的 AI 工作流，或者做视频讲「如何用 AI Agent 开一家虚拟公司」。

### 5. NVIDIA-NeMo/Switchyard — ⭐ +408/day（Rust）
**🔗** https://github.com/NVIDIA-NeMo/Switchyard
**📝** LLM 流量路由器，跨模型、跨供应商路由请求，保持 OpenAI/Anthropic API 兼容性，支持基准测试和成本优化。
**🔥 为什么火：** NVIDIA 出品，解决多模型调度的实际问题。Rust 写的，性能拉满。
**💡 跟主子有关：** 如果你的项目用了多个 LLM 供应商，这个值得集成。

---

## 📈 技术趋势洞察

### 1. Agent Skills 生态大爆发 ⚡
今天最炸裂的趋势。不是一个人搞 Agent Skills，是所有人都在搞：
- **Anthropic** 官方开源 `anthropics/skills`（+312/day）
- **Google** 推出 `google/skills`（周榜 +2,359）
- **Obsidian 创始人 kepano** 发布 `kepano/obsidian-skills`（+292/day）
- **Addy Osmani**（Chrome 团队大佬）的 `addyosmani/agent-skills`（周榜 +4,562）
- 还有把技术书转成 skill 的 `book-to-skill`（周榜 +3,789）
- 安全/逆向方向的 `reverse-skill`（周榜 +5,270）

**结论：** Agent Skills 正在成为 AI 编程 Agent 的「App Store」，各家都在抢占标准。谁先建好技能生态，谁就能锁定开发者。

### 2. 多 Agent 编排和工作空间
- `stablyai/orca`（TS，+1,157/day）—— 并行跑多个 Agent 的 ADE
- `earendil-works/pi`（TS，+1,029/day）—— Agent 开发工具包
- `holaboss-ai/holaOS`（TS，+241/day）—— 全能 AI Agent 工作空间
- `compozy/compozy`（Go）—— Agent 操作系统
- `huangruiteng/loopx`（Python，周榜 +1,967）—— 长时间 Agent 团队的状态管理

### 3. Agent 记忆系统
- `TencentCloud/TencentDB-Agent-Memory`（周榜 +5,388）—— 腾讯开源的团队级 Agent 记忆中枢，支持聊天记忆、技能、Wiki、代码图谱四种形态

### 4. 端侧/小模型持续升温
- `cactus-compute/needle`（14MB 基础模型）
- `shiyu-coder/Kronos`（+215/day）—— 金融市场基础模型

### 5. 语言/框架热度
- **Rust** 继续强势：macro、Switchyard、pdf-inspector 都上了榜
- **TypeScript** 在 Agent 工具链领域占据主导
- **Python** 依然是 AI/ML 主力语言
- **Go** 在基础设施和 RAG 领域稳定输出

---

## 💡 值得深挖 TOP 3

### 1. 🔥 stablyai/orca — ⭐ +1,157/day
**🔗** https://github.com/stablyai/orca
**理由：** 并行多 Agent 的 ADE（Agent Development Environment），支持桌面、手机和 VPS。这个品类是新的——相当于给 Agent 舰队用的 IDE。
**建议：** clone 下来试试，看它的多 Agent 并行调度机制是怎么做的。

### 2. 🔥 TencentCloud/TencentDB-Agent-Memory
**🔗** https://github.com/TencentCloud/TencentDB-Agent-Memory
**理由：** 腾讯开源的 Agent 记忆系统，周增 5,388 star，解决的是 Agent 跨会话、跨团队共享记忆的硬需求。
**建议：** 值得深入研究其记忆架构，看能不能整合到自己的 Agent 项目里。

### 3. 🔥 rtk-ai/rtk — ⭐ +160/day（Rust）
**🔗** https://github.com/rtk-ai/rtk
**理由：** CLI 代理工具，能把 LLM 的 token 消耗降低 60-90%。单个 Rust 二进制，零依赖。Agent 用 shell 命令时特别烧 token，这个直接解决了。
**建议：** 立刻装上试试，省钱就是赚钱。

---

## 📅 周榜亮点

### 持续霸榜
- **PrimeIntellect-ai/prime-agent** — 周增 12,476 ⭐，自我进化的 RLM Agent，本周最大黑马
- **cloudflare/computer** — 周增 3,599 ⭐，Cloudflare 出品，「给你的 Agent 一台电脑」，浏览器环境沙箱

### 本周新晋黑马
- **zhaoxuya520/reverse-skill** — 周增 5,270 ⭐，逆向/渗透安全技能路由包，支持 Claude Code、Kiro、Cursor 等，中文作者
- **virgiliojr94/book-to-skill** — 周增 3,789 ⭐，把技术书 PDF 转成 Claude Code 技能，学习+工作一体化
- **firecrawl/pdf-inspector** — 周增 3,251 ⭐，Rust 写的 PDF 智能分类和提取库，Firecrawl 出品
- **TapXWorld/ChinaTextbook** — 周增 2,369 ⭐，中国小初高大学全套 PDF 教材（持续有热度）

---

## 🎬 视频选题建议

### 选题 1：「14MB 的 AI 模型能在手机上干什么？」
围绕 `cactus-compute/needle` 做实测视频。14MB 的基础模型到底能干什么？和云端大模型比差多少？端侧 AI 的未来到底什么样？这个选题有数据、有冲突、有看点。

### 选题 2：「Agent Skills 生态大乱斗：Anthropic vs Google vs Obsidian」
Agent Skills 正在成为 AI 编程时代的 App Store。Anthropic、Google、Obsidian 创始人都在做，但路线完全不同。可以做个横向对比：谁的标准更好？谁的生态更有前途？开发者该怎么选？

---

## 📊 附录：各语言日榜 TOP 3

### Python
1. cactus-compute/needle（+769）— 14MB 端侧基础模型
2. semantica-agi/semantica（+713）— 图原生 AI 基础设施
3. unslothai/unsloth（+328）— 本地 LLM 运行/训练 UI

### TypeScript
1. stablyai/orca（+1,157）— 并行多 Agent ADE
2. earendil-works/pi（+1,029）— AI Agent 工具包
3. paperclipai/paperclip（+450）— Agent 管理应用

### Rust
1. macro-inc/macro（+1,239）— 团队统一工作空间
2. NVIDIA-NeMo/Switchyard（+408）— LLM 流量路由器
3. rtk-ai/rtk（+160）— CLI 代理降低 60-90% token 消耗

### Go
1. infiniflow/ragflow（+465）— RAG + Agent 引擎
2. knadh/listmonk（+40）— 自托管邮件列表管理
3. netdata/netdata（+34）— AI 驱动全栈可观测性

---

*报告生成时间：2026-08-14 09:00 | 数据来源：GitHub Trending*
