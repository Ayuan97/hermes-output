# 🔥 GitHub 趋势速览 — 2026-07-10

## 一句话总览

**今天的 GitHub Trending 被 "AI Agent Skills" 彻底屠榜了。** 日榜前 7 名里有 5 个都是给 AI 编程 Agent（Claude Code / Codex / Cursor 等）提供"技能包"的仓库，周榜更是被各种 Agent 工具、MCP Server、token 优化方案塞满。这不是一个两个项目的热度，而是一个完整的生态在爆发。

---

## 🚀 爆款项目 TOP 5（按日增 star 排序）

### 1. mattpocock/skills — ⭐+1,712/day
🔗 https://github.com/mattpocock/skills

**干什么的：** Matt Pocock（TypeScript 圈知名博主）把自己 `.claude` 目录里的 Agent Skills 公开了，Shell 脚本为主，直接给 Claude Code 用。

**为什么火：** "Skills" 是 2026 年 AI 编程的新范式——你不再每次从零 prompt 开始，而是把工程最佳实践打包成可复用的技能文件。Matt 带头开源，引发了 FOMO 式传播。

**对主子的价值：** 直接 clone 下来挑适合自己项目的 skills 用，能大幅提升 Claude Code 的代码质量。也值得研究他怎么组织 skills 结构的。

---

### 2. iOfficeAI/OfficeCLI — ⭐+1,224/day（周 +5,789）
🔗 https://github.com/iOfficeAI/OfficeCLI

**干什么的：** 专为 AI Agent 打造的 Office 套件 CLI 工具。一个二进制文件就能读写 Word/Excel/PPT，不需要安装 Office。

**为什么火：** 解决了 AI Agent 处理办公文档的大痛点——以前要依赖 python-docx、openpyxl 等一堆库，现在 Agent 一条命令就能搞定。C# 写的，跨平台。

**对主子的价值：** 如果主子有任何自动化处理 Office 文档的需求，这个工具可以直接集成到工作流里。Agent + 文档自动化 = 效率炸弹。

---

### 3. addyosmani/agent-skills — ⭐+1,116/day（周 +7,944）
🔗 https://github.com/addyosmani/agent-skills

**干什么的：** Google Chrome 团队大佬 Addy Osmani 出品的 "production-grade" 工程技能包，面向 AI 编程 Agent。

**为什么火：** Addy 自带流量 + 内容确实硬核（性能优化、架构设计、代码审查等 skill），和 Matt Pocock 的形成了互补——一个是实战派，一个是工程派。

**对主子的价值：** 和 #1 一起看，把两家的高质量 skills 合并到自己的 Agent 配置里，等于白嫖了两个顶级工程师的经验。

---

### 4. obra/superpowers — ⭐+1,013/day
🔗 https://github.com/obra/superpowers

**干什么的：** 一个完整的 Agent 技能框架 + 软件开发方法论，不只是 skills 集合，还定义了"怎么用 Agent 写软件"的流程。

**为什么火：** 它不只是一堆 prompt，而是提出了一个方法论——怎么让 Agent 像高级工程师一样思考、分解任务、执行。Shell 脚本为主，轻量好改。

**对主子的价值：** 如果主子想系统性地用 Agent 做项目，这个值得深读。方法论 + 实践框架一步到位。

---

### 5. TencentCloud/CubeSandbox — ⭐+291/day（周 +2,514）
🔗 https://github.com/TencentCloud/CubeSandbox

**干什么的：** 腾讯出品的 AI Agent 安全沙箱。让 Agent 执行代码时有一个隔离环境，即时启动、并发安全、资源受限。

**为什么火：** Agent 越来越能干，但安全问题也越来越大。这个沙箱让 Agent 可以大胆执行代码而不用担心搞坏宿主系统。Rust 写的，性能很好。

**对主子的价值：** 如果主子在用 Agent 跑各种实验/测试，这个沙箱能提供一个安全边界。也可以看看腾讯在 Agent 基础设施上的思路。

---

## 📈 技术趋势洞察

### 🔥 正在爆发的方向

1. **Agent Skills 生态** — 这是今天最大的信号。不是 Agent 本身在火了，而是"怎么让 Agent 更好用"的基础设施在爆发。Skills、MCP Server、Agent Memory、Agent Sandbox 都在涨。这就像 2015 年的 npm 生态——围绕核心工具的工具链在快速生长。

2. **Token 经济学** — Caveman（周 +5,348）用"穴居人语法"砍掉 65% token，OmniRoute（周 +4,268）做 AI 网关聚合 231 个供应商。说明大家开始认真算 Agent 的使用成本了。

3. **AI 安全/治理** — 微软出了 Agent Governance Toolkit（Python 榜 #7），腾讯出了 CubeSandbox，NVIDIA 出了 OpenShell。大厂在补 Agent 的安全短板。

4. **Rust 在 Agent 基础设施中的地位** — Bun、CubeSandbox、OpenShell、Herdr、Meetily……Agent 生态的底层组件大量用 Rust。性能敏感的工具层 = Rust，这个趋势在加固。

### 📊 语言/框架热度

- **C++ 异常活跃** — 日榜出现 5 个 C++ 项目（abseil、yaml-cpp、Catch2、asio、meshoptimizer），这很反常，可能是某个 C++ 大会或版本发布带动的。
- **Go 持续稳健** — Tailscale、Terraform、Headscale 稳定上榜，DevOps/基础设施领域 Go 还是王者。
- **Python** — AI/ML 方向依然主导，但今天的 Python 榜也被 Agent Skills 和 Agent 治理工具入侵了。

---

## 💡 值得深挖 TOP 3

### 1. 🏆 JuliusBrussee/caveman（周 +5,348）
🔗 https://github.com/JuliusBrussee/caveman

**理由：** 用"穴居人语法"压缩 prompt 省 65% token 这个思路太骚了。省钱 + 提速，而且原理简单，容易做视频讲清楚。
**建议：** Clone 下来跑一下看看实际省多少，做个对比测试。视频选题 +1。

### 2. 🏆 Zackriya-Solutions/meetily（周 +8,795 霸榜第一）
🔗 https://github.com/Zackriya-Solutions/meetily

**理由：** 开源 AI 会议助手，Rust 写的，100% 本地处理，支持实时转录 + 摘要。周增 8,795 star 是绝对王者。
**建议：** 直接下载试试，如果效果好的话可以替代付费的 Otter.ai/Fireflies。日常开会神器。

### 3. 🏆 huggingface/speech-to-speech（周 +811）
🔗 https://github.com/huggingface/speech-to-speech

**理由：** HuggingFace 官方出品的本地语音 Agent 框架，开源模型驱动。语音交互是下一个 Agent 入口。
**建议：** 值得跑个 demo 看看延迟和效果，评估是否能整合到主子的项目里。

---

## 📅 周榜亮点（与日榜差异）

### 持续霸榜
- **addyosmani/agent-skills** — 日榜 +1,116、周榜 +7,944，稳定输出，说明不是一天的热度而是持续的需求。
- **iOfficeAI/OfficeCLI** — 日榜 +1,224、周榜 +5,789，Agent + Office 这个赛道被验证了。

### 本周新晋黑马
- **asgeirtj/system_prompts_leaks**（周 +7,765）— 收集各家 AI 系统 prompt 的泄露合集。Claude Fable 5、GPT-5.6、Gemini 3.5 的 prompt 都在里面。争议性强但传播力惊人。
- **usestrix/strix**（周 +6,443）— AI 渗透测试工具。用 AI 找漏洞 + 自动修复。安全赛道 + AI = 新热点。
- **ogulcancelik/herdr**（周 +4,714）— 终端里的 Agent 多路复用器，同时跑多个 Agent。Rust 写的。

---

## 🎬 视频选题建议

### 选题 1：「Agent Skills 是什么？为什么 GitHub 前 10 全是它」
角度：从今天的 Trending 现象切入，讲清楚 2026 年 AI 编程的新范式——Skills > Prompts。实操演示怎么用 Matt Pocock / Addy Osmani 的 skills 提升 Claude Code 的效果，最后给出自己组织 skills 的最佳实践。流量保证 + 技术深度。

### 选题 2：「省 65% 的钱？Caveman 穴居人 Prompt 压缩实测」
角度：猎奇标题 + 实用内容。先讲原理（为什么少说话 Agent 反而理解更好），再实测对比 token 消耗和输出质量，最后讨论 token 经济学——2026 年跑 Agent 到底要花多少钱。

---

*报告生成时间：2026-07-10 09:00 | 数据来源：GitHub Trending*
