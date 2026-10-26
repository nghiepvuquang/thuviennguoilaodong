import os, re, json, html, shutil
import glob, datetime
from articles import ARTICLES as A1
from articles2 import A2

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED = ['slug', 'cat', 'date', 'title', 'desc', 'lead', 'keys', 'laws', 'body']


def load_json_articles():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'content', 'bai-viet', '*.json'))):
        a = json.load(open(f, encoding='utf-8'))
        miss = [k for k in REQUIRED if not a.get(k)]
        if miss:
            raise SystemExit(f'{f}: thiếu trường {miss}')
        a['faq'] = [tuple(x) for x in a.get('faq', [])]
        out.append(a)
    return out


_J = load_json_articles()
for _a in _J:
    _a['_json'] = 1
ARTICLES = A1 + A2 + _J
_slugs = [a['slug'] for a in ARTICLES]
if len(_slugs) != len(set(_slugs)):
    raise SystemExit('Trùng slug: ' + str([x for x in _slugs if _slugs.count(x) > 1]))
# mới nhất lên trước; cùng ngày giữ thứ tự gốc
ARTICLES = [a for _, a in sorted(enumerate(ARTICLES), key=lambda t: (t[1].get('updated', t[1]['date']), t[1].get('_json', 0), -t[0]), reverse=True)]

SITE = 'https://thuviennguoilaodong.com'
OUT = os.path.join(ROOT, 'site')
TODAY = datetime.date.today().isoformat()
CAT = {'luong': ('Tiền lương', 't-luong'), 'thue': ('Thuế TNCN', 't-thue'),
       'bh': ('Bảo hiểm', 't-bh'), 'lv': ('Nghỉ việc & thời giờ', 't-lv')}

FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%23d9632b'/%3E%3Ctext x='32' y='45' font-size='38' font-family='Arial' font-weight='900' fill='white' text-anchor='middle'%3E%C4%91%3C/text%3E%3C/svg%3E"

THEME_JS = "<script>try{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t)}catch(e){}function toggleTheme(){var r=document.documentElement,c=r.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'),n=c==='dark'?'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem('theme',n)}catch(e){}}</script>"


def head(title, desc, url, ld, og_type='article'):
    e = html.escape
    return f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="Thư Viện Người Lao Động">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="vi_VN">
<link rel="icon" href="{FAVICON}">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-QXWRGDZ79R"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-QXWRGDZ79R');</script>

<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800;900&display=swap">
<link rel="stylesheet" href="/assets/blog.css">
<script defer src="/assets/ads.js"></script>
{THEME_JS}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="site-header">
  <div class="hd pad">
    <a class="brand" href="/"><div class="brand-icon">₫</div><div class="brand-name">Thư Viện <span>Người Lao Động</span></div></a>
    <button class="btn-ghost" onclick="toggleTheme()">◐ Sáng / Tối</button>
  </div>
  <nav class="nav pad">
    <a href="/">Tính lương</a><a href="/#bhxh">BHXH 1 lần</a><a href="/#luat">Hỏi luật lao động</a><a class="on" href="/bai-viet/">Bài viết</a><a href="/#gioi-thieu">Giới thiệu</a>
  </nav>
</header>
'''


FOOT = '''<footer><div class="ft pad"><div><a href="/">Tính lương Gross – Net</a><a href="/#bhxh">Tính BHXH 1 lần</a><a href="/#luat">Tra cứu luật</a><a href="/bai-viet/">Bài viết</a><a href="/#gioi-thieu">Giới thiệu</a><a href="/#bao-mat">Chính sách bảo mật</a><a href="/lien-he/">Liên hệ</a></div><div>© 2026 Thư Viện Người Lao Động · lienhe@thuviennguoilaodong.com</div></div></footer>
</body></html>
'''


def fmt_date(d):
    y, m, dd = d.split('-')
    return f'{dd}/{m}/{y}'


def read_minutes(body):
    words = len(re.sub('<[^>]+>', ' ', body).split())
    return max(3, round(words / 200))


def ad(slot):
    return f'<div class="ad-slot" data-slot="{slot}" hidden></div>'


def mid_ad(body):
    # chèn quảng cáo giữa bài: trước thẻ <h2> thứ 3 (nếu có)
    idx = [m.start() for m in re.finditer(r'<h2[ >]', body)]
    if len(idx) >= 3:
        return body[:idx[2]] + ad('bai-giua') + '\n' + body[idx[2]:]
    return body


def build_article(a, all_):
    url = f"{SITE}/bai-viet/{a['slug']}/"
    # TOC from h2 with id
    h2s = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', a['body'])
    toc = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in h2s)
    keys = ''.join(f'<li>{k}</li>' for k in a['keys'])
    laws = ''.join(f'<li>{l}</li>' for l in a['laws'])
    faq_html = ''
    faq_ld = None
    if a.get('faq'):
        faq_html = '<h2 id="hoi-dap">Câu hỏi thường gặp</h2><div class="faq">' + ''.join(
            f'<details><summary>{q}</summary><p>{ans}</p></details>' for q, ans in a['faq']) + '</div>'
        faq_ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": re.sub('<[^>]+>', '', q),
                  "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', ans)}} for q, ans in a['faq']]}
        toc += '<li><a href="#hoi-dap">Câu hỏi thường gặp</a></li>'
    rel = [x for x in all_ if x['slug'] in a.get('rel', [])] or [x for x in all_ if x['slug'] != a['slug']][:4]
    rel_html = ''.join(f'<li><a href="/bai-viet/{x["slug"]}/">{x["title"]}</a></li>' for x in rel)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": a['title'], "description": a['desc'], "datePublished": a['date'],
         "dateModified": a.get('updated', a['date']), "inLanguage": "vi",
         "mainEntityOfPage": url, "author": {"@type": "Organization", "name": "Thư Viện Người Lao Động", "url": SITE + '/'},
         "publisher": {"@type": "Organization", "name": "Thư Viện Người Lao Động", "url": SITE + '/'}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": SITE + '/'},
            {"@type": "ListItem", "position": 2, "name": "Bài viết", "item": SITE + '/bai-viet/'},
            {"@type": "ListItem", "position": 3, "name": a['title'], "item": url}]}]}
    if faq_ld:
        ld['@graph'].append(faq_ld)
    cat, _ = CAT[a['cat']]
    page = head(a['title'] + ' | Thư Viện Người Lao Động', a['desc'], url, ld) + f'''
<div class="main pad">
<article>
  <nav class="crumb"><a href="/">Trang chủ</a> › <a href="/bai-viet/">Bài viết</a> › {cat}</nav>
  <h1>{a['title']}</h1>
  <div class="meta"><span>Cập nhật: <b>{fmt_date(a.get('updated', a['date']))}</b></span><span>Đọc khoảng <b>{read_minutes(a['body'])} phút</b></span><span>Chuyên mục: <b>{cat}</b></span></div>
  <p class="lead">{a['lead']}</p>
  <div class="keys"><h2>Ý chính</h2><ul>{keys}</ul></div>
  {ad('bai-dau')}
  <nav class="toc" aria-label="Mục lục"><b>Nội dung bài viết</b><ol>{toc}</ol></nav>
  <div class="body">
{mid_ad(a['body'])}
{faq_html}
  {ad('bai-cuoi')}
  <section class="law"><h2>Căn cứ pháp lý</h2><ul>{laws}</ul>
  <p class="disc">Bài viết mang tính tham khảo, tổng hợp từ văn bản pháp luật đang có hiệu lực tại thời điểm cập nhật. Trường hợp cụ thể của bạn có thể khác; khi cần chắc chắn, hãy hỏi phòng nhân sự, cơ quan BHXH, cơ quan thuế hoặc luật sư.</p></section>
  </div>
</article>
<aside>
  <div class="side tools"><h3>Công cụ miễn phí</h3><ul><li><a href="/">🧮 Tính lương Gross ↔ Net</a></li><li><a href="/#bhxh">💰 Tính tiền BHXH 1 lần</a></li><li><a href="/#luat">📖 Tra cứu luật lao động</a></li></ul></div>
  <div class="side"><h3>Bài viết liên quan</h3><ul>{rel_html}</ul></div>
  {ad('bai-ben-phai')}
</aside>
</div>
''' + FOOT
    d = os.path.join(OUT, 'bai-viet', a['slug'])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(page)


def build_list(all_):
    url = SITE + '/bai-viet/'
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Bài viết về lương, thuế, BHXH và luật lao động",
          "url": url, "inLanguage": "vi",
          "hasPart": [{"@type": "Article", "headline": a['title'], "url": f"{SITE}/bai-viet/{a['slug']}/"} for a in all_]}
    cards = ''
    for a in all_:
        cat, cls = CAT[a['cat']]
        cards += f'<a class="post" href="/bai-viet/{a["slug"]}/"><span class="tag {cls}">{cat}</span><h2>{a["title"]}</h2><p>{a["desc"]}</p><span class="more">Đọc bài →</span></a>'
    page = head('Bài viết: lương, thuế TNCN, BHXH, luật lao động 2026 | Thư Viện Người Lao Động',
                'Giải thích dễ hiểu về cách tính lương Net, thuế TNCN 5 bậc, lương tối thiểu vùng, BHXH, rút BHXH 1 lần, trợ cấp thất nghiệp, thôi việc, làm thêm giờ và nghỉ phép năm 2026.',
                url, ld, 'website') + f'''
<div class="list-head pad"><h1>Bài viết cho người lao động</h1><p>Giải thích dễ hiểu, có ví dụ tính tiền cụ thể, theo luật áp dụng năm 2026. Mỗi bài dẫn tới nguyên văn điều luật để bạn tự kiểm tra.</p></div>
<div class="grid pad">{cards}{ad('danh-sach')}</div>
''' + FOOT
    os.makedirs(os.path.join(OUT, 'bai-viet'), exist_ok=True)
    open(os.path.join(OUT, 'bai-viet', 'index.html'), 'w').write(page)


def build_sitemap(all_):
    urls = [(SITE + '/', TODAY, '1.0'), (SITE + '/bai-viet/', TODAY, '0.8')]
    urls += [(SITE + '/lien-he/', TODAY, '0.3')]
    urls += [(f"{SITE}/bai-viet/{a['slug']}/", a.get('updated', a['date']), '0.7') for a in all_]
    x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    x += ''.join(f'  <url><loc>{u}</loc><lastmod>{d}</lastmod><priority>{p}</priority></url>\n' for u, d, p in urls)
    x += '</urlset>\n'
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(x)


def build_contact():
    url = SITE + '/lien-he/'
    ld = {"@context": "https://schema.org", "@type": "ContactPage", "name": "Liên hệ – Thư Viện Người Lao Động", "url": url,
          "mainEntity": {"@type": "Organization", "name": "Thư Viện Người Lao Động", "url": SITE + '/', "email": "lienhe@thuviennguoilaodong.com"}}
    page = head('Liên hệ | Thư Viện Người Lao Động', 'Liên hệ Thư Viện Người Lao Động: góp ý, báo lỗi số liệu, đề xuất bài viết hoặc hợp tác.', url, ld, 'website').replace('<a class="on" href="/bai-viet/">', '<a href="/bai-viet/">') + f'''
<div class="main pad" style="grid-template-columns:minmax(0,1fr)">
<article style="max-width:760px">
  <nav class="crumb"><a href="/">Trang chủ</a> › Liên hệ</nav>
  <h1>Liên hệ</h1>
  <p class="lead" style="margin-top:12px">Thư Viện Người Lao Động là trang thông tin miễn phí giúp người lao động tự tính lương, bảo hiểm và tra cứu pháp luật lao động. Chúng tôi luôn muốn nghe góp ý của bạn.</p>
  <div class="body">
  <div class="keys"><h2>Email</h2><p style="font-size:1.15rem;font-weight:900;margin:4px 0"><a href="mailto:lienhe@thuviennguoilaodong.com">lienhe@thuviennguoilaodong.com</a></p><p style="margin:0;color:var(--fg-2)">Chúng tôi thường phản hồi trong vòng 1–3 ngày làm việc.</p></div>
  <h2 id="gop-y">Bạn có thể gửi cho chúng tôi</h2>
  <ul>
  <li><strong>Báo lỗi số liệu hoặc cách tính:</strong> ghi rõ trang, số liệu bạn nhập và kết quả bạn cho là chưa đúng.</li>
  <li><strong>Văn bản pháp luật mới:</strong> nếu có nghị định, thông tư mới chưa được cập nhật.</li>
  <li><strong>Đề xuất chủ đề bài viết</strong> mà bạn đang cần tìm hiểu.</li>
  <li><strong>Hợp tác, quảng cáo:</strong> vui lòng ghi rõ tên đơn vị và nội dung đề xuất.</li>
  </ul>
  <div class="note"><b>Lưu ý:</b> Chúng tôi không tư vấn pháp lý cho từng vụ việc cụ thể và không nhận hồ sơ thay cơ quan nhà nước. Vui lòng <b>không gửi</b> số CCCD, số tài khoản, mật khẩu hay giấy tờ cá nhân qua email. Với tranh chấp lao động, hãy liên hệ công đoàn, cơ quan BHXH, thanh tra lao động hoặc luật sư.</div>
  <h2 id="ve-chung-toi">Về chúng tôi</h2>
  <p>Nội dung trên trang được tổng hợp từ văn bản pháp luật đang có hiệu lực (Bộ luật Lao động 2019, Luật Bảo hiểm xã hội 2024, Luật Thuế thu nhập cá nhân 2025, Luật Việc làm 2025 và các nghị định hướng dẫn), có trích nguyên văn điều luật để bạn đối chiếu. Xem thêm tại trang <a href="/#gioi-thieu">Giới thiệu</a> và <a href="/#bao-mat">Chính sách bảo mật</a>.</p>
  </div>
</article>
</div>
''' + FOOT
    os.makedirs(os.path.join(OUT, 'lien-he'), exist_ok=True)
    open(os.path.join(OUT, 'lien-he', 'index.html'), 'w').write(page)


def refresh_home_strip(all_):
    p = os.path.join(OUT, 'index.html')
    h = open(p, encoding='utf-8').read()
    links = ''.join(f'<a href="/bai-viet/{a["slug"]}/">{a["title"]}</a>' for a in all_[:9])
    new, n = re.subn(r'(<div class="bs-list">).*?(</div></div></section>)', lambda m: m.group(1) + links + m.group(2), h, count=1, flags=re.S)
    if n != 1:
        raise SystemExit('Không tìm thấy khung "Bài viết hữu ích" trong index.html')
    open(p, 'w', encoding='utf-8').write(new)


if __name__ == '__main__':
    build_contact()
    os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
    shutil.copy(os.path.join(ROOT, 'tools', 'blog.css'), os.path.join(OUT, 'assets', 'blog.css'))
    for a in ARTICLES:
        build_article(a, ARTICLES)
    build_list(ARTICLES)
    build_sitemap(ARTICLES)
    refresh_home_strip(ARTICLES)
    print('built', len(ARTICLES))
