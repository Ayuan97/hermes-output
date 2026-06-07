# 米家接入 Apple Home / HomeKit / Home Assistant 调研方案

> 适用场景：家里已有大量米家设备，平时主要用米家 App 控制；希望后续能接入 Apple Home（家庭 App / Siri / HomePod）或 Home Assistant，实现更统一、更自动化的智能家居控制。
>
> 结论先行：如果设备很多且品牌混杂，推荐走 **Home Assistant 作为中枢**；如果只想让少量设备进 Apple Home，优先买/换 **原生 HomeKit 或 Matter 设备/网关**；如果只想低成本桥接米家到 Apple Home，可以考虑 **HomeBridge**，但长期维护性不如 Home Assistant。

---

## 1. 先分清几个概念

### 1.1 米家 App

米家是小米 IoT 生态的控制入口。设备可能来自：

- 小米 / 米家 Wi-Fi 设备：灯、插座、空气净化器、扫地机等。
- Zigbee / BLE 子设备：门窗传感器、人体传感器、温湿度计、开关等，需要网关。
- Aqara / 绿米设备：部分可同时支持米家、Aqara Home、Apple HomeKit。
- 新设备：部分开始支持 Matter。

### 1.2 Apple Home / HomeKit

Apple Home 是苹果家庭 App，底层常说 HomeKit。优点是：

- Siri / HomePod / iPhone / Apple Watch 控制体验好。
- 本地控制体验通常稳定。
- 家庭成员权限和自动化比较舒服。

限制是：

- 不是所有米家设备都能原生进 Apple Home。
- 需要设备本身支持 HomeKit / Matter，或者通过桥接器转进去。

### 1.3 Home Assistant

Home Assistant（HA）是开源智能家居中枢，适合把米家、Apple Home、Aqara、Matter、Zigbee、蓝牙、MQTT 等统一起来。

它可以做两件事：

1. **接入米家设备**：从米家生态把设备拉进 HA。
2. **暴露给 Apple Home**：通过 HA 内置 HomeKit Bridge，把 HA 里的设备桥到 Apple Home。

所以典型链路是：

```text
米家设备 → Home Assistant → HomeKit Bridge → Apple Home / Siri / HomePod
```

---

## 补充：小米智能家居的大模型 / AI Agent 新进展

主子问到“米家以前基本是规则驱动，现在大模型这么火，小米有没有模型相关的智能家居内容”。目前能看到的关键进展有三层：

### 1. 超级小爱：从语音助手升级成系统级 Agent

小米近年的方向不是只做“如果 A 就 B”的规则自动化，而是把小爱同学升级为更强的系统级助手：

- 手机、平板、电视、音箱、车机等终端逐步接入大模型能力。
- HyperOS / 澎湃 OS 上的“超级小爱”开始承担跨应用理解、问答、摘要、写作、图片处理、设备控制等任务。
- DeepSeek-R1 等推理模型能力也被接入到系统助手场景，用于更复杂的推理、写作和问答。

但这部分更偏“个人智能助手 / 系统 Agent”，不是专门针对家庭自动化的完整替代方案。

### 2. Xiaomi Miloco：小米智能家居 AI 最值得关注的项目

官方项目：<https://github.com/XiaoMi/xiaomi-miloco>

小米在 2025 年开源了 **Xiaomi Miloco / Xiaomi Local Copilot**，这是目前最贴近“智能家居大模型化”的动作。

官方 README 对它的定位是：

```text
以米家摄像机为视觉信息来源，以自研大模型为核心，打通全屋 IoT 设备。
基于大模型的开发范式，让用户能够以自然语言定义家庭的各种需求和规则。
```

核心点：

- **自然语言定义规则**：不再只靠手工 if-this-then-that，而是让用户用自然语言描述家庭需求。
- **端侧大模型**：使用小米自研 `Xiaomi MiMo-VL-Miloco-7B`，把家庭任务拆成“规划 + 视觉理解”。
- **摄像头作为感知入口**：用米家摄像头数据理解家庭场景事件。
- **打通米家生态**：支持获取/执行米家设备和米家场景，也能发送米家通知。
- **隐私方向**：强调端侧视频理解，减少家庭视觉数据上云。

和传统米家规则的区别：

| 传统米家自动化 | Xiaomi Miloco 方向 |
|---|---|
| 用户手动设置触发条件和动作 | 用户用自然语言描述需求 |
| 主要依赖传感器状态 | 摄像头视觉 + 大模型理解场景 |
| 规则固定，难处理模糊场景 | 模型可以做意图理解和场景推理 |
| 适合简单联动 | 目标是复杂家庭需求/多设备协同 |

重要限制：

- 目前更像“未来探索 / 开发者项目”，不是普通用户在米家 App 里一键启用的成熟功能。
- 依赖摄像头视觉场景，无摄像头或不愿摄像头参与的家庭收益有限。
- 本地跑模型有硬件要求：官方 README 写到需要 x64、NVIDIA 30 系及以上显卡，显存最低 8GB、建议 12GB+；Windows 需要 WSL2；macOS 暂不支持。
- 它目前不能简单理解成“买个小爱音箱就自动拥有家庭大模型”。

#### 主子的本机能不能跑 Xiaomi Miloco

主子的当前机器是 **Mac mini / Apple M4 / 16GB 统一内存 / 10 核 Apple GPU / macOS 15.5**。按小米官方要求判断：

- **不能直接跑完整 Xiaomi Miloco AI Engine**：官方 AI Engine 要求 x64 + NVIDIA 30 系及以上显卡 + CUDA + NVIDIA Container Toolkit；macOS 标注为暂不支持。
- **Apple M4 的 GPU 不等于 NVIDIA CUDA 显卡**：Miloco 的 Docker GPU 路线走 CUDA，Apple Metal 不能直接替代。
- **主服务可能能在 macOS Docker 上跑一部分**：官方环境文档提到 macOS 主服务和 Docker 网络桥接问题，但 AI Engine 仍然不支持 macOS，所以不能视为完整可用。
- **单独体验模型有探索空间**：`Xiaomi MiMo-VL-Miloco-7B-GGUF` 是量化 GGUF 版本，理论上可尝试用支持 Metal 的 `llama.cpp` 类工具在 M4 上加载做离线测试；但这不等于完整 Miloco 智能家居系统，视频流、米家设备执行、规划模型联动都需要额外适配。

结论：这台 M4 Mac mini **不适合作为 Miloco 完整部署机器**。如果要完整跑，优先准备一台 **Ubuntu / Windows WSL2 + NVIDIA RTX 3060 12GB、RTX 4060 Ti 16GB、RTX 4070 12GB 或更高** 的主机。

### 3. Home Assistant 也在走本地 LLM / Assist 路线

如果主子要的是“可控、可折腾、能把米家和大模型结合起来”，Home Assistant 反而是近期最实际的路线之一。

可用方向：

- HA 的 Assist 语音助手。
- 接 Ollama / OpenAI / Anthropic / Gemini 等模型。
- 本地模型理解自然语言，再调用 HA 里的设备和自动化。
- 米家设备先通过 Xiaomi Home / Xiaomi Miot Auto 接进 HA，再让 HA 的 LLM/Assist 调用。

链路可以是：

```text
米家设备 → Home Assistant → Assist / LLM Agent → 自动化 / Apple Home
```

这条路线对主子更现实，因为它不等小米把所有功能产品化；只要米家设备能进 HA，就能开始用模型做自然语言控制和自动化编排。

### 4. 奴才判断

小米确实已经在做“模型驱动智能家居”，最关键的是 **Xiaomi Miloco**，但现在还偏开发者和探索项目；普通家庭真正落地，短期还是建议：

```text
Home Assistant 接入米家 → 再接 HA Assist / 本地 LLM → 稳定设备桥到 Apple Home
```

后续如果小米把 Miloco 能力整合进米家 App / 小米中枢网关 / 小爱音箱，那才会从“规则驱动”真正进入“意图驱动”。

---

## 2. 主流路线对比

### 路线 A：设备原生支持 HomeKit / Matter

这是最省心路线。

```text
设备 / 网关 → Apple Home
```

适合：

- 新买设备。
- 设备本身有 HomeKit 二维码。
- Aqara M2 / M3 这类 HomeKit 网关。
- 明确支持 Matter 的新设备。

优点：

- 稳定、省心。
- 不需要额外服务器。
- Siri / Apple Home 体验最好。

缺点：

- 旧米家设备大多不支持。
- 米家 App 里能用，不代表 Apple Home 里能用。
- Matter 目前在米家生态里覆盖还不算完整。

适合主子家的用法：

- 后续新买设备时优先选支持 HomeKit / Matter 的型号。
- 现有大量米家旧设备不要指望这条路线一次性解决。

---

### 路线 B：Home Assistant + 小米官方 Xiaomi Home 集成

官方项目：

- GitHub：<https://github.com/XiaoMi/ha_xiaomi_home>

特点：

- 小米官方出的 Home Assistant 集成。
- 通过米家账号 OAuth 登录。
- 覆盖面理论上会越来越好。
- 支持云端控制；本地控制依赖小米中枢网关或设备内置中枢能力。

官方 README 里提到：

- 本地模式由 **Xiaomi Central Hub Gateway / 小米中枢网关** 或内置中枢能力设备实现。
- 中枢网关需要对应固件版本。
- 海外环境/设备区域会影响能力。

优点：

- 官方维护，未来潜力最大。
- 不需要自己找 token。
- 对普通用户更友好。

缺点：

- 很多情况下仍依赖云端。
- 本地控制要求中枢网关/固件/设备支持。
- 相比老社区插件，部分细节和兼容性还在发展。

推荐程度：**建议重点关注，作为未来主路线候选。**

适合主子家的用法：

- 如果准备长期搭 HA，官方 Xiaomi Home 集成值得优先试。
- 如果家里设备很多，官方集成 + 社区插件可以并行测试，哪个设备稳定用哪个。

---

### 路线 C：Home Assistant + Xiaomi Miot Auto（社区插件）

项目：

- GitHub：<https://github.com/al-one/hass-xiaomi-miot>

特点：

- 社区里非常常见的米家接入方案。
- 基于 MIoT spec 自动识别设备。
- 支持 Wi-Fi、BLE、Zigbee 设备。
- 可选自动、本地、云端模式。
- 通常通过 HACS 安装。

优点：

- 设备覆盖广。
- 社区使用量大，坑多但资料也多。
- 对米家杂牌/生态链设备支持往往比官方集成更灵活。

缺点：

- 社区维护，不是官方。
- 部分设备依赖云端，稳定性取决于米家云。
- 有时设备实体命名、属性映射需要手动调。

推荐程度：**当前最实用的米家接入 HA 路线之一。**

适合主子家的用法：

```text
米家设备 → Xiaomi Miot Auto → Home Assistant → HomeKit Bridge → Apple Home
```

这是目前最适合“已有一堆米家设备，想统一进 HA / Apple Home”的路线。

---

### 路线 D：Home Assistant 内置 Xiaomi Miio

官方文档：

- <https://www.home-assistant.io/integrations/xiaomi_miio/>

特点：

- Home Assistant 内置集成。
- 主要面向部分小米 Wi-Fi 设备，比如扫地机、空气净化器、风扇、加湿器等。
- 通常需要设备 token。
- 偏本地控制。

优点：

- HA 官方内置。
- 本地控制，延迟和隐私更好。

缺点：

- 覆盖面窄。
- token 获取麻烦。
- 不适合整个米家生态一把梭。

推荐程度：**适合特定设备，不适合作为总方案。**

---

### 路线 E：Home Assistant + Xiaomi Gateway 3

项目：

- GitHub：<https://github.com/AlexxIT/XiaomiGateway3>

特点：

- 面向小米多模网关 / Gateway 3 / 部分 Aqara 网关。
- 可以把网关下的 Zigbee / BLE 子设备本地接进 Home Assistant。
- 项目说明里强调可局域网控制。

优点：

- 本地控制，延迟低。
- 对传感器、开关等子设备体验好。
- 不完全依赖米家云。

缺点：

- 需要指定网关型号。
- 可能涉及网关固件/模式/兼容性问题。
- 对纯 Wi-Fi 米家设备没法全覆盖。

推荐程度：**如果家里有小米多模网关，值得研究。**

---

### 路线 F：HomeBridge + homebridge-miot

项目：

- GitHub：<https://github.com/merdok/homebridge-miot>

链路：

```text
米家设备 → HomeBridge → Apple Home
```

特点：

- HomeBridge 是专门把各种设备桥进 HomeKit 的工具。
- homebridge-miot 支持 MIoT 设备。
- 比 Home Assistant 轻量。

优点：

- 目标直接：就是进 Apple Home。
- 不想搭完整 HA 时比较省事。

缺点：

- 自动化能力不如 HA。
- 后续扩展性不如 HA。
- 调试复杂设备时不如 HA 生态丰富。

推荐程度：**只想进 Apple Home 可以用；如果准备长期折腾智能家居，不如 HA。**

---

### 路线 G：Matter 桥接

Matter 是未来方向，但现在不能神化。

理论路线：

```text
Matter 设备 / Matter Bridge → Apple Home / Home Assistant / Google Home
```

优点：

- 跨平台标准。
- Apple Home、Home Assistant 都支持 Matter。
- 后续新设备会越来越多。

现实限制：

- 米家旧设备大多不是 Matter 设备。
- “支持米家”不等于“支持 Matter”。
- 小米是否提供完整 Matter Bridge，要看具体网关/固件/地区。
- Matter 设备能力映射有时比原 App 少。

推荐程度：**新设备优先 Matter，旧设备不要指望 Matter 一次解决。**

---

## 3. 主子家更推荐怎么做

如果主子现在已经是米家为主，奴才建议按这个顺序推进。

### 第一阶段：先搭 Home Assistant 做中枢

硬件选择：

- 低功耗小主机 / N100 迷你主机：最稳。
- 树莓派：能用，但现在性价比不一定好。
- NAS / Docker：如果主子已有 NAS，可以跑容器。
- 旧 Mac / 旧电脑：测试可以，长期运行不如小主机省心。

推荐安装方式：

- 想省心：Home Assistant OS。
- 想和其他服务共用机器：Docker / Container。

### 第二阶段：把米家接进 HA

优先尝试：

1. 官方 Xiaomi Home 集成：`XiaoMi/ha_xiaomi_home`
2. Xiaomi Miot Auto：`al-one/hass-xiaomi-miot`
3. 内置 Xiaomi Miio：只给个别设备用
4. Xiaomi Gateway 3：如果家里有小米多模网关

不要一上来追求所有设备一次性完美接入。建议按房间/设备类型分批测试：

- 灯和开关
- 传感器
- 插座
- 空调/空净
- 扫地机
- 摄像头（这个最麻烦，通常不要优先）

### 第三阶段：HA 桥到 Apple Home

Home Assistant 自带 HomeKit Bridge。

链路：

```text
Home Assistant → HomeKit Bridge → Apple Home
```

这样主子可以继续用：

- iPhone 家庭 App
- Siri
- HomePod
- Apple Watch

同时高级自动化放在 HA 里做。

---

## 4. 推荐总架构

```text
                           ┌────────────────────┐
                           │ Apple Home / Siri   │
                           │ HomePod / iPhone    │
                           └─────────▲──────────┘
                                     │ HomeKit Bridge
┌──────────────┐        ┌────────────┴────────────┐
│ 米家 Wi-Fi   │        │ Home Assistant           │
│ 米家 Zigbee  ├───────►│ - Xiaomi Home 官方集成   │
│ 米家 BLE     │        │ - Xiaomi Miot Auto       │
│ Aqara 设备   │        │ - Xiaomi Gateway 3       │
└──────────────┘        │ - Matter / Zigbee / MQTT │
                        └────────────▲────────────┘
                                     │
                           ┌─────────┴─────────┐
                           │ 本地中枢/网关/小主机 │
                           └───────────────────┘
```

---

## 5. 成本和复杂度

### 最省心

```text
买原生 HomeKit / Matter 设备 → Apple Home
```

- 成本：中到高
- 复杂度：低
- 稳定性：高
- 对现有米家旧设备：帮助有限

### 最适合已有米家设备

```text
Home Assistant + Xiaomi Miot Auto / 官方 Xiaomi Home + HomeKit Bridge
```

- 成本：小主机几百到一千多
- 复杂度：中
- 稳定性：中到高，取决于设备
- 扩展性：最高

### 只想进 Apple Home

```text
HomeBridge + homebridge-miot
```

- 成本：低
- 复杂度：中
- 稳定性：中
- 扩展性：一般

---

## 6. 避坑清单

1. **别以为米家设备都能进 HomeKit**
   - 米家支持 ≠ HomeKit 支持。

2. **摄像头不要优先折腾**
   - 米家摄像头经常是封闭协议，进 HA / HomeKit 麻烦且不稳定。

3. **云端控制不等于本地控制**
   - 很多米家设备在 HA 里能控制，但其实走米家云。
   - 网络或米家云异常时会失效。

4. **Zigbee 子设备要看网关**
   - 子设备能不能本地进 HA，很大程度取决于网关型号。

5. **Apple Home 里显示的能力可能变少**
   - HA 里有很多实体，但桥到 Apple Home 后可能只剩开关/亮度/温度等标准能力。

6. **Matter 现在适合新设备，不适合拯救所有旧设备**
   - 不要为 Matter 预期过高。

7. **自动化逻辑尽量放 HA**
   - Apple Home 适合日常控制。
   - 复杂条件、跨品牌联动、状态机逻辑放 HA 更稳。

---

## 7. 推荐落地步骤

### Step 1：盘点设备

列一个表：

```text
设备名 / 型号 / 接入方式 / 当前在哪个 App / 是否有网关 / 是否刚需进 Apple Home
```

重点记录：

- Wi-Fi 还是 Zigbee/BLE
- 是否 Aqara
- 是否有 HomeKit 二维码
- 是否支持 Matter
- 是否接在小米多模网关下

### Step 2：先搭 HA 测试环境

推荐先用 Docker 或一台小主机跑起来。

### Step 3：先接 5 类核心设备

优先顺序：

1. 灯
2. 开关
3. 插座
4. 人体/门窗/温湿度传感器
5. 空调/空气净化器

摄像头、扫地机、复杂家电后面再看。

### Step 4：桥到 Apple Home

用 HA 的 HomeKit Bridge 暴露核心设备。

### Step 5：稳定后再决定是否买新网关

如果发现大量 Zigbee/BLE 子设备依赖网关，可以再考虑：

- Aqara M3
- 小米中枢网关
- 小米多模网关
- Zigbee2MQTT 方案（更极客，后续再单独研究）

---

## 8. 奴才给主子的推荐路线

**短期：**

```text
Home Assistant + Xiaomi Miot Auto + 官方 Xiaomi Home 集成并行测试
```

**中期：**

```text
把稳定设备通过 HomeKit Bridge 暴露给 Apple Home
```

**长期：**

```text
新设备优先 Matter / HomeKit；旧米家设备留在 HA 中转
```

这条路线最适合“现在已经有米家，又想以后用 Apple Home / Siri / HomePod”的情况。

---

## 9. 参考来源

- Xiaomi Home 官方 Home Assistant 集成：<https://github.com/XiaoMi/ha_xiaomi_home>
- Home Assistant 官方 Xiaomi Miio：<https://www.home-assistant.io/integrations/xiaomi_miio/>
- Xiaomi Miot Auto：<https://github.com/al-one/hass-xiaomi-miot>
- Xiaomi Gateway 3：<https://github.com/AlexxIT/XiaomiGateway3>
- HomeBridge Miot：<https://github.com/merdok/homebridge-miot>
- Home Assistant HomeKit Bridge：<https://www.home-assistant.io/integrations/homekit/>
- Home Assistant Matter：<https://www.home-assistant.io/integrations/matter/>
- Xiaomi Miloco / Xiaomi Local Copilot：<https://github.com/XiaoMi/xiaomi-miloco>
- Xiaomi MiMo-VL-Miloco 模型：<https://github.com/XiaoMi/xiaomi-mimo-vl-miloco>
- Home Assistant 本地 AI / Assist 进展：<https://www.home-assistant.io/blog/2025/09/11/ai-in-home-assistant/>
- Home Assistant Ollama 集成：<https://www.home-assistant.io/integrations/ollama/>
- 少数派米家官方 HA 集成体验：<https://sspai.com/post/94916>
- 蓝点网米家官方 HA + HomeKit 文章：<https://www.landiannews.com/archives/107117.html>
