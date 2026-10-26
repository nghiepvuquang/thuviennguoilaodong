D = '2026-10-26'


def cta(href, title, sub, btn):
    return f'<div class="cta"><p>{title}<small>{sub}</small></p><a href="{href}">{btn} →</a></div>'


def L(anchor, text):
    return f'<a href="/#{anchor}">{text}</a>'


def tbl(head, rows, num_cols=(), tot_last=False):
    h = ''.join(f'<th class="n">{c}</th>' if i in num_cols else f'<th>{c}</th>' for i, c in enumerate(head))
    body = ''
    for ri, r in enumerate(rows):
        cls = ' class="tot"' if tot_last and ri == len(rows) - 1 else ''
        body += f'<tr{cls}>' + ''.join(f'<td class="n">{c}</td>' if i in num_cols else f'<td>{c}</td>' for i, c in enumerate(r)) + '</tr>'
    w = ' class="w"' if len(head) > 3 else ''
    return f'<div class="tbl"><table{w}><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table></div>'


TOOL_LUONG = cta('/', 'Tính ngay lương thực nhận của bạn', 'Nhập lương, chọn xã/phường nơi làm việc, số người phụ thuộc — ra kết quả tức thì.', 'Mở công cụ tính lương')
TOOL_BHXH = cta('/#bhxh', 'Tính số tiền BHXH 1 lần bạn nhận được', 'Nhập từng giai đoạn đóng và mức lương, công cụ tự áp hệ số trượt giá.', 'Mở công cụ BHXH 1 lần')

ARTICLES = []

# 1 ─────────────────────────────────────────────
ARTICLES.append(dict(
    slug='cach-tinh-luong-net-tu-gross-2026', cat='luong', date=D,
    title='Cách tính lương Net từ lương Gross năm 2026 (có ví dụ cụ thể)',
    desc='Hướng dẫn từng bước tính lương thực nhận (Net) từ lương Gross năm 2026: trừ bảo hiểm 10,5%, giảm trừ gia cảnh 15,5 triệu và thuế TNCN 5 bậc mới, kèm bảng ví dụ 10–50 triệu.',
    lead='Lương Gross là con số ghi trên hợp đồng, còn lương Net là số tiền thật sự về tài khoản mỗi tháng. Khoảng chênh giữa hai con số này gồm tiền bảo hiểm bắt buộc và thuế thu nhập cá nhân. Năm 2026 cách tính thuế thay đổi lớn, nên nhiều người sẽ thấy lương Net tăng lên dù lương Gross giữ nguyên.',
    keys=['Lương Net = Lương Gross − Bảo hiểm (10,5%) − Thuế TNCN (− đoàn phí công đoàn nếu có).',
          'Năm 2026: giảm trừ bản thân <strong>15,5 triệu/tháng</strong>, mỗi người phụ thuộc <strong>6,2 triệu/tháng</strong>; biểu thuế còn <strong>5 bậc</strong>.',
          'Lương 20 triệu, không có người phụ thuộc → nhận về <strong>17.780.000 đ</strong>, ít hơn năm 2025 tới 320.000 đ tiền thuế mỗi tháng.'],
    laws=[f'Luật Thuế thu nhập cá nhân số 109/2025/QH15 – {L("bieu-thue-tncn","Điều 9 (biểu thuế)")}, {L("giam-tru-gia-canh","Điều 10 (giảm trừ gia cảnh)")}',
          f'Luật Bảo hiểm xã hội số 41/2024/QH15 – {L("ty-le-dong-bh","tỷ lệ và căn cứ đóng")}',
          'Luật Việc làm số 74/2025/QH15 – đóng bảo hiểm thất nghiệp',
          f'Luật Bảo hiểm y tế (sửa đổi 2024) – Điều 22; Luật Công đoàn 2024 – {L("cong-doan","đoàn phí, kinh phí công đoàn")}'],
    rel=['bieu-thue-tncn-5-bac-2026', 'giam-tru-gia-canh-2026', 'ty-le-dong-bhxh-bhyt-bhtn-2026', 'luong-toi-thieu-vung-2026'],
    body=f'''
<h2 id="gross-net-la-gi">Lương Gross và lương Net khác nhau thế nào?</h2>
<p><strong>Lương Gross</strong> (lương tổng) là tổng thu nhập trước khi trừ bất cứ khoản nào – thường là con số ghi trong hợp đồng lao động hoặc thư mời nhận việc. <strong>Lương Net</strong> (lương thực nhận) là phần còn lại sau khi trừ:</p>
<ul>
<li><strong>Bảo hiểm bắt buộc</strong> phần người lao động đóng: BHXH 8%, BHYT 1,5%, BHTN 1% – tổng <strong>10,5%</strong> trên tiền lương đóng bảo hiểm.</li>
<li><strong>Thuế thu nhập cá nhân (TNCN)</strong> – chỉ phải nộp khi thu nhập sau giảm trừ còn dương.</li>
<li><strong>Đoàn phí công đoàn</strong> 1% (nếu bạn là đoàn viên), tối đa 253.000 đ/tháng.</li>
</ul>
<p>Khi đàm phán lương, hãy hỏi rõ con số được nói là Gross hay Net. Chênh lệch có thể lên tới vài triệu đồng mỗi tháng.</p>

<h2 id="cong-thuc">Công thức tính lương Net 2026 – 4 bước</h2>
<h3>Bước 1: Tính tiền bảo hiểm phải đóng</h3>
<p>Tiền bảo hiểm = Tiền lương đóng bảo hiểm × 10,5%. Tiền lương đóng bảo hiểm thường bằng lương trên hợp đồng (gồm lương chức danh và các khoản phụ cấp trả thường xuyên). Mức đóng tối đa của BHXH và BHYT là 20 lần mức tham chiếu, tức <strong>50.600.000 đ</strong> từ ngày 01/7/2026; BHTN tối đa 20 lần lương tối thiểu vùng.</p>
<h3>Bước 2: Tính thu nhập tính thuế</h3>
<div class="calc"><p><b>Thu nhập tính thuế</b> = Lương Gross − Bảo hiểm − 15.500.000 − (6.200.000 × số người phụ thuộc)</p></div>
<p>Các khoản được miễn thuế như tiền làm thêm giờ, làm ban đêm theo quy định cũng được loại ra trước khi tính. Nếu kết quả âm hoặc bằng 0, bạn không phải nộp thuế.</p>
<h3>Bước 3: Tính thuế TNCN theo biểu 5 bậc</h3>
{tbl(['Bậc','Thu nhập tính thuế/tháng','Thuế suất'],[['1','Đến 10 triệu','5%'],['2','Trên 10 – 30 triệu','10%'],['3','Trên 30 – 60 triệu','20%'],['4','Trên 60 – 100 triệu','30%'],['5','Trên 100 triệu','35%']],(2,))}
<p>Thuế được tính lũy tiến: phần thu nhập nằm trong bậc nào chịu thuế suất của bậc đó. Xem cách tính nhanh trong bài <a href="/bai-viet/bieu-thue-tncn-5-bac-2026/">Biểu thuế TNCN 5 bậc 2026</a>.</p>
<h3>Bước 4: Lương Net</h3>
<div class="calc"><p><b>Lương Net</b> = Lương Gross − Bảo hiểm − Thuế TNCN (− đoàn phí nếu có) + các khoản phụ cấp không tính vào Gross</p></div>

<h2 id="vi-du">Ví dụ: lương Gross 20 triệu cầm về bao nhiêu?</h2>
<p>Chị Lan làm việc tại Vùng I, lương hợp đồng 20.000.000 đ, đóng bảo hiểm trên toàn bộ lương, chưa có người phụ thuộc, không phải đoàn viên công đoàn.</p>
<div class="calc">
<p class="t">Tính lương Net của chị Lan</p>
<p>Bảo hiểm: BHXH 1.600.000 + BHYT 300.000 + BHTN 200.000 = <b>2.100.000 đ</b></p>
<p>Thu nhập tính thuế: 20.000.000 − 2.100.000 − 15.500.000 = <b>2.400.000 đ</b></p>
<p>Thuế TNCN (bậc 1): 2.400.000 × 5% = <b>120.000 đ</b></p>
<p>Lương Net: 20.000.000 − 2.100.000 − 120.000 = <b>17.780.000 đ</b></p>
</div>
<p>Nếu tính theo quy định năm 2025 (giảm trừ 11 triệu, biểu 7 bậc), thuế của chị Lan là 440.000 đ. Như vậy năm 2026 chị nộp ít hơn <strong>320.000 đ/tháng</strong>, tức 3.840.000 đ/năm.</p>

<h2 id="bang-luong">Bảng lương Net tham khảo năm 2026</h2>
<p>Giả định: làm việc tại Vùng I, đóng bảo hiểm trên toàn bộ lương Gross, không phải đoàn viên công đoàn.</p>
{tbl(['Lương Gross','Người phụ thuộc','Bảo hiểm (10,5%)','Thuế TNCN','Lương Net'],[
['10.000.000','0','1.050.000','0','<b>8.950.000</b>'],
['15.000.000','0','1.575.000','0','<b>13.425.000</b>'],
['20.000.000','0','2.100.000','120.000','<b>17.780.000</b>'],
['20.000.000','1','2.100.000','0','<b>17.900.000</b>'],
['30.000.000','0','3.150.000','635.000','<b>26.215.000</b>'],
['30.000.000','2','3.150.000','0','<b>26.850.000</b>'],
['50.000.000','0','5.250.000','2.425.000','<b>42.325.000</b>'],
['60.000.000','1','5.407.000','3.078.600','<b>51.514.400</b>']],(0,2,3,4))}
<p>Ở mức 60 triệu, BHXH và BHYT chỉ tính trên mức trần 50.600.000 đ nên tiền bảo hiểm không còn đúng 10,5%.</p>
{TOOL_LUONG}

<h2 id="dong-bh-thap">Trường hợp đóng bảo hiểm thấp hơn lương thực tế</h2>
<p>Nhiều công ty ghi lương hợp đồng cao nhưng chỉ đóng bảo hiểm trên một phần lương (ví dụ bằng lương tối thiểu vùng). Khi đó tiền bảo hiểm bị trừ ít hơn, lương Net tháng đó cao hơn. Đổi lại, các quyền lợi tính theo lương đóng bảo hiểm sẽ thấp đi: tiền thai sản, ốm đau, trợ cấp thất nghiệp, BHXH một lần và lương hưu.</p>
<div class="calc"><p class="t">Ví dụ: lương 15 triệu, đóng bảo hiểm theo lương tối thiểu Vùng I (5.310.000 đ)</p>
<p>Bảo hiểm: 5.310.000 × 10,5% = 557.550 đ · Thuế: 0 đ</p>
<p>Lương Net: 15.000.000 − 557.550 = <b>14.442.450 đ</b> (cao hơn 1.017.450 đ so với đóng đủ)</p>
<p>Nhưng nếu nghỉ việc, trợ cấp thất nghiệp chỉ còn 60% × 5.310.000 = 3.186.000 đ/tháng thay vì 9.000.000 đ.</p></div>
<div class="note"><b>Lưu ý:</b> Luật BHXH quy định tiền lương đóng bảo hiểm gồm mức lương và các khoản phụ cấp, khoản bổ sung trả thường xuyên, ổn định. Đóng thấp hơn mức luật định là vi phạm. Bạn có thể tra quá trình đóng trên ứng dụng VssID.</div>

<h2 id="luu-y">Một số lưu ý khi đọc bảng lương</h2>
<ul>
<li><strong>Người phụ thuộc</strong> chỉ được giảm trừ khi đã đăng ký với công ty hoặc cơ quan thuế.</li>
<li><strong>Tiền làm thêm giờ</strong> và tiền lương những ngày phép chưa nghỉ được trả theo luật thuộc diện miễn thuế. Phần thuế phải nộp trên phiếu lương có thể thấp hơn bảng tính trên.</li>
<li><strong>Quy định mới áp dụng cho cả năm 2026.</strong> Luật Thuế TNCN 2025 quy định phần thu nhập từ tiền lương áp dụng từ kỳ tính thuế năm 2026. Nếu đầu năm công ty còn khấu trừ theo cách cũ, số thuế nộp thừa sẽ được xử lý khi quyết toán.</li>
</ul>
''',
    faq=[('Lương bao nhiêu thì bắt đầu phải nộp thuế TNCN năm 2026?', 'Nếu đóng bảo hiểm trên toàn bộ lương và không có người phụ thuộc, lương Gross từ khoảng 17,3 triệu đồng/tháng trở lên mới phát sinh thuế. Có 1 người phụ thuộc thì khoảng 24,2 triệu, có 2 người phụ thuộc thì khoảng 31,2 triệu.'),
         ('Lương Net có bao gồm phụ cấp ăn trưa, xăng xe không?', 'Tùy công ty. Nếu phụ cấp được trả cùng lương thì nằm trong số tiền nhận về, nhưng có khoản phải tính thuế, có khoản được miễn hoặc không tính vào lương đóng bảo hiểm. Hãy xem chi tiết trên phiếu lương.'),
         ('Thử việc có bị trừ bảo hiểm không?', 'Nếu bạn ký hợp đồng thử việc riêng thì thường chưa đóng bảo hiểm. Nếu nội dung thử việc ghi trong hợp đồng lao động thì công ty phải đóng bảo hiểm ngay từ đầu.')]))

# 2 ─────────────────────────────────────────────
ARTICLES.append(dict(
    slug='bieu-thue-tncn-5-bac-2026', cat='thue', date=D,
    title='Biểu thuế TNCN 5 bậc 2026: cách tính thuế thu nhập cá nhân từ tiền lương',
    desc='Biểu thuế TNCN lũy tiến 5 bậc theo Luật Thuế TNCN 2025 áp dụng từ năm 2026: thuế suất 5%–35%, công thức tính nhanh, ví dụ và so sánh với biểu 7 bậc cũ.',
    lead='Từ kỳ tính thuế năm 2026, thuế thu nhập cá nhân đối với tiền lương, tiền công được tính theo biểu lũy tiến mới chỉ còn 5 bậc thay cho 7 bậc trước đây. Các bậc được nới rộng, nên hầu hết người làm công ăn lương nộp ít thuế hơn.',
    keys=['Biểu thuế mới có 5 bậc: <strong>5% – 10% – 20% – 30% – 35%</strong>.',
          'Bậc 1 rộng gấp đôi: thu nhập tính thuế đến <strong>10 triệu/tháng</strong> chỉ chịu 5%.',
          'Áp dụng cho thu nhập từ tiền lương, tiền công <strong>từ kỳ tính thuế năm 2026</strong>.'],
    laws=[f'Luật Thuế thu nhập cá nhân số 109/2025/QH15 – {L("bieu-thue-tncn","Điều 9: Biểu thuế lũy tiến từng phần")}',
          'Luật Thuế thu nhập cá nhân số 109/2025/QH15 – Điều 29: Điều khoản thi hành',
          f'{L("giam-tru-gia-canh","Điều 10: Giảm trừ gia cảnh")}; {L("thu-nhap-mien-thue","Điều 4: Thu nhập được miễn thuế")}'],
    rel=['cach-tinh-luong-net-tu-gross-2026', 'giam-tru-gia-canh-2026', 'luong-lam-them-gio'],
    body=f'''
<h2 id="bieu-thue">Biểu thuế lũy tiến từng phần năm 2026</h2>
<p>Theo Điều 9 Luật Thuế TNCN số 109/2025/QH15, thu nhập tính thuế từ tiền lương, tiền công của cá nhân cư trú áp dụng biểu thuế sau:</p>
{tbl(['Bậc','Thu nhập tính thuế/tháng','Thu nhập tính thuế/năm','Thuế suất'],[
['1','Đến 10 triệu','Đến 120 triệu','5%'],['2','Trên 10 đến 30 triệu','Trên 120 đến 360 triệu','10%'],
['3','Trên 30 đến 60 triệu','Trên 360 đến 720 triệu','20%'],['4','Trên 60 đến 100 triệu','Trên 720 đến 1.200 triệu','30%'],
['5','Trên 100 triệu','Trên 1.200 triệu','35%']],(3,))}

<h2 id="thu-nhap-tinh-thue">Thu nhập tính thuế là gì?</h2>
<p>Biểu thuế không áp lên toàn bộ lương. Trước hết phải tính <strong>thu nhập tính thuế</strong>:</p>
<div class="calc"><p>Thu nhập tính thuế = Tổng thu nhập chịu thuế − Bảo hiểm bắt buộc − Giảm trừ gia cảnh (15,5 triệu + 6,2 triệu × số người phụ thuộc) − Các khoản giảm trừ khác (từ thiện, quỹ hưu trí tự nguyện…)</p></div>
<p>Các khoản thu nhập được miễn thuế, như tiền lương làm việc ban đêm, làm thêm giờ, tiền lương những ngày không nghỉ phép theo quy định, không bị tính vào thu nhập chịu thuế.</p>

<h2 id="cach-tinh-nhanh">Công thức tính thuế nhanh</h2>
<p>Thay vì cộng thuế từng bậc, bạn có thể dùng bảng rút gọn sau (TN = thu nhập tính thuế/tháng):</p>
{tbl(['Thu nhập tính thuế/tháng','Số thuế phải nộp'],[
['Đến 10 triệu','TN × 5%'],['Trên 10 – 30 triệu','TN × 10% − 0,5 triệu'],['Trên 30 – 60 triệu','TN × 20% − 3,5 triệu'],
['Trên 60 – 100 triệu','TN × 30% − 9,5 triệu'],['Trên 100 triệu','TN × 35% − 14,5 triệu']])}
<div class="calc"><p class="t">Ví dụ: thu nhập tính thuế 35 triệu/tháng</p>
<p>Tính theo từng bậc: 10 tr × 5% + 20 tr × 10% + 5 tr × 20% = 0,5 + 2 + 1 = <b>3,5 triệu</b></p>
<p>Tính nhanh: 35 tr × 20% − 3,5 tr = <b>3,5 triệu</b> ✓</p></div>

<h2 id="so-sanh">So sánh với biểu thuế 7 bậc năm 2025</h2>
<p>Biểu cũ có 7 bậc (5%, 10%, 15%, 20%, 25%, 30%, 35%) với bậc 1 chỉ đến 5 triệu; giảm trừ bản thân 11 triệu, người phụ thuộc 4,4 triệu. Bảng dưới so sánh thuế phải nộp mỗi tháng (đóng bảo hiểm trên toàn bộ lương):</p>
{tbl(['Lương Gross','Người phụ thuộc','Thuế năm 2025','Thuế năm 2026','Giảm'],[
['15.000.000','0','121.250','0','121.250'],['20.000.000','0','440.000','120.000','320.000'],
['30.000.000','0','1.627.500','635.000','992.500'],['30.000.000','2','455.000','0','455.000'],
['50.000.000','0','5.187.500','2.425.000','2.762.500']],(0,2,3,4))}
<p>Mức giảm lớn nhất rơi vào nhóm thu nhập trung bình và khá, nhờ đồng thời được tăng giảm trừ gia cảnh và nới rộng các bậc thuế.</p>
{TOOL_LUONG}

<h2 id="ai-khau-tru">Ai khấu trừ và khi nào quyết toán?</h2>
<ul>
<li>Nếu bạn ký hợp đồng lao động từ 3 tháng trở lên, <strong>công ty khấu trừ thuế hằng tháng</strong> theo biểu lũy tiến và nộp thay bạn.</li>
<li>Cuối năm, công ty quyết toán thay nếu bạn ủy quyền và chỉ có thu nhập tại một nơi. Nếu có thu nhập từ nhiều nơi, bạn có thể phải <strong>tự quyết toán</strong> để nộp thêm hoặc được hoàn thuế.</li>
<li>Hợp đồng dưới 3 tháng hoặc thu nhập vãng lai thường bị khấu trừ 10% trên mỗi lần chi trả. Đây là quy định riêng, không áp dụng biểu lũy tiến.</li>
</ul>
''',
    faq=[('Biểu thuế 5 bậc áp dụng từ khi nào?', 'Luật Thuế TNCN số 109/2025/QH15 có hiệu lực từ 01/7/2026, nhưng các quy định về thu nhập từ tiền lương, tiền công của cá nhân cư trú áp dụng từ kỳ tính thuế năm 2026, tức cho toàn bộ thu nhập năm 2026.'),
         ('Thưởng Tết có bị tính thuế theo biểu này không?', 'Có. Tiền thưởng nằm trong thu nhập từ tiền lương, tiền công. Thưởng được cộng vào thu nhập của tháng chi trả để tính thuế, rồi đối chiếu lại khi quyết toán năm.')]))

# 3 ─────────────────────────────────────────────
ARTICLES.append(dict(
    slug='giam-tru-gia-canh-2026', cat='thue', date=D,
    title='Giảm trừ gia cảnh 2026: 15,5 triệu cho bản thân, 6,2 triệu mỗi người phụ thuộc',
    desc='Mức giảm trừ gia cảnh mới năm 2026: 15,5 triệu/tháng cho người nộp thuế, 6,2 triệu/tháng cho mỗi người phụ thuộc. Ai được đăng ký người phụ thuộc, lương bao nhiêu thì không phải nộp thuế.',
    lead='Giảm trừ gia cảnh là khoản được trừ khỏi thu nhập trước khi tính thuế TNCN. Từ năm 2026, mức giảm trừ tăng mạnh, nhờ vậy nhiều người có lương dưới 17 triệu đồng không còn phải nộp thuế.',
    keys=['Bản thân người nộp thuế: <strong>15,5 triệu/tháng</strong> (186 triệu/năm), trước đây 11 triệu.',
          'Mỗi người phụ thuộc: <strong>6,2 triệu/tháng</strong>, trước đây 4,4 triệu.',
          'Mỗi người phụ thuộc chỉ được tính cho <strong>một</strong> người nộp thuế.'],
    laws=[f'Luật Thuế thu nhập cá nhân số 109/2025/QH15 – {L("giam-tru-gia-canh","Điều 10: Giảm trừ gia cảnh")}'],
    rel=['bieu-thue-tncn-5-bac-2026', 'cach-tinh-luong-net-tu-gross-2026'],
    body=f'''
<h2 id="muc-giam-tru">Mức giảm trừ gia cảnh năm 2026</h2>
{tbl(['Đối tượng','Năm 2025','Từ năm 2026'],[['Người nộp thuế','11.000.000 đ/tháng','<b>15.500.000 đ/tháng</b>'],['Mỗi người phụ thuộc','4.400.000 đ/tháng','<b>6.200.000 đ/tháng</b>']],(1,2))}
<p>Theo khoản 2 Điều 10 Luật Thuế TNCN 2025, khi giá cả, thu nhập biến động, Chính phủ trình Ủy ban Thường vụ Quốc hội điều chỉnh mức giảm trừ cho phù hợp.</p>

<h2 id="khong-nop-thue">Lương bao nhiêu thì không phải nộp thuế?</h2>
<p>Nếu bạn đóng bảo hiểm 10,5% trên toàn bộ lương và không có thu nhập miễn thuế nào khác, mức lương Gross tối đa chưa phải nộp thuế như sau:</p>
{tbl(['Số người phụ thuộc','Tổng giảm trừ/tháng','Lương Gross tối đa không phải nộp thuế'],[
['0','15.500.000','≈ 17.318.000'],['1','21.700.000','≈ 24.245.000'],['2','27.900.000','≈ 31.173.000'],['3','34.100.000','≈ 38.100.000']],(1,2))}
<p>Cách tính: Lương Gross × (1 − 10,5%) = Tổng giảm trừ, suy ra Lương Gross = Tổng giảm trừ ÷ 0,895.</p>

<h2 id="nguoi-phu-thuoc">Ai được đăng ký là người phụ thuộc?</h2>
<p>Theo khoản 4 Điều 10, người phụ thuộc là người mà người nộp thuế có trách nhiệm nuôi dưỡng, gồm:</p>
<ul>
<li><strong>Con chưa thành niên</strong>; con mất năng lực hành vi dân sự, con khuyết tật, không có khả năng lao động.</li>
<li>Những người <strong>không có thu nhập hoặc có thu nhập không vượt quá mức do Bộ trưởng Bộ Tài chính quy định</strong>, gồm: con đã thành niên đang học đại học, cao đẳng, trung học chuyên nghiệp, học nghề; vợ hoặc chồng không có khả năng lao động; bố, mẹ đã hết tuổi lao động hoặc không có khả năng lao động; người khác không nơi nương tựa mà người nộp thuế phải trực tiếp nuôi dưỡng.</li>
</ul>
<div class="note"><b>Lưu ý:</b> Mỗi người phụ thuộc chỉ được tính giảm trừ một lần vào một người nộp thuế. Ví dụ, hai vợ chồng cùng đi làm thì con chỉ được đăng ký cho bố <em>hoặc</em> mẹ, không được cho cả hai.</div>

<h2 id="dang-ky">Cách đăng ký người phụ thuộc</h2>
<ol>
<li>Lấy mẫu đăng ký người phụ thuộc tại phòng nhân sự, hoặc tự đăng ký trên Cổng thông tin điện tử của Tổng cục Thuế / ứng dụng eTax Mobile.</li>
<li>Chuẩn bị giấy tờ chứng minh quan hệ: giấy khai sinh của con, giấy tờ xác nhận quan hệ với bố mẹ…; với người trong độ tuổi lao động thì thêm giấy tờ chứng minh không có khả năng lao động hoặc đang đi học.</li>
<li>Nộp cho công ty để được giảm trừ ngay từ tháng đăng ký, hoặc kê khai khi quyết toán cuối năm.</li>
</ol>
<div class="calc"><p class="t">Ví dụ: anh Minh lương 30 triệu, nuôi 2 con nhỏ</p>
<p>Bảo hiểm: 3.150.000 đ · Giảm trừ: 15.500.000 + 2 × 6.200.000 = 27.900.000 đ</p>
<p>Thu nhập tính thuế: 30.000.000 − 3.150.000 − 27.900.000 = −1.050.000 → <b>không phải nộp thuế</b></p>
<p>Nếu chưa đăng ký 2 con, anh Minh bị khấu trừ 635.000 đ/tháng.</p></div>
{TOOL_LUONG}
''',
    faq=[('Đăng ký người phụ thuộc muộn có được tính lại không?', 'Được. Nếu trong năm chưa đăng ký, bạn vẫn có thể kê khai khi quyết toán thuế năm. Giảm trừ được tính từ tháng phát sinh nghĩa vụ nuôi dưỡng, ví dụ từ tháng con sinh ra.'),
         ('Bố mẹ có lương hưu có được đăng ký người phụ thuộc không?', 'Chỉ được khi thu nhập bình quân tháng của bố mẹ không vượt mức do Bộ trưởng Bộ Tài chính quy định. Mức này cần xem tại văn bản hướng dẫn hiện hành.')]))

# 4 ─────────────────────────────────────────────
ARTICLES.append(dict(
    slug='luong-toi-thieu-vung-2026', cat='luong', date=D,
    title='Lương tối thiểu vùng 2026 theo Nghị định 293/2025: mức lương và cách xác định vùng',
    desc='Mức lương tối thiểu vùng năm 2026: Vùng I 5.310.000 đ, Vùng II 4.730.000 đ, Vùng III 4.140.000 đ, Vùng IV 3.700.000 đ. Cách xác định vùng theo xã, phường mới và những khoản bị ảnh hưởng.',
    lead='Lương tối thiểu vùng là mức sàn: doanh nghiệp không được trả thấp hơn cho người làm đủ giờ. Từ 01/01/2026, mức lương tối thiểu tăng khoảng 7% và được áp dụng theo danh mục 3.321 xã, phường sau sắp xếp đơn vị hành chính.',
    keys=['Vùng I <strong>5.310.000 đ</strong> · Vùng II <strong>4.730.000 đ</strong> · Vùng III <strong>4.140.000 đ</strong> · Vùng IV <strong>3.700.000 đ</strong>/tháng.',
          'Vùng được xác định theo <strong>nơi doanh nghiệp (chi nhánh) hoạt động</strong>, không theo nơi bạn ở.',
          'Lương tối thiểu vùng còn quyết định mức trần đóng BHTN và mức trần trợ cấp thất nghiệp.'],
    laws=[f'Nghị định 293/2025/NĐ-CP – {L("luong-toi-thieu-vung","Điều 3: Mức lương tối thiểu")} và Phụ lục danh mục địa bàn',
          'Bộ luật Lao động 2019 – Điều 90, 91',
          'Luật Việc làm số 74/2025/QH15 – Điều 39 (mức trần trợ cấp thất nghiệp)'],
    rel=['cach-tinh-luong-net-tu-gross-2026', 'tro-cap-that-nghiep-2026', 'ty-le-dong-bhxh-bhyt-bhtn-2026'],
    body=f'''
<h2 id="muc-luong">Mức lương tối thiểu vùng từ 01/01/2026</h2>
{tbl(['Vùng','Lương tối thiểu tháng','Lương tối thiểu giờ','Mức cũ (2025)','Tăng'],[
['Vùng I','<b>5.310.000</b>','25.500','4.960.000','+350.000'],['Vùng II','<b>4.730.000</b>','22.700','4.410.000','+320.000'],
['Vùng III','<b>4.140.000</b>','20.000','3.860.000','+280.000'],['Vùng IV','<b>3.700.000</b>','17.800','3.450.000','+250.000']],(1,2,3,4))}
<p>Lương tối thiểu tháng áp dụng cho người hưởng lương theo tháng. Lương tối thiểu giờ áp dụng cho người hưởng lương theo giờ, ví dụ lao động bán thời gian.</p>

<h2 id="xac-dinh-vung">Xác định mình thuộc vùng nào</h2>
<p>Theo Điều 3 Nghị định 293/2025/NĐ-CP, vùng lương được xác định theo <strong>nơi hoạt động của người sử dụng lao động</strong>:</p>
<ul>
<li>Doanh nghiệp hoạt động ở địa bàn thuộc vùng nào thì áp dụng mức của vùng đó.</li>
<li>Doanh nghiệp có chi nhánh ở nhiều địa bàn: chi nhánh ở đâu áp dụng mức ở đó.</li>
<li>Doanh nghiệp trong <strong>khu công nghiệp, khu chế xuất, khu công nghệ cao</strong> nằm trên nhiều địa bàn có mức khác nhau: áp dụng <strong>mức cao nhất</strong>.</li>
<li>Địa bàn đổi tên hoặc chia tách: tạm giữ mức cũ. Địa bàn thành lập mới từ nhiều địa bàn có mức khác nhau: áp dụng mức cao nhất.</li>
</ul>
<div class="tip">Sau sắp xếp năm 2025, cả nước còn 34 tỉnh, thành và 3.321 xã, phường. Cách nhanh nhất là chọn tỉnh và xã, phường nơi bạn làm việc trong <a href="/">công cụ tính lương</a>: web tự hiện vùng lương tương ứng.</div>

<h2 id="anh-huong">Lương tối thiểu vùng ảnh hưởng đến những khoản nào?</h2>
{tbl(['Khoản','Vùng I','Vùng II','Vùng III','Vùng IV'],[
['Sàn lương hợp đồng (làm đủ giờ)','5.310.000','4.730.000','4.140.000','3.700.000'],
['Trần lương đóng BHTN (20 lần)','106.200.000','94.600.000','82.800.000','74.000.000'],
['Trần trợ cấp thất nghiệp/tháng (5 lần)','26.550.000','23.650.000','20.700.000','18.500.000']],(1,2,3,4))}
<ul>
<li><strong>Lương hợp đồng</strong> cho công việc giản đơn nhất, làm đủ thời giờ làm việc bình thường và đạt định mức, không được thấp hơn mức tối thiểu vùng.</li>
<li><strong>Tiền lương đóng bảo hiểm</strong> trên thực tế cũng không thấp hơn lương tối thiểu vùng, vì lương hợp đồng không được thấp hơn mức này.</li>
<li><strong>Trợ cấp thất nghiệp</strong> tối đa bằng 5 lần lương tối thiểu vùng của tháng cuối cùng đóng BHTN.</li>
</ul>

<h2 id="luu-y">Lưu ý quan trọng</h2>
<ul>
<li>Lương tối thiểu vùng <strong>khác lương cơ sở</strong>. Lương cơ sở (2.530.000 đ từ 01/7/2026) dùng để tính lương khu vực nhà nước và làm mức tham chiếu đóng BHXH. Doanh nghiệp tư nhân trả lương theo thỏa thuận, có sàn là lương tối thiểu vùng.</li>
<li>Quy định cũ buộc lao động đã qua học nghề phải được trả cao hơn ít nhất 7% đã bỏ từ năm 2021. Tuy vậy, nếu thỏa ước hoặc quy chế lương của công ty vẫn ghi mức này thì công ty vẫn phải thực hiện.</li>
<li>Nghị định 293/2025 có quy định bảo vệ người đã được tuyển dụng trước: nếu do điều chỉnh địa bàn mà mức mới thấp hơn mức đang áp dụng ngày 31/12/2025, thì người lao động tuyển dụng từ ngày đó trở về trước vẫn được giữ mức cũ.</li>
</ul>
{TOOL_LUONG}
''',
    faq=[('Làm ở văn phòng Hà Nội nhưng công ty đăng ký ở tỉnh khác thì tính vùng nào?', 'Tính theo nơi đơn vị trực tiếp sử dụng bạn hoạt động, tức địa bàn của văn phòng hoặc chi nhánh nơi bạn làm việc, không theo trụ sở công ty mẹ.'),
         ('Lương thử việc có được thấp hơn lương tối thiểu vùng không?', 'Lương thử việc tối thiểu bằng 85% lương của công việc đó. Còn lương chính thức của công việc đó, khi làm đủ giờ, không được thấp hơn lương tối thiểu vùng.')]))

# 5 ─────────────────────────────────────────────
ARTICLES.append(dict(
    slug='ty-le-dong-bhxh-bhyt-bhtn-2026', cat='bh', date=D,
    title='Tỷ lệ đóng BHXH, BHYT, BHTN năm 2026 của người lao động và doanh nghiệp',
    desc='Bảng tỷ lệ đóng bảo hiểm bắt buộc năm 2026: người lao động 10,5%, doanh nghiệp 21,5% (cộng 2% kinh phí công đoàn). Mức đóng tối đa, tối thiểu và ví dụ cụ thể.',
    lead='Mỗi tháng, ngoài tiền lương trả cho bạn, công ty còn phải đóng thêm hơn 20% vào các quỹ bảo hiểm. Bài này tổng hợp ai đóng bao nhiêu, đóng trên mức lương nào, và giới hạn trên dưới năm 2026.',
    keys=['Người lao động đóng <strong>10,5%</strong>: BHXH 8%, BHYT 1,5%, BHTN 1%.',
          'Doanh nghiệp đóng <strong>21,5%</strong>, cộng thêm <strong>2% kinh phí công đoàn</strong>, tổng 23,5%.',
          'Lương đóng BHXH, BHYT tối đa <strong>50.600.000 đ</strong> (20 lần mức tham chiếu 2.530.000 đ, từ 01/7/2026).'],
    laws=[f'Luật Bảo hiểm xã hội số 41/2024/QH15 – Điều 31 (căn cứ đóng), Điều 33, 34 (tỷ lệ đóng) – {L("ty-le-dong-bh","xem nguyên văn")}',
          'Luật Bảo hiểm y tế (sửa đổi 2024) – Điều 22',
          f'Luật Việc làm số 74/2025/QH15 – đóng bảo hiểm thất nghiệp – {L("bhtn","xem nguyên văn")}',
          f'Luật Công đoàn số 50/2024/QH15 – {L("cong-doan","Điều 29, 30")}',
          'Nghị định 161/2026/NĐ-CP – lương cơ sở 2.530.000 đ'],
    rel=['cach-tinh-luong-net-tu-gross-2026', 'rut-bhxh-1-lan-2026', 'tro-cap-that-nghiep-2026'],
    body=f'''
<h2 id="bang-ty-le">Bảng tỷ lệ đóng bảo hiểm bắt buộc năm 2026</h2>
{tbl(['Khoản đóng','Người lao động','Doanh nghiệp','Tổng'],[
['BHXH – Quỹ hưu trí, tử tuất','8%','14%','22%'],['BHXH – Quỹ ốm đau, thai sản','–','3%','3%'],
['BHXH – Quỹ tai nạn lao động, bệnh nghề nghiệp','–','0,5%','0,5%'],['Bảo hiểm y tế','1,5%','3%','4,5%'],
['Bảo hiểm thất nghiệp','1%','1%','2%'],['<b>Cộng bảo hiểm</b>','<b>10,5%</b>','<b>21,5%</b>','<b>32%</b>'],
['Kinh phí công đoàn','–','2%','2%'],['Đoàn phí công đoàn (nếu là đoàn viên)','1% (tối đa 253.000 đ)','–','']],(1,2,3))}
<p>Tỷ lệ đóng vào quỹ tai nạn lao động, bệnh nghề nghiệp có thể là 0,3% với doanh nghiệp thuộc ngành nghề có nguy cơ thấp và đủ điều kiện theo hướng dẫn. Bảng trên dùng mức phổ biến 0,5%.</p>

<h2 id="muc-luong-dong">Đóng trên mức lương nào?</h2>
<p>Theo Điều 31 Luật BHXH 2024, với người lao động hưởng lương do doanh nghiệp quyết định, tiền lương đóng bảo hiểm là <strong>tiền lương tháng</strong>, gồm mức lương theo công việc hoặc chức danh, phụ cấp lương và các khoản bổ sung khác được thỏa thuận trả thường xuyên, ổn định trong mỗi kỳ trả lương.</p>
{tbl(['Giới hạn','Mức năm 2026'],[
['Tối thiểu (BHXH)','Mức tham chiếu; thực tế không thấp hơn lương tối thiểu vùng vì lương hợp đồng không được thấp hơn mức này'],
['Tối đa BHXH, BHYT','20 × 2.530.000 = <b>50.600.000 đ</b> (từ 01/7/2026)'],
['Tối đa BHTN','20 × lương tối thiểu vùng (Vùng I: 106.200.000 đ)']])}

<h2 id="vi-du">Ví dụ tính tiền đóng bảo hiểm</h2>
<div class="calc"><p class="t">Lương 20.000.000 đ, đóng đủ trên toàn bộ lương</p>
<p>Người lao động: 20.000.000 × 10,5% = <b>2.100.000 đ</b> (BHXH 1.600.000 · BHYT 300.000 · BHTN 200.000)</p>
<p>Doanh nghiệp: 20.000.000 × 21,5% = <b>4.300.000 đ</b> + kinh phí công đoàn 400.000 đ = 4.700.000 đ</p>
<p>Tổng chi phí doanh nghiệp bỏ ra cho bạn: 20.000.000 + 4.700.000 = <b>24.700.000 đ/tháng</b></p></div>
<div class="calc"><p class="t">Lương 60.000.000 đ – vượt trần</p>
<p>BHXH: 50.600.000 × 8% = 4.048.000 đ · BHYT: 50.600.000 × 1,5% = 759.000 đ</p>
<p>BHTN: 60.000.000 × 1% = 600.000 đ (chưa vượt trần 106,2 triệu ở Vùng I)</p>
<p>Người lao động đóng: <b>5.407.000 đ</b>, thấp hơn 10,5% × 60 triệu = 6.300.000 đ</p></div>
{TOOL_LUONG}

<h2 id="quyen-loi">Đóng bảo hiểm để được gì?</h2>
<ul>
<li><strong>Hưu trí:</strong> từ 01/7/2025 chỉ cần đủ <strong>15 năm</strong> đóng BHXH là đủ điều kiện về thời gian đóng để hưởng lương hưu khi đủ tuổi.</li>
<li><strong>Ốm đau, thai sản:</strong> trợ cấp khi ốm, khi sinh con, khám thai… tính theo lương đóng bảo hiểm.</li>
<li><strong>Tai nạn lao động, bệnh nghề nghiệp:</strong> trợ cấp một lần hoặc hằng tháng.</li>
<li><strong>Thất nghiệp:</strong> trợ cấp 60% lương bình quân, hỗ trợ học nghề, tư vấn việc làm (xem <a href="/bai-viet/tro-cap-that-nghiep-2026/">trợ cấp thất nghiệp 2026</a>).</li>
<li><strong>Y tế:</strong> thẻ BHYT chi trả chi phí khám chữa bệnh.</li>
</ul>
<div class="note"><b>Tự kiểm tra:</b> Tải ứng dụng <b>VssID</b> của BHXH Việt Nam để xem công ty có đóng đủ, đúng mức lương hay không. Trường hợp công ty trừ tiền bảo hiểm trong lương mà không đóng, bạn có quyền khiếu nại tới cơ quan BHXH hoặc thanh tra lao động.</div>
''',
    faq=[('Phụ cấp ăn trưa có phải đóng bảo hiểm không?', 'Khoản hỗ trợ không gắn với công việc, không trả thường xuyên ổn định như tiền ăn giữa ca, hỗ trợ đi lại theo hướng dẫn thường không tính vào lương đóng bảo hiểm. Các khoản phụ cấp gắn với chức danh, điều kiện làm việc thì phải đóng.'),
         ('Làm hai công ty thì đóng bảo hiểm ở đâu?', 'Mỗi hợp đồng lao động thuộc diện bắt buộc đều phải đóng BHXH. Riêng BHYT chỉ đóng một lần, ở hợp đồng có mức lương cao nhất. Bạn nên báo cho cả hai công ty để tránh đóng trùng.')]))

# 6 ─────────────────────────────────────────────
ARTICLES.append(dict(
    slug='rut-bhxh-1-lan-2026', cat='bh', date=D,
    title='Rút BHXH 1 lần năm 2026: điều kiện, cách tính tiền và những điều cần biết',
    desc='Điều kiện rút BHXH một lần theo Luật BHXH 2024 áp dụng năm 2026, cách tính số tiền nhận (1,5 và 2 tháng lương bình quân mỗi năm đóng), ví dụ cụ thể và nên rút hay không.',
    lead='Từ 01/7/2025, Luật Bảo hiểm xã hội 2024 siết điều kiện rút BHXH một lần. Người bắt đầu đóng từ ngày này về sau gần như không thể rút chỉ vì nghỉ việc. Bài này giúp bạn biết mình có được rút không, rút được bao nhiêu và nên cân nhắc điều gì.',
    keys=['Người <strong>có thời gian đóng trước 01/7/2025</strong>: sau 12 tháng không đóng BHXH bắt buộc lẫn tự nguyện và chưa đủ 20 năm đóng thì được rút.',
          'Người bắt đầu đóng <strong>từ 01/7/2025</strong> chỉ được rút trong các trường hợp đặc biệt: đủ tuổi hưu mà chưa đủ 15 năm, ra nước ngoài định cư, mắc bệnh hiểm nghèo…',
          'Mỗi năm đóng được <strong>1,5 tháng</strong> lương bình quân (trước 2014) hoặc <strong>2 tháng</strong> (từ 2014).'],
    laws=[f'Luật Bảo hiểm xã hội số 41/2024/QH15 – {L("bhxh-mot-lan","Điều 70: Hưởng bảo hiểm xã hội một lần")}',
          'Luật Bảo hiểm xã hội số 41/2024/QH15 – Điều 72 (bình quân tiền lương), Điều 73 (điều chỉnh tiền lương đã đóng)',
          'Văn bản công bố hệ số trượt giá áp dụng năm 2026'],
    rel=['ty-le-dong-bhxh-bhyt-bhtn-2026', 'tro-cap-that-nghiep-2026', 'tro-cap-thoi-viec-mat-viec'],
    body=f'''
<h2 id="dieu-kien">Điều kiện rút BHXH một lần năm 2026</h2>
<p>Theo khoản 1 Điều 70 Luật BHXH 2024, người lao động đã chấm dứt tham gia BHXH và có đề nghị thì được hưởng BHXH một lần nếu thuộc <strong>một trong các trường hợp</strong>:</p>
<ol type="a">
<li>Đủ tuổi hưởng lương hưu mà chưa đủ 15 năm đóng BHXH (hoặc có thể chọn nhận trợ cấp hằng tháng);</li>
<li>Ra nước ngoài để định cư;</li>
<li>Đang mắc một trong các bệnh ung thư, bại liệt, xơ gan mất bù, lao nặng, AIDS;</li>
<li>Suy giảm khả năng lao động từ 81% trở lên; người khuyết tật đặc biệt nặng;</li>
<li><strong>Có thời gian đóng BHXH trước ngày 01/7/2025</strong>, sau 12 tháng không thuộc diện đóng BHXH bắt buộc mà cũng không đóng BHXH tự nguyện, và có thời gian đóng chưa đủ 20 năm;</li>
<li>Một số đối tượng thuộc lực lượng vũ trang khi phục viên, xuất ngũ, thôi việc không tiếp tục tham gia BHXH và không đủ điều kiện hưởng lương hưu.</li>
</ol>
<div class="note"><b>Điểm mấu chốt:</b> Trường hợp “nghỉ việc chờ 12 tháng rồi rút” (điểm đ) chỉ dành cho người <b>đã có thời gian đóng trước 01/7/2025</b>. Nếu bạn đi làm và đóng BHXH lần đầu từ 01/7/2025 trở đi, bạn không thể rút chỉ vì nghỉ việc. Thời gian đóng được bảo lưu để cộng dồn khi đi làm lại.</div>

<h2 id="cach-tinh">Cách tính số tiền BHXH một lần</h2>
<p>Theo khoản 3 Điều 70, mỗi năm đóng được tính:</p>
{tbl(['Giai đoạn đóng','Mức hưởng mỗi năm'],[['Trước năm 2014','1,5 tháng mức bình quân tiền lương đóng BHXH'],['Từ năm 2014 trở đi','2 tháng mức bình quân tiền lương đóng BHXH'],['Đóng chưa đủ 1 năm','Bằng số tiền đã đóng, tối đa 2 tháng mức bình quân']])}
<div class="calc"><p><b>Tiền BHXH 1 lần</b> = (1,5 × số năm trước 2014 + 2 × số năm từ 2014) × Mức bình quân tiền lương đã điều chỉnh</p></div>
<ul>
<li><strong>Mức bình quân tiền lương</strong>: lấy tiền lương đóng BHXH của từng tháng nhân với <strong>hệ số trượt giá</strong> của năm đó (để bù lạm phát), cộng lại rồi chia cho tổng số tháng đã đóng.</li>
<li><strong>Tháng lẻ trước 2014</strong> được chuyển sang giai đoạn từ 2014 để tính.</li>
<li><strong>Tháng lẻ</strong> theo hướng dẫn: từ 1 đến 6 tháng tính là nửa năm, từ 7 đến 11 tháng tính là một năm.</li>
</ul>
{tbl(['Năm đóng','2018','2019','2020','2021','2022','2023','2024','2025'],[['Hệ số trượt giá áp dụng năm 2026','1,23','1,20','1,16','1,14','1,11','1,07','1,03','1,00']])}

<h2 id="vi-du">Ví dụ tính tiền BHXH một lần</h2>
<p>Anh Tuấn đóng BHXH liên tục từ 01/2018 đến 12/2025 (8 năm). Mức lương đóng là 8.000.000 đ giai đoạn 2018–2021 và 10.000.000 đ giai đoạn 2022–2025. Anh nghỉ việc từ 01/2026 và không tham gia BHXH nữa.</p>
<div class="calc"><p class="t">Tính tiền BHXH một lần của anh Tuấn</p>
<p>2018–2021: 8.000.000 × 12 × (1,23 + 1,20 + 1,16 + 1,14) = 454.080.000 đ</p>
<p>2022–2025: 10.000.000 × 12 × (1,11 + 1,07 + 1,03 + 1,00) = 505.200.000 đ</p>
<p>Mức bình quân: (454.080.000 + 505.200.000) ÷ 96 tháng = <b>9.992.500 đ</b></p>
<p>Số tiền nhận: 2 × 8 năm × 9.992.500 = <b>159.880.000 đ</b></p>
<p>Anh Tuấn có thời gian đóng trước 01/7/2025, nên sớm nhất từ <b>01/2027</b> (sau 12 tháng không đóng) mới đủ điều kiện nộp hồ sơ.</p></div>
{TOOL_BHXH}

<h2 id="nen-rut-khong">Có nên rút BHXH một lần?</h2>
<p>Rút BHXH một lần nghĩa là <strong>xóa toàn bộ thời gian đã đóng</strong>. Trước khi quyết định, hãy cân nhắc:</p>
<ul>
<li><strong>Lương hưu:</strong> chỉ cần 15 năm đóng là đủ điều kiện về thời gian. Nếu bạn đã có 8–10 năm, giữ lại và đóng tiếp, kể cả đóng tự nguyện, sẽ có lương hưu hằng tháng và thẻ BHYT suốt đời.</li>
<li><strong>Số tiền nhận khi rút</strong> chỉ tương ứng phần quỹ hưu trí đã đóng (22%/tháng) cộng phần điều chỉnh trượt giá. Thường thấp hơn nhiều so với tổng lương hưu nhận được về sau.</li>
<li>Người <strong>không rút</strong> mà chưa đủ điều kiện hưởng lương hưu, khi đủ tuổi có thể được nhận <strong>trợ cấp hằng tháng</strong> theo Điều 23 Luật BHXH 2024 (với điều kiện nhất định).</li>
</ul>

<h2 id="ho-so">Hồ sơ và nơi nộp</h2>
<ul>
<li>Đơn đề nghị hưởng BHXH một lần theo mẫu của cơ quan BHXH;</li>
<li>Sổ BHXH (hoặc mã số BHXH), căn cước công dân;</li>
<li>Giấy tờ chứng minh trường hợp đặc biệt nếu có: giấy xác nhận định cư, hồ sơ bệnh án, biên bản giám định…</li>
</ul>
<p>Có thể nộp trực tuyến qua Cổng dịch vụ công quốc gia, ứng dụng VssID hoặc nộp trực tiếp tại cơ quan BHXH nơi cư trú. Thời điểm tính hưởng là thời điểm cơ quan BHXH ra quyết định hưởng (khoản 5 Điều 70).</p>
''',
    faq=[('Tôi bắt đầu đóng BHXH tháng 8/2025, nghỉ việc năm 2026 có rút được không?', 'Không, trừ khi thuộc các trường hợp đặc biệt (đủ tuổi hưu chưa đủ 15 năm, định cư nước ngoài, bệnh hiểm nghèo, suy giảm khả năng lao động từ 81%…). Thời gian đóng được bảo lưu và cộng dồn khi bạn đi làm lại.'),
         ('Đang nhận trợ cấp thất nghiệp có rút BHXH 1 lần được không?', 'Hai chế độ khác nhau. Điều kiện rút BHXH một lần (điểm đ) là phải đủ 12 tháng không tham gia BHXH, nên thường bạn chỉ nộp được hồ sơ sau khi đã hết thời gian chờ này.')]))

# 7 ─────────────────────────────────────────────
ARTICLES.append(dict(
    slug='tro-cap-that-nghiep-2026', cat='bh', date=D,
    title='Trợ cấp thất nghiệp 2026: điều kiện, mức hưởng và thời gian hưởng',
    desc='Trợ cấp thất nghiệp theo Luật Việc làm 2025 áp dụng từ 01/01/2026: điều kiện 12 tháng đóng BHTN, mức hưởng 60% lương bình quân (tối đa 5 lần lương tối thiểu vùng), thời gian hưởng 3–12 tháng, ví dụ cụ thể.',
    lead='Mất việc, bạn có thể nhận trợ cấp thất nghiệp hằng tháng từ quỹ bảo hiểm thất nghiệp mà bạn và công ty đã đóng. Từ 01/01/2026, chế độ này được thực hiện theo Luật Việc làm số 74/2025/QH15.',
    keys=['Điều kiện chính: đóng BHTN <strong>đủ 12 tháng trong 24 tháng</strong> trước khi nghỉ và nộp hồ sơ trong <strong>3 tháng</strong>.',
          'Mức hưởng: <strong>60%</strong> bình quân lương đóng BHTN 6 tháng gần nhất, tối đa 5 lần lương tối thiểu vùng.',
          'Đóng 12–36 tháng hưởng <strong>3 tháng</strong>; thêm mỗi 12 tháng được thêm 1 tháng, tối đa <strong>12 tháng</strong>.'],
    laws=[f'Luật Việc làm số 74/2025/QH15 – {L("bhtn","Điều 38: Điều kiện hưởng, Điều 39: Mức hưởng, thời gian hưởng")}',
          'Nghị định 293/2025/NĐ-CP – lương tối thiểu vùng (mức trần trợ cấp)'],
    rel=['tro-cap-thoi-viec-mat-viec', 'rut-bhxh-1-lan-2026', 'luong-toi-thieu-vung-2026'],
    body=f'''
<h2 id="dieu-kien">Điều kiện hưởng trợ cấp thất nghiệp</h2>
<p>Theo Điều 38 Luật Việc làm 2025, người lao động đang đóng BHTN được hưởng trợ cấp khi có <strong>đủ</strong> các điều kiện:</p>
<ol>
<li><strong>Đã chấm dứt hợp đồng lao động</strong> hoặc hợp đồng làm việc, trừ trường hợp người lao động đơn phương chấm dứt hợp đồng <em>trái pháp luật</em>, hoặc nghỉ việc khi đã đủ điều kiện hưởng lương hưu.</li>
<li><strong>Đã đóng BHTN từ đủ 12 tháng</strong> trong 24 tháng trước khi chấm dứt hợp đồng. Với hợp đồng từ 1 tháng đến dưới 12 tháng: đủ 12 tháng trong 36 tháng.</li>
<li><strong>Nộp đủ hồ sơ trong 3 tháng</strong> kể từ ngày chấm dứt hợp đồng.</li>
<li>Trong <strong>10 ngày làm việc</strong> kể từ ngày nộp hồ sơ, chưa có việc làm mới thuộc diện đóng BHXH bắt buộc, không đi nghĩa vụ quân sự, không đi học trên 12 tháng, không ra nước ngoài định cư…</li>
</ol>
<div class="note"><b>Nghỉ việc đúng luật:</b> Nếu bạn tự xin nghỉ, hãy báo trước đủ thời hạn theo Bộ luật Lao động (thường 45 ngày với hợp đồng không xác định thời hạn, 30 ngày với hợp đồng 12–36 tháng). Nghỉ ngang trái luật sẽ mất quyền hưởng trợ cấp thất nghiệp.</div>

<h2 id="muc-huong">Mức hưởng trợ cấp thất nghiệp</h2>
<div class="calc"><p><b>Trợ cấp hằng tháng</b> = 60% × Bình quân tiền lương đóng BHTN của 06 tháng gần nhất</p><p>Tối đa bằng 5 lần lương tối thiểu vùng của tháng cuối cùng đóng BHTN.</p></div>
{tbl(['Vùng','Lương tối thiểu','Trợ cấp tối đa/tháng'],[['Vùng I','5.310.000','26.550.000'],['Vùng II','4.730.000','23.650.000'],['Vùng III','4.140.000','20.700.000'],['Vùng IV','3.700.000','18.500.000']],(1,2))}

<h2 id="thoi-gian">Thời gian hưởng</h2>
{tbl(['Số tháng đã đóng BHTN','Số tháng được hưởng'],[['Đủ 12 – đủ 36 tháng','3 tháng'],['Đủ 48 tháng','4 tháng'],['Đủ 60 tháng','5 tháng'],['…mỗi 12 tháng thêm','+1 tháng'],['Đủ 144 tháng trở lên','12 tháng (tối đa)']])}
<p>Trợ cấp được tính từ <strong>ngày làm việc thứ 11</strong> kể từ ngày nộp đủ hồ sơ. Trong thời gian hưởng, bạn còn được cấp thẻ BHYT do quỹ BHTN đóng.</p>

<h2 id="vi-du">Ví dụ tính trợ cấp thất nghiệp</h2>
<div class="calc"><p class="t">Chị Hoa làm việc ở Vùng I, đóng BHTN 50 tháng, lương đóng 6 tháng cuối đều là 12.000.000 đ</p>
<p>Mức hưởng: 60% × 12.000.000 = <b>7.200.000 đ/tháng</b> (dưới mức trần 26.550.000 đ)</p>
<p>Thời gian hưởng: 36 tháng đầu → 3 tháng; 12 tháng tiếp theo → +1 tháng = <b>4 tháng</b></p>
<p>Tổng nhận: 7.200.000 × 4 = <b>28.800.000 đ</b></p></div>
<p>Nếu chị Hoa chỉ được công ty đóng bảo hiểm theo lương tối thiểu vùng (5.310.000 đ), mức hưởng chỉ còn 3.186.000 đ/tháng. Đây là lý do nên kiểm tra mức lương đóng bảo hiểm trên VssID.</p>

<h2 id="thu-tuc">Hồ sơ và thủ tục</h2>
<ol>
<li>Lấy <strong>quyết định nghỉ việc</strong> hoặc giấy tờ chứng minh chấm dứt hợp đồng, và đề nghị công ty <strong>chốt sổ BHXH</strong>.</li>
<li>Trong 3 tháng, nộp hồ sơ tại <strong>Trung tâm dịch vụ việc làm</strong> (hoặc nộp trực tuyến qua Cổng dịch vụ công): đơn đề nghị, giấy tờ chấm dứt hợp đồng, sổ BHXH.</li>
<li>Nhận quyết định hưởng, sau đó <strong>thông báo tình hình tìm kiếm việc làm</strong> hằng tháng theo lịch hẹn. Bỏ thông báo có thể bị tạm dừng hoặc chấm dứt hưởng.</li>
</ol>
''',
    faq=[('Tự xin nghỉ việc có được hưởng trợ cấp thất nghiệp không?', 'Có, nếu bạn nghỉ đúng luật (báo trước đủ thời hạn hoặc thuộc trường hợp được nghỉ không cần báo trước) và đủ các điều kiện về thời gian đóng, thời hạn nộp hồ sơ.'),
         ('Có việc làm mới khi đang hưởng thì sao?', 'Bạn phải thông báo cho trung tâm dịch vụ việc làm. Việc hưởng trợ cấp sẽ chấm dứt khi có việc làm thuộc diện đóng BHXH bắt buộc.')]))

# 8 ─────────────────────────────────────────────
ARTICLES.append(dict(
    slug='tro-cap-thoi-viec-mat-viec', cat='lv', date=D,
    title='Trợ cấp thôi việc và trợ cấp mất việc làm: ai được nhận, tính thế nào?',
    desc='Phân biệt trợ cấp thôi việc (nửa tháng lương mỗi năm) và trợ cấp mất việc làm (1 tháng lương mỗi năm, ít nhất 2 tháng) theo Bộ luật Lao động 2019, cách tính thời gian, ví dụ cụ thể.',
    lead='Khi nghỉ việc, nhiều người thắc mắc vì sao không được công ty trả trợ cấp thôi việc. Câu trả lời thường nằm ở thời gian đã đóng bảo hiểm thất nghiệp. Bài này giải thích hai loại trợ cấp do công ty chi trả và cách tự tính.',
    keys=['<strong>Trợ cấp thôi việc:</strong> mỗi năm làm việc được <strong>nửa tháng lương</strong>.',
          '<strong>Trợ cấp mất việc làm</strong> (do công ty cắt giảm, tái cơ cấu): mỗi năm <strong>1 tháng lương</strong>, ít nhất <strong>2 tháng</strong>.',
          'Thời gian đã đóng <strong>bảo hiểm thất nghiệp</strong> bị trừ ra, vì phần này đã được quỹ BHTN bảo đảm.'],
    laws=[f'Bộ luật Lao động 2019 – {L("thoi-viec","Điều 46: Trợ cấp thôi việc, Điều 47: Trợ cấp mất việc làm")}',
          'Bộ luật Lao động 2019 – Điều 34, 36, 40, 42, 43',
          'Nghị định 145/2020/NĐ-CP – Điều 8 (cách tính trợ cấp)'],
    rel=['tro-cap-that-nghiep-2026', 'nghi-phep-nam', 'rut-bhxh-1-lan-2026'],
    body=f'''
<h2 id="phan-biet">Phân biệt hai loại trợ cấp</h2>
{tbl(['','Trợ cấp thôi việc','Trợ cấp mất việc làm'],[
['Khi nào','Hợp đồng chấm dứt theo các khoản 1, 2, 3, 4, 6, 7, 9, 10 Điều 34 BLLĐ: hết hạn hợp đồng, hai bên thỏa thuận, người lao động hoặc công ty đơn phương chấm dứt đúng luật…','Mất việc do thay đổi cơ cấu, công nghệ, vì lý do kinh tế, hoặc do chia, tách, hợp nhất, sáp nhập doanh nghiệp (khoản 11 Điều 34)'],
['Điều kiện','Làm việc thường xuyên cho công ty từ đủ 12 tháng','Làm việc thường xuyên cho công ty từ đủ 12 tháng'],
['Mức','½ tháng lương × số năm','1 tháng lương × số năm, <b>ít nhất 2 tháng</b>'],
['Ai trả','Công ty','Công ty']])}
<p><strong>Không được trợ cấp thôi việc</strong> khi: đủ điều kiện hưởng lương hưu; tự ý bỏ việc 5 ngày làm việc liên tục trở lên không có lý do chính đáng (bị coi là đơn phương chấm dứt, điểm e khoản 1 Điều 36); hoặc người lao động đơn phương chấm dứt hợp đồng trái pháp luật (Điều 40).</p>

<h2 id="thoi-gian-tinh">Thời gian làm việc để tính trợ cấp</h2>
<div class="calc"><p><b>Thời gian tính trợ cấp</b> = Tổng thời gian làm việc thực tế cho công ty − Thời gian đã đóng BHTN − Thời gian đã được trả trợ cấp thôi việc/mất việc trước đó</p></div>
<p>BHTN bắt đầu thực hiện từ 01/01/2009. Vì vậy người được đóng BHTN đầy đủ thường chỉ còn tính trợ cấp cho:</p>
<ul>
<li>Thời gian làm việc <strong>trước năm 2009</strong>;</li>
<li>Thời gian <strong>thử việc</strong>, thời gian công ty không đóng BHTN dù thuộc diện phải đóng (khi đó công ty vẫn phải trả trợ cấp cho phần này);</li>
<li>Thời gian nghỉ ốm, thai sản hưởng BHXH, thời gian nghỉ có hưởng lương… vẫn được tính là thời gian làm việc thực tế theo hướng dẫn tại Nghị định 145/2020.</li>
</ul>
<p>Tháng lẻ: theo Nghị định 145/2020, dưới hoặc bằng 6 tháng tính <strong>½ năm</strong>, trên 6 tháng tính <strong>1 năm</strong>.</p>
<p><strong>Tiền lương để tính</strong> là tiền lương bình quân theo hợp đồng của <strong>06 tháng liền kề</strong> trước khi nghỉ.</p>

<h2 id="vi-du">Ví dụ tính trợ cấp</h2>
<div class="calc"><p class="t">Bà Mai làm cho công ty từ 01/2005 đến 12/2025, lương bình quân 6 tháng cuối 15.000.000 đ</p>
<p>Tổng thời gian làm việc: 21 năm. Thời gian đã đóng BHTN (01/2009 – 12/2025): 17 năm</p>
<p>Thời gian tính trợ cấp: 21 − 17 = <b>4 năm</b></p>
<p>Nếu nghỉ do hết hạn hoặc thỏa thuận → trợ cấp thôi việc: 4 × ½ × 15.000.000 = <b>30.000.000 đ</b></p>
<p>Nếu bị cắt giảm do tái cơ cấu → trợ cấp mất việc làm: 4 × 1 × 15.000.000 = <b>60.000.000 đ</b></p></div>
<div class="calc"><p class="t">Anh Nam vào làm từ 2019, đã đóng BHTN đầy đủ, chỉ có 2 tháng thử việc không đóng</p>
<p>Thời gian tính trợ cấp: 2 tháng → tính ½ năm → trợ cấp thôi việc = ½ × ½ tháng lương = <b>¼ tháng lương</b></p>
<p>Phần còn lại anh Nam được bảo đảm bằng <a href="/bai-viet/tro-cap-that-nghiep-2026/">trợ cấp thất nghiệp</a>.</p></div>

<h2 id="thoi-han">Thời hạn công ty phải thanh toán</h2>
<p>Trong <strong>14 ngày làm việc</strong> kể từ ngày chấm dứt hợp đồng, hai bên có trách nhiệm thanh toán đầy đủ các khoản liên quan: tiền lương, trợ cấp thôi việc, tiền phép năm chưa nghỉ… Trường hợp đặc biệt (doanh nghiệp tái cơ cấu, thiên tai…) có thể kéo dài nhưng không quá 30 ngày. Công ty cũng phải hoàn thành thủ tục xác nhận thời gian đóng bảo hiểm và trả lại giấy tờ cho người lao động.</p>
''',
    faq=[('Hết hạn hợp đồng mà công ty không ký tiếp có được trợ cấp thôi việc không?', 'Có, nếu bạn đã làm thường xuyên từ đủ 12 tháng và còn thời gian làm việc chưa đóng BHTN. Hết hạn hợp đồng là trường hợp tại khoản 1 Điều 34.'),
         ('Trợ cấp thôi việc và trợ cấp thất nghiệp có nhận cùng lúc được không?', 'Được, vì hai khoản tính cho hai khoảng thời gian khác nhau. Trợ cấp thôi việc do công ty trả cho thời gian không đóng BHTN; trợ cấp thất nghiệp do quỹ BHTN trả dựa trên thời gian đã đóng.')]))

# 9 ─────────────────────────────────────────────
ARTICLES.append(dict(
    slug='luong-lam-them-gio', cat='lv', date=D,
    title='Lương làm thêm giờ, làm ban đêm: cách tính 150%, 200%, 300% và giới hạn giờ làm thêm',
    desc='Cách tính tiền lương làm thêm giờ ngày thường 150%, ngày nghỉ tuần 200%, ngày lễ 300%; làm ban đêm thêm 30%; làm thêm ban đêm; giới hạn 40 giờ/tháng, 200–300 giờ/năm và miễn thuế TNCN.',
    lead='Tăng ca là chuyện thường ngày ở nhà máy và văn phòng, nhưng không phải ai cũng biết mình được trả bao nhiêu cho mỗi giờ làm thêm. Bộ luật Lao động 2019 quy định mức tối thiểu; công ty có thể trả cao hơn, không được trả thấp hơn.',
    keys=['Làm thêm ngày thường <strong>≥150%</strong>, ngày nghỉ hằng tuần <strong>≥200%</strong>, ngày lễ, Tết <strong>≥300%</strong>.',
          'Làm ban đêm (22h–6h) được trả thêm <strong>≥30%</strong>; làm thêm vào ban đêm còn được thêm <strong>20%</strong>.',
          'Làm thêm tối đa <strong>40 giờ/tháng</strong>, <strong>200 giờ/năm</strong> (một số ngành 300 giờ), và phải có sự đồng ý của người lao động.'],
    laws=[f'Bộ luật Lao động 2019 – {L("gio-lam-them","Điều 98: Tiền lương làm thêm giờ, làm việc ban đêm; Điều 106, 107")}',
          'Nghị định 145/2020/NĐ-CP – Điều 55, 56, 57 (cách tính)',
          f'Luật Thuế TNCN số 109/2025/QH15 – {L("thu-nhap-mien-thue","khoản 8 Điều 4 (thu nhập miễn thuế)")}'],
    rel=['nghi-phep-nam', 'cach-tinh-luong-net-tu-gross-2026', 'bieu-thue-tncn-5-bac-2026'],
    body=f'''
<h2 id="muc-tra">Mức trả lương làm thêm giờ tối thiểu</h2>
{tbl(['Thời điểm làm thêm','Ban ngày','Ban đêm (22h – 6h)'],[
['Ngày thường','<b>150%</b>','200% (210% nếu ban ngày hôm đó đã làm thêm)'],
['Ngày nghỉ hằng tuần','<b>200%</b>','270%'],
['Ngày lễ, Tết, ngày nghỉ có hưởng lương','<b>300%</b> (chưa kể lương ngày lễ)','390%']])}
<p>Mức ban đêm trong bảng là tổng hợp theo cách tính của Điều 98 BLLĐ và Điều 57 Nghị định 145/2020: tỷ lệ làm thêm + 30% làm đêm + 20% tiền lương ban ngày của ngày tương ứng. Ví dụ ngày nghỉ hằng tuần: 200% + 30% + 20% × 200% = 270%.</p>
<p>Người làm việc ban đêm trong giờ làm bình thường (không phải làm thêm), ví dụ ca 3, được trả thêm <strong>ít nhất 30%</strong> tiền lương của ngày làm việc bình thường.</p>

<h2 id="luong-gio">Cách tính tiền lương giờ</h2>
<div class="calc"><p><b>Tiền lương giờ</b> = Tiền lương tháng ÷ Số ngày làm việc bình thường trong tháng (theo quy định của công ty, tối đa 26 ngày) ÷ Số giờ làm việc bình thường/ngày</p></div>
<div class="calc"><p class="t">Ví dụ: lương 8.320.000 đ/tháng, công ty quy định 26 ngày, 8 giờ/ngày</p>
<p>Tiền lương giờ: 8.320.000 ÷ 26 ÷ 8 = <b>40.000 đ/giờ</b></p>
<p>Tăng ca 2 giờ tối thứ Ba: 40.000 × 150% × 2 = <b>120.000 đ</b></p>
<p>Làm 8 giờ ngày Chủ nhật (ngày nghỉ hằng tuần): 40.000 × 200% × 8 = <b>640.000 đ</b></p>
<p>Làm 8 giờ ngày 2/9: 40.000 × 300% × 8 = <b>960.000 đ</b>, cộng với lương ngày lễ vẫn được hưởng</p>
<p>Làm ca đêm bình thường 8 giờ: phụ cấp đêm 40.000 × 30% × 8 = <b>96.000 đ</b>/ca</p></div>

<h2 id="gioi-han">Giới hạn số giờ làm thêm</h2>
<p>Theo Điều 107 BLLĐ 2019, công ty chỉ được sử dụng người lao động làm thêm giờ khi:</p>
<ul>
<li><strong>Có sự đồng ý của người lao động</strong>;</li>
<li>Số giờ làm thêm không quá 50% giờ làm bình thường trong 1 ngày; nếu tính theo tuần thì tổng giờ làm bình thường và làm thêm không quá 12 giờ/ngày; <strong>không quá 40 giờ/tháng</strong>;</li>
<li><strong>Không quá 200 giờ/năm</strong>. Một số ngành được tới <strong>300 giờ/năm</strong>: dệt, may, da, giày, điện, điện tử, chế biến nông, lâm, thủy sản; sản xuất điện, viễn thông, lọc dầu, cấp thoát nước; công việc đòi hỏi trình độ cao hoặc công việc cấp bách không thể trì hoãn…</li>
</ul>
<p>Khi tổ chức làm thêm trên 200 giờ/năm, doanh nghiệp phải thông báo bằng văn bản cho cơ quan chuyên môn về lao động cấp tỉnh.</p>

<h2 id="thue">Tiền làm thêm giờ có bị tính thuế không?</h2>
<p>Khoản 8 Điều 4 Luật Thuế TNCN 2025 liệt kê vào nhóm thu nhập được miễn thuế: <em>“Tiền lương làm việc ban đêm, làm thêm giờ, tiền lương, tiền công trả cho những ngày không nghỉ phép theo quy định của pháp luật.”</em> Trước đây, chỉ phần trả cao hơn so với lương làm ban ngày, trong giờ mới được miễn. Cách xác định cụ thể phần được miễn theo luật mới thực hiện theo văn bản hướng dẫn của Bộ Tài chính; công ty sẽ tách riêng khoản này trên bảng lương.</p>
{TOOL_LUONG}
''',
    faq=[('Công ty bắt tăng ca mà không hỏi ý kiến có đúng không?', 'Không đúng, trừ một số trường hợp đặc biệt theo Điều 108 BLLĐ (thực hiện lệnh động viên, bảo vệ tính mạng, tài sản, phòng chống thiên tai, dịch bệnh…). Ngoài các trường hợp đó, làm thêm giờ phải có sự đồng ý của người lao động.'),
         ('Làm thêm có được nghỉ bù thay vì nhận tiền không?', 'Hai bên có thể thỏa thuận. Nếu nghỉ bù, công ty vẫn phải trả phần chênh lệch so với tiền lương của công việc đang làm trong ngày làm việc bình thường.')]))

# 10 ─────────────────────────────────────────────
ARTICLES.append(dict(
    slug='nghi-phep-nam', cat='lv', date=D,
    title='Nghỉ phép năm bao nhiêu ngày? Cách tính và tiền lương ngày phép chưa nghỉ',
    desc='Số ngày nghỉ phép năm theo Bộ luật Lao động 2019: 12, 14, 16 ngày, cộng thêm 1 ngày mỗi 5 năm thâm niên. Cách tính phép khi làm chưa đủ năm, tiền phép chưa nghỉ khi thôi việc, 11 ngày nghỉ lễ Tết.',
    lead='Nghỉ phép năm là quyền của người lao động, được hưởng nguyên lương. Nhiều người không biết mình có bao nhiêu ngày phép, phép chưa nghỉ có được trả tiền không, và nghỉ lễ Tết có bị trừ vào phép không.',
    keys=['Làm đủ 12 tháng: <strong>12 ngày</strong> (bình thường), <strong>14 ngày</strong> (nặng nhọc, độc hại; người chưa thành niên, người khuyết tật), <strong>16 ngày</strong> (đặc biệt nặng nhọc).',
          'Cứ đủ <strong>5 năm</strong> làm cho một công ty được cộng thêm <strong>1 ngày</strong> phép.',
          'Nghỉ việc mà chưa nghỉ hết phép thì được <strong>trả tiền</strong> cho những ngày chưa nghỉ.'],
    laws=[f'Bộ luật Lao động 2019 – {L("phep-nam","Điều 113: Nghỉ hằng năm, Điều 114")}',
          f'Bộ luật Lao động 2019 – {L("nghi-le","Điều 112: Nghỉ lễ, Tết")}',
          'Nghị định 145/2020/NĐ-CP – Điều 65, 66, 67',
          f'Luật Thuế TNCN số 109/2025/QH15 – {L("thu-nhap-mien-thue","khoản 8 Điều 4")}'],
    rel=['tro-cap-thoi-viec-mat-viec', 'luong-lam-them-gio', 'cach-tinh-luong-net-tu-gross-2026'],
    body=f'''
<h2 id="so-ngay">Số ngày nghỉ phép năm</h2>
{tbl(['Loại công việc / người lao động','Số ngày phép (làm đủ 12 tháng)'],[
['Công việc trong điều kiện bình thường','<b>12 ngày làm việc</b>'],
['Người chưa thành niên, người khuyết tật, nghề nặng nhọc, độc hại, nguy hiểm','<b>14 ngày làm việc</b>'],
['Nghề đặc biệt nặng nhọc, độc hại, nguy hiểm','<b>16 ngày làm việc</b>']])}
<p><strong>Thâm niên:</strong> theo Điều 114, cứ đủ 05 năm làm việc cho một công ty thì được tăng thêm 01 ngày. Ví dụ làm việc bình thường được 7 năm: 12 + 1 = <strong>13 ngày</strong>; được 10 năm: 12 + 2 = <strong>14 ngày</strong>.</p>
<p>Phép năm tính theo <strong>ngày làm việc</strong>, nên ngày nghỉ hằng tuần và ngày lễ, Tết rơi vào kỳ nghỉ phép không bị trừ vào số ngày phép.</p>

<h2 id="chua-du-nam">Làm chưa đủ 12 tháng thì tính thế nào?</h2>
<p>Người làm chưa đủ 12 tháng được nghỉ theo tỷ lệ tương ứng với số tháng làm việc:</p>
<div class="calc"><p><b>Số ngày phép</b> = (Số ngày phép năm + ngày thâm niên nếu có) ÷ 12 × Số tháng làm việc thực tế</p>
<p>Ví dụ vào làm từ tháng 5, đến cuối năm làm 8 tháng: 12 ÷ 12 × 8 = <b>8 ngày</b></p></div>
<p>Thời gian học nghề, tập nghề, thử việc rồi làm cho chính công ty đó; thời gian nghỉ việc riêng có lương; thời gian nghỉ ốm cộng dồn không quá 2 tháng/năm; thời gian nghỉ thai sản… được tính là thời gian làm việc để tính phép năm, theo Điều 65 Nghị định 145/2020.</p>

<h2 id="tien-phep">Tiền lương ngày phép chưa nghỉ</h2>
<p>Khoản 3 Điều 113 BLLĐ: <em>trường hợp thôi việc, bị mất việc làm mà chưa nghỉ hằng năm hoặc chưa nghỉ hết số ngày nghỉ hằng năm thì được người sử dụng lao động thanh toán tiền lương cho những ngày chưa nghỉ.</em></p>
<div class="calc"><p class="t">Ví dụ: chị Thu nghỉ việc, còn 5 ngày phép chưa nghỉ, lương hợp đồng 9.100.000 đ, công ty quy định 26 ngày công</p>
<p>Tiền lương 1 ngày: 9.100.000 ÷ 26 = 350.000 đ</p>
<p>Tiền phép chưa nghỉ: 350.000 × 5 = <b>1.750.000 đ</b></p></div>
<p>Tiền lương làm căn cứ là tiền lương theo hợp đồng của tháng trước liền kề tháng nghỉ việc, theo Nghị định 145/2020. Theo khoản 8 Điều 4 Luật Thuế TNCN 2025, tiền lương trả cho những ngày không nghỉ phép theo quy định của pháp luật thuộc thu nhập được miễn thuế.</p>
<div class="note"><b>Còn đang làm việc mà hết năm chưa nghỉ hết phép?</b> Luật chỉ bắt buộc trả tiền khi thôi việc hoặc mất việc. Phép còn lại cuối năm được chuyển sang năm sau, trả tiền hay hủy tùy thỏa thuận, nội quy, quy chế của công ty. Người lao động có thể thỏa thuận nghỉ gộp tối đa 3 năm một lần.</div>

<h2 id="le-tet">11 ngày nghỉ lễ, Tết hưởng nguyên lương</h2>
{tbl(['Ngày lễ','Số ngày'],[['Tết Dương lịch (01/01)','1'],['Tết Âm lịch','5'],['Ngày Chiến thắng (30/4)','1'],['Quốc tế Lao động (01/5)','1'],['Quốc khánh (02/9 và 1 ngày liền kề trước hoặc sau)','2'],['Giỗ Tổ Hùng Vương (10/3 âm lịch)','1'],['<b>Tổng cộng</b>','<b>11</b>']],(1,))}
<p>Nếu ngày lễ trùng ngày nghỉ hằng tuần, người lao động được nghỉ bù vào ngày làm việc kế tiếp. Lịch nghỉ Tết Âm lịch và Quốc khánh cụ thể hằng năm do Thủ tướng Chính phủ quyết định.</p>
''',
    faq=[('Công ty có được ép nhân viên nghỉ phép vào thời điểm công ty chọn không?', 'Công ty quy định lịch nghỉ hằng năm sau khi tham khảo ý kiến người lao động và phải thông báo trước. Người lao động có thể thỏa thuận nghỉ nhiều lần hoặc nghỉ gộp tối đa 3 năm một lần.'),
         ('Nghỉ phép đi xa có được thêm ngày đi đường không?', 'Có. Nếu đi bằng đường bộ, đường sắt, đường thủy mà tổng số ngày đi đường cả đi và về trên 2 ngày, thì từ ngày thứ 3 trở đi được tính thêm thời gian đi đường, chỉ áp dụng cho 1 lần nghỉ trong năm.')]))
