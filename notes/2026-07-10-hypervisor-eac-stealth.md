# Hypervisor EAC 反检测加固 - 全阶段完成

**日期**: 2026-07-10  
**项目**: hypervisor  
**里程碑**: 5/5 EAC 无冻结，HV 稳定存活 50+ 分钟

## 完成的工作

### P2 隐身拦截
- EFER/APERF/MPERF/LBR MSR 读取拦截与伪装
- 对 EAC 检测的 Model-Specific Registers 进行读取劫持，返回正常值

### P3.1 LBR 保护
- 每次 VM-exit 前后保存/恢复 Last Branch Record
- 隐藏宿主机分支预测痕迹，防止 EAC 通过 LBR 检测虚拟化

### P3.2 崩溃回调
- 注册 `KeBugCheckCallback`
- CMOS + RAM 面包屑持久化，蓝屏时保留调试信息

### P3.3 软 IDT 处理
- 为保留向量和外部向量注册默认 IDT handler
- 确保中断描述符表对 EAC 呈现正常状态

### P3.4 NMI 直通
- 放弃 NMI-exiting 模式
- 直接传递 Non-Maskable Interrupt 给客户机，减少 VM-exit 开销

## 稳定性修复
- 修复物理内存读取失败时的错误传播
- MXCSR 跨去虚拟化场景的保存/恢复
- VMX 抢占定时器启用

## Git 提交记录
- `3e0bf34` Check KeDeregisterBugCheckCallback return value
- `6a5e946` Surface physical-read failures; preserve MXCSR

## 备注
这是 EAC 反检测的完整方案落地，从 MSR 拦截到 NMI 直通全链路贯通。
后续可关注更深层的检测向量（如 timing side-channel）。
