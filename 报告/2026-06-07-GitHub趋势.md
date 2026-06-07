# 🔥 今日 GitHub 趋势速览 — 2026-06-07

## 一句话总览

AI Agent 生态全面爆发：记忆系统、技能框架、前端 UI 协议、数据抓取工具齐上榜，「让 AI 能用工具」已经从概念进入工程落地阶段。同时 NotebookLM 开源替代品和 OCR 工具包持续霸榜。

---

## 🚀 爆款项目 TOP 5（日增 star 最多）

### 1. lfnovo/open-notebook ⭐+794/day | TypeScript | 26.6k total
- **干什么**：开源版 Google NotebookLM，支持上传文档后自动生成播客式对话音频、摘要、Q&A
- **为什么火**：Google NotebookLM 一直不开源，这个项目补齐了空缺，功能更灵活（支持自定义 LLM、多文档交叉引用）
- **对主子的价值**：可以用来做视频素材——把技术文档/论文变成播客音频，直接用作视频旁白。clone 试一试
- 🔗 https://github.com/lfnovo/open-notebook

### 2. obra/superpowers ⭐+700/day | Shell | 219.7k total
- **干什么**：一套 Agentic Skills 框架和软件开发方法论，给 AI Agent 注入「超能力」技能包
- **为什么火**：把 AI Agent 的能力拆解成可复用的 skill 文件，社区在大量 fork 和二次创作
- **对主子的价值**：Hermes Agent 本身就是 skill 驱动的，这个项目的 skill 设计思路值得参考。做一期「AI Agent 技能框架对比」视频有看点
- 🔗 https://github.com/obra/superpowers

### 3. Panniantong/Agent-Reach ⭐+683/day | Python | 22.3k total
- **干什么**：让 AI Agent 能读取 Twitter、Reddit、YouTube、GitHub、B站、小红书等平台内容，一个 CLI 搞定，零 API 费用
- **为什么火**：解决了 Agent 最大的痛点——数据来源太窄。不用申请 API key 就能抓全网信息
- **对主子的价值**：研究利器。配合 last30days-skill 可以做深度技术调研。值得 clone 备用
- 🔗 https://github.com/Panniantong/Agent-Reach

### 4. CopilotKit/CopilotKit ⭐+631/day | TypeScript | 33.2k total
- **干什么**：Agent 前端开发栈，提供 React/Angular/移动端/Slack 的 Agent UI 组件，同时是 AG-UI 协议的发起者
- **为什么火**：AG-UI（Agent-User Interface）协议正在成为行业标准，CopilotKit 是参考实现。前端开发者终于有了给 Agent 做 UI 的标准化方案
- **对主子的价值**：如果要给自己的 Agent 做可视化界面，这是最成熟的方案。做视频的话「AG-UI 协议解读」是个好选题
- 🔗 https://github.com/CopilotKit/CopilotKit

### 5. 666ghj/MiroFish ⭐+493/day | Python | 65k total
- **干什么**：群体智能引擎，用群体智慧预测各种事件（类似 Polymarket 的开源替代）
- **为什么火**：「预测万物」的概念很抓眼球，支持多种预测场景
- **对主子的价值**：有趣但实用性待验证。可以作为视频素材讲「群体智能 vs LLM 预测」
- 🔗 https://github.com/666ghj/MiroFish

---

## 📈 技术趋势洞察

### AI Agent 基础设施全面成熟
今天 trending 里 Agent 相关项目占比超过 60%，而且不是概念项目，全是工程级工具：
- **记忆层**：MemPalace（54k⭐，开源最强 AI 记忆系统）
- **技能层**：obra/superpowers、last30days-skill
- **UI 层**：CopilotKit + AG-UI 协议
- **数据层**：Agent-Reach（全网数据抓取）
- **语音层**：microsoft/VibeVoice（语音 AI）、openai/whisper（语音识别）

这说明 Agent 生态已经从「能聊天」进化到「能干活」的阶段。

### 开源替代品持续爆发
- open-notebook 替代 Google NotebookLM
- PaddleOCR 替代商业 OCR 服务（百度出品，80k+⭐，支持 100+ 语言）
- MiroFish 替代 Polymarket

### 语言热度
- **Python** 依然是 AI/Agent 项目的首选语言
- **TypeScript** 在 Agent UI 层发力（CopilotKit、open-notebook）
- **Rust** 在底层工具链持续渗透（mxc 隔离框架、goose Agent）
- **Go** 在安全/基础设施领域稳定（trivy、multica）

---

## 💡 值得深挖 TOP 3

### 1. open-notebook
**理由**：开源 NotebookLM 是刚需，Google 的版本不开源且有地区限制。这个项目功能更丰富，社区活跃度爆表（单日 794 星）。
**建议**：clone 下来跑一遍，用中文文档测试效果，考虑做一期「开源 NotebookLM 横评」视频。

### 2. Agent-Reach + last30days-skill 组合
**理由**：两个项目解决同一个问题的不同层面——Agent-Reach 负责数据抓取，last30days-skill 负责信息综合。组合起来就是一个完整的研究 Agent。
**建议**：整合进 Hermes Agent 作为 skill，每天自动做技术情报收集。

### 3. PaddleOCR
**理由**：80k+ 星的老牌项目今天又涨 433 星，说明在 AI Agent 场景下 OCR 需求重新爆发（Agent 需要「看懂」图片和 PDF）。
**建议**：如果主子有文档处理需求，这是最成熟的选择。支持中文识别效果很好。

---

## 📅 周榜亮点

### 持续霸榜
- **microsoft/markitdown** ⭐+15,015/week | 146k total — 文件转 Markdown 工具，周增恐怖。Agent 生态的基础设施项目
- **anthropics/claude-code** ⭐+2,527/week | 130k total — Claude Code 终端编程 Agent，持续高热
- **NousResearch/hermes-agent** ⭐+11,355/week | 184k total — 咱主子用的这个，周增过万 🎉

### 本周新晋黑马
- **chopratejas/headroom** ⭐+13,308/week | 15.8k total — 压缩 Agent 工具输出/日志/RAG 数据，减少 60-95% token 消耗。这个方向很有价值，token 成本是 Agent 的核心痛点
- **Leonxlnx/taste-skill** ⭐+6,085/week | 35k total — 给 AI 注入「品味」，防止生成无聊的套话。有趣的 skill 设计
- **EveryInc/compound-engineering-plugin** ⭐+1,752/week | 20k total — Compound Engineering 插件，支持 Claude Code/Codex/Cursor
- **OpenBMB/VoxCPM** ⭐+4,450/week | 27k total — 无 Tokenizer 的 TTS，支持多语言和声音克隆。语音 AI 领域的新玩家
- **D4Vinci/Scrapling** ⭐+6,002/week | 61.6k total — 自适应爬虫框架，从单次请求到大规模爬取都能搞定

---

## 🎬 视频选题建议

### 选题 1：「开源 NotebookLM 来了！open-notebook 全面体验」
- **切入点**：Google NotebookLM 不开源、有地区限制，开源社区给出了更好的答案
- **内容**：安装部署 → 上传技术文档 → 生成播客音频 → 与 Google 版对比 → 自定义 LLM 的优势
- **受众**：知识工作者、学生、内容创作者
- **预估热度**：⭐⭐⭐⭐⭐（794 日增说明需求巨大）

### 选题 2：「AI Agent 的五脏六腑——2026 年 Agent 基础设施全景图」
- **切入点**：今天 trending 里 Agent 相关项目占 60%+，正好做一个全景梳理
- **内容**：记忆（MemPalace）→ 技能（superpowers）→ 数据（Agent-Reach）→ UI（CopilotKit/AG-UI）→ 语音（VibeVoice）→ 压缩（headroom），展示一个完整 Agent 的技术栈
- **受众**：AI 开发者、技术博主
- **预估热度**：⭐⭐⭐⭐（系统性内容，长尾价值高）

---

*数据采集时间：2026-06-07 09:00 CST*
*来源：GitHub Trending (Daily + Weekly + Python/TypeScript/Rust/Go)*
