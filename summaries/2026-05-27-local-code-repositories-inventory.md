# 2026-05-27 本机代码仓库清单

扫描范围：

- `/Users/administer/Desktop/go`
- `/Users/administer/Desktop/php`
- `/Users/administer/Desktop/赵程远`
- `/Users/administer/Documents`
- `/Users/administer/clawd`

共发现 Git 仓库：32 个。

## 公司业务仓库 / GitLab

### Justus / 内容生产相关

- `justus-content-core`
  - 路径：`/Users/administer/Desktop/go/justus-content-core`
  - 远程：`git@gitlab.e-idear.com:enginer/justus-content-core.git`
  - 分支：`master`
  - 语言：Go 为主
  - 状态：有本地改动
  - 用途：Content 业务模块独立仓库，内容域核心业务实现。

- `justus/justus-content-core`
  - 路径：`/Users/administer/Desktop/go/justus/justus-content-core`
  - 远程：`git@gitlab.e-idear.com:enginer/justus-content-core.git`
  - 分支：`dev`
  - 语言：Go 为主
  - 状态：干净
  - 用途：同一项目的开发分支工作区。

- `justus/justus-go`
  - 路径：`/Users/administer/Desktop/go/justus/justus-go`
  - 远程：`git@gitlab.e-idear.com:enginer/justuscut.git`
  - 分支：`v3/dev`
  - 语言：Go 为主
  - 状态：干净
  - 用途：Justuscut 宿主仓，业务接口、领域逻辑、服务端实现。

- `justus/justus-web`
  - 路径：`/Users/administer/Desktop/go/justus/justus-web`
  - 远程：`git@gitlab.e-idear.com:enginer/justus-web.git`
  - 分支：`web-admin-v2`
  - 语言：TypeScript / React / Monorepo
  - 状态：干净
  - 用途：Justus 前端管理端，基于 Vue Vben Admin / pnpm monorepo。

- `justus/ln-agents`
  - 路径：`/Users/administer/Desktop/go/justus/ln-agents`
  - 远程：`git@gitlab.e-idear.com:enginer/ln-agents.git`
  - 分支：`v2/master`
  - 语言：Python 为主
  - 状态：干净
  - 用途：基于 Pydantic AI 的多模态 Agent 服务。

- `justus/lnct-web`
  - 路径：`/Users/administer/Desktop/go/justus/lnct-web`
  - 远程：`git@gitlab.e-idear.com:zhaowenlong/lnct-web.git`
  - 分支：`dev-ay`
  - 语言：TypeScript / Monorepo
  - 状态：干净
  - 用途：公司前端 monorepo 项目。

- `gemini_image_auto-code`
  - 路径：`/Users/administer/Desktop/go/justus/gemini_image_auto-code`
  - 远程：`git@gitlab.e-idear.com:enginer/engine-image-generation.git`
  - 分支：`main`
  - 语言：Go + Vue/TypeScript
  - 状态：干净
  - 用途：图片生成调度服务，多中转站、多模型统一接入、调度和管理。

- `justus-prompt`
  - 路径：`/Users/administer/Desktop/php/justus-prompt`
  - 远程：`git@gitlab.e-idear.com:enginer/justus-prompt.git`
  - 分支：`master`
  - 语言：PHP / Laravel
  - 状态：干净
  - 用途：Prompt / Laravel Web 项目。

### OA / 内部系统

- `oa-go`
  - 路径：`/Users/administer/Desktop/go/oa-go`
  - 远程：`git@gitlab.e-idear.com:root/oa-go.git`
  - 分支：`main`
  - 语言：Go
  - 状态：干净
  - 用途：OA 后端服务。

- `oa-new`
  - 路径：`/Users/administer/Desktop/go/oa-new`
  - 远程：`git@gitlab.e-idear.com:root/oa-new.git`
  - 分支：`main`
  - 语言：Go + TypeScript + Python
  - 状态：干净
  - 用途：新 OA 多模块项目，包含 CLI、Go 服务、Runner、文档和前端。

### AI / Agent / 自动化

- `ai_ads`
  - 路径：`/Users/administer/Desktop/go/ai_ads`
  - 远程：`git@gitlab.e-idear.com:root/ai_ads.git`
  - 分支：`teams`
  - 语言：Python
  - 状态：有本地改动
  - 用途：AI 广告投放/团队 Agent 相关项目。

- `boss-agi`
  - 路径：`/Users/administer/Desktop/go/boss-agi`
  - 远程：`git@gitlab.e-idear.com:enginer/boss-agi.git`
  - 分支：`v2`
  - 语言：Python + Markdown + Vue
  - 状态：有本地改动
  - 用途：AGI / CLI 沙箱 / 种子记忆 / 自进化相关项目。

- `whale-flow`
  - 路径：`/Users/administer/Desktop/go/whale-flow`
  - 远程：`git@gitlab.e-idear.com:root/whale-flow.git`
  - 分支：`main`
  - 语言：Markdown + JavaScript + TypeScript + Python
  - 状态：有本地改动
  - 用途：工作流 / Agent / SOP / 引擎相关项目。

- `claude_proxy`
  - 路径：`/Users/administer/Desktop/go/claude_proxy`
  - 远程：`git@gitlab.e-idear.com:root/claude_proxy.git`
  - 分支：`main`
  - 语言：Go + TypeScript + Rust
  - 状态：有本地改动
  - 用途：Claude 代理、后端、管理端、打包相关项目。

### 爬虫 / 小红书 / 广告系统

- `crawler-server`
  - 路径：`/Users/administer/Desktop/go/crawler-server`
  - 远程：`git@gitlab.e-idear.com:enginer/crawler-server.git`
  - 分支：`master`
  - 语言：Go
  - 状态：干净
  - 用途：多个平台数据抓取服务。

- `xhs/crawler-server`
  - 路径：`/Users/administer/Desktop/go/xhs/crawler-server`
  - 远程：`git@gitlab.e-idear.com:enginer/crawler-server.git`
  - 分支：`master`
  - 语言：Go
  - 状态：干净
  - 用途：crawler-server 的另一份工作区。

- `xhs/cloud-phone-env-forge`
  - 路径：`/Users/administer/Desktop/go/xhs/cloud-phone-env-forge`
  - 远程：`git@gitlab.e-idear.com:enginer/xhsapp/cloud-phone-env-forge.git`
  - 分支：`main`
  - 语言：Python
  - 状态：干净
  - 用途：小红书 App 设备参数提取、云手机环境配置相关工具。

- `ln-xhs`
  - 路径：`/Users/administer/Desktop/go/ln-xhs`
  - 远程：无
  - 分支：`master`
  - 语言：Python + JSON
  - 状态：有本地改动
  - 用途：AI 广告投放员工系统，商品分析、广告创建、监控、优化、扩量。

### 其他公司/工具仓库

- `ares`
  - 路径：`/Users/administer/Desktop/go/ares`
  - 远程：`git@gitlab.e-idear.com:root/ares.git`
  - 分支：`master`
  - 语言：Go
  - 状态：干净
  - 用途：Go 基础包，如 HTTP/流式请求等。

- `win`
  - 路径：`/Users/administer/Desktop/go/win`
  - 远程：`git@gitlab.e-idear.com:enginer/app/oceanEngineManager.git`
  - 分支：`dev-v3-react`
  - 语言：Go + JavaScript/React
  - 状态：有本地改动
  - 用途：Wails / Ocean Engine Manager 类桌面或管理工具。

## 个人 GitHub / 研究项目

- `DMA`
  - 路径：`/Users/administer/Desktop/go/DMA`
  - 远程：`git@github.com:Ayuan97/DMA.git`
  - 分支：`main`
  - 语言：Markdown
  - 状态：干净
  - 用途：PCIe DMA / IOMMU / VT-d 硬件安全研究笔记。

- `VTD`
  - 路径：`/Users/administer/Desktop/go/VTD`
  - 远程：`git@github.com:Ayuan97/VTD.git`
  - 分支：`main`
  - 语言：Markdown
  - 状态：干净
  - 用途：Windows VT-d / IOMMU 内核机制系统学习项目。

- `boss`
  - 路径：`/Users/administer/Desktop/go/boss`
  - 远程：`git@github.com:Ayuan97/atlas.git`
  - 分支：`main`
  - 语言：Python + Markdown
  - 状态：干净
  - 用途：Atlas / Boss，自成长 AI 助理、终端和 Web 形态。

- `buff-go`
  - 路径：`/Users/administer/Desktop/go/buff-go`
  - 远程：`ssh://git@github.com:Ayuan97/buff-go.git`
  - 分支：`dev`
  - 语言：Go
  - 状态：有本地改动
  - 用途：BUFF / Steam 相关数据或交易工具。

- `lover-order`
  - 路径：`/Users/administer/Desktop/go/lover-order`
  - 远程：`git@github.com:Ayuan97/lover-order.git`
  - 分支：`master`
  - 语言：Go + Swift
  - 状态：干净
  - 用途：后端 + iOS 项目。

- `hermes-output`
  - 路径：`/Users/administer/Desktop/go/hermes-output`
  - 远程：`git@github.com:Ayuan97/hermes-output.git`
  - 分支：`main`
  - 语言：Markdown
  - 状态：干净
  - 用途：Hermes 输出仓库，保存教程、总结、规划、资料。

- `interview-prep`
  - 路径：`/Users/administer/Desktop/赵程远/interview-prep`
  - 远程：`git@github.com:Ayuan97/solo.git`
  - 分支：`main`
  - 语言：Markdown
  - 状态：干净
  - 用途：面试与技术学习仓库，围绕简历技术栈和项目深度说明。

- `AsrTools`
  - 路径：`/Users/administer/Desktop/go/AsrTools`
  - 远程：`ssh://git@github.com:WEIFENG2333/AsrTools.git`
  - 分支：`main`
  - 语言：Python + Go
  - 状态：有本地改动
  - 用途：ASR / 字幕相关工具，上游项目。

- `openhuman`
  - 路径：`/Users/administer/Desktop/go/openhuman`
  - 远程：`git@github.com:tinyhumansai/openhuman.git`
  - 分支：`main`
  - 语言：Rust + TypeScript + React
  - 状态：干净
  - 用途：开源 openhuman 项目，上游/外部项目。

## 本地/无远程/待确认项目

- `clawd`
  - 路径：`/Users/administer/clawd`
  - 远程：无
  - 分支：`master`
  - 语言：Markdown + Python
  - 状态：有本地改动
  - 用途：本地 agent/记忆/工具/技能实验目录。

- `Documents/New project`
  - 路径：`/Users/administer/Documents/New project`
  - 远程：无
  - 分支：`master`
  - 语言：未识别
  - 状态：干净
  - 用途：空仓或未初始化内容。

- `Documents/New project 2`
  - 路径：`/Users/administer/Documents/New project 2`
  - 远程：无
  - 分支：`master`
  - 语言：未识别
  - 状态：干净
  - 用途：空仓或未初始化内容。

## 有本地未提交改动的仓库

- `AsrTools`
- `ai_ads`
- `boss-agi`
- `buff-go`
- `claude_proxy`
- `justus-content-core`（`/Users/administer/Desktop/go/justus-content-core`）
- `ln-xhs`
- `whale-flow`
- `win`
- `clawd`

## 重复/多工作区仓库

- `justus-content-core`
  - `/Users/administer/Desktop/go/justus-content-core`：`master`，有本地改动
  - `/Users/administer/Desktop/go/justus/justus-content-core`：`dev`，干净

- `crawler-server`
  - `/Users/administer/Desktop/go/crawler-server`
  - `/Users/administer/Desktop/go/xhs/crawler-server`

## 初步分类建议

- **公司主线业务**：`justus-content-core`、`justus-go`、`justus-web`、`ln-agents`、`lnct-web`、`engine-image-generation`
- **公司内部系统**：`oa-go`、`oa-new`、`ares`
- **AI/Agent 实验与产品化**：`boss`、`boss-agi`、`whale-flow`、`ai_ads`、`claude_proxy`、`clawd`
- **爬虫/广告/小红书**：`crawler-server`、`cloud-phone-env-forge`、`ln-xhs`
- **安全研究/学习**：`DMA`、`VTD`
- **个人输出/知识库**：`hermes-output`、`interview-prep`
- **外部参考项目**：`AsrTools`、`openhuman`

## 下一步建议

1. 先处理有本地改动的 10 个仓库，确认哪些需要提交、哪些是临时文件。
2. 合并或标注重复工作区，尤其是 `justus-content-core` 和 `crawler-server`。
3. 为每个公司主线项目补一份简短 `项目说明 / 当前分支用途 / 负责人 / 部署方式`。
4. 可以建立一个固定仓库索引文件，后续每日 GitLab 日报、项目巡检都基于这个索引做重点过滤。
