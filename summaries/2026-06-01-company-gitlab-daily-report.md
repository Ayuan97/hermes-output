📅 2026-06-01 · whale-flow 引擎大面积重构，lnct-web CI 部署链路迁移

【项目】
whale-flow：全仓 silentFail 容错加固（400+ 异常路径覆盖 daemon/agent/run/workspace/memory/trust/wealth/skill 等全部核心模块）；巨型 methods.ts 拆分为 11 个领域子模块（27 个 RPC 迁移完成）；ENGINE_CONFIG 环境变量统一接入 22+ 配置项；建成 5 路 run-end-distill 蒸馏探测器并接通 workspace 权重/阈值；shell/notes/todo/video/memory/opencli 等 30+ 工具统一加 businessOk 透传与异常兜底；修复 composer break 致 0 工具调用（P0）、daemon fire-and-forget 真并行调度、首-run bootstrap 永久休眠等关键缺陷；reasoning text 透传、prompt 组装优化、SQLite WAL 显式配置、工具反馈第三档检测等基础能力补全
lnct-web：CI 部署链路从 staging 迁移到 prod-tx，删除 staging 环境配置

【提交排行】
🥇 zhaowenlong：87 次提交 / +5156 -1985
🥈 Administrator：2 次提交 / +82 -120
