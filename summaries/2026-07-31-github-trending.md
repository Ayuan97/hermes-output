# 🔥 GitHub 趋势速览 | 2026-07-31

## 一句话总览

**今天 GitHub 被 AI Agent 工具链彻底屠榜了。** "Coding Agent Skills"成为全新爆款品类——给 Claude Code/Codex 写技能插件成了最火的技术活，日榜和周榜半数项目都跟 Agent 生态相关。Rust 写的开发者工具持续强势，语音 AI 和金融 AI 模型也在冒头。

---

## 🚀 爆款项目 TOP 5

### 1. mattpocock/skills ⭐ 周增 12,147
🔗 https://github.com/mattpocock/skills

**是什么：** TypeScript 知名博主 Matt Pocock 公开了自己的 `.agents` 目录，里面是他日常开发用的 Agent Skills 集合。

**为什么火：** Coding Agent Skills 是今年最大的开发者范式转变——相当于给你的 AI 编程助手装"技能包"。Matt Pocock 自带流量，加上 Skills 这个概念正好戳中了所有人的需求：怎么让 AI 真正按你的习惯干活。

**对主子的价值：** 直接 clone 研究 Skill 的写法和结构，可以借鉴给自己的 Hermes Agent 做 Skills，也是做视频选题的金矿。

### 2. block/buzz ⭐ 周增 12,444
🔗 https://github.com/block/buzz

**是什么：** Block（Jack Dorsey 的公司）出品的 Rust 通讯平台，描述为 "hive mind communication platform"。

**为什么火：** Block 出品必属精品，Rust 写的通讯平台本身就够吸引眼球，加上"蜂群心智"这种概念，暗示这可能是去中心化协作的新尝试。

**对主子的价值：** 值得关注其架构设计，Rust 通讯基础设施可能影响未来 Agent-to-Agent 通信方式。

### 3. different-ai/openwork ⭐ 日增 915
🔗 https://github.com/different-ai/openwork

**是什么：** Claude Cowork 的开源替代品，基于 opencode 构建，TypeScript 写的协作式 AI 编码工具。

**为什么火：** Claude Cowork 刚出来大家都很感兴趣，但它是闭源的。这个项目第一时间做了开源复刻，满足了很多人的"我也要能用"的需求。

**对主子的价值：** 可以直接试用，对比 Claude Cowork 的体验，也是研究"AI 协作编程"产品形态的好素材。

### 4. affaan-m/ECC ⭐ 日增 804
🔗 https://github.com/affaan-m/ECC

**是什么：** Agent 性能优化系统，包含 Skills、本能反应、记忆、安全机制等，适配 Claude Code/Codex/Cursor 等多种 Agent。

**为什么火：** 把 Agent 的"技能+记忆+安全"打包成一套可复用的框架，解决了大家用 Agent 编码时最头疼的"怎么让它记住上下文、别瞎搞"的问题。

**对主子的价值：** 参考其 Skill 设计和记忆管理方案，直接整合到自己的 Agent 工作流。

### 5. pascalorg/editor ⭐ 日增 625 | 周增 2,433
🔗 https://github.com/pascalorg/editor

**是什么：** 在线 3D 建筑编辑器，TypeScript 写的，可以在浏览器里创建和分享 3D 建筑项目。

**为什么火：** 浏览器内做 3D 建筑设计，直接干掉了 SketchUp 这类桌面软件的入门门槛。日增和周增都很稳，说明不是昙花一现。

**对主子的价值：** 如果对建筑/设计领域有兴趣可以玩玩，技术上 WebGL 3D 编辑器的实现也值得学习。

---

## 📈 技术趋势洞察

### 🔴 爆发方向

- **AI Agent Skills 生态**：这是今天最大的主题。`mattpocock/skills`、`book-to-skill`（把书变成 Skill）、`i-have-adhd`（ADHD 友好的 Agent 输出）、`last30days-skill`（30天话题研究 Skill）——给 Agent 写"技能包"已经成了一个新的开源品类。
- **AI 网关/路由**：`OmniRoute` 周增 8,464，一个 API 端点接 290+ 模型提供商，解决的是"Agent 要随时切换不同模型"的基础设施问题。
- **Agent 安全沙箱**：`NVIDIA/OpenShell` 和 `nolabs-ai/nono` 都在做 Agent 的安全运行环境，说明大家开始认真对待"AI 别把系统搞崩"这个问题。

### 🟡 持续热门

- **Rust 开发者工具链**：`tuicr`（vim 风格代码审查 TUI）、`jcode`（最省内存的 Agent harness）、`topcoat`（tokio 出品的 Web 框架）、`harper`（离线语法检查器）——Rust 在开发者工具领域继续攻城略地。
- **语音 AI**：`huggingface/speech-to-speech` 日增 628，本地语音 Agent 方案。
- **金融 AI**：`Kronos` 金融基础模型、`awesome-systematic-trading` 系统化交易资源汇总。

### 🟢 新信号

- **Coding Agent 的"操作系统"概念**：`ECC` 和 `jcode` 都在做"Agent 运行时"，包含技能、记忆、安全——这不是单个工具，而是在构建 Agent 的"操作系统层"。
- **中文开源书的爆发**：`ai-agent-book`（《深入理解 AI Agent》）周增 9,304，说明中文技术内容在 GitHub 上的影响力在快速增长。

---

## 💡 值得深挖 TOP 3

### 1. mattpocock/skills — 直接抄作业
🔗 https://github.com/mattpocock/skills

**理由：** 这是目前质量最高的公开 Agent Skills 集合。Matt Pocock 是 TypeScript 圈顶级教育者，他的 Skill 写法就是最好的范本。

**建议：** clone 下来逐个研究，挑适合自己的改造成 Hermes Agent 的 Skills。

### 2. virgiliojr94/book-to-skill — 知识管理新思路
🔗 https://github.com/virgiliojr94/book-to-skill

**理由：** 把任何技术书 PDF 自动转换成 Claude Code 可用的 Skill。这打通了"读书→实践"的闭环，日增 1,224 说明需求真实。

**建议：** 试试把最近在看的书转成 Skill，边工作边用，看效果如何。

### 3. alibaba/open-code-review — 大厂级代码审查
🔗 https://github.com/alibaba/open-code-review

**理由：** 阿里开源的代码审查工具，周增 5,322。混合架构（确定性规则 + LLM），内置 NPE、线程安全、XSS 等精细规则，兼容 OpenAI/Anthropic。

**建议：** 如果团队有代码审查需求，可以直接试。也值得研究它怎么把确定性检查和 AI 审查结合的。

---

## 📅 周榜亮点

### 持续霸榜
- **Agent Skills 生态**全面爆发：`mattpocock/skills`(12,147/周)、`book-to-skill`(4,135/周)、`i-have-adhd`(4,978/周)
- **AI 基础设施**：`OmniRoute`(8,464/周) 和 `ego-lite`(5,037/周，让 Agent 共享你的浏览器会话)

### 本周新晋黑马
- **`koala73/worldmonitor`** (6,150/周)：实时全球情报仪表盘，AI 新闻聚合+地缘政治监测+基础设施追踪。概念很酷。
- **`CoreBunch/Instatic`** (2,872/周)：Webflow/Framer/WordPress 的开源替代品，Agent 友好的可视化 CMS，输出干净静态页面。
- **`earendil-works/pi`** (4,799/周)：AI Agent 工具包，统一 LLM API + Agent 循环 + TUI + 编码 Agent CLI。

### 日榜 vs 周榜差异
日榜比较"传统"（Ansible、Jenkins、PowerToys 等老项目也在），周榜则几乎全是 Agent 生态相关项目，说明 Agent 工具链是本周的核心叙事。

---

## 🎬 视频选题建议

### 选题 1：「我给 AI 编程助手写了 10 个技能包，效率直接翻倍」
**角度：** 以 Matt Pocock 的 Skills 仓库为切入点，展示什么是 Agent Skill、怎么写、怎么用。挑 3 个最实用的 Skill 做演示，最后教大家写一个自己的。这个选题正好踩在风口上，搜索量会很大。

### 选题 2：「把一整本技术书喂给 AI，它变成了我的私人教练」
**角度：** 用 `book-to-skill` 工具，把一本经典技术书（比如《设计模式》或《Rust 编程之道》）转换成 Agent Skill，然后演示在实际编码中 Agent 如何用书中的知识帮你做决策。读书 + AI + 实战，三合一。

---

*报告生成时间：2026-07-31 09:00 | 数据来源：GitHub Trending*
