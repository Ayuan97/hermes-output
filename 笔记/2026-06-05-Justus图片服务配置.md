# Justus 图片生成服务配置

> 日期：2026-06-05

## 服务信息

| 配置项 | 值 |
|--------|-----|
| 服务地址 | `http://47.245.107.22:9001` |
| API Key | `zhaochengyuan` |
| 管理员账号 | `admin` |
| 管理员密码 | `zhaochengyuan` |
| 数据库端口 | `16033` |
| 数据库用户 | `image_gateway` |
| 数据库密码 | `MyYpH2xA537SKYGy` |
| OSS Bucket | `justus` |
| OSS域名 | `https://justus.oss-cn-shanghai.aliyuncs.com` |

## 调用示例

```bash
# 同步生成
curl -X POST http://47.245.107.22:9001/generate \
  -H "Authorization: Bearer zhaochengyuan" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "你的提示词", "aspect_ratio": "16:9"}'

# 异步生成
curl -X POST http://47.245.107.22:9001/generate/async \
  -H "Authorization: Bearer zhaochengyuan" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "你的提示词"}'
```

## 测试结果
- HTTP 状态码：200
- 生成耗时：~12秒
- 使用模型：`gemini-3.1-flash-image-preview`
- 中转站：`sudocode`

## 技能文件
已创建 `justus-image-gen` 技能，包含调用脚本 `scripts/generate.sh`
