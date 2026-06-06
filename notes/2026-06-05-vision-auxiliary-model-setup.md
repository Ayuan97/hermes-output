# 辅助 Vision 模型配置

> 日期：2026-06-05

## 问题
主模型 `mimo-v2.5-pro` 是纯文本推理模型，不支持图片输入。`computer_use` 截图后需要 vision 模型分析图片。

## 解决方案
配置辅助 vision 模型，Hermes 自动将截图路由到辅助模型分析：

```bash
hermes config set auxiliary.vision.model mimo-v2-omni
```

## 当前架构
- **主模型**：`mimo-v2.5-pro`（纯文本推理，负责对话）
- **辅助 vision**：`mimo-v2-omni`（多模态，专门看图/截图）
- computer_use 截图 → 自动路由到 mimo-v2-omni 分析 → 返回文字描述给主模型

## 注意事项
- 需要 `/reset` 新会话后生效
- 代码里小米的 vision 模型映射默认写的是 `mimo-v2.5`，需要手动改为 `mimo-v2-omni`
