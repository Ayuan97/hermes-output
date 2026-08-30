# 🔥 GitHub 趋势速览 — 2026年8月30日（周六）

## 一句话总览

**AI Agent Skills 生态大爆发。** 今天 GitHub 日榜 19 个项目里，至少 7 个跟 AI Agent 技能/插件直接相关。从 Anthropic 官方插件目录、Cursor 插件规范，到科学领域 Agent Skills、视频制作 Agent 系统——整个行业正在从"用 AI 写代码"快速转向"给 AI 装上专业工具箱"。

---

## 🚀 爆款项目 TOP 5

### 1. tt-a1i/archify ⭐+3,902/天
🔗 https://github.com/tt-a1i/archify

**干什么的：** AI Agent 技能插件，让 AI 能画出漂亮的架构图、流程图、时序图、数据流图，输出为自包含 HTML，带动画效果，还能导出高清图。

**为什么火：** 解决了 AI 画图一直以来的痛点——画出来的图丑、不可控、难复用。这个技能让 Agent 能直接生成可验证的架构图，自带样式和动画，不再需要人工去 Mermaid/Draw.io 里折腾。

**跟主子的关系：** 做技术内容的话这个非常值得试，让 AI 画架构图的效果可以做成视频演示，视觉冲击力强。

---

### 2. bilawalsidhu/gods-eye-view ⭐+1,855/天
🔗 https://github.com/bilawalsidhu/gods-eye-view

**干什么的：** 浏览器里的"间谍卫星模拟器"——在 3D 地球上叠加真实开源空间情报数据，效果逼真。

**为什么火：** OSINT（开源情报）+ 3D 可视化，电影感拉满。虽然数据是公开的，但呈现方式极其酷炫，传播性极强。

**跟主子的关系：** 视频选题金矿。"用浏览器模拟间谍卫星"这个标题就能爆，而且技术实现可以讲很多。

---

### 3. K-Dense-AI/scientific-agent-skills ⭐+1,587/天
🔗 https://github.com/K-Dense-AI/scientific-agent-skills

**干什么的：** 把任意 AI Agent 变成"AI 科学家"——165 个科学领域技能 + 100+ 数据库（生物、化学、医学、药物发现），兼容 Cursor/Claude Code/Codex 等。

**为什么火：** 全球 19 万科学家在用。这是 Agent Skills 生态在垂直领域最成功的案例之一，证明了"给 AI 装专业工具箱"这个模式在学术界也跑通了。

**跟主子的关系：** 如果主子有科研相关的需求或者想做科研 AI 方向的内容，这个项目值得深挖。

---

### 4. THU-MAIC/OpenMAIC ⭐+907/天
🔗 https://github.com/THU-MAIC/OpenMAIC

**干什么的：** 清华出品的"开放多智能体交互课堂"——一键启动沉浸式多 Agent 学习体验。

**为什么火：** 多 Agent 协作 + 教育场景，清华背书，开源可玩。把"AI 老师互相讨论"变成可视化的课堂体验。

**跟主子的关系：** 教育 + AI 赛道的新玩法，可以体验一下看看效果，说不定能启发新的内容方向。

---

### 5. calesthio/OpenMontage ⭐+806/天
🔗 https://github.com/calesthio/OpenMontage

**干什么的：** 全球首个开源 AI 视频制作系统。12 条制作流水线、100+ 工具、700+ Agent 技能文件，把你的 AI 编程助手变成完整的视频制作工作室。

**为什么火：** 直接把"AI Agent + 视频制作"做到了产品级。不是 demo，是真的能用的完整工作流。

**跟主子的关系：** 如果主子做视频内容，这个工具链值得认真研究——用 AI Agent 辅助视频生产流程，效率可能大幅提升。

---

## 📈 技术趋势洞察

### 🔥 Agent Skills 生态正式进入"军备竞赛"阶段

今天最明显的信号：**AI Agent 插件/技能生态正在被大厂和开源社区同时推进。**

- **Anthropic 官方**下场做了 `claude-plugins-official`（官方插件目录）和 `claude-plugins-community`（社区插件市场）
- **Cursor** 发布了 `cursor/plugins`（插件规范 + 官方插件）
- **JetBrains** 搞了 `go-modern-guidelines`（帮 AI Agent 写现代 Go 代码的指南）
- **Google** 也上了 `google/skills`（Google 产品的 Agent 技能集）
- **社区**更是遍地开花：`awesome-claude-skills`、`awesome-agent-skills`、`garden-skills`、`scientific-agent-skills`...

这说明 **"AI 编程助手"正在从"通用工具"变成"专业平台"**，就像 VS Code 靠插件生态赢了一样，下一阶段的 AI 编程工具竞争核心是**技能生态**。

### 🌍 其他值得关注的趋势

- **Rust 桌面工具持续走强**：`OpenLogi`（罗技鼠标驱动的 Rust 替代品，周增 4000+）说明 Rust 在"干掉闭源驱动"这条路上越走越远
- **Go 在 Agent 基础设施领域发力**：`workweave/router`（模型路由器，<50ms 路由到最优模型）和 `tailscale/tailcat`（Tailscale 版 netcat）都是基础设施工具
- **免费 LLM API 聚合**：`freellmapi` 周增 2,691，聚合了 34 个免费 LLM 提供商、635 个模型端点。说明大家还是想白嫖
- **OSINT 工具热度不减**：`user-scanner`（455+ 扫描向量的邮箱/用户名 OSINT 套件）和 `gods-eye-view` 都上了榜

---

## 💡 值得深挖 TOP 3

### 1. every-app/open-seo ⭐+517/天
🔗 https://github.com/every-app/open-seo

**理由：** 开源版 Semrush/Ahrefs。SEO 工具赛道的付费产品动辄 $100/月起步，如果这个开源替代能用，对内容创作者和小团队来说是巨大的成本节省。值得 clone 下来试试看实际效果。

### 2. ChromeDevTools/chrome-devtools-mcp ⭐+216/天
🔗 https://github.com/ChromeDevTools/chrome-devtools-mcp

**理由：** Google 官方出品，让 AI 编程 Agent 能直接操作 Chrome DevTools。这意味着 AI 可以自动调试网页、分析性能、查看网络请求——前端开发的自动化测试和调试效率会大幅提升。值得整合进现有开发流程。

### 3. t8y2/dbx ⭐+119/天
🔗 https://github.com/t8y2/dbx

**理由：** 20MB 轻量级跨平台数据库客户端，支持 90+ 数据库（MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB 等），内置 AI 和 MCP Server。一个工具搞定所有数据库，还自带 AI 助手，Rust 写的性能也有保障。

---

## 📅 周榜亮点

### 持续霸榜
- **tt-a1i/archify** 🏆 周增 14,875 ⭐ — 本周绝对王者
- **freestylefly/awesome-gpt-image-2** 周增 13,141 — GPT-Image2 提示词工程，中文社区的爆款项目
- **openai/codex** 周增 7,775 — OpenAI 的终端编程 Agent，Rust 写的

### 本周新晋黑马
- **MadsLorentzen/ai-job-search** 周增 5,145 — 用 Claude Code 驱动的 AI 求职框架（自动评估岗位、定制简历、写求职信、面试准备），在这个就业市场下确实是刚需
- **Alishahryar1/free-claude-code** 周增 4,942 — 免费用 Claude Code/Codex 等工具（13 亿+ 免费 token），虽然名字很直白，但确实火
- **AprilNEA/OpenLogi** 周增 4,114 — Rust 写的罗技鼠标驱动替代品，本地运行，不要账号，没有遥测。Linux 用户的福音

---

## 🎬 视频选题建议

### 选题 1：「我在浏览器里装了个间谍卫星」
基于 `bilawalsidhu/gods-eye-view` 做一期演示视频。3D 地球 + 真实卫星数据 + 开源情报叠加，视觉效果极其震撼，标题党属性满分，传播性极强。技术角度可以讲 WebGL/3D 渲染 + 开源情报收集方法。

### 选题 2：「2026 年 AI 编程工具大变局：Agent Skills 生态全面解析」
今天日榜 19 个项目里 7 个是 Agent Skills 相关，这不是巧合。可以做一期深度分析视频，讲讲 Anthropic 官方插件生态、Cursor 插件规范、以及社区 Skills 库的对比，帮观众理解"AI 编程助手"的下一步走向。

---

## 📊 语言分布速览

| 语言 | 日榜占比 | 趋势 |
|------|---------|------|
| Python | ~35% | Agent Skills 生态主力 |
| TypeScript | ~20% | 前端 + MCP 工具 |
| Go | ~15% | Agent 基础设施 |
| Rust | ~15% | 桌面工具 + 系统级 |
| JavaScript | ~10% | 可视化 + 插件 |
| C++/Shell/其他 | ~5% | |

**核心观察：** Python 依然是 AI 生态的绝对主力语言，但 Agent Skills 这个新赛道正在把 TypeScript、Go、Rust 都拉进来——技能生态是跨语言的。

---

*报告由奴才于 2026-08-30 09:00 自动生成，主子早安 ☀️*
