# 每周 AI 工具热门选题（2026-07-21 ~ 2026-07-27）

> 数据来源：GitHub Trending（周榜）、Hacker News Top Stories、GitHub 新建高星仓库
> 生成时间：2026-07-27

---

## 选题 1：Orca —— 多 Agent 并行开发环境

- **工具/项目**：[stablyai/orca](https://github.com/stablyai/orca)
- **Star**：29,700+
- **热门原因**：YC 支持项目，支持在桌面/手机/VPS 上同时跑多个 AI 编程 Agent（Claude Code、Codex、Cursor 等），用你自己的订阅，Worktree 并行开发。概念新颖，解决了"一个 Agent 不够用"的痛点。
- **视频切入角度**：
  - "一个程序员同时让 5 个 AI 帮你写代码"
  - "AI 编程不再是单线程！Orca 并行 Agent 实测"
- **目标观众**：程序员、AI 工具爱好者、效率工具控
- **可演示步骤**：
  1. 安装 Orca 桌面端
  2. 配置自己的 API Key
  3. 同时开 3 个 Agent 处理不同任务
  4. 展示 Agent 之间如何协调、Worktree 隔离
  5. 手机端远程控制 Agent
- **风险/坑点**：需要多个 AI 订阅/API Key，成本较高；并行 Agent 可能冲突
- **推荐指数**：⭐⭐⭐⭐⭐

---

## 选题 2：Kronos —— 金融市场基础模型

- **工具/项目**：[shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)
- **Star**：34,100+
- **热门原因**：专门为金融市场设计的基础模型，理解"金融语言"。近期 Star 暴涨，金融 + AI 是流量密码。
- **视频切入角度**：
  - "AI 终于学会炒股了？金融大模型 Kronos 深度测评"
  - "让 AI 读懂K线图：Kronos 金融模型实测"
- **目标观众**：投资者、量化交易爱好者、AI 技术关注者
- **可演示步骤**：
  1. 克隆仓库、安装环境
  2. 加载模型并展示能力
  3. 输入真实股票数据，看模型如何分析
  4. 与通用大模型对比金融理解能力
  5. 讨论实际应用场景
- **风险/坑点**：模型可能很大，本地跑需要 GPU；金融预测有风险，需声明不构成投资建议
- **推荐指数**：⭐⭐⭐⭐⭐

---

## 选题 3：OmniRoute —— 一个接口调用 290+ AI 服务

- **工具/项目**：[diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)
- **Star**：31,000+
- **热门原因**：MIT 协议免费开源，一个端点接入 290+ 供应商、500+ 模型（含 90+ 免费）。支持 Claude Code、Codex、Cursor 等工具无缝对接。自带智能 fallback、Token 压缩（节省 15-95%）。500+ 贡献者。
- **视频切入角度**：
  - "白嫖 500 个 AI 模型！OmniRoute 网关保姆级教程"
  - "API Key 太多管不过来？一个网关搞定所有 AI"
- **目标观众**：AI 开发者、Claude Code/Codex 用户、省钱党
- **可演示步骤**：
  1. 部署 OmniRoute（Docker 一键启动）
  2. 配置多个供应商 Key
  3. 在 Claude Code 中接入 OmniRoute
  4. 演示智能 fallback（一个供应商挂了自动切换）
  5. 展示 Token 压缩效果对比
- **风险/坑点**：免费供应商稳定性待验证；配置项较多，新手可能晕
- **推荐指数**：⭐⭐⭐⭐⭐

---

## 选题 4：DeepTutor —— 终身个性化 AI 家教

- **工具/项目**：[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)
- **Star**：30,000+
- **热门原因**：港大团队出品，多 Agent + RAG 架构，主打"终身学习伙伴"概念。不只是问答，而是根据你的水平调整教学策略。
- **视频切入角度**：
  - "AI 终于能当你的私人老师了！DeepTutor 深度体验"
  - "考研/考公/学编程？DeepTutor 个性化 AI 家教实测"
- **目标观众**：学生、考证党、终身学习者、家长
- **可演示步骤**：
  1. 部署 DeepTutor
  2. 上传学习资料（PDF、课本）
  3. 让 DeepTutor 根据资料出题
  4. 展示它如何根据你的薄弱点调整讲解
  5. 与通用 ChatGPT 对比教学效果
- **风险/坑点**：本地部署有门槛；中文支持待验证；学习曲线可能需要适应
- **推荐指数**：⭐⭐⭐⭐

---

## 选题 5：RuView —— 用 WiFi 信号替代摄像头

- **工具/项目**：[ruvnet/RuView](https://github.com/ruvnet/RuView)
- **Star**：86,600+
- **热门原因**：把普通 WiFi 信号变成实时空间感知、生命体征监测、存在检测——完全不需要摄像头。概念极其吸引眼球，Star 数爆炸。
- **视频切入角度**：
  - "不用摄像头也能监控房间？WiFi 感应黑科技实测"
  - "WiFi 信号能检测你在不在家！RuView 深度体验"
- **目标观众**：智能家居爱好者、隐私关注者、科技猎奇者
- **可演示步骤**：
  1. 硬件需求介绍（普通 ESP32 或路由器）
  2. 部署 RuView 并配置
  3. 演示存在检测：人进房间→检测到
  4. 演示生命体征监测（呼吸、心率）
  5. 与传统摄像头方案对比隐私性
- **风险/坑点**：需要特定硬件；精度可能受环境影响大；演示效果不一定稳定
- **推荐指数**：⭐⭐⭐⭐

---

## 选题 6：文字转手绘日记动画（story-to-handdrawn-video）

- **工具/项目**：[gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video)
- **Star**：653（新项目，快速增长中）
- **热门原因**：专为中文内容设计！把中文故事文案或图片序列转成手绘日记风格的动画视频（MP4）。完美契合短视频创作者需求。
- **视频切入角度**：
  - "中文故事秒变手绘动画！这个 AI 工具太适合做视频了"
  - "不用画画也能做手绘风短视频？AI 手绘日记生成器"
- **目标观众**：短视频创作者、自媒体博主、内容创业者
- **可演示步骤**：
  1. 准备一段中文故事文案
  2. 运行工具生成手绘动画
  3. 展示不同风格的输出效果
  4. 对比手动制作的时间成本
  5. 实际应用到短视频平台发布
- **风险/坑点**：生成质量可能不稳定；风格选择有限；可能需要 GPU
- **推荐指数**：⭐⭐⭐⭐⭐

---

## 选题 7：Hallmark —— 反 AI 味设计技能

- **工具/项目**：[Nutlope/hallmark](https://github.com/Nutlope/hallmark)
- **Star**：18,200+
- **热门原因**：Vercel 工程师出品，专门解决 Claude Code/Cursor/Codex 生成的代码"AI味太重"的问题。一套 Skill 让 AI 生成的 UI 更像人类设计师写的。
- **视频切入角度**：
  - "AI 写的代码一眼就能看出来？一个 Skill 解决 AI 味问题"
  - "让你的 AI 编程助手告别 AI 味！Hallmark Skill 实测"
- **目标观众**：前端开发者、AI 编程用户、UI/UX 设计师
- **可演示步骤**：
  1. 先用 Claude Code 生成一个页面（展示 AI 味）
  2. 安装 Hallmark Skill
  3. 重新生成同样页面
  4. 前后对比细节差异
  5. 讲解 Skill 的核心设计原则
- **风险/坑点**：仅适用于特定 AI 编码工具；效果主观，不一定人人觉得好
- **推荐指数**：⭐⭐⭐⭐

---

## 选题 8：手写变字体（draw-your-font）

- **工具/项目**：[danilo-znamerovszkij/draw-your-font](https://github.com/danilo-znamerovszkij/draw-your-font)
- **Star**：306（新项目，本周热门）
- **热门原因**：拍照手写→自动生成真正的字体文件（TTF/WOFF/WOFF2），完全免费开源、不上传数据。Node CLI + Claude Code Skill。
- **视频切入角度**：
  - "你的手写体变成电脑字体！AI 字体生成器免费开源"
  - "拍张照就能拥有专属字体！draw-your-font 教程"
- **目标观众**：设计师、书法爱好者、个性化需求用户
- **可演示步骤**：
  1. 手写一张字母/汉字样本
  2. 拍照上传
  3. 运行工具生成字体
  4. 安装字体并在文档中使用
  5. 展示不同手写风格的效果
- **风险/坑点**：中文支持待验证（可能仅支持拉丁字母）；手写质量影响输出
- **推荐指数**：⭐⭐⭐

---

## 选题 9：AI 代码审查图谱（code-review-graph）

- **工具/项目**：[tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)
- **Star**：26,600+
- **热门原因**：本地优先的代码智能图谱，为 MCP 和 CLI 构建持久化的代码库地图。AI 编码工具只读取相关代码，大幅减少上下文浪费。有基准测试数据支撑。
- **视频切入角度**：
  - "AI 编程工具总是读不懂你的代码？这个图谱工具解决了"
  - "让 Claude Code 真正理解你的项目！代码图谱实战"
- **目标观众**：AI 编程重度用户、大型项目维护者
- **可演示步骤**：
  1. 在大型项目上安装 code-review-graph
  2. 构建代码图谱
  3. 对比开启前后的 AI 代码审查质量
  4. 展示 Token 消耗对比
  5. 在 Claude Code/Cursor 中集成使用
- **风险/坑点**：小项目效果不明显；索引构建需要时间
- **推荐指数**：⭐⭐⭐⭐

---

## 选题 10：Claude-of-Duty —— 一句话生成 3A 级 FPS 游戏

- **工具/项目**：[mshumer/Claude-of-Duty](https://github.com/mshumer/Claude-of-Duty)
- **Star**：659（新项目，本周爆发）
- **热门原因**：一个 Prompt 生成使命召唤级别的 Three.js FPS 游戏。视觉冲击力极强，完美适合视频展示。
- **视频切入角度**：
  - "一句话让 AI 做出使命召唤？！Claude-of-Duty 实测"
  - "AI 编程的极限：一个 Prompt 生成完整 FPS 游戏"
- **目标观众**：游戏爱好者、AI 技术关注者、泛科技用户
- **可演示步骤**：
  1. 展示原始 Prompt
  2. 运行生成过程
  3. 实际游玩生成的游戏
  4. 分析代码质量和游戏性
  5. 尝试修改 Prompt 生成不同风格游戏
- **风险/坑点**：生成结果可能不稳定；需要 Claude API 访问
- **推荐指数**：⭐⭐⭐⭐⭐

---

## 选题 11：《动手学 Pi》+ Pi Agent 生态

- **工具/项目**：
  - [earendil-works/pi](https://github.com/earendil-works/pi)（78,000+ Stars）
  - [hahhforest/pi-textbook](https://github.com/hahhforest/pi-textbook)（441 Stars）
  - [agegr/pi-web](https://github.com/agegr/pi-web)（2,875 Stars）
- **热门原因**：Pi 是目前最火的 AI Agent 工具包之一，统一 LLM API + Agent Loop + TUI + CLI。中文社区出了配套教程《动手学 Pi》，15 个 checkpoint 从零构建 Pi-style Agent。
- **视频切入角度**：
  - "从零构建自己的 AI Agent！《动手学 Pi》教程系列"
  - "78000 Star 的 AI 框架 Pi 到底怎么用？保姆级入门"
- **目标观众**：AI 开发者、想学 Agent 开发的程序员
- **可演示步骤**：
  1. 介绍 Pi 生态全景
  2. 快速上手 Pi CLI
  3. 跟着教程构建第一个 Agent
  4. 展示 Agent Loop 工作原理
  5. 自定义 Skill 和工具
- **风险/坑点**：学习曲线较陡；需要一定编程基础
- **推荐指数**：⭐⭐⭐⭐

---

## 选题 12：钢笔线稿知识动画（muyang-flat-animation）

- **工具/项目**：[yokel1121/muyang-flat-animation](https://github.com/yokel1121/muyang-flat-animation)
- **Star**：208（新项目）
- **热门原因**：将中文观点转成纸上钢笔线稿与彩铅风格的知识讲解动画素材。与选题 6 类似但风格不同，面向知识类博主。
- **视频切入角度**：
  - "做知识类视频不用愁！AI 自动生成钢笔线稿动画"
  - "中文知识博主福音：AI 生成讲解动画素材"
- **目标观众**：知识类短视频创作者、教育博主
- **可演示步骤**：
  1. 输入一段中文知识文案
  2. 生成钢笔线稿风格动画
  3. 展示彩铅风格变体
  4. 实际应用到视频中
  5. 对比手工绘制的时间
- **风险/坑点**：项目较新，稳定性待验证；风格可能有限
- **推荐指数**：⭐⭐⭐

---

## 🏆 本周最推荐拍的 Top 3

### 🥇 第一名：Claude-of-Duty（一句话生成 FPS 游戏）

**为什么**：
1. **视觉冲击力最强**——"一句话做出使命召唤"这个标题本身就是流量密码
2. **演示效果极佳**——可以直接在视频里玩 AI 生成的游戏
3. **受众面最广**——游戏 + AI 双流量，不需要编程知识也能看懂
4. **制作成本低**——一个 Prompt + 录屏就能出片

---

### 🥈 第二名：文字转手绘日记动画（story-to-handdrawn-video）

**为什么**：
1. **精准命中中文创作者需求**——专门为中文内容设计
2. **实用性极高**——直接解决"做视频没素材"的痛点
3. **教程空间大**——可以出系列教程，从入门到进阶
4. **差异化强**——手绘日记风格在中文市场还不饱和

---

### 🥉 第三名：OmniRoute（一个接口调用 290+ AI 服务）

**为什么**：
1. **省钱属性天然吸引点击**——"白嫖""免费"是永恒流量词
2. **实用价值高**——解决 AI 开发者真实痛点（API 管理混乱）
3. **教程属性强**——配置过程本身就是好内容
4. **受众精准且粘性高**——AI 开发者群体付费意愿强、传播力大

---

## 补充信息

### 数据来源说明
- GitHub Trending 周榜：已验证
- GitHub 新建高星仓库（7月20日后创建）：已验证
- Hacker News Top Stories：部分获取成功
- Product Hunt / Reddit：403 被拦截，未能获取（待验证）

### 未入选但值得关注的项目
- **mattpocock/skills**（189,000+ Stars）：Skills for Real Engineers，但偏向高级开发者
- **awesome-claude-skills**（70,000+ Stars）：Claude Skills 汇总列表，适合做盘点但不适合单独选题
- **ai-agent-book**（20,800+ Stars）：《深入理解 AI Agent》开源书，适合做读书分享但不够"工具向"
- **Instatic**（5,600+ Stars）：开源 Webflow 替代品，但偏建站方向，受众窄
