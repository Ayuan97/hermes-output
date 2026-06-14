# 🔥 GitHub 趋势速览 — 2026-06-14

## 一句话总览

**AI Agent 技能生态全面爆发。** 今天的 GitHub Trending 几乎被 Agent Skills 类项目屠榜——从技能框架、安全扫描到会话分析，整个 AI Agent 工具链正在快速成型。同时 Apple 开源容器工具、LLM 推理优化也是热门方向。

---

## 🚀 爆款项目 TOP 5（日增 star 排序）

### 1. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — ⭐+1,514/day
- **是什么**：为 AI 编程助手（Claude Code、Cursor 等）提供生产级工程技能包
- **为什么火**：Addy Osmani（Google Chrome 团队大佬）出品，直接给 AI Agent 装上"会写测试、会做 code review、会搞性能优化"的能力模块。解决的核心痛点：AI 写代码很溜，但工程素养不够
- **对主子的价值**：值得 clone 研究一下，看看它定义了哪些 skill 模板，可以借鉴到自己的 Agent 工作流里

### 2. [apple/container](https://github.com/apple/container) — ⭐+1,487/day（周增 9,173）
- **是什么**：Apple 官方开源的 macOS 容器工具，用 Swift 写的，基于轻量虚拟机运行 Linux 容器
- **为什么火**：Apple 终于下场做容器了！专为 Apple Silicon 优化，比 Docker Desktop 更轻量原生。这是 Apple 在开发者工具领域的重要布局
- **对主子的价值**：macOS 用户必看。如果日常用 Docker，这个项目可能会成为更优的替代方案。值得 early adopt

### 3. [obra/superpowers](https://github.com/obra/superpowers) — ⭐+924/day
- **是什么**：一套 Agentic 技能框架 + 软件开发方法论，让 AI Agent 真正"能干活"
- **为什么火**：不只是给 Agent 塞 prompt，而是一套完整的开发范式。和 agent-skills 形成互补——一个偏技能定义，一个偏方法论
- **对主子的价值**：研究其方法论设计，对理解"怎么让 AI Agent 更靠谱"有启发

### 4. [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) — ⭐+804/day（周增 2,799）
- **是什么**：AI Agent 技能的安全扫描器，检测漏洞、恶意模式和安全风险
- **为什么火**：NVIDIA 出品。当大家疯狂给 Agent 装技能的时候，安全问题浮出水面——你装的 skill 里有没有后门？有没有数据泄露风险？这个项目就是干这个的
- **对主子的价值**：如果用了第三方 agent skills，建议跑一遍这个扫一下。安全不能马虎

### 5. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) — ⭐+12,602/week（周榜冠军）
- **是什么**：AI Agent 技能——自动在 Reddit、X、YouTube、HN、Polymarket 等平台搜索任意话题，生成综合摘要
- **为什么火**：一周涨了 1.2 万 star！解决了"AI Agent 只能用训练数据"的痛点，让 Agent 具备实时联网调研能力
- **对主子的价值**：灵感来源——做视频选题调研时，类似思路可以自动化。看看它的多源聚合逻辑

---

## 📈 技术趋势洞察

### 1. Agent Skills 生态爆发
今天 trending 里至少有 **6 个** 项目直接跟 Agent Skills 相关：
- `agent-skills`（技能包）
- `superpowers`（技能框架）
- `SkillSpector`（技能安全）
- `last30days-skill`（联网技能）
- `agentsview`（Agent 会话分析）
- `pm-skills`（产品经理技能集）

**判断**：AI Agent 正从"单一对话"走向"技能模块化"，类似手机 App 生态。谁先把 skill marketplace 做起来，谁就占先机。

### 2. LLM 推理优化持续推进
- `LMCache`（KV Cache 加速）日增 238 star
- `headroom`（压缩 LLM 输入，减少 60-95% token）周增 10,406

**判断**：随着 Agent 调用 LLM 频率飙升，推理成本和延迟成为核心瓶颈。KV Cache 优化、输入压缩这类"省 token"方案需求旺盛。

### 3. AI 工具的"元信息"需求
- `system-prompts-and-models-of-ai-tools`（收集各 AI 工具的系统提示词）日增 109
- 这类项目持续上榜，说明开发者对"AI 工具到底怎么工作的"有强烈好奇

### 4. 语言热度
- **Python**：AI/ML 工具链主导（SkillSpector、LMCache、aisuite、headroom）
- **TypeScript**：AI Agent 前端 + 开发工具（opencode、CopilotKit、tolaria）
- **Rust**：基础设施工具稳步上升（tauri、swc、biome、gpui-component）
- **Go**：Agent 运维工具异军突起（agentsview、MasterDnsVPN、coder）

---

## 💡 值得深挖 TOP 3

### 1. [chopratejas/headroom](https://github.com/chopratejas/headroom) — ⭐+10,406/week
**理由**：压缩 LLM 输入 60-95% token 但答案质量不变。对所有重度使用 AI API 的场景都有价值。
**建议**：clone 试试，评估能否集成到自己的 Agent 工作流里省成本。

### 2. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) — ⭐+5,183/week
**理由**：给 AI Agent 装上"眼睛"——一键读取 Twitter、Reddit、YouTube、GitHub、B站、小红书，零 API 费用。中文社交平台支持是亮点。
**建议**：做中文内容调研的利器，值得研究实现方式。

### 3. [anomalyco/opencode](https://github.com/anomalyco/opencode) — ⭐+353/day
**理由**：开源编程 Agent，TypeScript 写的。在 AI 编程助手赛道里是新选手。
**建议**：可以关注对比，看看跟 Claude Code、Cursor 的差异化在哪。

---

## 📅 周榜亮点

**持续霸榜：**
- `apple/container`（周增 9,173）— Apple 官方容器工具，热度持续
- `NVIDIA/SkillSpector`（周增 2,799）— Agent 安全扫描，稳居前列

**本周新晋黑马：**
- `mvanhorn/last30days-skill`（周增 12,602）— 本周最大赢家，AI 联网调研技能
- `chopratejas/headroom`（周增 10,406）— LLM token 压缩，切中痛点
- `Leonxlnx/taste-skill`（周增 8,097）— 给 AI 装"审美"，让输出不那么平庸
- `phuryn/pm-skills`（周增 5,408）— PM 技能集，Agent 应用向非技术岗位渗透

---

## 🎬 视频选题建议

### 选题 1：《AI Agent 的"App Store"来了？GitHub 上正在发生的事》
- 切入点：agent-skills、superpowers、SkillSpector 等项目集体爆发，Agent Skills 生态正在成型
- 内容方向：解释什么是 Agent Skills、为什么模块化是趋势、安全问题怎么解决、未来会怎样
- 受众：AI 开发者、对 AI Agent 感兴趣的技术观众

### 选题 2：《Apple 终于做了自己的容器工具，Docker 要慌了吗？》
- 切入点：apple/container 开源，Apple Silicon 原生优化
- 内容方向：跟 Docker Desktop 对比、性能测试、实际使用体验、对开发者生态的影响
- 受众：macOS 开发者、容器技术爱好者
