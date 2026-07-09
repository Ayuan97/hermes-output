# 🔥 今日 GitHub 趋势速览

**日期：2026年7月9日（周四）**

## 一句话总览

> **AI Agent 生态大爆发！** 今天 GitHub 趋势榜被 AI 编程 Agent 的技能/插件/框架项目屠榜了——从 Claude Code 到 Codex，几乎所有热门 AI 编码工具都在建"技能商店"。安全领域也出现 AI 渗透测试工具，Rust 在 Agent 基础设施层持续渗透。

---

## 🚀 爆款项目 TOP 5

### 1. iOfficeAI/OfficeCLI ⭐+1,717/天
🔗 https://github.com/iOfficeAI/OfficeCLI  
**干什么的：** 专门给 AI Agent 用的 Office 套件（C#），能读写 Word/Excel/PPT，不需要装 Office，单文件部署。  
**为什么火：** 解决了 AI Agent 处理办公文档的痛点——之前 Agent 要操作 Excel 得靠 python-pptx 这些笨重库，现在一个二进制搞定。  
**对主子的价值：** 如果做自动化工作流或者让 Agent 帮忙处理文档，这个直接能用。值得 clone 试试。

### 2. addyosmani/agent-skills ⭐+1,297/天
🔗 https://github.com/addyosmani/agent-skills  
**干什么的：** Addy Osmani（Google Chrome 团队大佬）搞的生产级 AI 编码 Agent 技能库（JS）。  
**为什么火：** 名人效应 + 实战验证。Agent 技能现在是刚需，大家都在给 Claude Code/Codex 写 prompt 工程。  
**对主子的价值：** 可以直接抄作业——看看顶级工程师怎么给 Agent 写技能指令的。做视频选题也不错，"Google 大佬怎么教 AI 写代码"。

### 3. asgeirtj/system_prompts_leaks ⭐+1,218/天
🔗 https://github.com/asgeirtj/system_prompts_leaks  
**干什么的：** 收集各大 AI（Claude 5、GPT 5.5、Gemini 3.5 等）的系统提示词泄露合集。  
**为什么火：** 大家对 AI 背后的"咒语"充满好奇。泄露的系统提示词对 prompt 工程有参考价值。  
**对主子的价值：** 做 AI 视频的好素材——"各大 AI 的系统提示词长什么样"是个不错的选题角度。

### 4. Diolinux/PhotoGIMP ⭐+1,125/天
🔗 https://github.com/Diolinux/PhotoGIMP  
**干什么的：** 给 GIMP 3+ 打的补丁，让它用起来像 Photoshop（界面/快捷键）。  
**为什么火：** GIMP 3 刚发布不久，Photoshop 用户迁移需求大。开源免费替代 Adobe 是永恒话题。  
**对主子的价值：** 做"免费替代 Photoshop"的视频选题，受众面广。

### 5. obra/superpowers ⭐+1,116/天（总星数 249,818！）
🔗 https://github.com/obra/superpowers  
**干什么的：** Agent 技能框架 + 软件开发方法论，号称"真的能用"。  
**为什么火：** 快 25 万星了，说明社区对 Agent 辅助开发的巨大需求。把方法论和技能模板打包在一起。  
**对主子的价值：** 可以研究它的框架设计思路，看看怎么给自家 Agent 搭建技能体系。

---

## 📈 技术趋势洞察

### 1. AI Agent 技能生态 — 绝对的 #1 主题
今天超过一半的 trending 项目跟 AI Agent 技能/插件有关：
- **技能库**：agent-skills, superpowers, claude-skills, dotnet/skills, last30days-skill
- **Agent 工具**：OfficeCLI, CubeSandbox, herdr, DesktopCommanderMCP
- **Agent 框架**：page-agent, codex-plugin-cc, agency-agents, orca
- **Agent 优化**：caveman（省 65% token）、SkillOpt

这说明 AI Agent 已经从"能用"阶段进入"好用"阶段，生态建设全面展开。

### 2. Rust 成为 Agent 基础设施首选语言
- **CubeSandbox**（腾讯的沙箱）用 Rust
- **RuView**（WiFi 感知）用 Rust
- **meetily**（会议助手）用 Rust
- **herdr**（Agent 多路复用器）用 Rust
- Rust 在安全、性能敏感的 Agent 底层设施中持续蚕食 C/C++ 地盘

### 3. AI 安全赛道起势
- **strix**（周增 10,274 星！）：AI 渗透测试工具
- **pentagi**：全自主 AI 渗透测试系统
- **CubeSandbox**：Agent 安全沙箱
- AI 红蓝对抗和自动化安全测试正在成为新热点

### 4. 本地/隐私优先的 AI 工具
- **meetily**：本地会议转录（不用云服务）
- **pocket-tts**：CPU 上跑的 TTS
- **immich**：自托管照片管理（持续霸榜）
- 隐私焦虑推动本地 AI 持续增长

### 5. MCP 协议生态扩张
Chrome DevTools MCP、DesktopCommander MCP、Google Analytics MCP……MCP 正在成为 Agent 与外部工具交互的事实标准。

---

## 💡 值得深挖 TOP 3

### 1. 🥇 usestrix/strix（周增 10,274 星）
**理由：** 本周最大黑马。AI 驱动的渗透测试工具，自动找漏洞并修复建议。  
**建议：** 赶紧 clone 研究！安全 + AI 的交叉点，做视频"AI 帮你做渗透测试"绝对有流量。

### 2. 🥈 JuliusBrussee/caveman（周增 8,080 星）
**理由：** Claude Code 技能，通过"说穴居人的话"节省 65% token。思路巧妙——压缩 prompt 而不是模型。  
**建议：** 研究它的压缩策略，看看能不能应用到自己的 Agent 工作流里省钱。

### 3. 🥉 alibaba/page-agent（周增 4,295 星）
**理由：** 阿里的 JS 网页 GUI Agent，用自然语言控制网页界面。RPA + AI Agent 的结合。  
**建议：** clone 试试，看看国产 Agent 方案的水平。可以跟自己用的工具做对比评测。

---

## 📅 周榜亮点

### 持续霸榜项目
- **obra/superpowers**：近 25 万星，Agent 技能框架稳坐头部
- **immich-app/immich**：10.7 万星，自托管照片管理持续受欢迎
- **msitarzewski/agency-agents**：12.9 万星，AI 代理公司模板

### 本周新晋黑马
- **usestrix/strix**（10,274/周）：AI 渗透测试，一周爆到 3.9 万星
- **JuliusBrussee/caveman**（8,080/周）：token 节省技能，一周涨到 8.7 万星
- **Zackriya-Solutions/meetily**（8,366/周）：本地 AI 会议助手，Rust 实现
- **facebook/astryx**（4,943/周）：Facebook 出的设计系统，Agent-ready

---

## 🎬 视频选题建议

### 选题 1：「AI Agent 技能大战：2026年最火的 5 个 Agent 插件」
**角度：** 盘点本周 Agent 技能/插件项目，对比各家方案的优劣，给观众一个"该装哪个"的指南。素材充足（agent-skills、superpowers、caveman、claude-skills）。

### 选题 2：「AI 帮你做黑客：strix 渗透测试工具实测」
**角度：** strix 一周涨了一万星，用 AI 做渗透测试听起来就很酷。实测一下它的能力边界，讲讲 AI 安全的机遇和风险。话题性强，容易上热门。

---

## 附：语言维度趋势

| 语言 | 热门方向 |
|------|---------|
| **Python** | Agent 技能（claude-skills, claude-video）、本地 TTS（pocket-tts）、小模型训练（minimind） |
| **TypeScript** | Agent 记忆（TencentDB-Agent-Memory）、GUI Agent（page-agent）、可观测性（SigNoz） |
| **Rust** | 安全沙箱（CubeSandbox）、WiFi 感知（RuView）、会议助手（meetily）、Agent 多路复用（herdr） |
| **Go** | 渗透测试 Agent（pentagi）、飞书 CLI（larksuite/cli）、K8s 部署（argo-cd） |

---

*报告由奴才自动生成 | 数据来源：GitHub Trending | 2026-07-09 09:00*
