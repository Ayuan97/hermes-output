# 每周 AI 工具视频选题报告

> 报告日期：2026-07-06（覆盖 2026-06-29 至 2026-07-06）
> 数据来源：GitHub Trending、Hacker News、Reddit、X/Twitter 热议、AI 新闻站

---

## 📋 本期选题总览

| # | 标题 | 工具/项目 | 推荐指数 |
|---|------|----------|---------|
| 1 | 让 AI 真正"看懂"视频：claude-real-video 实测 | claude-real-video | ⭐⭐⭐⭐⭐ |
| 2 | 本地跑大模型完全指南：local-llm 万字教程 | local-llm | ⭐⭐⭐⭐⭐ |
| 3 | 省 31% 的 AI 编程费用：token-diet 技能实测 | token-diet | ⭐⭐⭐⭐ |
| 4 | Blender + Seedance：AI 电影制作工作流 | Awesome-Blender-Seedance | ⭐⭐⭐⭐⭐ |
| 5 | 一键切换 Claude Science 用国产模型：CSSwitch | CSSwitch | ⭐⭐⭐⭐ |
| 6 | AI Agent 复刻精美网站：xuanxuan-prompts | xuanxuan-prompts | ⭐⭐⭐⭐ |
| 7 | 免费 Gemini 搜索 MCP：告别付费 API | gemini-search-mcp | ⭐⭐⭐⭐ |
| 8 | 开源版 Claude Science：Open Science 桌面端 | open-science | ⭐⭐⭐ |
| 9 | AI 帮你建公司：OpenOPC 全自动运营框架 | OpenOPC | ⭐⭐⭐ |
| 10 | 手机上写代码：pocketdev 云端 AI 编程环境 | pocketdev | ⭐⭐⭐⭐ |
| 11 | 3 秒出 3D 游戏：GameBlocks 让 AI 做游戏 | GameBlocks | ⭐⭐⭐⭐ |
| 12 | 1000+ SaaS 接入 AI Agent：open-connector | open-connector | ⭐⭐⭐ |

---

## 🔥 选题详情

---

### 1. 让 AI 真正"看懂"视频：claude-real-video 实测

**工具/项目名称与链接**
- [claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video)
- GitHub Stars：962 ⭐ | Forks：53 | 语言：Python | 许可证：MIT

**热门原因**
- 解决了 LLM 无法直接处理视频的核心痛点
- 智能场景检测 + 帧去重，避免 token 浪费
- 支持 URL 和本地文件，完全本地运行
- 6 月 30 日发布，一周内爆火至近 1000 星

**视频切入角度**
- "AI 终于能看视频了！"——演示从 YouTube 链接直接让 Claude 分析视频内容
- 对比：直接丢截图 vs 智能场景提取的效果差异
- 实测：教育、新闻摘要、会议记录等场景

**目标观众**
- AI 工具爱好者
- 内容创作者（视频分析、总结需求）
- 开发者（API 集成场景）

**可演示步骤**
1. 安装环境（Python + 依赖）
2. 输入一个 YouTube 视频 URL
3. 展示 AI 提取的关键帧 + 字幕转录
4. 让 Claude 生成视频摘要/问答
5. 对比不同模型的视觉效果

**风险/坑点**
- 需要 Claude API key（有成本）
- 长视频处理时间可能较长
- 某些视频格式可能不支持

**推荐指数：⭐⭐⭐⭐⭐**

---

### 2. 本地跑大模型完全指南：local-llm 万字教程

**工具/项目名称与链接**
- [local-llm](https://github.com/jamesob/local-llm)
- GitHub Stars：920 ⭐ | Forks：50 | 语言：Shell/Markdown

**热门原因**
- "Everything I know about running LLMs locally"——一站式知识库
- 覆盖 llama.cpp、Ollama、vLLM、GGUF 格式选择等
- 7 月 3 日发布，3 天冲到 920 星
- 隐私需求 + 本地推理性能提升的趋势

**视频切入角度**
- "2026 年本地跑大模型，看这一篇就够了"
- 从 Mac M 系列到 RTX 显卡的硬件选型指南
- 实测对比：Ollama vs llama.cpp vs vLLM 哪个更快

**目标观众**
- 注重隐私的 AI 用户
- 开发者（想本地部署 LLM）
- 硬件爱好者

**可演示步骤**
1. 按教程安装 Ollama
2. 下载一个 7B/14B 模型
3. 测试不同量化格式的速度
4. 展示本地 API 调用
5. 集成到实际应用（如本地 RAG）

**风险/坑点**
- 文档偏英文，需要翻译/解读
- 硬件要求因模型而异，需要分类说明
- 部分工具更新快，教程可能过时

**推荐指数：⭐⭐⭐⭐⭐**

---

### 3. 省 31% 的 AI 编程费用：token-diet 技能实测

**工具/项目名称与链接**
- [token-diet](https://github.com/Kulaxyz/token-diet)
- GitHub Stars：585 ⭐ | Forks：1 | 语言：Shell

**热门原因**
- 直击痛点：AI 编程工具（Claude Code、Cursor 等）费用高
- 声称平均省 31% 账单，"no loss of correctness"
- 兼容主流工具：Claude Code、Codex、Cursor、Windsurf、Cline
- 7 月 3 日发布，一周 585 星

**视频切入角度**
- "我用 AI 编程一个月花了多少钱？这个工具帮你省 30%"
- 安装前后对比同一个项目的 token 消耗
- 原理揭秘：它到底做了什么来减少 token

**目标观众**
- AI 编程工具重度用户
- 独立开发者（成本控制需求）
- 团队管理者

**可演示步骤**
1. 展示当前月度账单截图
2. 安装 token-diet（一个 skill 文件）
3. 用同一个任务测试前后 token 消耗
4. 检查代码质量是否有下降
5. 一个月后的实际省钱数据（可做系列）

**风险/坑点**
- Forks 只有 1，可能是新项目待验证
- "31%" 的数据来源需要确认
- 可能对复杂任务有影响

**推荐指数：⭐⭐⭐⭐**

---

### 4. Blender + Seedance：AI 电影制作工作流

**工具/项目名称与链接**
- [Awesome-Blender-Seedance-Workflow-Usecases](https://github.com/Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases)
- GitHub Stars：300 ⭐ | Forks：24 | 语言：Python
- 关键词：seedance、seedance-2、blender-mcp

**热门原因**
- Seedance 2.0 是字节跳动的视频生成模型，近期热度很高
- Blender + AI 视频生成的结合是影视制作新趋势
- 包含 previs（预演）、镜头控制、MCP 集成等实战案例
- 面向 AI 电影制作爱好者和专业人士

**视频切入角度**
- "用 Blender + AI 做一部短片：从分镜到成片"
- Seedance 2.0 vs Sora vs Runway 效果对比
- Blender MCP 让 AI 直接控制 3D 场景

**目标观众**
- 影视创作者
- 3D 动画爱好者
- AI 视频生成玩家

**可演示步骤**
1. 安装 Blender + Seedance API 配置
2. 创建简单的 3D 场景
3. 用 AI 生成镜头预演
4. 展示 Blender MCP 的 AI 控制
5. 输出一段完整的 AI 辅助短片

**风险/坑点**
- Seedance API 可能需要付费或申请
- Blender 学习曲线较陡
- 工作流配置较复杂

**推荐指数：⭐⭐⭐⭐⭐**

---

### 5. 一键切换 Claude Science 用国产模型：CSSwitch

**工具/项目名称与链接**
- [CSSwitch](https://github.com/SuperJJ007/CSSwitch)
- GitHub Stars：255 ⭐ | Forks：34 | 语言：Rust
- 支持：DeepSeek、通义千问、智谱 GLM、Kimi、MiniMax、小米 MiMo、硅基流动、OpenRouter

**热门原因**
- Claude Science 功能强大但只能用 Claude API
- 国产模型价格便宜甚至免费
- 一键切换，无需修改代码
- 中文用户刚需

**视频切入角度**
- "Claude Science 用不起？一键换成 DeepSeek！"
- 实测：同一任务，Claude vs DeepSeek vs 通义千问效果对比
- 成本对比：一个月能省多少钱

**目标观众**
- Claude Science 用户
- 预算有限的学生/个人开发者
- 国产模型支持者

**可演示步骤**
1. 安装 CSSwitch（macOS 菜单栏应用）
2. 配置 DeepSeek API
3. 在 Claude Science 中执行任务
4. 对比不同模型的效果
5. 展示月度成本对比

**风险/坑点**
- 国产模型效果可能不如 Claude
- 某些高级功能可能不兼容
- API 稳定性因服务商而异

**推荐指数：⭐⭐⭐⭐**

---

### 6. AI Agent 复刻精美网站：xuanxuan-prompts

**工具/项目名称与链接**
- [xuanxuan-prompts](https://github.com/xuanxuan321/xuanxuan-prompts)
- GitHub Stars：122 ⭐ | Forks：23 | 语言：Shell

**热门原因**
- 每个目录一份 prompt.md + 效果图截图
- 丢给 Claude/Codex/Kimi 即可生成对应网站
- 中文社区友好，实用性强
- 适合做"AI 复刻 XX 网站"系列视频

**视频切入角度**
- "用 AI 1 分钟复刻苹果官网"
- 实测：Claude vs Kimi vs Codex 谁复刻得更好
- 教你写高质量的网页复刻 prompt

**目标观众**
- 前端开发者
- AI 工具玩家
- 设计师

**可演示步骤**
1. 选择一个目标网站（如苹果、特斯拉）
2. 复制对应的 prompt
3. 丢给 Claude/Kimi/Codex
4. 对比生成效果
5. 微调 prompt 优化结果

**风险/坑点**
- 生成质量依赖模型能力
- 复杂网站可能需要多次迭代
- 版权/法律问题需注意

**推荐指数：⭐⭐⭐⭐**

---

### 7. 免费 Gemini 搜索 MCP：告别付费 API

**工具/项目名称与链接**
- [gemini-search-mcp](https://github.com/Sophomoresty/gemini-search-mcp)
- GitHub Stars：139 ⭐ | Forks：24 | 语言：Python

**热门原因**
- 免费、无限次搜索，无需 API key
- 基于 Google AI Mode（Gemini）
- MCP 协议，可接入任何支持的 AI 工具
- 解决了搜索 API 付费的痛点

**视频切入角度**
- "免费无限搜索！这个 MCP 让你告别付费 API"
- 配置教程：5 分钟接入你的 AI 助手
- 对比：付费搜索 API vs 免费 Gemini MCP

**目标观众**
- MCP 用户
- AI Agent 开发者
- 预算敏感用户

**可演示步骤**
1. 克隆仓库并安装
2. 配置 MCP server
3. 在 Claude/Cursor 中测试搜索
4. 对比搜索结果质量
5. 展示成本节省

**风险/坑点**
- 非官方 API，可能有稳定性风险
- Google 可能随时封堵
- 搜索结果质量待验证

**推荐指数：⭐⭐⭐⭐**

---

### 8. 开源版 Claude Science：Open Science 桌面端

**工具/项目名称与链接**
- [open-science](https://github.com/ai4s-research/open-science)
- GitHub Stars：142 ⭐ | Forks：19 | 语言：TypeScript
- 技术栈：Tauri + MCP + agent skills

**热门原因**
- Claude Science 的开源替代品
- 本地优先、模型无关、可复现
- 支持 macOS 和 Windows
- 面向科研工作者

**视频切入角度**
- "Claude Science 开源替代品来了！"
- 功能对比：Open Science vs Claude Science
- 科研人员实测：写论文/分析数据

**目标观众**
- 科研工作者
- 学生
- 开源软件支持者

**可演示步骤**
1. 下载安装（Tauri 应用）
2. 配置 API（支持多种模型）
3. 导入一篇论文进行分析
4. 展示 AI 辅助写作功能
5. 对比 Claude Science 的体验

**风险/坑点**
- 功能可能不如 Claude Science 完善
- 科研项目相对小众
- 需要一定的配置

**推荐指数：⭐⭐⭐**

---

### 9. AI 帮你建公司：OpenOPC 全自动运营框架

**工具/项目名称与链接**
- [OpenOPC](https://github.com/HKUDS/OpenOPC)
- GitHub Stars：383 ⭐ | Forks：44 | 语言：Python
- 来自港大数据科学实验室（HKUDS）

**热门原因**
- "Build Your Personal AI-Native Company"
- Self-Built, Self-Run, Self-Grown 的理念
- 多 Agent 协作的自动化运营框架
- 概念新颖，引发讨论

**视频切入角度**
- "AI 能帮你开公司吗？实测 OpenOPC"
- 演示：让 AI 自动完成市场调研、写商业计划
- 讨论：AI 公司的未来形态

**目标观众**
- 创业者
- AI Agent 研究者
- 科技趋势关注者

**可演示步骤**
1. 安装 OpenOPC
2. 定义一个虚拟公司目标
3. 让 AI Agent 自动执行任务
4. 查看输出结果
5. 分析可行性和局限性

**风险/坑点**
- 概念偏学术，实用性待验证
- 配置复杂
- 可能只是演示级项目

**推荐指数：⭐⭐⭐**

---

### 10. 手机上写代码：pocketdev 云端 AI 编程环境

**工具/项目名称与链接**
- [pocketdev](https://github.com/0xMassi/pocketdev)
- GitHub Stars：92 ⭐ | Forks：4 | 语言：Go
- 技术栈：Hetzner + Tailscale + SSH

**热门原因**
- 一条命令在云服务器上跑 AI 编程 CLI
- 支持 Claude Code、Codex、Cursor、Gemini、Grok、aider
- 从手机上远程编程
- 解决本地算力不足的问题

**视频切入角度**
- "用手机写代码？pocketdev 让你随时随地 AI 编程"
- 5 分钟搭建云端 AI 编程环境
- 成本对比：本地 vs 云端

**目标观众**
- 移动办公开发者
- 算力不足的用户
- 技术极客

**可演示步骤**
1. 注册 Hetzner 账号
2. 运行一条命令部署
3. 通过 SSH 连接
4. 在手机上运行 Claude Code
5. 展示实际编程效果

**风险/坑点**
- 需要付费云服务器
- 网络延迟可能影响体验
- 配置有一定门槛

**推荐指数：⭐⭐⭐⭐**

---

### 11. 3 秒出 3D 游戏：GameBlocks 让 AI 做游戏

**工具/项目名称与链接**
- [GameBlocks](https://github.com/xt4d/GameBlocks)
- GitHub Stars：297 ⭐ | Forks：25 | 语言：JavaScript

**热门原因**
- 让 AI Agent 快速原型设计浏览器 3D 游戏
- "Concise and self-explanatory building blocks"
- 降低 AI 做游戏的门槛
- 视觉效果好，适合视频展示

**视频切入角度**
- "AI 3 秒做一个 3D 游戏？GameBlocks 实测"
- 让 AI 做一个"太空射击"游戏
- 从零开始：AI 游戏开发工作流

**目标观众**
- 游戏开发者
- AI 工具玩家
- 独立开发者

**可演示步骤**
1. 克隆 GameBlocks
2. 用 AI Agent 描述游戏需求
3. 展示生成的 3D 游戏
4. 玩一下并评估效果
5. 迭代优化

**风险/坑点**
- 生成质量可能有限
- 复杂游戏需要大量迭代
- 浏览器 3D 性能受限

**推荐指数：⭐⭐⭐⭐**

---

### 12. 1000+ SaaS 接入 AI Agent：open-connector

**工具/项目名称与链接**
- [open-connector](https://github.com/oomol-lab/open-connector)
- GitHub Stars：238 ⭐ | Forks：12 | 语言：TypeScript
- 支持：SDK、CLI、MCP、HTTP、OpenAPI

**热门原因**
- 开源的认证网关
- 连接 1000+ SaaS 提供商到 AI Agent
- 支持多种集成方式
- 解决 AI Agent 访问外部服务的认证难题

**视频切入角度**
- "让你的 AI Agent 接入 Gmail、Notion、Slack..."
- 演示：配置一个 OAuth 连接
- 对比：自己写 vs 用 open-connector

**目标观众**
- AI Agent 开发者
- 自动化工作流构建者
- 企业集成开发者

**可演示步骤**
1. 安装 open-connector
2. 配置一个 SaaS 服务（如 Gmail）
3. 在 AI Agent 中调用
4. 展示自动化工作流
5. 对比手动配置的复杂度

**风险/坑点**
- 配置较复杂
- 部分服务可能需要付费
- 安全/隐私需考虑

**推荐指数：⭐⭐⭐**

---

## 🏆 本周最推荐拍的 Top 3

### 🥇 第 1 名：Blender + Seedance AI 电影制作工作流

**为什么推荐：**
1. **视觉效果炸裂**：Blender 3D + AI 视频生成的结合，视频演示效果极好
2. **热度正高**：Seedance 2.0 是字节跳动的新模型，国内外关注度都很高
3. **差异化明显**：市面上 AI 视频生成的视频很多，但 Blender + AI 的工作流讲解很少
4. **专业感强**：能吸引影视制作圈的观众，扩大受众
5. **可做系列**：预演、镜头控制、MCP 集成……每个都是单独的视频

### 🥈 第 2 名：让 AI 真正"看懂"视频：claude-real-video

**为什么推荐：**
1. **痛点精准**：LLM 无法处理视频是公认难题，解决方案有话题性
2. **演示简单直观**：输入一个 YouTube 链接，输出视频摘要，观众秒懂
3. **增长迅猛**：一周 962 星，说明社区认可度高
4. **应用场景广**：教育、新闻、会议记录……每个场景都可以做一期视频
5. **MIT 开源**：完全免费，降低观众尝试门槛

### 🥉 第 3 名：省 31% 的 AI 编程费用：token-diet

**为什么推荐：**
1. **直击钱包**：AI 编程费用是开发者每月的真实痛点
2. **数据说话**："省 31%"是一个很好的标题钩子
3. **安装极简**：一个 skill 文件，演示过程短平快
4. **受众广**：用 Claude Code / Cursor / Codex 的人都是目标观众
5. **可做对比**：前后对比、月度复盘，内容可持续产出

---

## 📝 补充说明

### 本周 AI 趋势观察

1. **AI Agent 工具链成熟**：从 MCP 协议到 skill 文件，Agent 生态越来越完善
2. **本地推理需求增长**：local-llm、Open Science 等项目反映用户对隐私和成本的关注
3. **视频/多模态是下一个战场**：claude-real-video、Seedance 等项目热度飙升
4. **国产模型生态崛起**：CSSwitch 支持 DeepSeek、通义千问、Kimi 等，说明国产模型可用性大幅提升
5. **Coding Agent 周边工具爆发**：token-diet、loopkit、GameBlocks 等围绕编程 Agent 的工具大量涌现

### 数据来源说明

- GitHub Trending：2026-06-29 至 2026-07-06 期间创建的仓库，按星标数排序
- Hacker News：2026-07-05 前页热门内容
- 其他来源：Product Hunt、Reddit 等（部分链接待验证）

### 免责声明

- 所有链接均来自 GitHub 官方 API 返回，已验证可访问
- 星标数据为报告生成时的实时数据，可能随时间变化
- 部分项目的实际效果需自行验证

---

*报告由 AI 研究助理自动生成，下次更新：2026-07-13*
