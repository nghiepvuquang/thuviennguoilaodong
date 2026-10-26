"""Kiểm tra toàn bộ web sau khi build. Thoát mã 1 nếu có lỗi.
Dùng: python3 tools/check.py
"""
import os, re, sys, glob, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, 'site')
GA = 'G-QXWRGDZ79R'
HOME_ROUTES = {'bhxh', 'luat', 'gioi-thieu', 'bao-mat', 'tinh-luong'}
home = open(os.path.join(SITE, 'index.html'), encoding='utf-8').read()
HOME_ROUTES |= set(re.findall(r"\{id:'([a-z0-9-]+)'", home))
errs = []
pages = sorted(glob.glob(os.path.join(SITE, '**', 'index.html'), recursive=True))
for p in pages:
    rel = '/' + os.path.relpath(os.path.dirname(p), SITE).replace('.', '').strip('/')
    rel = rel if rel == '/' else rel + '/'
    h = open(p, encoding='utf-8').read()
    if GA not in h: errs.append(f'{rel}: thiếu mã Google Analytics')
    if '/assets/ads.js' not in h: errs.append(f'{rel}: thiếu tệp cấu hình quảng cáo /assets/ads.js')
    if '/bai-viet/' in rel and rel != '/bai-viet/' and h.count('class="ad-slot"') < 3: errs.append(f'{rel}: thiếu vị trí quảng cáo trong bài')
    if not re.search(r'<title>[^<]{10,}</title>', h): errs.append(f'{rel}: thiếu <title>')
    if p != os.path.join(SITE, 'index.html') and 'name="description"' not in h: errs.append(f'{rel}: thiếu meta description')
    ids = set(re.findall(r'id="([^"]+)"', h))
    for a in re.findall(r'href="#([^"]+)"', h):
        if a not in ids and p != os.path.join(SITE, 'index.html'): errs.append(f'{rel}: mục lục trỏ tới #{a} không tồn tại')
    for href in set(re.findall(r'href="(/[^"]*)"', h)):
        path, _, frag = href.partition('#')
        if path == '/' and frag:
            if frag not in HOME_ROUTES: errs.append(f'{rel}: liên kết /#{frag} không có trên trang chủ')
            continue
        if path.startswith('/assets/'):
            if not os.path.exists(os.path.join(SITE, path.lstrip('/'))): errs.append(f'{rel}: thiếu file {path}')
            continue
        target = os.path.join(SITE, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(SITE, path.lstrip('/'))
        if not os.path.exists(target): errs.append(f'{rel}: liên kết hỏng {href}')
    for s in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, flags=re.S):
        try: json.loads(s)
        except Exception as e: errs.append(f'{rel}: JSON-LD lỗi {e}')
sm = open(os.path.join(SITE, 'sitemap.xml'), encoding='utf-8').read()
locs = re.findall(r'<loc>(.*?)</loc>', sm)
if len(locs) != len(pages): errs.append(f'sitemap có {len(locs)} URL nhưng có {len(pages)} trang')
print(f'Đã kiểm tra {len(pages)} trang, sitemap {len(locs)} URL.')
if errs:
    print('LỖI:'); [print(' -', e) for e in errs]; sys.exit(1)
print('OK – không có lỗi.')
