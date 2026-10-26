"""In nguyên văn điều luật đã lưu trong tools/law_text.js.
Dùng:  python3 tools/law.py --list          (liệt kê khóa)
       python3 tools/law.py bhxh:70 bllđ:35  (in nguyên văn)
"""
import os, re, sys, json
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'law_text.js')
src = open(P, encoding='utf-8').read()
LAW = dict(re.findall(r"'([^'\n]+:\d+)':`(.*?)`", src, flags=re.S))
if len(sys.argv) < 2 or sys.argv[1] == '--list':
    for k, v in LAW.items():
        print(k.ljust(14), v.split('\n')[0][:100])
else:
    for k in sys.argv[1:]:
        print('=' * 8, k, '=' * 8)
        print(LAW.get(k, '(không có khóa này)'))
