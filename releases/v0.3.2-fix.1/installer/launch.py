#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys,json,hashlib
ROOT=Path(__file__).resolve().parent
for s in (sys.stdout,sys.stderr):
    if hasattr(s,'reconfigure'):s.reconfigure(encoding='utf-8',errors='backslashreplace')
def path_input(prompt):
    value=input(prompt+'\n').strip()
    if sys.platform!='win32':
        import shlex
        try:
            parsed=shlex.split(value)
            if len(parsed)==1:value=parsed[0]
        except ValueError:pass
    return value.strip('"')
def run(script,*args):return subprocess.call([sys.executable,'-B','-X','utf8',str(ROOT/script),*args])
def main():
    if len(sys.argv)>1:return run('install.py',*sys.argv[1:])
    print('装甲核心2 中文 0.3.2-fix.1 · 安装与校验工具')
    print('1  从日文原版生成中文ISO\n2  只检查原版和差分\n3  校验生成的中文ISO\n4  识别ISO版本\n5  检查整个解压包\n0  退出')
    option=input('输入数字并按回车：').strip()
    if option in ('1','2'):
        source=path_input('拖入或粘贴日文原版ISO的完整路径：')
        if not source:raise ValueError('没有选择ISO')
        if option=='2':return run('install.py',source,'--check-only')
        output=path_input('输出ISO完整路径；直接按回车保存在原版旁边：')
        return run('install.py',source,*(['--output',output] if output else []))
    if option=='3':return run('install.py','--verify-result',path_input('选择要校验的0.3.2-fix.1 ISO：'))
    if option=='4':return run('tools/identify_iso.py',path_input('选择ISO：'))
    if option=='5':return run('tools/check_package.py')
    if option=='0':return 0
    raise ValueError('请输入0至5')
if __name__=='__main__':
    try:raise SystemExit(main())
    except (Exception,KeyboardInterrupt) as e:print('未完成：'+str(e),file=sys.stderr);raise SystemExit(1)
