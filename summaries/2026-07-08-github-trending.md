# 🔥 GitHub Trending 每日报告
**日期**: 2026-07-08 (周三)  
**数据来源**: GitHub Trending (Daily + Weekly + 语言分类)

---

## 🎯 一句话总览

**AI Agent 工具链和 Claude Code 生态全面爆发**。今天 GitHub Trending 超过 70% 的项目与 AI 编码代理（Coding Agent）相关——从 Agent 技能库、MCP 服务器、Agent 沙箱到 token 压缩工具，整个生态正在围绕"让 AI 写代码更高效"这条主线快速生长。Claude Code 相关项目尤其火爆，日榜前 5 中有 3 个直接相关。

---

## 🚀 爆款项目 TOP 5

### 1. 🏆 MadsLorentzen/ai-job-search
- **链接**: https://github.com/MadsLorentzen/ai-job-search
- **热度**: ⭐ +2,514/day | +5,363/week | TypeScript
- **是什么**: 基于 Claude Code 的 AI 求职框架。Fork 后填入个人信息，让 Claude 评估岗位匹配度、定制简历、写求职信、准备面试。
- **为什么火**: 精准击中"用 AI 提效求职"的刚需痛点。Claude Code 的技能系统让它能做到传统求职工具做不到的个性化定制。
- **价值**: 如果正在看机会可以直接用起来。也适合做一期"AI 帮你找工作"的视频选题。

### 2. 🎙️ Zackriya-Solutions/meetily
- **链接**: https://github.com/Zackriya-Solutions/meetily
- **热度**: ⭐ +1,777/day | +7,349/week | Rust
- **是什么**: 完全本地运行的 AI 会议助手。基于 Rust 构建，使用 Parakeet/Whisper 做实时转录（号称比竞品快 4 倍），支持说话人分离和 Ollama 本地摘要。macOS + Windows 双平台。
- **为什么火**: 隐私敏感用户不想把会议录音上传云端，Meetily 提供了 100% 本地化方案。Rust 写的性能确实能打。
- **价值**: 替代 Wispr Flow 等付费方案的好选择。可以整合到日常工作流中。

### 3. 🔓 asgeirtj/system_prompts_leaks
- **链接**: https://github.com/asgeirtj/system_prompts_leaks
- **热度**: ⭐ +1,691/day | +5,337/week | JavaScript
- **是什么**: 收录各大 AI 产品的系统提示词（System Prompt）。覆盖 Anthropic Claude 系列、OpenAI ChatGPT/Codex、Google Gemini、xAI Grok、Cursor、Copilot、VS Code、Perplexity 等。定期更新。
- **为什么火**: Prompt 工程师和 AI 产品开发者都想知道竞品怎么设计系统提示词。这个仓库是最全的公开收集项目之一。
- **价值**: 研究竞品 prompt 设计的宝库。做 AI 产品或 Agent 开发必看。

### 4. 🧠 addyosmani/agent-skills
- **链接**: https://github.com/addyosmani/agent-skills
- **热度**: ⭐ +1,317/day | JavaScript
- **是什么**: Addy Osmani（Google Chrome 团队大佬）出品的"生产级 AI 编码代理技能集"。为 Claude Code 等 AI Agent 提供高质量的工程实践指导。
- **为什么火**: Addy Osmani 个人影响力 + Agent Skills 是当前最热的 AI 开发范式。给 Agent 喂"技能"比写 prompt 更系统化。
- **价值**: 如果在使用 Claude Code，直接把这个技能库装上。质量比社区随便写的 prompt 高很多。

### 5. 📡 ruvnet/RuView
- **链接**: https://github.com/ruvnet/RuView
- **热度**: ⭐ +1,129/day | Rust
- **是什么**: 用普通 WiFi 信号实现空间感知、生命体征监测和存在检测——完全不需要摄像头。
- **为什么火**: 非常有想象力的项目。WiFi 感知（WiFi Sensing）是物联网和智能家居的下一个风口，用 Rust 写保证了低延迟和高可靠性。
- **价值**: 技术探索价值极高。如果做智能家居或 IoT 相关项目，值得深入了解其信号处理算法。视频选题也不错——"用 WiFi 当摄像头"天然有话题度。

---

## 📈 技术趋势洞察

### 🔥 正在爆发

**1. AI Agent 工具链 — 本周最大主题**
- Agent Skills（技能库）成为新范式：`agent-skills`、`dotnet/skills`、`awesome-claude-code`、`anthropics/claude-plugins-official` 全部上榜
- Agent 基础设施：`CubeSandbox`（腾讯的 Agent 沙箱）、`herdr`（Agent 多路复用器）、`Orca`（并行 Agent ADE）
- Agent 记忆和上下文：`codebase-memory-mcp`、`TencentDB-Agent-Memory`
- 结论：AI Agent 正从"玩具"走向"生产"，配套基础设施在快速补齐

**2. MCP (Model Context Protocol) 协议生态扩张**
- `codebase-memory-mcp`（周增 5,457 ⭐）：代码库知识图谱 MCP 服务器
- `chrome-devtools-mcp`（周增 1,480 ⭐）：Chrome DevTools 的 MCP 接口
- MCP 正在成为 AI Agent 连接外部工具的标准协议，类似当年 REST 之于 Web 开发

**3. Claude Code 生态一骑绝尘**
- 日榜 13 个项目中至少 7 个直接围绕 Claude Code
- 从技能库到视频处理（`claude-video`）、token 压缩（`caveman`，周增 8,066 ⭐）、求职（`ai-job-search`），生态丰富度碾压其他 AI 编码工具

**4. 本地优先 / 隐私优先 AI**
- `meetily`：本地会议转录
- `pocket-tts`：CPU 能跑的 TTS
- `openmed`：本地医疗 NER
- 隐私合规需求推动越来越多 AI 工具走本地化路线

### 📊 语言/框架热度

| 语言 | 上榜项目数 | 趋势 |
|------|-----------|------|
| Rust | 4 个日榜 + 多个语言榜 | 📈 Agent 基础设施和性能工具首选 |
| TypeScript | 3 个日榜 + 多个语言榜 | 📈 Agent 前端和网关类项目 |
| Python | 多个语言榜 | ➡️ 稳定，AI/ML 工具为主 |
| Go | 语言榜 | ➡️ 稳定，基础设施和工具为主 |
| C# | 2 个日榜 | 📈 AI Agent + Office 自动化方向 |

---

## 💡 值得深挖 TOP 3

### 1. DeusData/codebase-memory-mcp ⭐ +5,457/week
- **链接**: https://github.com/DeusData/codebase-memory-mcp
- **理由**: 把代码库索引成持久化知识图谱，毫秒级查询，号称减少 99% 的 token 消耗。158 种语言，零依赖单二进制。
- **建议**: 立刻 clone 试试。如果你用 Claude Code 处理大型代码库，这个 MCP 服务器可能是目前最强的上下文管理方案。

### 2. browser-use/video-use ⭐ +3,435/week
- **链接**: https://github.com/browser-use/video-use
- **理由**: 让 AI 编码代理直接编辑视频。browser-use 团队出品，之前做浏览器自动化的，现在扩展到视频领域。
- **建议**: 做视频选题的好素材——"让 AI 帮你剪视频"。也值得整合到内容创作工作流中。

### 3. usestrix/strix ⭐ +10,741/week（周榜第一！）
- **链接**: https://github.com/usestrix/strix
- **理由**: AI 渗透测试工具，自动发现并修复应用安全漏洞。本周总增星超过 1 万，是所有项目中最多的。
- **建议**: 安全方向的同学必关注。也可以做一期"AI 黑客帮你找漏洞"的视频。

---

## 📅 周榜亮点

### 持续霸榜
- **Meetily**（+7,349/week）：本地 AI 会议助手持续火爆，日榜和周榜双上榜
- **system_prompts_leaks**（+5,337/week）：系统提示词收集项目热度不减
- **ai-job-search**（+5,363/week）：AI 求职框架一周内积累了超过 5000 星

### 本周新晋黑马
- **usestrix/strix**（+10,741/week）：AI 渗透测试工具，周榜第一，但今天没在日榜，可能热度峰值已过
- **JuliusBrussee/caveman**（+8,066/week）：让 Claude Code 像原始人一样说话来省 token，省 65% 消耗。创意满分。
- **msitarzewski/agency-agents**（+8,597/week）：一套完整的"AI 公司"代理集，从前端开发到 Reddit 运营都有
- **diegosouzapw/OmniRoute**（+4,797/week）：免费 AI 网关，231+ 提供商，一个端点接入所有 AI 模型

### 日榜 vs 周榜差异
- **日榜新面孔**：`CodexBar`（macOS 菜单栏显示 Codex/Claude Code 用量）、`OfficeCLI`（AI Agent 操作 Office 文档）、`Website-downloader`（下载整站源码）
- **周榜独有的重磅项目**：`strix`（AI 渗透测试）、`caveman`（token 压缩）、`orca`（并行 Agent 平台）、`video-use`（AI 视频编辑）

---

## 🎬 视频选题建议

### 选题 1：「用 WiFi 替代摄像头？这个 Rust 项目做到了」
- **主角**: [RuView](https://github.com/ruvnet/RuView)
- **卖点**: WiFi 感知技术 + 隐私保护 + Rust 高性能。技术原理讲清楚（CSI 信号分析），演示效果对比，讨论应用场景（老人监护、智能家居）。天然有科技感和话题度。

### 选题 2：「2026 年 Claude Code 生态有多疯狂？盘点 10 个最强 Agent 工具」
- **素材**: `agent-skills`、`caveman`（省 65% token）、`claude-video`（看视频）、`codebase-memory-mcp`（代码知识图谱）、`ai-job-search`（AI 求职）、`OfficeCLI`（操作 Office）
- **卖点**: Claude Code 生态全景图，每个工具 2-3 分钟演示，观众直接能用。适合做成"合集向"视频。

---

## 📋 附录：完整数据

### 日榜全部项目（13 个）
| # | 项目 | ⭐/day | 语言 | 简介 |
|---|------|--------|------|------|
| 1 | ai-job-search | 2,514 | TypeScript | AI 求职框架 |
| 2 | meetily | 1,777 | Rust | 本地 AI 会议助手 |
| 3 | agent-skills | 1,317 | JavaScript | AI Agent 技能库 |
| 4 | RuView | 1,129 | Rust | WiFi 空间感知 |
| 5 | system_prompts_leaks | 1,691 | JavaScript | 系统提示词收集 |
| 6 | CubeSandbox | 664 | Rust | Agent 沙箱 |
| 7 | Website-downloader | 140 | HTML | 整站下载 |
| 8 | CodexBar | 376 | Swift | Codex 用量展示 |
| 9 | dotnet/skills | 64 | C# | .NET Agent 技能 |
| 10 | OfficeCLI | 893 | C# | AI 操作 Office |
| 11 | claude-video | 965 | Python | Claude 看视频 |
| 12 | pocket-tts | 531 | Python | 轻量 TTS |
| 13 | awesome-claude-code | 144 | Python | Claude Code 资源集 |

### 语言榜精选
**Python 热点**: claude-video (+965), last30days-skill (+659), pocket-tts (+531), free-llm-api-resources (+412)  
**TypeScript 热点**: ai-job-search (+2,514), OmniRoute (+640), TencentDB-Agent-Memory (+610), karakeep (+420)  
**Rust 热点**: meetily (+1,777), RuView (+1,129), herdr (+683), CubeSandbox (+664)  
**Go 热点**: gastown (+274), sub2api (+190), agentsview (+123), ntfy (+90)

---
*报告由 Hermes Agent 自动生成 | 2026-07-08 09:00*
