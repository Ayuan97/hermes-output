# ComfyUI 零基础使用教程

> 更新时间：2026-05-28  
> 说明：主子语音里说的“confake ui”，奴才按目前最可能的 **ComfyUI** 来研究。如果你说的是另一个工具，再告诉奴才名字，我再改。

## 1. ComfyUI 是什么

ComfyUI 是一个基于**节点工作流**的 AI 生成工具。它最早主要用于 Stable Diffusion 图片生成，现在也支持视频、3D、音频、LLM、商业 API 节点等。

你可以把它理解成：

- 普通画图软件：你点按钮，调几个参数；
- ComfyUI：你把“加载模型 → 写提示词 → 采样生成 → 解码图片 → 保存图片”这些步骤用节点连起来。

它的优点是：

- 可控性强：每一步都能看见、能改；
- 可复用：别人发给你的 workflow 图片，拖进去就能复现；
- 扩展性强：可以安装各种自定义节点；
- 适合复杂流程：LoRA、ControlNet、高清修复、换脸、产品图、视频生成等都能串起来。

缺点是：

- 初看比较吓人；
- 节点、模型路径、插件依赖容易让新手懵；
- 模型体系很多：SD1.5、SDXL、Flux、SD3、Qwen Image 等，混错会报错。

## 2. ComfyUI 和 Stable Diffusion WebUI / A1111 的区别

### A1111 / WebUI

适合：

- 刚开始玩图；
- 想要一个“表单式”的界面；
- 文生图、图生图、高清修复、ControlNet 用现成面板搞定。

特点：

- 上手快；
- 参数集中；
- 流程隐藏在后台；
- 复杂自动化不如 ComfyUI 灵活。

### ComfyUI

适合：

- 想精确控制流程；
- 想复用别人完整工作流；
- 想把多个模型、多个处理步骤串起来；
- 想做产品图、批量图、视频、复杂 ControlNet、局部重绘、高清放大。

特点：

- 上手慢一点；
- 但一旦理解节点，扩展能力更强；
- 官方示例图里带 workflow 元数据，拖进窗口就能复现。

一句话：

> A1111 像傻瓜相机，ComfyUI 像摄影棚里的线路板。新手先跑通模板，不要一开始自己手搓节点。

## 3. 安装方式怎么选

### 3.1 最推荐：ComfyUI Desktop

适合主子这种“先用起来”的场景。

官方下载：

- https://www.comfy.org/download

支持情况：

- Windows Desktop：适合 Windows + NVIDIA / AMD；
- macOS Desktop：目前主要支持 Apple Silicon，也就是 M 系列 Mac；
- Desktop 还是 Beta，但安装体验最简单。

优点：

- 像普通 App 一样安装；
- 自动配置 Python 和依赖；
- 可以导入已有 ComfyUI 设置、模型、workflow；
- 对新手最省心。

macOS 也可以用 Homebrew：

```bash
brew install comfyui
```

### 3.2 Windows Portable 便携版

适合：

- Windows 用户；
- 想用最新版；
- 不想污染系统 Python；
- 想整个文件夹搬来搬去。

官方 GitHub Release：

- https://github.com/comfyanonymous/ComfyUI/releases

下载后解压，常见结构：

```text
ComfyUI_windows_portable/
├── ComfyUI/
├── python_embeded/
├── update/
├── run_cpu.bat
└── run_nvidia_gpu.bat
```

NVIDIA 显卡双击：

```text
run_nvidia_gpu.bat
```

看到类似：

```text
To see the GUI go to: http://127.0.0.1:8188
```

就说明服务起来了。浏览器打开：

```text
http://127.0.0.1:8188
```

### 3.3 手动源码安装

适合：

- Linux；
- 需要定制环境；
- 已经熟悉 Python / venv / CUDA；
- 想跟最新代码。

大概流程：

```bash
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

Windows PowerShell 类似：

```powershell
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## 4. 第一次生成图片：最短上手流程

主子不要一开始自己建节点。按这个来：

### 第一步：启动 ComfyUI

打开 ComfyUI Desktop，或者启动 portable / 源码版。

进入：

```text
http://127.0.0.1:8188
```

### 第二步：加载官方模板

ComfyUI 通常会自动加载默认文生图工作流。如果没有：

```text
左侧 / 顶部菜单 → Templates / Workflow Templates → 找 Text to Image
```

也可以打开官方示例：

- https://docs.comfy.org/tutorials/basic/text-to-image
- https://comfyanonymous.github.io/ComfyUI_examples/

很多示例图片本身带 workflow 元数据，**直接拖进 ComfyUI 窗口**就能加载完整流程。

### 第三步：准备一个 checkpoint 模型

最基础 SD1.5 示例模型：

- `v1-5-pruned-emaonly-fp16.safetensors`

放到：

```text
ComfyUI/models/checkpoints/
```

如果是 Desktop 版，模型目录可能在 ComfyUI 设置里显示，或者通过界面下载/管理。

### 第四步：选择模型

在 `Load Checkpoint` 节点里选择模型，比如：

```text
v1-5-pruned-emaonly-fp16.safetensors
```

不要是 `null`。

### 第五步：写提示词

通常有两个 `CLIP Text Encode` 节点：

- Positive：你想要什么；
- Negative：你不想要什么。

示例：

Positive：

```text
a cinematic photo of a futuristic city at night, neon lights, rain, highly detailed, 4k
```

Negative：

```text
low quality, blurry, bad anatomy, text, watermark
```

SD1.5/SDXL 这类模型通常英文提示词效果更稳。

### 第六步：点 Queue

点击：

```text
Queue
```

或者快捷键：

```text
Ctrl + Enter
```

Mac 上一般是：

```text
Cmd + Enter
```

生成完会在 `Save Image` 节点看到图，输出文件默认在：

```text
ComfyUI/output/
```

## 5. 必须理解的节点概念

先记住这条主线：

```text
Load Checkpoint
  ↓
CLIP Text Encode 正向/反向提示词
  ↓
Empty Latent Image
  ↓
KSampler
  ↓
VAE Decode
  ↓
Save Image
```

### 5.1 Load Checkpoint

加载大模型，也就是“画师”。

输出通常有三个：

- `MODEL`：给 KSampler 用；
- `CLIP`：给提示词编码用；
- `VAE`：把 latent 解码成图片用。

### 5.2 CLIP Text Encode

把提示词变成模型能理解的条件。

一般有两个：

- positive：正向提示词；
- negative：反向提示词。

### 5.3 Empty Latent Image

生成一张“潜空间空画布”。

常见参数：

- width：宽度；
- height：高度；
- batch_size：一次生成几张。

SD1.5 常用：

```text
512 x 512
512 x 768
768 x 512
```

SDXL 常用：

```text
1024 x 1024
832 x 1216
1216 x 832
```

### 5.4 KSampler

最核心节点，负责采样生成。

常用参数：

- `seed`：随机种子。一样的 seed + 参数通常能复现相似结果；
- `steps`：步数。常见 20–35；
- `cfg`：提示词服从度。常见 5–8；
- `sampler_name`：采样器，例如 `euler`、`dpmpp_2m`；
- `scheduler`：调度器，例如 `normal`、`karras`；
- `denoise`：重绘强度。

`denoise` 很重要：

- 文生图：一般 `1.0`；
- 图生图：通常 `0.3–0.8`；
- 越低越像原图；
- 越高变化越大。

### 5.5 VAE Decode

把模型内部的 latent 图像解码成普通图片。

如果 VAE 和模型架构不匹配，会报各种维度错误。

### 5.6 Save Image

保存图片，也能在节点里预览结果。

## 6. 模型文件放哪里

以源码版 / portable 版为例，核心目录是：

```text
ComfyUI/models/
```

常用路径：

```text
ComfyUI/models/checkpoints/       # 大模型：SD1.5、SDXL checkpoint
ComfyUI/models/vae/               # VAE
ComfyUI/models/loras/             # LoRA
ComfyUI/models/controlnet/        # ControlNet
ComfyUI/models/upscale_models/    # 放大模型，例如 ESRGAN
ComfyUI/models/embeddings/        # textual inversion / embedding
ComfyUI/models/clip/              # CLIP 文本编码器，Flux/SD3 常用
ComfyUI/models/unet/              # 分离式 UNet / diffusion model
```

如果用的是 Flux / SD3 / Qwen Image 这类新模型，往往不是一个 checkpoint 文件搞定，而是会分成：

- diffusion model / unet；
- clip；
- t5 / text encoder；
- vae。

这时一定要用官方模板或模型作者提供的 ComfyUI workflow，不要乱拼。

## 7. 常用工作流

### 7.1 文生图 Txt2Img

用途：输入文字，生成图片。

核心节点：

```text
Load Checkpoint → CLIP Text Encode → Empty Latent Image → KSampler → VAE Decode → Save Image
```

关键参数：

- 模型：决定画风和能力；
- prompt：决定内容；
- seed：决定随机性；
- width/height：决定尺寸；
- steps/cfg：影响细节和稳定性。

### 7.2 图生图 Img2Img

用途：给一张图，让模型按提示词改风格、修复、重绘。

比文生图多了：

```text
Load Image → VAE Encode
```

关键参数：

- KSampler 的 `denoise` 必须小于 1；
- `0.2–0.4`：轻微变化；
- `0.5–0.7`：明显变化；
- `0.8+`：基本重画。

### 7.3 LoRA

用途：给基础模型加风格、人物、产品、服装、姿势等能力。

模型放到：

```text
ComfyUI/models/loras/
```

常用节点：

```text
Load LoRA
```

连接方式：

```text
Load Checkpoint 的 MODEL/CLIP
  ↓
Load LoRA
  ↓
KSampler / CLIP Text Encode
```

常见参数：

- `strength_model`：LoRA 对画面模型的影响强度；
- `strength_clip`：LoRA 对提示词理解的影响强度。

常用范围：

```text
0.5–1.0
```

多个 LoRA 可以串联，但越多越容易冲突。

### 7.4 ControlNet

用途：用参考图控制构图、姿势、边缘、深度、线稿。

常见类型：

- Canny：控制边缘；
- Depth：控制深度；
- OpenPose：控制人物姿势；
- Scribble：草图控制；
- Lineart：线稿控制。

注意：

- SD1.5 checkpoint 要配 SD1.5 ControlNet；
- SDXL checkpoint 要配 SDXL ControlNet；
- Flux / SD3 也要用对应体系的 ControlNet；
- ControlNet 经常需要预处理器，自定义节点常见是 `ComfyUI ControlNet aux`。

### 7.5 高清修复 / 二段生成

常见思路：

1. 先低分辨率生成；
2. latent upscale 或图片 upscale；
3. 再用 KSampler 低 denoise 精修；
4. 最后保存。

简单理解：

```text
先画草稿 → 放大 → 再细化
```

参数建议：

- 第一段：正常文生图；
- 放大倍率：1.5x / 2x；
- 第二段 denoise：`0.2–0.45`。

### 7.6 图片放大 Upscale

本地 AI 放大模型放到：

```text
ComfyUI/models/upscale_models/
```

常用节点：

```text
Load Upscale Model
Image Upscale With Model
```

常见模型来源：

- https://openmodeldb.info/

例如 ESRGAN / RealESRGAN 类模型。

### 7.7 导入别人 workflow

这是 ComfyUI 最好用的地方。

导入方式：

- 把带 workflow 元数据的图片拖进 ComfyUI；
- 或者菜单 `Workflows → Open` 打开 `.json`；
- 或者从 ComfyUI Examples 下载示例图。

官方示例：

- https://comfyanonymous.github.io/ComfyUI_examples/
- https://docs.comfy.org/tutorials/basic/text-to-image
- https://docs.comfy.org/tutorials/basic/image-to-image
- https://docs.comfy.org/tutorials/basic/lora
- https://docs.comfy.org/tutorials/controlnet/controlnet

导入后如果一堆红色报错，通常是：

- 缺模型；
- 缺自定义节点；
- 模型路径不对；
- workflow 用的是另一个模型体系。

## 8. 自定义节点和 Manager

### 8.1 ComfyUI Manager 是什么

ComfyUI Manager 是最常用的管理扩展，可以用来：

- 安装自定义节点；
- 启用/禁用节点；
- 安装缺失节点；
- 管理模型；
- 查看节点信息。

GitHub：

- https://github.com/ltdrdata/ComfyUI-Manager

官方文档：

- https://docs.comfy.org/manager/overview

### 8.2 安装 Manager

如果是普通源码/portable 版：

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager comfyui-manager
```

然后重启 ComfyUI。

Windows portable 也可以用它提供的 bat 安装脚本，但新手建议先看官方 README。

### 8.3 新手常用自定义节点

不要一次装一堆。建议用到再装。

常见：

- `ComfyUI-Manager`：管理器；
- `ComfyUI ControlNet Aux`：ControlNet 预处理；
- `rgthree-comfy`：界面和工作流增强；
- `ComfyUI Impact Pack`：检测、分割、修脸、工作流增强；
- `ComfyUI Essentials`：常用工具节点集合。

安全提醒：

- 自定义节点本质上是 Python 代码；
- 不要乱装来路不明节点；
- 重要环境先备份；
- 插件出错时先禁用最近安装的节点。

## 9. 常见错误和排查

### 9.1 `Value not in list: ckpt_name ... not in []`

意思：ComfyUI 没找到 checkpoint。

处理：

1. 确认模型放在：

```text
ComfyUI/models/checkpoints/
```

2. 刷新 ComfyUI；
3. 重启 ComfyUI；
4. 检查文件后缀是不是 `.safetensors` / `.ckpt`。

### 9.2 缺少自定义节点

表现：导入 workflow 后出现红色节点，提示节点不存在。

处理：

1. 安装 ComfyUI Manager；
2. 用 `Install Missing Custom Nodes`；
3. 重启 ComfyUI；
4. 再加载 workflow。

### 9.3 VAE / 模型架构不匹配

常见错误：

```text
expected input ... to have 4 channels, but got 16 channels
mat1 and mat2 shapes cannot be multiplied
```

原因：不同模型体系混用了。

例如：

- Flux 用了 SDXL VAE；
- SDXL checkpoint 配了 SD1.5 ControlNet；
- Flux 的 CLIP / T5 没按模板连接；
- SD3 / Flux / SD1.5 的节点混在一起。

处理：

- 用官方模板；
- 模型、VAE、CLIP、ControlNet 保持同一个家族；
- 先跑通官方示例，再替换模型。

### 9.4 显存不足 / CUDA out of memory

处理：

- 降低分辨率；
- 降低 batch size；
- 关掉其他占显存程序；
- 换 fp8 / quantized 模型；
- 用更小模型；
- 不要一次上 4K。

### 9.5 图片生成很慢

原因可能是：

- CPU 模式运行；
- 没用到 NVIDIA GPU；
- 模型太大；
- 分辨率太高；
- steps 太多；
- 第一次加载模型本来就慢。

处理：

- 看启动日志是否识别 GPU；
- Windows NVIDIA 用 `run_nvidia_gpu.bat`；
- steps 先设 20；
- 分辨率先 512 或 1024；
- 不要一开始跑视频模型。

### 9.6 workflow 导入后自动下载失败

处理：

- 手动看缺什么模型；
- 去 Hugging Face / Civitai 下载；
- 放到对应目录；
- 重启或刷新模型列表。

## 10. 新手建议参数

### SD1.5

```text
尺寸：512x512 / 512x768 / 768x512
steps：20–30
cfg：6–8
sampler：euler / dpmpp_2m
scheduler：normal / karras
denoise：文生图 1.0，图生图 0.3–0.7
```

### SDXL

```text
尺寸：1024x1024 / 832x1216 / 1216x832
steps：25–35
cfg：5–7
sampler：dpmpp_2m / dpmpp_sde
denoise：文生图 1.0，图生图 0.3–0.7
```

### LoRA

```text
strength_model：0.6–1.0
strength_clip：0.6–1.0
```

### 高清修复第二段

```text
upscale：1.5x–2x
denoise：0.2–0.45
steps：10–20
```

## 11. 主子的学习路线

### 第 1 天：只跑模板

目标：别管节点原理，先生成图。

做：

1. 安装 ComfyUI Desktop；
2. 打开默认 Text to Image 模板；
3. 放一个 SD1.5 或 SDXL checkpoint；
4. 改提示词；
5. 点 Queue；
6. 找到输出目录。

### 第 2 天：理解主链路

只理解这几个节点：

```text
Load Checkpoint
CLIP Text Encode
Empty Latent Image
KSampler
VAE Decode
Save Image
```

目标：能知道每个节点干嘛。

### 第 3 天：图生图

学习：

- Load Image；
- VAE Encode；
- KSampler 的 denoise。

目标：能用参考图改风格。

### 第 4 天：LoRA

学习：

- LoRA 放哪里；
- Load LoRA 怎么接；
- strength 怎么调。

目标：能套一个风格 LoRA。

### 第 5 天：ControlNet

学习：

- ControlNet 类型；
- 预处理器；
- 模型体系匹配。

目标：能用姿势/线稿控制构图。

### 第 6 天：高清修复

学习：

- upscale；
- 二段 KSampler；
- denoise 低强度精修。

目标：能从 1024 做到更高清。

### 第 7 天：导入别人 workflow

学习：

- 拖图导入；
- 安装缺失节点；
- 下载缺失模型；
- 改提示词和模型。

目标：能复用社区 workflow。

## 12. 主子可以先照这个最小实践

如果你现在就是想马上体验：

1. 安装 ComfyUI Desktop；
2. 打开默认 Text to Image；
3. 下载一个 SDXL checkpoint，放进 `models/checkpoints`；
4. 在 `Load Checkpoint` 选它；
5. Positive 写：

```text
a high quality cinematic photo of a Chinese businessman standing in a futuristic office, soft light, realistic, 4k
```

6. Negative 写：

```text
low quality, blurry, deformed, watermark, text
```

7. 点 `Queue`；
8. 去 `output` 目录看图。

## 13. 视频生成：关键帧、每帧图片和质量控制

ComfyUI 生成视频时，主子可以这么理解：

```text
视频质量 = 单帧画面质量 + 帧间一致性 + 运动自然度 + 后期放大/插帧质量
```

所以“先把关键帧或每一帧图片做好，再生成视频”，方向是对的，但要分清两种情况。

### 13.1 先生成关键帧，再生成视频：推荐

这是高质量 AI 视频最稳的路线之一。

典型流程：

```text
高质量首帧 / 关键帧
  ↓
图生视频 / 关键帧到视频
  ↓
插帧
  ↓
视频放大
  ↓
去闪烁 / 修脸 / 调色
```

为什么有效：

- 关键帧能锁定人物长相、产品外观、画风、光影和构图；
- 视频模型只需要负责“怎么动起来”；
- 比纯文生视频更稳定；
- 比每帧单独生成更不容易闪烁。

适合：

- 产品展示视频；
- 人物短镜头；
- 广告镜头；
- 动漫角色动效；
- 有明确起点/终点的镜头。

如果 workflow 支持 `Start Image` / `End Image` / `First Frame` / `Last Frame` / `Keyframe`，优先用这种关键帧控制方式。

### 13.2 每一帧都单独生成：理论强，实际难

理论上，每帧都先生成高清图片，再合成视频，单帧质量会很高。

但最大问题是：**帧与帧之间会闪。**

常见问题：

- 人脸每帧微变；
- 眼睛、手指、头发乱跳；
- 衣服纹理闪烁；
- 背景细节每帧不一样；
- 光影不连续；
- 合成后像“高质量 PPT 抖动”，不是自然视频。

所以视频不是“每张图好看”就够了，还要求：

```text
相邻帧之间稳定、连续、自然
```

如果确实要逐帧重绘，必须用结构控制，例如：

- 原视频抽帧；
- ControlNet Pose / Depth / Canny；
- 低 `denoise`；
- 固定 seed / 固定角色参考；
- 后期去闪烁。

### 13.3 最推荐的视频生产公式

对新手和实际出片来说，推荐这套：

```text
1. 先生成高质量关键帧
2. 用图生视频模型让画面动起来
3. 用插帧模型补到 24/30fps
4. 用视频放大提升分辨率
5. 最后做去闪烁、修脸、调色
```

不要一上来：

```text
一句提示词 → 10 秒高清视频
```

更稳的是：

```text
多个 2–5 秒短镜头 → 分别生成 → 剪辑合成
```

### 13.4 不同场景的做法

#### 人物视频

推荐：

```text
高质量人物首帧
→ 图生视频
→ 人脸修复 / 局部重绘
→ 插帧
→ 放大
```

重点：人物脸最怕逐帧漂移，不建议每帧自由生成。

#### 产品视频

推荐：

```text
高质量产品主图
→ 多角度关键帧
→ 关键帧到视频 / 图生视频
→ 放大
```

重点：产品外观必须稳定，关键帧比纯文生视频可靠很多。

#### 动漫 / 插画视频

推荐：

```text
角色设定图
→ LoRA / IPAdapter / 参考图保持角色
→ 图生视频
→ 插帧
→ 放大
```

重点：角色一致性比动作幅度更重要。

#### 真人视频转风格

推荐：

```text
原视频
→ 抽帧
→ Pose / Depth / Canny 控制
→ 低 denoise 重绘
→ 去闪烁
→ 合成视频
```

重点：不要每帧自由发挥，要用原视频结构约束。

### 13.5 ComfyUI 里常见对应节点

图生视频常见节点：

```text
Load Image
Image to Video Conditioning
Video Sampler / KSampler
VAE Decode
Video Combine / Save Video
```

关键帧控制常见节点名：

```text
Start Image
End Image
First Frame
Last Frame
Keyframe
```

插帧常见：

```text
RIFE
FILM
Frame Interpolation
```

视频放大常见：

```text
Video Upscale
Image Upscale With Model
Upscale Model Loader
```

### 13.6 参数建议

新手先从短视频开始：

```text
帧数：16–32
fps：8–12
分辨率：512x512 / 768x432 / 832x480
steps：15–25
```

如果图生视频有 `denoise`：

```text
0.2–0.4：轻微动，最稳
0.5–0.7：动作明显，但更容易变形
0.8+：接近重画，容易失控
```

最后再：

```text
插帧到 24/30fps
放大到目标分辨率
```

### 13.7 一句话原则

高质量 AI 视频不要追求“一次生成完”。更稳的是：

```text
先做高质量关键帧 → 再让视频模型补运动 → 最后插帧和放大
```

单帧质量决定上限，帧间一致性决定它像不像视频。

## 14. 来源链接

官方：

- ComfyUI 官网：https://www.comfy.org/
- ComfyUI 官方文档：https://docs.comfy.org/
- ComfyUI GitHub：https://github.com/comfyanonymous/ComfyUI
- ComfyUI Examples：https://comfyanonymous.github.io/ComfyUI_examples/
- First Generation 官方入门：https://docs.comfy.org/get_started/first_generation
- Text to Image：https://docs.comfy.org/tutorials/basic/text-to-image
- Image to Image：https://docs.comfy.org/tutorials/basic/image-to-image
- LoRA：https://docs.comfy.org/tutorials/basic/lora
- ControlNet：https://docs.comfy.org/tutorials/controlnet/controlnet
- Upscale：https://docs.comfy.org/tutorials/basic/upscale
- Model troubleshooting：https://docs.comfy.org/troubleshooting/model-issues
- ComfyUI Manager：https://github.com/ltdrdata/ComfyUI-Manager

## 15. 奴才一句话建议

主子别从“学节点”开始，先从“跑官方模板 + 拖别人 workflow”开始。等能稳定出图，再学 `KSampler`、`denoise`、`LoRA`、`ControlNet`。ComfyUI 的学习关键不是背节点，而是知道一条工作流里每一步的输入输出。