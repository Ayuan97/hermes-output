# 🔥 GitHub 趋势速览 - 2026-07-02

## 一句话总览

**AI Agent 生态全面井喷** — 今天 GitHub 日榜几乎被 AI Agent 工具链霸屏：从 Agent 多路复用器、沙盒运行环境、代码智能记忆、到 AI 渗透测试工具，整个 Agent 开发生命周期的基础设施都在集中爆发。同时 AI+金融交易和 AI+视频制作两条线也在快速升温。

---

## 🚀 爆款项目 TOP 5（日增 star 排名）

### 1. hasaneyldrm/exercises-dataset ⭐+2,470/day（总计 8,425）
- **干什么的**：433 个健身运动的数据集，每条包含名称、目标肌群、器械、指令、缩略图和动画视频
- **为什么火**：健身 AI 应用的数据基础设施，开源+结构化+带动画，正好填了运动健康 AI 领域的空白
- **跟主子有啥关系**：如果做健身类 AI 应用或数据分析选题，这个数据集直接可用。也可以作为"开源数据集"选题聊聊 AI 训练数据的质量问题
- 🔗 https://github.com/hasaneyldrm/exercises-dataset

### 2. msitarzewski/agency-agents ⭐+2,114/day（总计 123,434）
- **干什么的**：一套完整的 AI Agent 集合——前端工程师、Reddit 社区运营、创意注入器、事实核查员等，每个 Agent 都有人设、流程和交付物
- **为什么火**：12万+ star 的超级爆款，把 "AI Agent 专业化" 做到了极致，每个 Agent 都是可落地的角色模板
- **跟主子有啥关系**：直接参考里面的 Agent prompt 和角色设计，对自己的 AI 工作流有帮助。做视频可以聊"AI 公司组织架构"
- 🔗 https://github.com/msitarzewski/agency-agents

### 3. usestrix/strix ⭐+1,211/day（总计 29,729）
- **干什么的**：开源 AI 渗透测试工具，用 AI 自动发现和修复应用漏洞
- **为什么火**：安全+AI 的组合拳，解决了安全团队人手不足的核心痛点。周榜也同时在涨（+2,804/week）
- **跟主子有啥关系**：关注 AI 安全赛道，可以做一期"AI 黑客工具"的选题，话题热度很高
- 🔗 https://github.com/usestrix/strix

### 4. diegosouzapw/OmniRoute ⭐+1,010/day（总计 9,532）
- **干什么的**：免费 AI 网关，一个端点接入 231+ 家模型提供商（50+ 免费），支持 Claude Code、Codex、Cursor、Cline 等编码工具，RTK+Caveman 压缩省 15-95% token
- **为什么火**：精准命中 AI 编码工具用户的痛点——多模型切换麻烦、API 费用高。免费+多模型+省 token 三杀
- **跟主子有啥关系**：如果日常用多个 AI 编码工具，这个能统一管理 API 并省钱。值得试用
- 🔗 https://github.com/diegosouzapw/OmniRoute

### 5. microsoft/AI-For-Beginners ⭐+1,096/day（总计 50,449）
- **干什么的**：微软官方出品的 AI 入门课程，12 周 24 节课
- **为什么火**：微软背书+免费+体系化，在 AI 全民化浪潮下持续霸榜
- **跟主子有啥关系**：推荐给朋友入门用，或者作为视频素材来源——"微软免费 AI 课程推荐"
- 🔗 https://github.com/microsoft/AI-For-Beginners

---

## 📈 技术趋势洞察

### 🔴 强势方向

1. **AI Agent 基础设施层**：herdr（Agent 多路复用终端）、CubeSandbox/agentos（Agent 沙盒）、cognee（Agent 记忆平台）、codebase-memory-mcp（代码智能 MCP）、page-agent（页面 GUI Agent）—— 整个 Agent 运行时的基础件都在补齐
2. **AI + 安全/渗透**：strix、VulnClaw、Anthropic Cybersecurity Skills 三个项目同时上榜，AI 在安全攻防领域的应用正在加速
3. **AI + 金融交易**：Vibe-Trading、AI-Berkshire、daily_stock_analysis，AI 交易/投研工具形成一个小集群
4. **MCP 协议生态**：多个项目明确提到 MCP server/skill，说明 MCP 正在成为 Agent 工具调用的事实标准

### 🟡 值得关注

- **Rust 在 Agent 工具链的渗透**：herdr、CubeSandbox、karukan 都是 Rust 写的，高性能 Agent 基础设施偏好 Rust
- **视频制作 AI 化**：OpenMontage（周增 12,624 star！）和 video-use 都在做"用 AI Agent 编辑视频"
- **design.md**：Google Labs 出的视觉设计规范标准，专门给编码 Agent 用的，说明大厂在认真考虑"让 Agent 理解设计语言"

### 🟢 语言/框架热度

| 语言 | 日榜项目数 | 趋势 |
|------|-----------|------|
| Python | 最多 | AI/ML 领域依旧统治者 |
| TypeScript | 次多 | Agent 前端/全栈工具 |
| Rust | 3个 | Agent 基础设施首选 |
| Go | 较少 | 偏传统 DevOps/网络工具 |
| Swift | 1个 | macOS 原生应用冒头 |

---

## 💡 值得深挖 TOP 3

### 1. ogulcancelik/herdr（Rust，⭐+609/day）
- **理由**：终端里的 Agent 多路复用器，一个终端同时管理多个 AI Agent 并行工作。解决了"开一堆终端跑 Agent"的效率问题
- **建议**：clone 试试，如果你日常跑多个 Claude Code/Codex 实例，这个工具能大幅改善体验

### 2. calesthio/OpenMontage（周增 12,624 star）
- **理由**：全球首个开源 Agentic 视频制作系统，12 条 pipeline，52 个工具。周增 star 数炸裂
- **建议**：关注+clone 研究，AI 视频制作是下一个风口，这个项目的架构值得深入了解。适合做视频选题

### 3. facebook/astryx（TypeScript，⭐+708/day）
- **理由**：Facebook 开源的设计系统，号称"agent ready"——意味着这套设计系统天然适合 AI Agent 来生成和操作 UI
- **建议**：关注 Facebook 在 Agent-native UI 方向上的思路，对未来 Agent 做前端开发有参考价值

---

## 📅 周榜亮点

### 持续霸榜
- **microsoft/AI-For-Beginners**：50k+ star，AI 入门领域的常青树
- **ripienaar/free-for-dev**：4,268/week，开发者免费资源合集永远有人看

### 本周黑马 🐴
- **calesthio/OpenMontage**：周增 12,624 star！开源 AI 视频制作系统，本周最大黑马
- **DeusData/codebase-memory-mcp**：周增 9,697 star，代码智能 MCP 服务器，把代码库索引成持久化记忆给 Agent 用
- **Panniantong/Agent-Reach**：周增 8,791 star，给 AI Agent 装上"眼睛"，能读取和搜索 Twitter、Reddit 等全网内容
- **xbtlin/ai-berkshire**：周增 6,758 star，AI 版伯克希尔，用 Claude Code/Codex 做价值投资研究

### 日榜 vs 周榜差异
日榜偏重"新出炉+爆发力强"的项目（如 exercises-dataset、OmniRoute），周榜偏重"持续影响力"的项目（如 simplex-chat 周增 6,289、cognee 周增 5,171）。

---

## 🎬 视频选题建议

### 选题 1：「AI Agent 的操作系统长什么样？」
- 角度：今天 trending 里有 Agent 多路复用器（herdr）、Agent 沙盒（CubeSandbox）、Agent 记忆（cognee）、Agent 网关（OmniRoute）—— 拼起来就是一个完整的 "Agent OS"。可以做一期"AI Agent 的基础设施全家桶"
- 热度：极高，多个项目同时在榜

### 选题 2：「AI 黑客来了：开源渗透测试工具大赏」
- 角度：strix + VulnClaw + Anthropic 安全技能包，三个项目展示 AI 在安全攻防中的应用。可以做"我用 AI 工具给自己的网站做渗透测试"的实操视频
- 热度：安全+AI 话题自带流量

---

*数据采集时间：2026-07-02 09:00 | 来源：GitHub Trending*
