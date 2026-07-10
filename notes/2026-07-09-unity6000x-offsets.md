# Unity 6000.x 偏移适配笔记

**日期**: 2026-07-09  
**项目**: rust-cheating  
**提交数**: 34 次  
**触发原因**: 游戏版本更新（Unity 引擎升级到 6000.x），导致大量硬编码偏移失效

---

## 核心变更

### 1. Transform 链读取逻辑重写

Unity 6000.x 的 Transform 结构发生了变化，不再直接通过 `visual_state` 偏移获取位置，需要遍历 hierarchy chain：

```
go pointer → hierarchy chain → TransformData → 位置数据
```

关键偏移：
- `go + 0x18` → component 指针
- `comp + 0x08` → TransformData 指针
- `TransformData + 0xB8` → 资源位置（resource position）

**修复方法**: 重写 `resolve_vis_ptr` 函数，同时支持新旧两种 Transform 链结构。

### 2. PlayerModel 偏移更新

| 项目 | 旧值 | 新值 |
|------|------|------|
| PlayerModel 偏移 | 0x508 | 0x3D8 |
| Pose 偏移 | +0 | +8 shift |
| PlayerModel pos | — | 0x1F8 |

### 3. CULL_MASK_OFF 修正

地形移除功能的 culling mask 偏移：
- 旧值: `0x43C`
- 新值: `0x42C`

### 4. static_fields 偏移探测

`static_fields` 偏移不再固定，采用动态探测方式：
```rust
// 探测范围: 0xB8..0xE0
let offset = probe_static_fields(base_addr, 0xB8, 0xE0);
```

### 5. 偏移集中管理

将所有硬编码偏移迁移到 `offsets.rs`，便于后续版本更新时快速修改：
- 游戏对象偏移
- 组件指针偏移
- TransformData 偏移
- 解密相关偏移

---

## 资源类修复

矿石、大麻等资源的位置获取依赖 TransformData，修复后从 `TransformData + 0xB8` 读取。

## 解密路径清理

- 移除了已废弃的 LP decrypt 路径
- 改用 direct wrapper deref + camera inference
- 眼睛/背包解密添加 `decrypt_value` 支持 inline HiddenValue

---

## 诊断方法总结

适配过程中使用的诊断手段（可供后续版本更新参考）：

1. **内存扫描**: 在 `vis+0x00..0xFF` 范围扫描坐标样浮点数
2. **层级遍历**: 从 game object 指针逐级遍历到 TransformData
3. **多偏移尝试**: 同时扫描多个候选偏移，匹配已知坐标值
4. **条件日志**: 仅在 `diag` feature 开启时输出诊断日志
5. **实体校验**: 读取前校验 entity klass，丢弃陈旧 name cache

---

## 提交记录（关键节点）

| 提交 | 说明 |
|------|------|
| `55317a0` | 偏移集中到 offsets.rs + 7/8 补丁更新 |
| `733ec0a` | 重写 resolve_vis_ptr 支持双 Transform 链 |
| `8b6cf4e` | 添加 TransformData 间接寻址 |
| `564a115` | PlayerModel 偏移 0x508→0x3D8 + 硬编码集中 |
| `45d5395` | Pose 偏移 +8 shift 修正 |
| `7d2320e` | 资源位置从 TransformData+0xB8 读取 |
| `f987c67` | CULL_MASK_OFF 0x43C→0x42C |
| `49e740f` | 清理废弃 LP decrypt 路径 |
