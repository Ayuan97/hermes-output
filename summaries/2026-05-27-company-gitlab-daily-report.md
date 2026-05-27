# 2026-05-27 公司 GitLab 每日项目进度汇报（改进版）

- 统计窗口：2026-05-26 14:25 ~ 2026-05-27 14:25（北京时间）
- 统计口径：覆盖默认分支、dev/develop、feature/release/hotfix 等最近 72 小时活跃分支，并补充 MR / Issue / Pipeline。
- 扫描项目：60；有活动项目：8；有动作人员：13。

## 一句话结论
近 24 小时推进集中在 enginer/justus-content-core 等 5 个项目；存在 7 个风险需跟进。

## 项目看板
- **enginer/justus-content-core**｜分支：dev、feat/video-agent、feature/agent-billing-precheck、fix/dev-hank、dev-gq｜提交 38 / MR 6 / Issue 0 / Pipeline failed,success｜人员：guoqiang、guoqiang ton、hank、hank hank｜**需跟进 pipeline**
- **zhaowenlong/lnct-web**｜分支：dev、feat/seeding-note-workflow、feat/video-agent、dev-duouo、dev-duouo-v2｜提交 23 / MR 0 / Issue 0 / Pipeline canceled,failed,pending,running,success｜人员：hank、hd、lichengduo、wj｜**需跟进 pipeline**
- **root/whale-flow**｜分支：main｜提交 31 / MR 0 / Issue 0 / Pipeline 无｜人员：zhaowenlong｜**提交密集，注意验收节奏**
- **enginer/justuscut**｜分支：feat/video-agent、dev-gq、v3/dev、v3/dev-qh、v3/fix/dev-hank｜提交 7 / MR 2 / Issue 0 / Pipeline failed,success｜人员：hank、hank hank、qh、yuqiao.xu｜**需跟进 pipeline**
- **enginer/justus-web**｜分支：feat/video-agent、web-admin-v2｜提交 5 / MR 0 / Issue 0 / Pipeline 无｜人员：hank、yuqiao.xu｜**正常推进**
- **enginer/engine-image-generation**｜分支：main｜提交 2 / MR 0 / Issue 0 / Pipeline 无｜人员：guoqiang、赵华鹏｜**正常推进**
- **customers/duoyan-ai**｜分支：master｜提交 0 / MR 0 / Issue 0 / Pipeline 无｜人员：暂无｜**正常推进**
- **enginer/ln-agents**｜分支：v2/dev、v2/dev-hank｜提交 0 / MR 0 / Issue 0 / Pipeline 无｜人员：暂无｜**正常推进**

## 人员看板
- **zhaowenlong**｜提交 31 / MR 0 / Issue 0｜项目：root/whale-flow｜分支：root/whale-flow:main｜**推进很活跃，注意 review/验收**
- **hd**｜提交 17 / MR 0 / Issue 0｜项目：enginer/justus-content-core、zhaowenlong/lnct-web｜分支：enginer/justus-content-core:dev、enginer/justus-content-core:hd_dev、zhaowenlong/lnct-web:dev｜**推进很活跃，注意 review/验收**
- **hank**｜提交 11 / MR 0 / Issue 0｜项目：enginer/justus-content-core、enginer/justus-web、enginer/justuscut｜分支：enginer/justus-content-core:dev、enginer/justus-web:web-admin-v2、enginer/justuscut:dev-gq｜**正常推进**
- **zhaohua**｜提交 8 / MR 0 / Issue 0｜项目：enginer/justus-content-core、enginer/justuscut、zhaowenlong/lnct-web｜分支：enginer/justus-content-core:dev、enginer/justus-content-core:feature/agent-billing-precheck、enginer/justuscut:dev-gq｜**正常推进**
- **赵华鹏**｜提交 6 / MR 2 / Issue 0｜项目：enginer/engine-image-generation、enginer/justus-content-core、enginer/justuscut｜分支：enginer/engine-image-generation:未知分支(all=true)、enginer/justus-content-core:dev、enginer/justus-content-core:未知分支(all=true)｜**正常推进**
- **lichengduo**｜提交 7 / MR 0 / Issue 0｜项目：zhaowenlong/lnct-web｜分支：zhaowenlong/lnct-web:dev｜**正常推进**
- **huang huangd**｜提交 4 / MR 4 / Issue 0｜项目：enginer/justus-content-core｜分支：enginer/justus-content-core:未知分支(all=true)｜**正常推进**
- **hank hank**｜提交 4 / MR 2 / Issue 0｜项目：enginer/justus-content-core、enginer/justuscut｜分支：enginer/justus-content-core:dev、enginer/justus-content-core:未知分支(all=true)、enginer/justuscut:dev-gq｜**正常推进**
- **wj**｜提交 5 / MR 0 / Issue 0｜项目：zhaowenlong/lnct-web｜分支：zhaowenlong/lnct-web:dev-wj-workflow｜**正常推进**
- **yuqiao.xu**｜提交 4 / MR 0 / Issue 0｜项目：enginer/justus-content-core、enginer/justus-web、enginer/justuscut｜分支：enginer/justus-content-core:feat/video-agent、enginer/justus-web:feat/video-agent、enginer/justuscut:feat/video-agent｜**正常推进**
- **guoqiang**｜提交 4 / MR 0 / Issue 0｜项目：enginer/engine-image-generation、enginer/justus-content-core｜分支：enginer/engine-image-generation:main、enginer/justus-content-core:dev-gq｜**正常推进**
- **qh**｜提交 4 / MR 0 / Issue 0｜项目：enginer/justus-content-core、enginer/justuscut｜分支：enginer/justus-content-core:dev-qh、enginer/justuscut:v3/dev-qh｜**正常推进**
- 另有 1 人有动作，详见完整明细。

## 风险/阻塞
- 【高】enginer/justus-content-core pipeline failed（ref=refs/merge-requests/290/head）
- 【高】enginer/justus-content-core pipeline failed（ref=hd_dev）
- 【高】enginer/justus-content-core pipeline failed（ref=hd_dev）
- 【高】zhaowenlong/lnct-web pipeline canceled（ref=dev-wj-workflow）
- 【高】zhaowenlong/lnct-web pipeline canceled（ref=dev）

## 明日跟进
- 优先处理：enginer/justus-content-core pipeline failed（ref=refs/merge-requests/290/head）
- enginer/justus-content-core：MR 较活跃，安排 review/合并节奏。
- enginer/justus-content-core：提交密集，确认阶段验收和回归测试。
- zhaowenlong/lnct-web：提交密集，确认阶段验收和回归测试。
- root/whale-flow：提交密集，确认阶段验收和回归测试。

## 完整明细：活跃分支提交数
### enginer/justus-content-core
- dev: 20 commits
- feat/video-agent: 1 commits
- feature/agent-billing-precheck: 13 commits
- fix/dev-hank: 7 commits
- dev-gq: 19 commits
- dev-qh: 14 commits
- hd_dev: 22 commits
### zhaowenlong/lnct-web
- dev: 17 commits
- feat/video-agent: 1 commits
- dev-duouo: 13 commits
- dev-hank: 5 commits
- dev-hd: 15 commits
- dev-wj-workflow: 20 commits
- dev-zzz2: 15 commits
### root/whale-flow
- main: 31 commits
### enginer/justuscut
- feat/video-agent: 1 commits
- dev-gq: 3 commits
- v3/dev: 3 commits
- v3/dev-qh: 1 commits
- v3/fix/dev-hank: 1 commits
- v3/hd: 3 commits
### enginer/justus-web
- feat/video-agent: 1 commits
- web-admin-v2: 4 commits
### enginer/engine-image-generation
- main: 1 commits
### customers/duoyan-ai
- 无分支级提交，但存在 MR/Issue/Pipeline 活动。
### enginer/ln-agents
- 无分支级提交，但存在 MR/Issue/Pipeline 活动。

## 统计限制
- `all=true` 补充分支提交；若个别项目 API 不支持，会以活跃分支扫描结果为准。
