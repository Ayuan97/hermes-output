# 🔥 GitHub 趋势速览 — 2026年8月17日（周日）

## 一句话总览

**AI Agent 全面渗透开发者工具链**——从 Agent 记忆（TencentDB-Agent-Memory）、Agent 技能（agent-skills）、Agent 管理（paperclip）到 Agent 可观测性（agentsview），"Agent 基建"成了本周最大主题。同时，端侧小模型（14MB 的 needle、4GB 显存微调的 Soup）持续升温，"让 AI 跑在破硬件上"成为刚需。

---

## 🚀 爆款项目 TOP 5（日增 star 排名）

### 1. public-apis/public-apis — ⭐+1,588/天
🔗 https://github.com/public-apis/public-apis
- **干什么的**：免费 API 大合集，按类别整理，方便开发者快速找到可用的公共接口
- **为什么火**：老牌项目周期性爆发，可能被某个大号/博主重新推荐了。对做 AI Agent 的人来说，这是给 Agent 找"工具"的宝库
- **对主子的价值**：做 AI 相关内容时可以当素材库参考，也适合推荐给做开发的朋友

### 2. cordiverse/cordis — ⭐+720/天
🔗 https://github.com/cordiverse/cordis
- **干什么的**：时空可组合性的元框架（Meta-Framework of Spatiotemporal Composability），TypeScript 编写
- **为什么火**：概念新颖——把"时空"维度的组合能力做成框架，可能跟 AI Agent 的工作流编排相关
- **对主子的价值**：值得关注其设计理念，但目前生态还不成熟，先加 star 观察

### 3. unslothai/unsloth — ⭐+572/天 | 周增 +2,645
🔗 https://github.com/unslothai/unsloth
- **干什么的**：本地运行和训练 LLM/扩散模型的 UI，支持 Qwen3.8、Kimi K3、DeepSeek-V4、FLUX 等主流模型
- **为什么火**：本地化 AI 的大趋势 + 开箱即用的 UI + 支持最新模型。Unsloth 本身就是量化/加速领域的标杆
- **对主子的价值**：强烈推荐！本地跑模型的首选工具，做视频演示时效果很好

### 4. harry0703/MoneyPrinterTurbo — ⭐+494/天
🔗 https://github.com/harry0703/MoneyPrinterTurbo
- **干什么的**：根据主题/关键词一键生成高清短视频，利用 AI 大模型+自动化工作流
- **为什么火**：直击"短视频批量生产"痛点，中文项目，对国内创作者吸引力极大
- **对主子的价值**：⭐ 视频选题神器！可以直接用来快速产出视频内容，也适合做一期"AI 自动做视频"的选题

### 5. cactus-compute/needle — ⭐+443/天 | 周增 +2,950
🔗 https://github.com/cactus-compute/needle
- **干什么的**：14MB 的端侧基础模型，面向手机、可穿戴设备、智能家居和机器人
- **为什么火**：14MB！把基础模型压缩到这种程度，让物联网设备也能跑 AI，端侧智能的里程碑
- **对主子的价值**：极好的技术选题——"14MB 的 AI 能干什么"可以做一期爆款视频

---

## 📈 技术趋势洞察

### 本周最强趋势：AI Agent 基础设施大爆发

不是一两个 Agent 产品火了，而是整条工具链都在涨：
- **Agent 记忆**：TencentCloud/TencentDB-Agent-Memory（周+3,637）—— 团队级 Agent 记忆中心
- **Agent 技能**：addyosmani/agent-skills（周+2,882）—— 给 AI 编程 Agent 的生产级技能包
- **Agent 管理**：paperclipai/paperclip（周+2,499）—— 管理多个 Agent 的开源平台
- **Agent 可观测**：kenn-io/agentsview —— Claude Code/Codex 等 Agent 的会话分析和 token 统计
- **Agent 路由**：NVIDIA-NeMo/Switchyard（周+1,435）—— LLM 流量跨模型/供应商路由
- **Agent 自主进化**：PrimeIntellect-ai/prime-agent（周+6,435）—— 自我改进的 RLM Agent

### 端侧/小模型持续升温
- needle（14MB 端侧模型）、Soup（4GB 显存微调 8B 模型）、llmfit（一键检测你的硬件能跑什么模型）
- 反映开发者对"不依赖云端"的强烈需求

### AI 编程工具进入"插件化"时代
- cursor/plugins（Cursor 插件规范）—— AI 编辑器开始走 VS Code 的插件生态路线
- CodebuffAI/freebuff —— 免费编程 Agent
- code-graph-rag（周+1,686）—— 用知识图谱做代码 RAG，理解大型代码库

### 内容创作工具
- MoneyPrinterTurbo（一键短视频）、OpenCut（开源 CapCut）、remotion（React 做视频）、manim（数学动画老牌项目周+1,978）

---

## 💡 值得深挖 TOP 3

### 1. PrimeIntellect-ai/prime-agent
🔗 https://github.com/PrimeIntellect-ai/prime-agent
- **理由**：周增 6,435 star，自我改进的 RLM Agent，概念非常前沿——Agent 能自己优化自己的编码能力
- **建议**：clone 下来跑一跑，看看"自我改进"到底是怎么实现的，非常适合做深度技术视频

### 2. cathrynlavery/diagram-design
🔗 https://github.com/cathrynlavery/diagram-design
- **理由**：周增 15,600 star（本周最高！），专为 Claude Code 设计的 29 种编辑图表类型，纯 HTML+SVG，拒绝 Mermaid 风格
- **建议**：整合进日常工作流——用 Claude Code 生成高质量技术图表，也可以做一期"告别丑陋的 Mermaid 图表"的视频

### 3. MakazhanAlpamys/Soup
🔗 https://github.com/MakazhanAlpamys/Soup
- **理由**：一个 YAML 文件微调 LLM，4GB 显存的笔记本 GPU 就能训练 8B 模型，极大降低了微调门槛
- **建议**：clone 试试，在自己的机器上跑一次微调，体验"穷人也能训模型"的快感

---

## 📅 周榜亮点

### 持续霸榜
- **unslothai/unsloth**：日榜+周榜都在，本地 AI 工具的王者
- **ToolJet/ToolJet**：日+452/周+1,518，企业级低代码平台持续吃香
- **basecamp/omarchy**：Basecamp 出的 Linux 发行版，日+270/周+759，小而美的桌面系统

### 本周新晋黑马
- **cathrynlavery/diagram-design**：周+15,600，但今天不在日榜前五，说明本周早期爆发过
- **semantica-agi/semantica**：周+5,284，图原生 AI 基础设施，今天没在日榜说明热度在回落
- **macro-inc/macro**：周+2,588，Rust 写的统一工作空间（邮件+聊天+文档+任务+Agent），概念很新但今天没在日榜

---

## 🎬 视频选题建议

### 选题 1："14MB 的 AI 模型能干什么？端侧智能的未来"
- **素材**：cactus-compute/needle（14MB 基础模型）+ MakazhanAlpamys/Soup（4GB 显存微调）+ AlexsJones/llmfit（硬件兼容性检测）
- **角度**：把三个项目串起来——"检测你的硬件 → 选合适的模型 → 在超小设备上跑"，展示端侧 AI 的完整链路
- **爆点**：在树莓派/手表上跑 AI 的视觉冲击力

### 选题 2："AI Agent 已经能自己进化了"
- **素材**：PrimeIntellect-ai/prime-agent（自我改进 Agent）+ addyosmani/agent-skills（Agent 技能包）+ TencentCloud/TencentDB-Agent-Memory（Agent 记忆）
- **角度**：Agent 生态三件套——技能、记忆、自我进化，展示 AI Agent 正在从"工具"变成"同事"
- **爆点**：让 Agent 自己写代码改进自己，拍出"AI 自己改自己"的名场面

---

## 附录：语言维度亮点

### 🐍 Python 热点
| 项目 | 日增 | 亮点 |
|------|------|------|
| public-apis/public-apis | +1,588 | 经典 API 合集 |
| unslothai/unsloth | +572 | 本地模型 UI |
| harry0703/MoneyPrinterTurbo | +494 | AI 一键短视频 |
| cactus-compute/needle | +443 | 14MB 端侧模型 |
| MakazhanAlpamys/Soup | +443 | 4GB 显存微调 |
| HKUDS/CLI-Anything | +384 | 让所有软件 Agent 原生 |

### 📘 TypeScript 热点
| 项目 | 日增 | 亮点 |
|------|------|------|
| cordiverse/cordis | +720 | 时空可组合框架 |
| chaitanyagiri/munder-difflin | +181 | 本地多 Agent 调度 |
| OpenCut-app/OpenCut | +150 | 开源 CapCut |
| cursor/plugins | +144 | Cursor 插件生态 |
| CodebuffAI/freebuff | +141 | 免费编程 Agent |

### 🦀 Rust 热点
| 项目 | 日增 | 亮点 |
|------|------|------|
| AlexsJones/llmfit | +187 | 一键检测硬件能跑什么模型 |
| rustdesk/rustdesk | +143 | 开源远程桌面 |
| ZSeven-W/openpencil | +138 | AI 原生矢量设计工具 |
| nautechsystems/nautilus_trader | +58 | 量化交易引擎 |
| Automattic/harper | +40 | 离线语法检查器 |

### 🐹 Go 热点
| 项目 | 日增 | 亮点 |
|------|------|------|
| ollama/ollama | +127 | 本地模型运行时 |
| putyy/res-downloader | +74 | 国内平台资源下载 |
| kenn-io/agentsview | +35 | Agent 会话分析 |
| knadh/listmonk | +39 | 自建邮件列表 |

---

*数据来源：GitHub Trending（日榜 + 周榜）| 采集时间：2026-08-17 09:00*
