# 🔥 GitHub 趋势速览 — 2026年7月26日（周日）

## 一句话总览

**AI Agent 生态全面爆发：从"Skills 技能包"到"Agent 网关"再到"Agent 并行开发环境"，开发者正在为 AI Agent 搭建完整的基础设施。** 今天日榜和周榜超过一半的项目都跟 AI Agent 开发相关——Skills 框架、代码审查、Agent 路由、Agent IDE，这不是一个趋势，这是一场运动。

---

## 🚀 爆款项目 TOP 5

### 1. mattpocock/skills — ⭐+1,740/天 | +11,790/周
🔗 https://github.com/mattpocock/skills

**一句话：** Matt Pocock（TypeScript 圈顶流博主）把自己的 `.agents` 目录开源了，里面是精心调教的 Agent Skills 文件。

**为什么火：** AI Agent 时代，"怎么喂给 Agent 指令"成了新的核心技能。Matt 用 TypeScript 圈的名人效应带火了整个 Agent Skills 赛道，让开发者意识到：写好 skills 文件和写好代码一样重要。

**跟主子的关系：** 直接 clone 参考他的 skills 结构，优化自己的 Hermes/Agent 配置。做视频选题也非常合适——"大神是怎么调教 AI Agent 的"。

---

### 2. block/buzz — ⭐+2,491/天
🔗 https://github.com/block/buzz

**一句话：** Block（Jack Dorsey 的公司）出品的去中心化通信平台，Rust 写的，主打"蜂群思维"式多人协作。

**为什么火：** 日增 2491 星说明市场对"非 Slack/Discord 的团队协作"有强烈需求。Rust 实现保证性能，去中心化保证隐私。跟 bitchat（蓝牙网状通信）同一天上榜，去中心化通信赛道明显升温。

**跟主子的关系：** 关注去中心化社交/协作趋势，可以跟 bitchat 一起做一期"后 Slack 时代的沟通工具"选题。

---

### 3. permissionlesstech/bitchat — ⭐+1,720/天 | Swift
🔗 https://github.com/permissionlesstech/bitchat

**一句话：** 纯蓝牙网状网络聊天，不需要服务器、不需要互联网，IRC 风格。

**为什么火：** 1720 星/天，极其炸裂。在 AI 时代大家反而开始关注离线/无网通信，说明对数字主权和抗审查的需求在增长。Swift 写的，iOS 原生体验。

**跟主子的关系：** 话题性极强——"断网也能聊天"。适合做视频，演示两个手机在飞行模式下互相发消息。

---

### 4. diegosouzapw/OmniRoute — ⭐+1,381/天 | +11,147/周 | TypeScript
🔗 https://github.com/diegosouzapw/OmniRoute

**一句话：** 免费开源的 AI 模型网关，一个端点接入 290+ 供应商、500+ 模型（包括 90+ 免费），支持自动降级、token 压缩省 15-95%。

**为什么火：** 周增 11,147 星！Agent 开发者最痛的问题就是"我要接 Claude 又要接 GPT 又要接 DeepSeek"，OmniRoute 一站式解决。还内置 RTK+Caveman 压缩，直接省钱。

**跟主子的关系：** 如果主子在用多个 LLM API，这个可以直接用起来。也是很好的视频选题——"一个 API key 用遍所有大模型"。

---

### 5. earendil-works/pi — ⭐+523/天 | +5,167/周 | TypeScript
🔗 https://github.com/earendil-works/pi

**一句话：** 开源 AI Agent 工具包：统一 LLM API + Agent 循环 + TUI + 编码 Agent CLI，全套打包。

**为什么火：** 周增 5167 星，配套 pi-web（Web UI）也上了榜。定位是"开源版 Claude Code / Codex"，开发者想要自主可控的 Agent 开发栈。

**跟主子的关系：** 可以 clone 下来研究 Agent 循环的实现原理，对理解 Agent 架构很有价值。

---

## 📈 技术趋势洞察

### 🔥 Agent Skills 成为新赛道
今天最显著的信号：**"怎么写 Skills 文件"比"怎么写代码"更重要了**。上榜的 Skills 相关项目：
- `mattpocock/skills` — 1,740/天，TypeScript 大神的 .agents 目录
- `obra/superpowers` — 479/天，Agent 技能框架
- `Nutlope/hallmark` — 4,881/周，反 AI 垃圾设计风格的 Skills
- `ComposioHQ/awesome-claude-skills` — 577/天，Claude Skills 精选列表
- `affaan-m/ECC` — 377/天，Agent 性能优化系统
- `ibelick/ui-skills` — 1,647/周，给设计工程师的 Skills

这说明 **Agent 开发正在从"写代码驱动"转向"写 Prompt/Skills 驱动"**，一个新的软件工程范式正在成形。

### 🔥 AI 代码审查工具扎堆
- `alibaba/open-code-review`（431/天）— 阿里出品，混合架构（确定性管线 + LLM Agent），内置 NPE/线程安全/XSS/SQL注入检测规则
- `tirth8205/code-review-graph`（6,423/周）— 本地优先的代码智能图谱，让 AI 只读需要的代码

说明 AI 代码审查正从"玩具"走向"生产级工具"。

### 📊 语言热度
- **Rust**：buzz（通信）、harper（语法检查）、Pumpkin（MC服务器）、RuView（WiFi感知）、rtk（token压缩）—— 5 个项目上榜，持续走强
- **TypeScript**：依然是 Agent/Web 生态主力，OmniRoute、pi、worldmonitor 等
- **Go**：阿里 open-code-review、superfile（终端文件管理器）表现稳健
- **Python**：偏向 ML/教育方向（Kronos 金融模型、dive-into-llms 教程）

### 🆕 新兴模式
- **Agent 并行开发**：`stablyai/orca`（7,327/周）让你同时跑多个 Agent，桌面/手机/VPS 都行
- **Agent 网关**：OmniRoute 做模型路由，rtk 做 token 压缩，配套基础设施在完善
- **去中心化通信回潮**：buzz + bitchat 同天爆发

---

## 💡 值得深挖 TOP 3

### 1. OmniRoute — 建议：直接用起来
> 一个端点接所有大模型，还自带 token 压缩省钱。主子如果日常用多个 LLM API，这个能省不少事。500+ 模型的统一接口，还支持 MCP/A2A。

### 2. alibaba/open-code-review — 建议：clone 研究 + 整合
> 阿里在大规模代码审查上的实战经验沉淀，混合架构设计很精妙（确定性规则 + LLM Agent 协作）。可以看看它的内置规则集怎么写的，对优化自己的代码审查流程很有参考价值。

### 3. ruvnet/RuView — 建议：做视频
> WiFi 信号变空间感知——不需要摄像头就能检测人体存在、监测生命体征。Rust 实现，话题性满分。"用 WiFi 就能当监控？"这种标题点击率绝对高。

---

## 📅 周榜亮点

### 持续霸榜
- **mattpocock/skills** — 周增 11,790，绝对王者，Agent Skills 赛道的定义者
- **OmniRoute** — 周增 11,147，AI 网关赛道的搅局者
- **bojieli/ai-agent-book** — 周增 16,579！《深入理解 AI Agent》开源书，中文作者李博杰，这本书的爆火说明 Agent 知识体系化需求巨大

### 本周黑马
- **koala73/worldmonitor** — 周增 12,085，AI 驱动的实时全球情报仪表盘，地缘政治监控 + 新闻聚合 + 基础设施追踪
- **stablyai/orca** — 周增 7,327，"Agent 并行开发环境"这个品类可能是它定义的
- **tirth8205/code-review-graph** — 周增 6,423，用图谱给 AI 做代码上下文压缩

### 日榜 vs 周榜差异
日榜上 `block/buzz` 和 `bitchat`（去中心化通信）是今天新爆发的，周榜上还没有。`ai-agent-book` 虽然今天没上日榜，但周增 16,579 说明持续热度极高。

---

## 🎬 视频选题建议

### 选题 1：「AI Agent 时代最重要的不是写代码，是写 Skills」
角度：从 mattpocock/skills 爆火切入，讲 Agent Skills 这个新赛道。演示怎么给自己的 Agent 写好的 Skills 文件，对比写得好和写得烂的效果差异。可以串联 obra/superpowers、Nutlope/hallmark 等项目。

### 选题 2：「一个 API 用遍所有大模型？OmniRoute 深度体验」
角度：演示 OmniRoute 的实际使用——接 Claude、接 GPT、接 DeepSeek、接 Kimi，展示自动降级和 token 压缩效果。算一笔经济账：用 OmniRoute 能省多少钱？

---

## 📋 各语言日榜速览

### Python
| 项目 | 日增星 | 说明 |
|------|--------|------|
| ComposioHQ/awesome-claude-skills | +577 | Claude Skills 精选列表 |
| shiyu-coder/Kronos | +319 | 金融市场基础模型 |
| Alishahryar1/free-claude-code | +213 | 免费用 Claude Code |
| VectifyAI/PageIndex | +180 | 无向量化 RAG 索引 |
| OpenDCAI/DataFlow | +118 | LLM 数据清洗管线 |

### TypeScript
| 项目 | 日增星 | 说明 |
|------|--------|------|
| diegosouzapw/OmniRoute | +1,381 | AI 模型网关 290+ 供应商 |
| koala73/worldmonitor | +1,041 | 全球情报仪表盘 |
| earendil-works/pi | +523 | AI Agent 工具包 |
| CoreBunch/Instatic | +426 | 开源 Webflow 替代品 |
| pingdotgg/t3code | +202 | 编码工具 |

### Rust
| 项目 | 日增星 | 说明 |
|------|--------|------|
| block/buzz | +2,491 | 去中心化通信平台 |
| ruvnet/RuView | +559 | WiFi 信号空间感知 |
| Automattic/harper | +503 | 离线语法检查器 |
| Pumpkin-MC/Pumpkin | +358 | 高性能 MC 服务器 |
| rtk-ai/rtk | +179 | LLM token 压缩代理 |

### Go
| 项目 | 日增星 | 说明 |
|------|--------|------|
| yorukot/superfile | +586 | 终端文件管理器 |
| alibaba/open-code-review | +431 | AI 代码审查工具 |
| multica-ai/multica | +156 | Agent 管理平台 |
| infiniflow/ragflow | +71 | RAG 引擎 |
| gohugoio/hugo | +34 | 静态网站生成器 |

---

*报告生成时间：2026-07-26 09:00 | 数据来源：GitHub Trending*
