# 🔥 GitHub 趋势速览 — 2026年7月14日

## 一句话总览

**AI Agent 技能生态大爆发 + 开源视频剪辑工具起飞。** 今天 GitHub 最突出的主题是：给 AI 编程助手（Claude Code / Codex / Cursor）造"技能插件"的项目疯狂刷屏，同时 AI 交易 Agent 和开源视频编辑工具也在强势霸榜。

---

## 🚀 爆款项目 TOP 5（日增 star 最多）

### 1. OpenCut-app/OpenCut ⭐+1,229/天
- **链接**: https://github.com/OpenCut-app/OpenCut
- **一句话**: 开源版 CapCut，用浏览器剪视频
- **为什么火**: CapCut 在国内外都是现象级产品，但闭源+云端依赖让人不爽。OpenCut 用 TypeScript 搞了个完全开源、可自部署的替代品，戳中了"视频创作自由"的痛点
- **跟主子有啥关系**: 如果做技术视频，这个选题天然自带流量——"开源版剪映来了"。技术上也可以 clone 下来看看 WebCodecs API 的玩法

### 2. HKUDS/Vibe-Trading ⭐+1,153/天
- **链接**: https://github.com/HKUDS/Vibe-Trading
- **一句话**: 港大出品的个人 AI 交易 Agent，"氛围交易"（Vibe Trading）
- **为什么火**: 把 LLM Agent 和金融交易结合，号称让 AI 帮你做交易决策。AI 炒股这个方向一直有热度，但这次套了"Vibe"概念加上港大背书，传播力拉满
- **跟主子有啥关系**: 做视频选题的好素材——"AI 帮你炒股靠谱吗？"话题性极强。技术上也可以研究 Agent 做金融决策的架构

### 3. Graphify-Labs/graphify ⭐+1,095/天
- **链接**: https://github.com/Graphify-Labs/graphify
- **一句话**: 给 Claude Code / Codex / Cursor 等 AI 编程工具加"技能"——把任意文件夹变成 AI 可理解的知识图谱
- **为什么火**: AI 编程助手的"技能/插件"生态正在快速膨胀。graphify 让 AI 能更好地理解项目结构，解决"AI 不理解我的代码库"的核心痛点
- **跟主子有啥关系**: 直接用！给 Hermes Agent 或日常开发工具装上，提升 AI 对项目上下文的理解能力

### 4. Shubhamsaboo/awesome-llm-apps ⭐+996/天
- **链接**: https://github.com/Shubhamsaboo/awesome-llm-apps
- **一句话**: 100+ 个可以直接跑的 AI Agent 和 RAG 应用合集
- **为什么火**: 老项目持续霸榜，因为它解决了"我想用 AI 但不知道从哪开始"的问题。clone → customize → ship 的模式非常友好
- **跟主子有啥关系**: 视频选题宝库，随便挑一个拆解就是内容。也是快速原型开发的好资源

### 5. Nutlope/hallmark ⭐+794/天
- **链接**: https://github.com/Nutlope/hallmark
- **一句话**: "反 AI 垃圾审美"的设计技能——教 Claude Code 和 Cursor 做出有品味的设计
- **为什么火**: AI 生成的 UI 越来越"千篇一律"，hallmark 直接给 AI 工具注入"好设计"的标准。这个方向非常新颖——不是让 AI 更强，而是让 AI 更有品味
- **跟主子有啥关系**: 如果做前端/设计相关项目，这个 skill 值得装上试试。选题也不错——"教 AI 做设计"

---

## 📈 技术趋势洞察

### 1. AI Agent "技能生态"全面开花 🔥🔥🔥
今天最明显的趋势：**给 AI 编程助手造插件/技能的项目集体爆发**。
- `graphify`（代码理解）、`hallmark`（设计审美）、`marketingskills`（营销技能）、`archify`（架构图）、`impeccable`（设计语言）——全是给 Claude Code / Codex / Cursor 造"能力扩展"的
- 这说明 AI 编程助手的竞争已经从"谁更强"转向"谁的生态更丰富"

### 2. AI 金融交易 Agent 扎堆
- Vibe-Trading、ai-hedge-fund、TradingAgents 三个项目同时上榜
- LLM + 金融交易是 2026 年最火的 AI 应用方向之一

### 3. Agent 基础设施层快速成熟
- `DesktopCommanderMCP`（终端控制 MCP 服务器）、`CubeSandbox`（腾讯出品的 Agent 沙箱）、`herdr`（Agent 多路复用器）、`OmniRoute`（231+ 供应商的 AI 网关）
- Agent 需要的运行环境、安全隔离、API 路由——基础设施都在快速补齐

### 4. 安全/渗透测试 AI 化
- `strix`（开源 AI 渗透测试，周增 3,403⭐）和 `pentagi`（全自动渗透测试 Agent）
- 安全领域正在被 AI Agent 深度改造

### 5. Rust 在 Agent 基础设施中占比极高
- CubeSandbox、herdr、RuView、pgrust 都是 Rust
- Rust 正在成为"AI Agent 基础设施"的首选语言

### 6. "反 AI 垃圾"运动兴起
- hallmark（反 AI 审美垃圾）和 system_prompts_leaks（泄露系统提示词）代表了两种不同的"反 AI"姿态
- 社区开始反思 AI 生成内容的质量和透明性

---

## 💡 值得深挖 TOP 3

### 1. 🥇 OpenCut（开源视频剪辑）
- **理由**: CapCut 替代品 + Web 技术栈 + 日增 1,229 星，热度炸裂
- **建议**: clone 下来体验一把，看看 Web 端视频编辑的技术方案（WebCodecs / WebAssembly），出视频选题"开源版剪映能打吗？"

### 2. 🥈 Vibe-Trading（AI 交易 Agent）
- **理由**: 港大背书 + 话题性极强 + 金融 AI 是流量密码
- **建议**: 研究下它的 Agent 架构和交易策略模块，做视频"港大 AI 炒股 Agent 实测"

### 3. 🥉 stablyai/orca（并行 Agent 编排平台）
- **理由**: 周增 5,263⭐，让多个 AI 编程 Agent 并行工作
- **建议**: 这个方向是 Agent 工作流的下一步——不是单个 Agent 干活，而是一群 Agent 协作。clone 试试架构设计

---

## 📅 周榜亮点（和日榜的差异）

### 持续霸榜
- `awesome-llm-apps` 持续在日榜和周榜都有存在感，是 AI 应用领域的常青树

### 本周黑马
| 项目 | 周增星 | 亮点 |
|------|--------|------|
| **iOfficeAI/OfficeCLI** | +7,596 | 给 AI Agent 造的 Office 套件，读/编辑/自动化文档 |
| **asgeirtj/system_prompts_leaks** | +6,284 | 泄露各大模型的系统提示词，争议性极强 |
| **Zackriya-Solutions/meetily** | +5,392 | Rust 写的 AI 会议助手，实时转录+说话人识别 |
| **stablyai/orca** | +5,263 | 并行 Agent 编排平台，一群 Agent 同时干活 |
| **diegosouzapw/OmniRoute** | +4,345 | 免费 AI 网关，一个端点接 231+ 供应商（50+ 免费） |

---

## 🎬 视频选题建议

### 选题 1：「开源版剪映来了！OpenCut 能替代 CapCut 吗？」
- **切入点**: 体验 OpenCut 的核心功能，对比 CapCut，分析 Web 端视频编辑的技术实现
- **预期流量**: 高——"开源替代" + "视频剪辑" 都是高热度关键词

### 选题 2：「港大 AI 炒股 Agent 实测：Vibe-Trading 真的能赚钱吗？」
- **切入点**: 拆解 Vibe-Trading 的 Agent 架构，跑一下回测，讨论 AI 金融交易的可行性
- **预期流量**: 极高——"AI 炒股"自带争议和好奇心

---

## 附录：今日数据详情

### 日榜完整数据（全部语言）
| # | 项目 | 日增星 | 语言 | 简介 |
|---|------|--------|------|------|
| 1 | OpenCut-app/OpenCut | +1,229 | TypeScript | 开源版 CapCut |
| 2 | HKUDS/Vibe-Trading | +1,153 | Python | AI 个人交易 Agent |
| 3 | Graphify-Labs/graphify | +1,095 | Python | AI 编程助手技能 - 代码知识图谱 |
| 4 | Shubhamsaboo/awesome-llm-apps | +996 | Python | 100+ AI Agent & RAG 应用合集 |
| 5 | Nutlope/hallmark | +794 | CSS | 反 AI 垃圾审美的设计技能 |
| 6 | github/spec-kit | +543 | Python | 规范驱动开发工具 |
| 7 | hasaneyldrm/exercises-dataset | +451 | HTML | 1,324 个健身动作数据集 |
| 8 | coreyhaines31/marketingskills | +299 | JavaScript | AI Agent 营销技能 |
| 9 | Raphire/Win11Debloat | +118 | PowerShell | Win11 去臃肿脚本 |
| 10 | moeru-ai/airi | +78 | TypeScript | 自部署 AI 伴侣 |

### 语言榜亮点
- **Python**: 交易 Agent 三连（Vibe-Trading / ai-hedge-fund / TradingAgents）+ AI 应用合集
- **TypeScript**: OpenCut 霸榜 + claudian（Obsidian 里嵌 Claude Code）+ heygen 的 hyperframes（HTML 渲染视频）
- **Rust**: pgrust（Rust 重写 Postgres，通过 100% 回归测试！）+ cc-switch（跨平台 Claude Code 桌面助手）
- **Go**: engram（AI 编程 Agent 的持久记忆系统）+ Pulse（Proxmox/Docker/K8s 监控）

---

*报告生成时间: 2026-07-14 09:00 | 数据来源: GitHub Trending*
