# Hypervisor EPT Hook 与去虚拟化改进

**日期**: 2026-07-11 (周六)  
**项目**: hypervisor  
**本地提交**: 5 个新提交（总计 13 个待推送）

---

## 核心变更

### 1. EPT Bugcheck Hook 编译开关

新增 `HV_NO_ENTRY_HOOK` 编译时开关，控制 EPT bugcheck hook 的启用/禁用：

```rust
#[cfg(not(feature = "hv_no_entry_hook"))]
{
    // 安装 EPT-execute hook 到 nt!KeBugCheckEx
    install_ept_execute_hook(ke_bugcheck_ex_addr);
}
```

**提交**: `203799e` Add HV_NO_ENTRY_HOOK build gate to disable EPT bugcheck hook

### 2. CMOS 清除逻辑扩展

扩展 CMOS field 8 的清除逻辑，同时擦除：
- 冻结回调标记 (callback marker)
- 入口钩子标记 (entry-hook marker)

这样硬重启后不会误读旧的 hook 状态。

**提交**: `c1de4fb` Extend CMOS clear (field 8) to also wipe callback + entry-hook markers

### 3. EPT-Execute Hook 安装

直接安装 EPT-execute hook 到 `nt!KeBugCheckEx`：
- 当 EAC 触发 bugcheck 时，HV 可以拦截并观察
- 通过 `cpuid_ping` 工具显示 hook 状态

**提交**: 
- `c35eb61` Install EPT-execute hook on nt!KeBugCheckEx
- `cf686a5` cpuid_ping: display KeBugCheckEx entry-hook state

### 4. CMOS Field 10 修复

修复 CMOS field 10 的分发逻辑，正确路由到 `cmos_read_step4`：

**提交**: `e95ec6a` Fix CMOS field 10 dispatch to cmos_read_step4

---

## 其他改进（来自 Claude Code 对话）

以下改进在 7 月 11 日通过 Claude Code 完成，尚未推送到 GitLab：

- **CR8>=15 去虚拟化路径回滚**: 保留 WHEA 辅助解析，快速路径 CPUID 前填充 guest RSP/RFLAGS
- **停止 NMI 注入**: 不再向空闲 guest RIP 注入 NMI，减少异常开销
- **DEBUGCTL VMCS 路由**: guest DEBUGCTL 改为通过 VMCS 路由，不再直写裸硬件
- **LBR 冻结调整**: 先 revert 再重新实现 LBR 冻结逻辑

---

## 技术背景

这些改进是在 7 月 10 日完成 EAC 反检测全阶段（5/5 无冻结）之后的持续优化：

1. **EPT Hook 目的**: 拦截 EAC 触发的 `KeBugCheckEx`，观察 bugcheck 参数（如 0x139 = KERNEL_SECURITY_CHECK_FAILURE）
2. **CMOS 持久化**: 硬重启后保留调试信息，便于分析冻结根因
3. **NMI 优化**: 减少不必要的 VM-exit，降低被检测风险

## 下一步

- 推送 13 个本地提交到 GitHub
- 测试 EPT hook 在 EAC 环境下的实际表现
- 关注时序侧信道等更深层检测向量
