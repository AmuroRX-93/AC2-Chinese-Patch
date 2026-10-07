<!-- latest-release-20261007 -->
## 最新正式发布（2026-10-07）

[AC2 中文 0.3.1 正式版](https://github.com/AmuroRX-93/AC2-Chinese-Patch/releases/tag/v0.3.1)

从日文原版累计安装，包含双摇杆、竞技场与零件校对修订、41个新增字形。已通过包内 macOS ARM64 Python 从原版完整还原，目标 SHA256 为 22c6d66d43ee860e5cd48e934c3a7e11ba3e908f0021badba3f1961aa21d7f4e。文本与字库已静态读回核验；尚未进行本轮游戏内验证，语音/影片与未编号任务不是本次完整校对范围。
<!-- /latest-release-20261007 -->

# 装甲核心2 中文版 0.3.0 · 任务文本修订 / True Analogs

适用 PS2 日版 **SLPS-25007**。这是**日文原版 → 0.3.0 累计差分**，继承0.2.5零件校译、r1启动修复和既有True Analogs双摇杆修改。

[下载0.3.0](https://github.com/AmuroRX-93/AC2-Chinese-Patch/releases/tag/v0.3.0)

下载附件 **AC2_JP_to_CHS_0.3.0_Delta.zip**（92,713,578字节，约93MB），不要用GitHub自动生成的Source code压缩包安装。差分数据与Python运行环境在Release附件中。

## 更新内容

采用MISSION10–35中日对照测试表的最新测试版列。455条有原文记录全部对照：449条在r1中已有等效译文，实际修订6条、对应7处文本槽位。保留原分页和控制码，修改页面按既有行宽重排。

相对r1，可执行文件和字体完全不变；相对公开0.2.5，包含此前r1的启动死循环修复。本版不改零件数值，不宣称全游戏文本已完美校译。逐条采用和修订清单随包。

## Windows / macOS 使用

1. 完整解压ZIP，准备校验匹配的日文原版ISO。
2. Windows x64双击`Windows_Install.cmd`；Apple Silicon或Intel Mac双击`macOS_安装.command`。
3. 拖入原版ISO按回车，等待完整合成和校验。**已附对应平台Python，无需额外安装Python或pip，不联网。**
4. 在模拟器中选择`AC2_CHS_0.3.0_TrueAnalogs.iso`正常开机，沿用记忆卡内存档；不要恢复旧版即时状态。

已有0.2.x/r1也用原版重新合成。本包不能直接套旧汉化、其他地区、CHD或压缩包。不改输入ISO、记忆卡、模拟器配置，不自动启动游戏；已有输出拒绝覆盖。建议输出盘另留6GB空间，不能使用FAT32。

详细PowerShell/终端命令、故障排查见[Python使用说明](docs/Python使用说明.txt)，安装步骤见[先读说明](docs/先读说明.txt)。这些文档亦在ZIP内。

## 校验值

输入和输出均为4,380,393,472字节。

| 文件 | SHA256 |
|---|---|
| 日文原版输入 | `fa1460abc92aa89db1806235620251f9b4cdb00a825cc0fadb36342601d088bc` |
| 0.3.0输出ISO | `7ffa17be41ae24565bb335c0548387016eea959ad2364b6a71839fcc8c8c603d` |
| 发布ZIP | `4cc0ae8219aeb574fdefca17acf95200a9a68f269118f7759558cc7ccd65b2d5` |

## 手机和实机路线

电脑合成后可将ISO传到Android，再让模拟器扫描；只有手机可尝试包内标准xdelta与兼容工具，大文件限制需自行确认。本包不兼容旧L10N Android更新器。PS2实机需先合成ISO，再按已有OPL及介质版本规则安装，FAT32不能直接复制完整ISO。详见[三平台安装方法](docs/三平台安装方法.txt)。没有本版本手机/实机运行验收。

## 验证范围与已知限制

已验证：455条译表记录实际ISO回读匹配、7处变化容量/控制码/分页检查、全部非目标字节不变；Apple Silicon包内Python从完整原版合成成功，XDelta全量还原一致；11项安装器成功/拒绝/中断检查；ZIP每条目CRC与SHA验证。

**本轮0.3.0未启动游戏。** r1此前通过标题/菜单检查，不等于0.3.0全关卡测试。配色卡死反馈仍未完成复现验收，本版不宣称解决。Windows、Intel Mac、Android和PS2实机未执行本版本测试。

True Analogs沿用既有第1手柄与回放等限制，不提供关闭开关，不要重复叠加其他双摇杆补丁。

## 来源与许可

本次使用用户提供的任务校译表，沿用既有汉化工程及PARTS PACK零件修订。双摇杆源自[VanLaser True Analogs](https://github.com/VanLaser/analog-controls-for-armored-core-ps2)，字体沿用思源黑体；许可与Python来源随包。

无偿、非官方社区修改，不含完整游戏、BIOS或个人存档。差分包含修改后的局部资源字节，请自行合法准备原版，不冒充官方或收费贩售。
