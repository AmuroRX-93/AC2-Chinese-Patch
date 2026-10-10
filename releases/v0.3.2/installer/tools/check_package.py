#!/usr/bin/env python3
from pathlib import Path
import hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(8<<20),b''):h.update(chunk)
    return h.hexdigest()
failed=[];count=0
for line in (ROOT/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
    expected,name=line.split('  ',1);p=(ROOT/name).resolve()
    if not p.is_relative_to(ROOT.resolve()) or not p.is_file() or digest(p)!=expected:failed.append(name)
    count+=1
if failed:
    print('包不完整或文件改变：\n'+'\n'.join(failed),file=sys.stderr);raise SystemExit(1)
print('完整解压包校验通过，'+str(count)+'个文件一致。')
