# 装甲核心2 中文 0.3.2-fix.1

[下载最新累计差分](https://github.com/AmuroRX-93/AC2-Chinese-Patch/releases/tag/v0.3.2-fix.1)

附件：`AC2_JP_to_CHS_0.3.2-fix.1_AllPlatforms_Delta.zip`。仅支持 PS2 日版 SLPS-25007 原版直升，旧汉化也请从保留的原版重新生成。

装甲核心2 中文 0.3.2-fix.1 · 累计修订版（2026-10-12）
PS2 日版 SLPS-25007；仅支持匹配日文原版ISO直升。

包含0.3.2全部累计汉化与True Analogs双摇杆；新增奖励金额提示、名称输入中的汉字/符号标签修正，以及PROLOGJ、PROLOGE、ENDINGJ、ENDINGE、OVER五段剧情影片中文字幕和音频预缓冲封装调整。
标题界面与TITLE.PSS按要求保留原版；职员名单不汉化。
本版不含“细线修复”。已撤销全纹理偏移实验，不修改模拟器配置。原版也出现的细线尚未解决。

差分包：完整解压AC2_JP_to_CHS_0.3.2-fix.1_AllPlatforms_Delta.zip，Windows双击Windows_安装.cmd，Mac双击macOS_安装.command，Linux运行sh run.sh。菜单1选择原版ISO，生成的新文件默认在原版旁边；完成时会打印完整输出路径。包内附六架构Python，不需另装Python或pip。
整合包：完整解压AC2_CHS_0.3.2-fix.1_AllPlatforms_Full.7z，直接添加根目录ISO运行，不用再打补丁；维护工具用于校验或从原版重新生成。
PC、安卓和PS2实机共用同一个生成ISO；安卓仅手机修补可用包内标准XDelta配合支持大文件的修补器。PS2按已有OPL/介质部署。详细步骤、命令、回退见三平台使用说明.txt与命令与排错.txt。

输入SHA256：fa1460abc92aa89db1806235620251f9b4cdb00a825cc0fadb36342601d088bc
输出SHA256：2a59f11c08856f3c905c6af536f661823497ebc9fac636d37a4582efe9b65b25
输入/输出大小均4,380,393,472字节，超过FAT32单文件上限。
旧汉化版本请用保留的日文原版重新生成；不得把旧汉化ISO当作输入。工具不覆写已有输出、不改原版或记忆卡。回退直接选择保留的旧ISO。冷启动后读记忆卡，不恢复旧即时状态。不要再次叠加双摇杆补丁。

验证边界：包内Mac ARM64 Python和标准XDelta均从完整原版重建到同一目标SHA256，13项安装保护检查通过；用户已反馈当前游戏能进入设置界面。五段剧情影片的全部播放/跳过/转场尚未逐一验收；不宣称全剧情已测或黑屏彻底根治。Windows、Intel Mac、Linux、Android和PS2实机未实跑。六架构工具随包提供不等于各设备游戏运行已通过。
不含模拟器、BIOS、固件、私人配置或个人存档；无解压密码。


详细说明与工具源码见 [本次发行目录](releases/v0.3.2-fix.1/docs/先读说明.txt)。沿用社区汉化、用户历次校译与 PARTS PACK 内容；True Analogs 来自 [VanLaser 项目](https://github.com/VanLaser/analog-controls-for-armored-core-ps2)，字体为思源黑体，许可和各平台 Python 来源随完整差分包保留。
