# Hermes Agent 社区使用方式学习笔记

日期：2026-05-27

## 信息来源

- 官方仓库 README：<https://github.com/NousResearch/hermes-agent>
- 官方 User Stories & Use Cases：<https://hermes-agent.nousresearch.com/docs/user-stories>
- 官方 Skills 文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/>
- 官方 Messaging Gateway 文档：<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/>
- 官方 Cron 文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/>
- 社区集合：<https://github.com/aliaihub/awesome-hermes-usecases>
- 技术解读：<https://dev.to/softwarebuilding/hermes-agent-by-nous-research-the-agent-that-grows-with-your-server-plf>

## 一句话结论

别人不是把 Hermes 当普通聊天机器人用，而是当一个“常驻的个人/团队操作系统代理”用：能连 Telegram/Slack/Discord，能跑命令，能查资料，能定时执行任务，能把做过的复杂流程沉淀成 skills，以后重复调用。

## 官方和社区里最常见的用法

### 1. Telegram/Discord/Slack 常驻助理

典型模式：

- 在服务器或本机常驻 `hermes gateway`。
- 从 Telegram、Discord、Slack 等聊天平台发命令。
- 让它执行开发、研究、运维、文档、提醒等任务。
- 结果直接回到聊天软件。

官方 Messaging Gateway 支持 Telegram、Discord、Slack、WhatsApp、Signal、Email、Matrix、Feishu/Lark、WeCom、Home Assistant、Yuanbao 等。社区里最常见的是 Telegram，因为部署简单、通知直达、适合个人自动化。

可借鉴点：主子现在正在 Telegram 里用 Hermes，这条路线是对的。下一步关键不是“能不能聊天”，而是把它变成可以长期接任务、能回传文件和总结的执行端。

### 2. 自然语言定时任务（Cron）

典型例子：

```text
Every weekday at 9am, summarize my inbox and post to Slack.
```

社区用法包括：

- 每天早上推送新闻/市场/邮件摘要。
- 每小时监控服务器、日志、RSS 或网站变化。
- 每周自动研究热门 AI 工具，生成视频选题。
- 用 no-agent 脚本先过滤变化，只有真的有信号才唤醒 LLM，省 token。

关键点：Hermes 的 cron 不是传统脚本定时器，而是“定时启动一个新 agent 会话”。它可以加载 skills、指定 workdir/profile、把结果发回 Telegram 或其他平台。

适合主子的落地方式：

- 早报：每天 9 点汇总 AI 新闻、GitHub 趋势、模型更新。
- 项目巡检：每天检查指定仓库 issue/PR/CI 状态。
- 资料归档：每晚把当天解决的问题整理到 `hermes-output`。
- 服务器监控：脚本先检查端口/磁盘/进程，有异常才通知。

### 3. Skills：把经验变成可复用技能

Hermes 最核心的差异是 skills。别人用得比较狠的地方在于：

- 做完一个复杂任务后，让 Hermes 写成 `SKILL.md`。
- 下次遇到同类任务，直接加载对应 skill，不再从零摸索。
- 团队会把 skills 当代码库一样维护：命名、审查、更新、废弃。

官方技能系统支持：

- `/skill-name` 直接调用。
- `skills_list()` / `skill_view()` 渐进加载，省上下文。
- 技能带脚本、模板、参考资料。
- 外部技能目录，可以把团队技能库挂进 Hermes。

可借鉴点：主子的高频流程应该技能化，比如：

- “调试 Hermes 本体”
- “总结并保存到 hermes-output”
- “GitLab 自签证书仓库操作”
- “Telegram gateway 排障”
- “模型/provider 切换和验证”

### 4. 软件开发工作流

社区案例里开发类最多，官方 User Stories 里 Dev Workflow 约 60 条。常见玩法：

- 让 Hermes 读仓库、改代码、跑测试、提交 PR。
- 用 `delegate_task` 或额外 Hermes 子进程并行拆任务。
- 用 GitHub/GitLab/Linear/Jira 之类工具做 issue、PR、CI 管理。
- 定时 PR review，或者通过 webhook 触发代码审查。
- 在 VS Code / ACP / Open WebUI 里做前端界面。

高价值模式：

- 主 agent 负责需求理解和验收。
- 子 agent 负责独立实现、调研、测试。
- 关键节点跑测试、看 diff、写总结。
- 成功流程沉淀成 skill。

### 5. 个人知识库/第二大脑

社区里不少人把 Hermes 接到 Obsidian、Nextcloud、Google Drive、LibreOffice、邮件、任务系统。

典型用法：

- 每天写日志，自动归档到 Obsidian。
- 让 Hermes 读已有笔记，生成每日/每周回顾。
- 把项目经验写进 markdown 仓库。
- 用记忆系统记偏好、环境、常用路径。

这和主子的 `hermes-output` 仓库很契合：让 Hermes 不只是“答完就没了”，而是把方案、调研、教程留下来。

### 6. 内容和创意流水线

社区案例包括：

- 自动小说、插图、有声书、网站。
- 从屏幕录制生成教程视频。
- HTML 设计稿转 MP4。
- ComfyUI 工作流编排。
- 每周选题研究、生成视频脚本。

这类用法的关键不是单次生成，而是流水线：选题 → 调研 → 大纲 → 生成素材 → 输出文件 → 归档 → 下次复用偏好。

### 7. 自托管、隐私和团队部署

技术文章里强调 Hermes 适合：

- 想自托管，不想把运行时交给 SaaS 的团队。
- 有数据驻留/合规要求的组织。
- 需要 shell、Docker、SSH、远程服务器、多平台消息入口的场景。

社区里有人把 Hermes 放在 VPS 上，连 Telegram 和 Browser Harness；也有人配本地 SearXNG，减少外部搜索 API 依赖。

对主子的启发：后面如果要稳定长期用，最好把 Hermes 当服务部署，而不是临时 CLI。gateway、cron、日志、备份、skills、output 仓库都要体系化。

## 可以直接抄的主子版 Hermes 使用体系

### 第一层：聊天入口

- Telegram：主入口，适合日常发任务、收结果、收文件。
- CLI：调试和本机重活。
- 必要时接 Open WebUI 或 IDE ACP，做长文档/代码场景。

### 第二层：沉淀体系

- `memory`：只存长期稳定事实，比如偏好、路径、账号环境。
- `skills`：存流程，比如“怎么排查 gateway”、“怎么总结入库”。
- `hermes-output`：存结果，比如教程、调研、总结、计划。
- `session_search`：查过去对话，不要把一次性进度写进 memory。

### 第三层：自动化

优先做这些 cron：

1. 每日 AI/模型/GitHub 趋势简报。
2. 每晚把当天重要会话总结到 `hermes-output`。
3. 每天检查 Hermes 自身状态、gateway 日志、磁盘、关键服务。
4. 每周整理 skills：哪些流程值得沉淀，哪些失效。

### 第四层：开发模式

- 小任务：当前 agent 直接做。
- 中任务：先写 plan，再执行。
- 大任务：`delegate_task` 并行调研/实现/审查。
- 长任务：后台进程或 cron，不要靠单轮聊天硬扛。

## 使用 Hermes 的关键心得

1. **别只聊天，要让它干活。** Hermes 的价值在工具、文件、终端、定时、消息网关。
2. **别只干一次，要沉淀。** 复杂任务做完要变成 skill 或 markdown 总结。
3. **别什么都塞 memory。** memory 存长期事实，流程进 skill，结果进仓库。
4. **cron 是杀手功能。** 它让 Hermes 从“问答工具”变成“主动工作的助理”。
5. **Telegram 是好入口。** 手机发任务、电脑/服务器执行、结果回手机，这个体验最顺。
6. **skills 要维护。** 社区经验说，skill 不是越多越好，乱堆会污染判断；要像代码一样更新和废弃。
7. **自托管要看日志和安全边界。** gateway、cron、终端权限、用户 allowlist 都要管好。

## 下一步建议

主子现在最值得先做三件事：

1. **补齐 Telegram gateway allowlist 和稳定重启机制**，让它成为可靠入口。
2. **建立“总结入库”固定流程**：每次解决问题后写进 `hermes-output`。
3. **挑 3 个高频任务做 cron**：每日简报、Hermes 健康检查、当天知识归档。

做到这三件，Hermes 就不是玩具了，基本就是主子的随身数字奴才班子。