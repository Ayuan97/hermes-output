# 🔥 今日 GitHub 趋势速览 — 2026-06-18

## 一句话总览

**AI Agent 技能/工具生态全面爆发**。今天 trending 被「给 AI 编码助手加技能」的项目屠榜，同时 Apple 开源 Linux 容器工具、Google 发布时序预测基础模型，Rust 继续在基础设施领域攻城略地。

---

## 🚀 爆款项目 TOP 5（按日增 star 排序）

### 1. mattpocock/skills ⭐+1,523/day
- **语言**：Shell
- **链接**：https://github.com/mattpocock/skills
- **一句话**：Matt Pocock（TypeScript 大佬）的 `.claude` 目录，一套面向真实工程的 agent 技能集
- **为什么火**：直接从顶级工程师的实战配置里掏出来，不是理论派，是能用的东西。TypeScript 生态的开发者争相 clone
- **对主子有啥用**：可以参考里面的 skill 编写方式优化自己的 Hermes Agent 技能。**建议 clone 看看结构**

### 2. Panniantong/Agent-Reach ⭐+1,161/day
- **语言**：Python
- **链接**：https://github.com/Panniantong/Agent-Reach
- **一句话**：给 AI agent 一双「眼睛」，一个 CLI 工具读取/搜索 Twitter、Reddit、YouTube、GitHub、B站、小红书，零 API 费用
- **为什么火**：解决 AI agent 信息获取的刚需——不花钱就能让 agent 看全网内容。中文社区+海外同时爆发
- **对主子有啥用**：**强推关注**。可以整合进 Hermes 作为信息采集模块，做视频选题调研也极好用

### 3. obra/superpowers ⭐+1,129/day
- **语言**：Shell
- **链接**：https://github.com/obra/superpowers
- **一句话**：一套 agentic 技能框架 + 软件开发方法论，给 AI 编码助手注入「超能力」
- **为什么火**：不只是工具，是一套方法论。把 agent coding 从「能写代码」提升到「按工程规范写代码」
- **对主子有啥用**：可以借鉴其 skill 组织方式和开发流程思路

### 4. google-research/timesfm ⭐+606/day
- **语言**：Python
- **链接**：https://github.com/google-research/timesfm
- **一句话**：Google Research 出品的时序预测基础模型，预训练后可直接用于各类时间序列预测任务
- **为什么火**：时序预测一直是传统 ML 的领地，Google 把基础模型范式带进来了，效果碾压传统方法
- **对主子有啥用**：如果做量化/数据分析相关的内容，这个值得关注。**做视频选题的话热度够高**

### 5. Universal-Debloater-Alliance/universal-android-debloater-next-generation ⭐+457/day
- **语言**：Rust
- **链接**：https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation
- **一句话**：跨平台 GUI 工具，用 ADB 卸载 Android 预装垃圾应用，无需 root
- **为什么火**：隐私焦虑 + Android 用户苦预装应用久矣。Rust 写的 GUI，跨平台，开箱即用
- **对主子有啥用**：如果主子用 Android 设备，直接能用。**做「Android 去广告/去预装」类视频流量密码**

---

## 📈 技术趋势洞察

### 🔴 Agent Skills 生态大爆发（本周最强信号）
今天 trending 20 个项目里至少 **6 个直接和 AI agent 技能/工具链相关**：
- mattpocock/skills、obra/superpowers、earendil-works/pi、continuedev/continue、bytedance/UI-TARS-desktop、multica-ai/multica

这不是巧合——AI coding agent 已经从「能用」进入「好用」阶段，竞争焦点转向**技能生态**。谁的 agent 能力更强、skill 更丰富，谁就能吸引开发者。

### 🟡 Rust 基础设施持续扩张
- iroh（网络栈）、UAD-ng（Android 去预装）、nautilus_trader（量化交易引擎）、swc（前端工具链）
- Rust 在「需要性能 + 安全性」的基础设施领域已经站稳脚跟

### 🟢 时序 AI 走向主流
- TimesFM 今天日增 600+，基础模型进入时序预测领域
- 这意味着更多垂直 AI 应用将从「通用 LLM」转向「专用基础模型」

### 🔵 Apple 进军容器化
- 周榜第一 `apple/container`（+9,735/周）——Apple 官方开源的 Linux 容器工具
- 基于 Apple Virtualization.framework，纯 Swift 实现
- 信号：Apple 在服务器/云原生领域开始布局

---

## 💡 值得深挖 TOP 3

### 1. Panniantong/Agent-Reach
**理由**：零成本获取全网信息的能力，对 AI agent 来说是基础设施级别的能力
**建议**：clone 下来跑一遍，看能不能整合进 Hermes 的信息采集流程。**做一期「给 AI 装上千里眼」的视频，流量不会差**

### 2. google-research/timesfm
**理由**：Google 出品的基础模型，学术+工程双强，时序预测赛道的里程碑
**建议**：clone 跑个 demo 试试。**如果做「AI 预测未来」系列视频，这个是绝佳素材**

### 3. calesthio/OpenMontage
**理由**：开源 agentic 视频制作系统，12 条流水线、52 个工具、500+ agent 技能
**建议**：这个和主子做视频内容高度相关——**直接看看能不能用它辅助视频制作流程**。日增只有 98 但潜力巨大

---

## 📅 周榜亮点

| 项目 | 周增 star | 说明 |
|------|----------|------|
| addyosmani/agent-skills | +11,684/周 | Addy Osmani（Google Chrome 工程师）的 agent 技能集，**本周全站最火** |
| apple/container | +9,735/周 | Apple 官方 Linux 容器工具，Swift 实现 |
| chopratejas/headroom | +9,475/周 | 压缩 tool outputs/logs/RAG 上下文，节省 token |
| iptv-org/iptv | +7,355/周 | IPTV 频道集合，老牌常青项目 |
| Panniantong/Agent-Reach | +6,855/周 | 日榜+周榜双爆，持续霸榜 |
| phuryn/pm-skills | +5,333/周 | PM 技能市场，100+ agentic 技能 |
| NVIDIA/SkillSpector | +5,257/周 | NVIDIA 出的 AI agent 技能安全扫描器 |
| asgeirtj/system_prompts_leaks | +1,506/周 | 泄露各大 AI 模型的 system prompt |

**关键发现**：周榜前 10 里有 **6 个和 AI agent skills 相关**，加上 NVIDIA 都入局做安全扫描了——这个赛道已经不是概念，是真需求。

---

## 🎬 视频选题建议

### 选题 1：「AI Agent 的技能革命——从写代码到全栈工程」
- **切入点**：mattpocock/skills + obra/superpowers + addyosmani/agent-skills 三个项目对比
- **看点**：顶级工程师怎么调教 AI 编码助手？他们的 .claude 目录里藏了什么秘密？
- **预估热度**：🔥🔥🔥🔥（AI 编程 + 名人效应 + 实用干货）

### 选题 2：「给 AI 装上千里眼——零成本让 Agent 读遍全网」
- **切入点**：Panniantong/Agent-Reach 实操演示
- **看点**：一个 CLI 工具，不花一分钱 API 费，让 AI 能看 Twitter、Reddit、YouTube、B站、小红书
- **预估热度**：🔥🔥🔥🔥🔥（AI agent + 中文平台 + 零成本 + 实操性强）

---

*数据采集时间：2026-06-18 09:00 CST*
*数据来源：GitHub Trending (Daily + Weekly + Python/TypeScript/Rust/Go)*
