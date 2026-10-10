# 装甲核心2 中文 0.3.2

PS2 日版 **SLPS-25007** 的累计汉化差分，保留既有启动修复、True Analogs 双摇杆、任务、竞技场与零件校订。

**[下载 0.3.2 正式版](https://github.com/AmuroRX-93/AC2-Chinese-Patch/releases/tag/v0.3.2)**，选择附件 `AC2_JP_to_CHS_0.3.2_AllPlatforms_Delta.zip`。GitHub 自动生成的 Source code 压缩包不含差分载荷与便携 Python，不能直接安装。

## 本次修订

84 条返表修订写入 85 个物理位置：60 封邮件正文、7 个邮件标题、14 个发件人、2 条任务简报，以及有两份资源副本的 1 句战斗对白。按作者授权修正手误与四项待核对内容，保留“泰拉做成”“九球破坏者”“翡翠社”等指定译名。新增 17 个菜单字形，旧字形和字码映射保持一致。

邮件按每行 22 字位、每页 5 行排版；两条简报沿用 23 字位、4 行及原控制码／事件页。历史校订、启动修复和双摇杆程序保留；本次没有用空修订栏推断未校对，也不宣称全游戏终审。

## 怎么安装

完整解压，准备匹配的日文原版 ISO。

- **Windows x64／ARM64**：双击 `Windows_安装.cmd`。
- **macOS Apple 芯片／Intel**：双击 `macOS_安装.command`，或终端运行 `sh run.sh`。
- **Linux x64／ARM64**：终端运行 `sh run.sh`。附 glibc 运行时，Alpine/musl 不在其适用范围。

菜单选 1，输入原版 ISO 路径及输出位置，等待合成和完整校验。包内已附 6 种架构的 Python、脚本、版本识别和包校验工具、离线 HTML／文本说明及许可；无需安装 Python 或 pip。

生成 `AC2_CHS_0.3.2_TrueAnalogs.iso` 后重新选择它冷启动，可沿用记忆卡内存档；避免读取旧即时状态。旧汉化用户也用保留的日文原版重新生成，本包不直接覆写旧镜像。输出存在时拒绝覆盖。

详细命令、升级、回退和错误日志说明见[命令与排错](../../docs/命令与排错.txt)，快速操作见[先读说明](../../docs/先读说明.txt)，也随 Release 附件提供。

## Android 与 PS2

电脑生成的同一 ISO 可传入 Android 模拟器，或按已有 OPL／介质方式安装到 PS2。只使用手机的玩家，可尝试包内不使用二次压缩的标准 XDelta 补丁与兼容工具。UniPatcher 的[官方说明](https://github.com/btimofeev/UniPatcher)列出 XDelta 支持，但本项目没有其处理本版 4.38GB ISO 的手机实测；文件权限、大文件能力和空间需确认。

ISO 超过 FAT32 单文件上限。OPL 介质、exFAT、USBExtreme 或 SMB 部署按[官方说明](https://github.com/ps2homebrew/Open-PS2-Loader)及自己的实际版本选择。步骤、SHA256 和回退方式见[三平台使用说明](../../docs/三平台使用说明.txt)。本包不夹带第三方手机 APK、模拟器、BIOS、固件或个人存档。

## 校验与验证范围

输入、输出均为 **4,380,393,472 字节**。

| 内容 | SHA256 |
|---|---|
| 日文原版输入 | `fa1460abc92aa89db1806235620251f9b4cdb00a825cc0fadb36342601d088bc` |
| 中文 0.3.2 输出 | `3ba0d0b7df775738df95fdb641ebf4ec74aae5e8031384da07890bc519787f12` |

已验证文本独立回读、字形／容量／控制码／分页及非目标字节保持；包内 macOS ARM64 Python 从完整原版重建一致，中文／空格路径及 13 项安装保护检查通过。标准 XDelta 从原版全量重建一致，最终 ZIP 每个文件完整读回与 SHA256 匹配；6 种运行时的架构、入口、标准库、许可已静态检查。

**本版未启动游戏；Windows、Intel Mac、Linux、Android、PS2 尚未实跑。** “全平台”指运行内容及便利入口覆盖，不表示所有设备已通过游戏内验收。既有配色／卡死等反馈不由本次文本回填宣称根治。具体证据见[验证说明](../../docs/验证说明.json)。

## 来源与许可

沿用既有社区汉化和用户历次校译、PARTS PACK 零件说明。True Analogs 源自 [VanLaser 项目](https://github.com/VanLaser/analog-controls-for-armored-core-ps2)，本轮程序与 0.3.1 一致。字体为思源黑体；便携 Python 来源与第三方许可随包保留。参见[来源与致谢](../../docs/来源与致谢.txt)。

非官方、无偿社区修改；完整游戏仅由玩家自行准备。本仓库保留历史版本资料，最新安装请使用上方 0.3.2 Release 附件。
