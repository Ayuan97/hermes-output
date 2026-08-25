# 🔥 GitHub 趋势速览 — 2026年8月25日（周一）

## 📌 一句话总览

**DeepSeek Harness (DSH) 生态全面爆发**，两周内主仓库冲到 19.2 万星，插件市场、桌面端、Web 端、路由套件齐上阵，堪称"AI 时代的 VS Code 时刻"。同时 **AI Agent Skill（Claude Code / Codex 技能）** 成为新范式，开发者不再写插件，而是写"技能文件"给 AI 用。

---

## 🚀 爆款项目 TOP 5（本周新晋）

### 1️⃣ deepseek-ai/deepseek-harness ⭐192,016
🔗 https://github.com/deepseek-ai/deepseek-harness

**是什么：** DeepSeek 官方推出的 AI 编程框架，核心理念"Everything is a Plugin"（万物皆插件）。TypeScript 编写，8月13日创建，12天冲到 19 万星。

**为什么火：** 直接挑战 Claude Code 和 OpenAI Codex 的终端编程工具地位。DSH 的插件架构极其灵活，社区已经自发建立了完整的插件市场（dsh-market）、桌面端（dsh-desktop）、Web 端（dsh-web）、TUI 界面（dsh-TUI）等全套生态。这种"官方搭台、社区唱戏"的速度前所未见。

**跟主子的关系：** 🔴 **必须关注**。这是目前增长最快的开源项目之一，可能重塑 AI 编程工具的格局。DSH 插件开发是一个新的技能方向，值得提前布局。

---

### 2️⃣ MengTo/threeui ⭐3,475
🔗 https://github.com/MengTo/threeui

**是什么：** 开源的 ThreeUI 社区组件库，提供大量可交互的 Three.js / WebGL / Shader 组件，带完整的实时预览。

**为什么火：** 解决了 Three.js 组件复用难的痛点，设计师和开发者可以直接从目录中拖拽使用高质量的 3D Web 组件。4 天 3400+ 星，说明市场对高质量 3D Web UI 的需求很旺盛。

**跟主子的关系：** 🟡 如果做 3D 网页、产品展示、或者创意前端项目，这是一个宝藏库。也可以作为视频选题——"用 ThreeUI 5 分钟做一个炫酷的 3D 登陆页"。

---

### 3️⃣ b-nnett/grok-bot-0.18-reconstructed ⭐1,745
🔗 https://github.com/b-nnett/grok-bot-0.18-reconstructed

**是什么：** 非官方的 Grok Bot 0.18.0 macOS 版本重建和扩展。TypeScript 编写，2 天内冲到 1700+ 星，Fork 数高达 1900。

**为什么火：** xAI 的 Grok 在 macOS 上的原生体验一直不够好，这个项目填补了空缺。高 Fork 数说明很多人在做自己的定制版本。

**跟主子的关系：** 🟡 如果主子用 macOS 且对 Grok 感兴趣，可以试试。但要注意非官方项目的安全风险。

---

### 4️⃣ duty1g/x64dbg-mcp-server ⭐1,225
🔗 https://github.com/duty1g/x64dbg-mcp-server

**是什么：** 给 x64dbg 调试器接入了 MCP（Model Context Protocol）协议，让 AI 可以直接控制调试器——设置断点、读内存、分析寄存器，全通过自然语言。Zig 语言编写。

**为什么火：** MCP 是今年最火的 AI 协议标准，这个项目把"AI 辅助逆向工程"从概念变成了现实。安全研究员和逆向工程师的利器。

**跟主子的关系：** 🟢 如果做安全方向的内容，这是一个很好的视频选题——"让 AI 帮我逆向分析恶意软件"。技术上非常有创新性。

---

### 5️⃣ tobi/walgit ⭐1,056
🔗 https://github.com/tobi/walgit

**是什么：** Rust 编写的 Git 写前日志（Write-Ahead Log）工具。作者 Tobi（疑似 Shopify CEO Tobias Lütke）。

**为什么火：** Git 操作在某些场景下需要事务性保证（比如 CI/CD 流水线中的并发操作），WAL 是数据库领域的成熟方案，移植到 Git 上是一个新颖的思路。Rust 实现保证了性能和安全。

**跟主子的关系：** 🟡 偏底层工具，适合 Git 重度用户。如果主子在做 CI/CD 优化相关的研究，值得关注。

---

## 📈 技术趋势洞察

### 🔥 三大热门方向

**1. DeepSeek Harness 生态爆发**
- 主仓库 19.2 万星，周边生态项目全部上榜：
  - `dsh-desktop`（19.6K）：桌面端
  - `awesome-dsh-plugin`（12.2K）：插件精选列表
  - `dsh-routing-suite`（6.7K）：路由注入套件
  - `dsh-web`（5.9K）：Web 插件生态包
  - `dsh-TUI`（2.4K）：终端 UI 插件
  - `dsh-market`（2.2K）：可视化插件市场
- **判断：** DSH 正在复制 VS Code 的生态路径，但速度快了 10 倍。AI 编程工具从"单一产品"进化为"平台生态"。

**2. AI Agent Skill 成为新范式**
- 本周大量"Skill"类项目上榜：
  - `scroll-craft`（634⭐）：滚动动画设计技能
  - `no-negative-echo`（344⭐）：减少 AI 交付中的"残留废案"
  - `solo-skills`（249⭐）：一人企业家的 26 个自动化技能
  - `lanshu-create-ai-presenter-video`（837⭐）：AI 演示视频生成技能
  - `huashu-excel`（142⭐）：数据分析与 Excel 全流程技能
- **判断：** "Agent Skill"正在取代传统的"Plugin/Extension"，成为 AI 时代的扩展范式。写法是给 AI 看的自然语言 + 结构化指令，而不是给机器看的代码。

**3. MCP 协议持续渗透**
- `x64dbg-mcp-server`：调试器 MCP
- `sentio`（158⭐）：AI Agent 邮箱 API（MCP 集成）
- `chat-on-steroids`（75⭐）：ChatGPT 的 MCP 本地控制桥接
- **判断：** MCP 已经成为 AI 工具链的事实标准协议，任何能被 AI 调用的工具都在加 MCP 支持。

### 📊 语言/框架热度变化

| 方向 | 趋势 | 代表项目 |
|------|------|----------|
| TypeScript | 🔥🔥🔥 霸榜 | DSH 全家桶、doop、rome |
| Rust | 🔥🔥 稳定上升 | walgit、eidos、sentio |
| Python | 🔥🔥 AI/ML 刚需 | watermark-remover、cs-board、FrontierAgent |
| Zig | 🔥 冒头 | x64dbg-mcp-server |
| Go | ➡️ 平稳 | MeshLAN、cover |
| Swift | 🔥 小高峰 | herdrm（macOS 原生） |

---

## 💡 值得深挖 TOP 3

### 1. `yetone/cumora` ⭐3,037
🔗 https://github.com/yetone/cumora

**理由：** "AI Agent 团队聊天"——让 AI Agent 和人类在同一个聊天室里协作，Agent 是一等公民。这个产品形态非常新颖，是"人机协作"从 1v1 走向团队协作的关键一步。

**建议：** clone 下来体验一下，看看 Agent 协作的实际效果。适合做一个"AI 团队协作新范式"的深度视频。

### 2. `dmmulroy/anti-slop` ⭐3,588
🔗 https://github.com/dmmulroy/anti-slop

**理由：** 用 Oxlint 规则自动检测并拒绝 AI 生成的低质量 JS/TS 代码模式。这是对"AI 生成的代码越来越同质化"问题的直接回应。3500+ 星说明开发者对 AI slop 的忍耐度已经到了临界点。

**建议：** 整合进现有项目，作为 CI 的一部分。也可以做视频："用 anti-slop 让 AI 写出更好的代码"。

### 3. `kgoedecke/doop` ⭐320
🔗 https://github.com/kgoedecke/doop

**理由：** 开源版 Paper.design，一个多人协作的设计画布，人和 AI Agent 可以同时在上面设计。实时协作 + AI 参与的设计工具，赛道非常新。

**建议：** 试试它的实时协作功能，看看 AI 在画布上能做什么。如果效果好，是一个很好的"AI × 设计"选题。

---

## 📅 周榜亮点

### 持续霸榜
- **DeepSeek Harness** 生态项目本周全面爆发，占据周榜前 15 名中的 7 个位置
- **DSH 插件市场**（dsh-market）和**桌面端**（dsh-desktop）已经进入稳定期

### 本周新晋黑马
- **ThreeUI**（3.4K⭐）：4 天爆发，3D Web 组件赛道杀出的黑马
- **Grok Bot 重建版**（1.7K⭐）：macOS 社区的创造力不可小觑
- **cumora**（3K⭐）：AI Agent 团队聊天，产品形态创新

### 上周热点回顾
- `ip-as-logo-skill`（4.1K⭐）：IP 吉祥物 Logo 生成技能，上周爆火后持续活跃
- `cordiverse/paper`（2.7K⭐）：时空可组合编程范式，学术味很浓的创新

---

## 🎬 视频选题建议

### 选题 1：「DeepSeek Harness 两周 19 万星，AI 编程工具的"安卓时刻"来了？」

**角度：**
- DSH 是什么？和 Claude Code / Codex 有什么区别？
- 为什么社区能在两周内建立完整生态？
- 万物皆插件的架构设计解析
- 对开发者工具市场的影响

**素材来源：** deepseek-harness 主仓库 + dsh-market + dsh-desktop

### 选题 2：「不写代码写"技能"——AI Agent Skill 凭什么取代了 Plugin？」

**角度：**
- 什么是 Agent Skill？和传统 Plugin 的本质区别
- 实战：写一个自己的 Agent Skill（以 scroll-craft 或 huashu-excel 为例）
- 从 solo-skills 看"一人企业"的未来
- Skill 生态会怎么发展？

**素材来源：** scroll-craft + solo-skills + no-negative-echo + huashu-excel

---

## 📊 各语言热榜精选

### Python 本周新星
| 项目 | ⭐ | 简介 |
|------|---|------|
| [watermark-remover](https://github.com/ShadowAqueduct/watermark-remover) | 770 | 清除多种 AI 水印（Unicode、C2PA、元数据） |
| [no-negative-echo](https://github.com/LB623/no-negative-echo) | 344 | 让 Codex 减少交付中的废案残留 |
| [solo-skills](https://github.com/bam-bam-2/solo-skills) | 249 | 一人企业家 26 个 AI 自动化技能 |
| [cs-board](https://github.com/ChenShuo2004/cs-board) | 236 | 中文文案 → 白板动画视频，本地 AI |
| [huashu-excel](https://github.com/alchaincyf/huashu-excel) | 142 | 数据分析 + Excel 全流程 AI 技能 |

### TypeScript 本周新星
| 项目 | ⭐ | 简介 |
|------|---|------|
| [grok-bot-0.18-reconstructed](https://github.com/b-nnett/grok-bot-0.18-reconstructed) | 1,745 | Grok Bot macOS 非官方重建 |
| [biosecurity-agent](https://github.com/Forsy-AI/biosecurity-agent) | 513 | AI 生物安全态势感知 Agent |
| [doop](https://github.com/kgoedecke/doop) | 320 | 开源 Paper.design，人 + AI 协作画布 |
| [rome](https://github.com/rome-os/rome) | 293 | Agentic OS（Agent 操作系统） |
| [downvid](https://github.com/yxxbc/downvid) | 77 | yt-dlp 图形化界面，一键下载无水印视频 |

### Rust 本周新星
| 项目 | ⭐ | 简介 |
|------|---|------|
| [walgit](https://github.com/tobi/walgit) | 1,056 | Git 写前日志工具 |
| [eidos](https://github.com/josiah-nelson/eidos) | 166 | 跨设备离线智能搜索 |
| [sentio](https://github.com/truespar/sentio) | 158 | AI Agent 专属邮箱 API |
| [neuromesh](https://github.com/pinoox/neuromesh) | 60 | AI 编程助手的仿生上下文引擎 |

### Go 本周新星
| 项目 | ⭐ | 简介 |
|------|---|------|
| [MeshLAN](https://github.com/zhaoxuya520/MeshLAN) | 162 | P2P 虚拟局域网 + AI 自动化 |
| [cover](https://github.com/DavidCarliez/cover) | 41 | AI Agent 隐私代理（发假数据，本地恢复） |

---

*报告生成时间：2026-08-25 09:00 CST*
*数据来源：GitHub API + GitHub Trending*
