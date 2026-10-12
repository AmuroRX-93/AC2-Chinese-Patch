#!/usr/bin/env python3
from pathlib import Path
import hashlib,sys,json
p=Path(sys.argv[1]);h=hashlib.sha256()
with p.open('rb') as f:
    for chunk in iter(lambda:f.read(8<<20),b''):h.update(chunk)
sha=h.hexdigest()
known={'3ba0d0b7df775738df95fdb641ebf4ec74aae5e8031384da07890bc519787f12':'中文0.3.2旧发布版；请从日文原版重新生成0.3.2-fix.1','fa1460abc92aa89db1806235620251f9b4cdb00a825cc0fadb36342601d088bc': 'PS2日文原版 SLPS-25007（可用于本包）', '2a59f11c08856f3c905c6af536f661823497ebc9fac636d37a4582efe9b65b25': '中文0.3.2-fix.1 True Analogs（无需再修补）', '22c6d66d43ee860e5cd48e934c3a7e11ba3e908f0021badba3f1961aa21d7f4e': '中文0.3.1（请用保留的日文原版重新生成0.3.2-fix.1）', '7ffa17be41ae24565bb335c0548387016eea959ad2364b6a71839fcc8c8c603d': '中文0.3.0（请用保留的日文原版重新生成0.3.2-fix.1）'}
print('大小：'+str(p.stat().st_size)+'字节\nSHA256：'+sha+'\n识别：'+known.get(sha,'未知版本，禁止当作本包日文原版输入'))
