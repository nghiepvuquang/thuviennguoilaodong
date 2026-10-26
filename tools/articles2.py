from articles import cta, L, tbl, TOOL_LUONG, TOOL_BHXH

D = '2026-10-26'
A2 = []

# 11 ─────────── Thai sản
A2.append(dict(
    slug='che-do-thai-san-2026', cat='bh', date=D,
    title='Chế độ thai sản 2026: nghỉ bao lâu, nhận bao nhiêu tiền? (cả lao động nam)',
    desc='Chế độ thai sản theo Luật BHXH 2024: lao động nữ nghỉ 6 tháng hưởng 100% lương bình quân, trợ cấp một lần 2 lần mức tham chiếu (5.060.000 đ), lao động nam nghỉ 5–14 ngày khi vợ sinh. Ví dụ tính tiền.',
    lead='Sinh con là lúc chi tiêu nhiều nhất, và chế độ thai sản của BHXH giúp gia đình bớt áp lực. Bài này tổng hợp ai được hưởng, được nghỉ bao lâu và cách tính số tiền nhận được theo Luật BHXH 2024 (hiệu lực từ 01/7/2025).',
    keys=['Lao động nữ sinh con được nghỉ <strong>6 tháng</strong>, nhận trợ cấp bằng <strong>100%</strong> bình quân lương đóng BHXH 6 tháng gần nhất.',
          'Thêm <strong>trợ cấp một lần</strong> cho mỗi con bằng 2 lần mức tham chiếu, tức <strong>5.060.000 đ</strong> từ 01/7/2026.',
          'Chồng đang đóng BHXH được nghỉ <strong>5–14 ngày làm việc</strong> khi vợ sinh, trong 60 ngày đầu.'],
    laws=[f'Luật BHXH số 41/2024/QH15 – {L("om-dau-thai-san","Điều 53, 58, 59")} (thời gian nghỉ, trợ cấp một lần, mức trợ cấp)',
          'Luật BHXH số 41/2024/QH15 – Điều 50 (điều kiện hưởng)',
          'Bộ luật Lao động 2019 – Điều 139 (nghỉ thai sản)'],
    rel=['ty-le-dong-bhxh-bhyt-bhtn-2026', 'nghi-om-huong-bhxh-2026', 'luong-co-so-muc-tham-chieu-2026'],
    body=f'''
<h2 id="dieu-kien">Ai được hưởng chế độ thai sản khi sinh con?</h2>
<p>Lao động nữ đang đóng BHXH bắt buộc được hưởng chế độ khi sinh con nếu đã <strong>đóng BHXH bắt buộc từ đủ 06 tháng trở lên trong 12 tháng trước khi sinh</strong>. Có quy định riêng cho người phải nghỉ dưỡng thai theo chỉ định của bác sĩ: đóng từ đủ 12 tháng trở lên thì chỉ cần đóng đủ 03 tháng trong 12 tháng trước khi sinh.</p>
<div class="tip">Nghỉ việc trước khi sinh vẫn có thể được hưởng nếu đã đóng đủ thời gian trên. Khi đó bạn tự nộp hồ sơ tại cơ quan BHXH nơi cư trú.</div>

<h2 id="thoi-gian">Được nghỉ bao lâu?</h2>
{tbl(['Trường hợp','Thời gian nghỉ hưởng chế độ'],[
['Lao động nữ sinh con','<b>6 tháng</b>; nghỉ trước sinh không quá 2 tháng'],
['Sinh đôi trở lên','Từ con thứ 2, mỗi con nghỉ thêm <b>1 tháng</b>'],
['Chồng – vợ sinh thường','<b>5 ngày làm việc</b>'],
['Chồng – vợ sinh mổ hoặc sinh con dưới 32 tuần tuổi','<b>7 ngày làm việc</b>'],
['Chồng – vợ sinh đôi','<b>10 ngày làm việc</b> (sinh ba trở lên: thêm 3 ngày mỗi con)'],
['Chồng – vợ sinh đôi phải mổ','<b>14 ngày làm việc</b> (sinh ba trở lên: thêm 3 ngày mỗi con)']])}
<ul>
<li>Thời gian 6 tháng của mẹ <strong>tính cả ngày lễ, Tết và ngày nghỉ hằng tuần</strong>.</li>
<li>Chồng phải bắt đầu nghỉ trong <strong>60 ngày</strong> kể từ ngày vợ sinh, có thể nghỉ thành nhiều lần nhưng tổng không vượt số ngày trên.</li>
<li>Mẹ có thể đi làm lại sớm khi đã nghỉ ít nhất 4 tháng, nếu báo trước, được công ty đồng ý và có xác nhận của cơ sở y tế. Khi đó mẹ vừa nhận lương vừa nhận tiếp trợ cấp thai sản.</li>
<li>Thời gian mẹ nghỉ sinh vẫn được tính là thời gian đóng BHXH, dù mẹ và công ty không phải đóng.</li>
</ul>

<h2 id="tien">Nhận được bao nhiêu tiền?</h2>
<div class="calc"><p><b>Trợ cấp thai sản 1 tháng</b> = 100% × Bình quân tiền lương đóng BHXH của 6 tháng gần nhất trước khi nghỉ</p>
<p><b>Trợ cấp một lần</b> mỗi con = 2 × mức tham chiếu = 2 × 2.530.000 = <b>5.060.000 đ</b> (sinh từ 01/7/2026)</p>
<p><b>Lao động nam</b>: trợ cấp 1 ngày = trợ cấp 1 tháng ÷ 24</p></div>
<p>Nếu mẹ không đủ điều kiện nhận trợ cấp một lần mà chồng đủ điều kiện (đóng BHXH đủ 6 tháng trong 12 tháng trước khi vợ sinh), thì chồng được nhận khoản trợ cấp một lần này.</p>

<h2 id="vi-du">Ví dụ tính tiền thai sản</h2>
<div class="calc"><p class="t">Chị Hằng sinh con tháng 9/2026, lương đóng BHXH 6 tháng gần nhất đều là 10.000.000 đ</p>
<p>Trợ cấp 6 tháng: 10.000.000 × 100% × 6 = 60.000.000 đ</p>
<p>Trợ cấp một lần: 5.060.000 đ</p>
<p>Tổng: <b>65.060.000 đ</b></p></div>
<div class="calc"><p class="t">Chồng chị Hằng, anh Phong, lương đóng BHXH 12.000.000 đ, vợ sinh thường</p>
<p>Trợ cấp 1 ngày: 12.000.000 ÷ 24 = 500.000 đ</p>
<p>Nghỉ 5 ngày: <b>2.500.000 đ</b></p></div>
<div class="note"><b>Đóng bảo hiểm thấp thì thai sản cũng thấp.</b> Nếu chị Hằng chỉ được đóng theo lương tối thiểu Vùng I (5.310.000 đ), 6 tháng trợ cấp chỉ còn 31.860.000 đ, thấp hơn gần một nửa.</div>

<h2 id="ho-so">Hồ sơ và cách nhận tiền</h2>
<ul>
<li><strong>Còn đang đi làm:</strong> nộp bản sao giấy khai sinh hoặc trích lục khai sinh của con cho công ty. Công ty lập hồ sơ gửi BHXH, tiền được trả qua công ty hoặc vào tài khoản cá nhân.</li>
<li><strong>Đã nghỉ việc trước khi sinh:</strong> tự nộp hồ sơ tại cơ quan BHXH nơi cư trú hoặc qua Cổng dịch vụ công.</li>
<li>Lao động nam: nộp thêm giấy tờ chứng minh vợ sinh mổ hoặc sinh non nếu thuộc các trường hợp được nghỉ 7 hoặc 14 ngày.</li>
</ul>
''',
    faq=[('Tôi mới đóng BHXH được 5 tháng thì sinh con có được hưởng không?', 'Chưa đủ điều kiện trợ cấp thai sản khi sinh con (cần đủ 6 tháng trong 12 tháng trước khi sinh). Tuy vậy, nếu chồng đủ điều kiện thì chồng được nhận trợ cấp một lần và chế độ nghỉ của lao động nam.'),
         ('Trợ cấp thai sản có bị tính thuế TNCN không?', 'Không. Trợ cấp thai sản do quỹ BHXH chi trả không phải tiền lương, tiền công nên không bị tính thuế thu nhập cá nhân.')]))

# 12 ─────────── Ốm đau
A2.append(dict(
    slug='nghi-om-huong-bhxh-2026', cat='bh', date=D,
    title='Nghỉ ốm hưởng BHXH 2026: được bao nhiêu ngày, nhận bao nhiêu tiền?',
    desc='Chế độ ốm đau theo Luật BHXH 2024: được nghỉ 30–70 ngày/năm tùy thời gian đóng và điều kiện làm việc, mức hưởng 75% lương đóng BHXH, cách tính theo ngày và ví dụ.',
    lead='Khi bị ốm phải nghỉ làm, bạn không được công ty trả lương những ngày đó, nhưng có thể nhận trợ cấp ốm đau từ quỹ BHXH. Nhiều người không biết quyền lợi này nên bỏ qua.',
    keys=['Mức hưởng <strong>75%</strong> tiền lương đóng BHXH của tháng gần nhất trước khi nghỉ.',
          'Tối đa <strong>30 ngày/năm</strong> nếu đóng dưới 15 năm (40 ngày nếu 15–30 năm, 60 ngày nếu trên 30 năm), không tính ngày lễ, nghỉ hằng tuần.',
          'Trợ cấp 1 ngày = mức tháng ÷ 24. Cần có <strong>giấy nghỉ việc hưởng BHXH</strong> của cơ sở y tế.'],
    laws=[f'Luật BHXH số 41/2024/QH15 – {L("om-dau-thai-san","Điều 43: Thời gian hưởng, Điều 45: Trợ cấp ốm đau")}'],
    rel=['che-do-thai-san-2026', 'ty-le-dong-bhxh-bhyt-bhtn-2026', 'muc-huong-bhyt-2026'],
    body=f'''
<h2 id="so-ngay">Được nghỉ ốm hưởng BHXH bao nhiêu ngày?</h2>
<p>Theo Điều 43 Luật BHXH 2024, thời gian tối đa trong một năm (01/01 – 31/12), tính theo ngày làm việc, không kể ngày lễ, Tết, ngày nghỉ hằng tuần:</p>
{tbl(['Thời gian đã đóng BHXH','Điều kiện bình thường','Nặng nhọc, độc hại hoặc vùng đặc biệt khó khăn'],[
['Dưới 15 năm','30 ngày','40 ngày'],['Từ đủ 15 đến dưới 30 năm','40 ngày','50 ngày'],['Từ đủ 30 năm trở lên','60 ngày','70 ngày']])}
<p>Người mắc bệnh thuộc <strong>danh mục bệnh cần chữa trị dài ngày</strong> do Bộ Y tế ban hành, hết số ngày trên mà vẫn phải điều trị thì được hưởng tiếp với mức thấp hơn (50–65%).</p>

<h2 id="muc-huong">Mức hưởng trợ cấp ốm đau</h2>
{tbl(['Trường hợp','Mức hưởng'],[
['Nghỉ ốm thông thường, nghỉ chăm con ốm','<b>75%</b> tiền lương đóng BHXH tháng gần nhất'],
['Bệnh dài ngày – sau khi hết thời hạn, đóng dưới 15 năm','50%'],
['Bệnh dài ngày – đóng từ đủ 15 đến dưới 30 năm','55%'],
['Bệnh dài ngày – đóng từ đủ 30 năm','65%']])}
<div class="calc"><p><b>Trợ cấp 1 ngày</b> = Tiền lương đóng BHXH tháng gần nhất × 75% ÷ 24</p>
<p>Nghỉ dưới nửa ngày tính là nửa ngày; từ nửa ngày đến dưới một ngày tính là một ngày.</p></div>

<h2 id="vi-du">Ví dụ tính tiền nghỉ ốm</h2>
<div class="calc"><p class="t">Anh Quân đóng BHXH 6 năm, lương đóng tháng trước là 12.000.000 đ, nghỉ ốm 5 ngày làm việc có giấy của bệnh viện</p>
<p>Trợ cấp 1 ngày: 12.000.000 × 75% ÷ 24 = 375.000 đ</p>
<p>5 ngày: <b>1.875.000 đ</b></p>
<p>Anh Quân còn 25 ngày hưởng chế độ ốm đau trong năm.</p></div>

<h2 id="giay-to">Giấy tờ cần có</h2>
<ul>
<li><strong>Điều trị ngoại trú:</strong> giấy chứng nhận nghỉ việc hưởng BHXH do bệnh viện, phòng khám cấp (bác sĩ ghi số ngày nghỉ).</li>
<li><strong>Điều trị nội trú:</strong> giấy ra viện.</li>
<li>Nộp cho công ty trong thời hạn quy định. Công ty tổng hợp gửi cơ quan BHXH, sau đó trả tiền cho bạn.</li>
</ul>
<div class="note"><b>Lưu ý:</b> Tự nghỉ ở nhà không đi khám, hoặc chỉ có đơn thuốc mà không có giấy nghỉ việc hưởng BHXH, thì không được hưởng chế độ. Bị ốm do tự gây thương tích, do say rượu hoặc dùng chất ma túy cũng không được hưởng.</div>
''',
    faq=[('Nghỉ ốm có bị trừ vào ngày phép năm không?', 'Không. Nghỉ ốm hưởng BHXH và nghỉ phép năm là hai chế độ khác nhau. Thời gian nghỉ ốm cộng dồn không quá 2 tháng/năm vẫn được tính là thời gian làm việc để tính phép năm.'),
         ('Con ốm, bố mẹ có được nghỉ hưởng BHXH không?', 'Có. Luật BHXH có chế độ nghỉ chăm con ốm dưới 7 tuổi, mức hưởng 75%. Số ngày tối đa phụ thuộc tuổi của con.')]))

# 13 ─────────── Lương hưu
A2.append(dict(
    slug='cach-tinh-luong-huu-2026', cat='bh', date=D,
    title='Cách tính lương hưu 2026: cần đóng bao nhiêu năm, được hưởng bao nhiêu %?',
    desc='Điều kiện hưởng lương hưu theo Luật BHXH 2024 (đủ 15 năm đóng), công thức tính tỷ lệ hưởng 40%–75% cho lao động nam và nữ, cách tính bình quân tiền lương và ví dụ cụ thể.',
    lead='Từ 01/7/2025, người lao động chỉ cần đóng BHXH đủ 15 năm là đủ điều kiện về thời gian để có lương hưu. Đây là thay đổi rất lớn, đặc biệt với người đang phân vân có nên rút BHXH một lần.',
    keys=['Điều kiện: đủ <strong>tuổi nghỉ hưu</strong> và đóng BHXH bắt buộc từ đủ <strong>15 năm</strong>.',
          'Nữ: 15 năm = 45%, mỗi năm thêm +2%, tối đa 75% (30 năm). Nam: 20 năm = 45%, thêm +2%/năm, tối đa 75% (35 năm).',
          'Nam đóng 15 đến dưới 20 năm: 40%, mỗi năm thêm +1%.'],
    laws=[f'Luật BHXH số 41/2024/QH15 – {L("luong-huu","Điều 64: Điều kiện hưởng, Điều 66: Mức lương hưu, Điều 72")}',
          'Bộ luật Lao động 2019 – Điều 169 (tuổi nghỉ hưu)'],
    rel=['tuoi-nghi-huu-2026', 'rut-bhxh-1-lan-2026', 'ty-le-dong-bhxh-bhyt-bhtn-2026'],
    body=f'''
<h2 id="dieu-kien">Điều kiện hưởng lương hưu</h2>
<p>Theo Điều 64 Luật BHXH 2024, người lao động khi nghỉ việc có thời gian đóng BHXH bắt buộc <strong>từ đủ 15 năm trở lên</strong> được hưởng lương hưu khi <strong>đủ tuổi nghỉ hưu</strong> theo Điều 169 Bộ luật Lao động. Năm 2026, tuổi nghỉ hưu trong điều kiện bình thường là 61 tuổi 6 tháng (nam) và 57 tuổi (nữ). Xem chi tiết lộ trình trong bài <a href="/bai-viet/tuoi-nghi-huu-2026/">Tuổi nghỉ hưu 2026</a>.</p>
<p>Người làm nghề nặng nhọc, độc hại, nguy hiểm hoặc ở vùng đặc biệt khó khăn được nghỉ hưu sớm hơn tối đa 5 tuổi.</p>

<h2 id="ty-le">Tỷ lệ hưởng lương hưu</h2>
{tbl(['Số năm đóng BHXH','Lao động nữ','Lao động nam'],[
['15 năm','45%','40%'],['18 năm','51%','43%'],['20 năm','55%','45%'],['25 năm','65%','55%'],
['30 năm','<b>75%</b> (tối đa)','65%'],['35 năm','75%','<b>75%</b> (tối đa)']],(1,2))}
<p>Nghỉ hưu trước tuổi (do suy giảm khả năng lao động) bị giảm 2% cho mỗi năm nghỉ sớm. Nghỉ sớm dưới 6 tháng không bị giảm; từ đủ 6 tháng đến dưới 12 tháng giảm 1%.</p>

<h2 id="binh-quan">Mức bình quân tiền lương tính lương hưu</h2>
<div class="calc"><p><b>Lương hưu hằng tháng</b> = Tỷ lệ hưởng × Mức bình quân tiền lương đóng BHXH</p></div>
<p>Với người làm doanh nghiệp (lương do công ty quyết định), mức bình quân được tính trên <strong>toàn bộ thời gian đóng BHXH</strong>. Tiền lương của từng năm được nhân với hệ số trượt giá để quy về giá trị hiện tại, giống cách tính BHXH một lần.</p>

<h2 id="vi-du">Ví dụ tính lương hưu</h2>
<div class="calc"><p class="t">Bà Lan nghỉ hưu đủ tuổi, đóng BHXH 25 năm, bình quân tiền lương (đã điều chỉnh) 12.000.000 đ</p>
<p>Tỷ lệ: 45% + (25 − 15) × 2% = 65%</p>
<p>Lương hưu: 12.000.000 × 65% = <b>7.800.000 đ/tháng</b></p></div>
<div class="calc"><p class="t">Ông Hùng cũng đóng 25 năm, cùng mức bình quân 12.000.000 đ</p>
<p>Tỷ lệ: 45% + (25 − 20) × 2% = 55%</p>
<p>Lương hưu: 12.000.000 × 55% = <b>6.600.000 đ/tháng</b></p></div>
<div class="calc"><p class="t">Ông Tâm chỉ đóng được 17 năm</p>
<p>Tỷ lệ: 40% + (17 − 15) × 1% = 42% → với bình quân 10.000.000 đ: <b>4.200.000 đ/tháng</b>, kèm thẻ BHYT do quỹ BHXH đóng.</p></div>

<h2 id="so-sanh">Lương hưu hay BHXH một lần?</h2>
<p>Cũng 17 năm đóng như ông Tâm, nếu rút BHXH một lần (giả sử toàn bộ đóng từ 2014) thì nhận 2 × 17 = 34 tháng lương bình quân, khoảng 340 triệu. Còn lương hưu 4,2 triệu/tháng thì chỉ sau khoảng <strong>81 tháng (gần 7 năm)</strong> đã nhận đủ số đó, và tiếp tục nhận suốt đời, có điều chỉnh tăng theo chính sách. Đây là lý do nên cân nhắc kỹ trước khi rút.</p>
{TOOL_BHXH}
''',
    faq=[('Đã có 12 năm đóng BHXH, nghỉ việc rồi thì làm sao đủ 15 năm?', 'Bạn có thể tham gia BHXH tự nguyện để đóng tiếp cho đủ thời gian. Thời gian đóng bắt buộc và tự nguyện được cộng dồn khi tính lương hưu.'),
         ('Lương hưu có bị tính thuế TNCN không?', 'Không. Luật Thuế TNCN 2025 quy định tiền lương hưu do Quỹ BHXH chi trả là thu nhập được miễn thuế (khoản 9 Điều 4).')]))

# 14 ─────────── Tuổi nghỉ hưu
age_rows = []
m_y, m_m, f_y, f_m = 60, 3, 55, 4
for yr in range(2021, 2036):
    age_rows.append([str(yr), f'{m_y} tuổi' + (f' {m_m} tháng' if m_m else '') if yr <= 2028 else '62 tuổi',
                     f'{f_y} tuổi' + (f' {f_m} tháng' if f_m else '')])
    if yr < 2028:
        m_m += 3
        if m_m >= 12: m_y += 1; m_m -= 12
    if yr < 2035:
        f_m += 4
        if f_m >= 12: f_y += 1; f_m -= 12
age_rows = [r if r[0] != '2026' else [f'<b>{r[0]}</b>', f'<b>{r[1]}</b>', f'<b>{r[2]}</b>'] for r in age_rows]

A2.append(dict(
    slug='tuoi-nghi-huu-2026', cat='lv', date=D,
    title='Tuổi nghỉ hưu năm 2026 và lộ trình đến năm 2035',
    desc='Tuổi nghỉ hưu năm 2026: nam 61 tuổi 6 tháng, nữ 57 tuổi. Bảng lộ trình tăng tuổi nghỉ hưu từ 2021 đến 2035 theo Bộ luật Lao động 2019, các trường hợp nghỉ hưu sớm, muộn.',
    lead='Tuổi nghỉ hưu đang tăng dần mỗi năm cho đến khi nam đủ 62 tuổi (năm 2028) và nữ đủ 60 tuổi (năm 2035). Bảng dưới giúp bạn biết năm nay nghỉ hưu ở tuổi nào.',
    keys=['Năm 2026: nam <strong>61 tuổi 6 tháng</strong>, nữ <strong>57 tuổi</strong> (điều kiện lao động bình thường).',
          'Mỗi năm tăng thêm <strong>3 tháng</strong> với nam (đến 62 tuổi năm 2028), <strong>4 tháng</strong> với nữ (đến 60 tuổi năm 2035).',
          'Nghề nặng nhọc, độc hại, suy giảm khả năng lao động… được nghỉ sớm tối đa <strong>5 tuổi</strong>.'],
    laws=[f'Bộ luật Lao động 2019 – {L("tuoi-nghi-huu","Điều 169: Tuổi nghỉ hưu")}',
          'Nghị định 135/2020/NĐ-CP – quy định về tuổi nghỉ hưu (phụ lục tra theo tháng, năm sinh)'],
    rel=['cach-tinh-luong-huu-2026', 'rut-bhxh-1-lan-2026'],
    body=f'''
<h2 id="lo-trinh">Bảng lộ trình tuổi nghỉ hưu</h2>
<p>Theo khoản 2 Điều 169 Bộ luật Lao động 2019, kể từ năm 2021, tuổi nghỉ hưu trong điều kiện lao động bình thường là đủ 60 tuổi 03 tháng với nam và đủ 55 tuổi 04 tháng với nữ, sau đó mỗi năm tăng thêm 03 tháng với nam và 04 tháng với nữ:</p>
{tbl(['Năm nghỉ hưu','Lao động nam','Lao động nữ'], age_rows)}
<p>Để biết chính xác <strong>tháng, năm</strong> được nghỉ hưu theo ngày sinh của mình, bạn tra phụ lục ban hành kèm Nghị định 135/2020/NĐ-CP hoặc hỏi phòng nhân sự.</p>

<h2 id="som-muon">Nghỉ hưu sớm hơn hoặc muộn hơn</h2>
<ul>
<li><strong>Sớm hơn tối đa 5 tuổi</strong>: người bị suy giảm khả năng lao động; làm nghề, công việc nặng nhọc, độc hại, nguy hiểm hoặc đặc biệt nặng nhọc, độc hại, nguy hiểm; làm việc ở vùng có điều kiện kinh tế – xã hội đặc biệt khó khăn.</li>
<li><strong>Muộn hơn tối đa 5 tuổi</strong>: người có trình độ chuyên môn, kỹ thuật cao và một số trường hợp đặc biệt.</li>
</ul>

<h2 id="huu-va-bhxh">Tuổi nghỉ hưu liên quan gì đến quyền lợi BHXH?</h2>
<ul>
<li>Đủ tuổi nghỉ hưu và có từ đủ 15 năm đóng BHXH → được <a href="/bai-viet/cach-tinh-luong-huu-2026/">lương hưu hằng tháng</a>.</li>
<li>Đủ tuổi mà chưa đủ 15 năm → được chọn đóng tiếp, nhận BHXH một lần, hoặc nhận trợ cấp hằng tháng nếu đủ điều kiện.</li>
<li>Người đủ tuổi nghỉ hưu được đơn phương chấm dứt hợp đồng lao động không cần báo trước, trừ khi hai bên có thỏa thuận khác.</li>
<li>Người nghỉ việc khi đã đủ điều kiện hưởng lương hưu thì không được trợ cấp thôi việc và không được trợ cấp thất nghiệp.</li>
</ul>
''',
    faq=[('Đủ tuổi nghỉ hưu nhưng muốn đi làm tiếp có được không?', 'Được, nếu hai bên thỏa thuận. Người đang hưởng lương hưu mà đi làm theo hợp đồng lao động vẫn được nhận lương hưu, kèm tiền lương theo hợp đồng mới.')]))

# 15 ─────────── Thử việc
A2.append(dict(
    slug='hop-dong-thu-viec', cat='lv', date=D,
    title='Thử việc: tối đa bao lâu, lương bao nhiêu, có phải đóng bảo hiểm không?',
    desc='Quy định thử việc theo Bộ luật Lao động 2019: thời gian thử việc tối đa 6 ngày đến 180 ngày, lương thử việc ít nhất 85%, chỉ thử việc một lần, quyền hủy bỏ không cần báo trước, bảo hiểm khi thử việc.',
    lead='Thử việc là giai đoạn hai bên tìm hiểu nhau, nhưng cũng là lúc người lao động dễ bị thiệt nhất: thử việc quá lâu, lương quá thấp, hoặc thử việc nhiều lần. Pháp luật có giới hạn rõ ràng cho từng điểm.',
    keys=['Thời gian thử việc tối đa: <strong>180 ngày</strong> (quản lý doanh nghiệp), <strong>60 ngày</strong> (cao đẳng trở lên), <strong>30 ngày</strong> (trung cấp), <strong>6 ngày làm việc</strong> (công việc khác).',
          'Lương thử việc ít nhất <strong>85%</strong> lương của công việc đó.',
          'Chỉ được thử việc <strong>một lần</strong> cho một công việc; không áp dụng thử việc với hợp đồng dưới 1 tháng.'],
    laws=[f'Bộ luật Lao động 2019 – {L("hop-dong-lao-dong","Điều 24, 25, 26, 27")}'],
    rel=['cac-loai-hop-dong-lao-dong', 'nghi-viec-dung-luat', 'cach-tinh-luong-net-tu-gross-2026'],
    body=f'''
<h2 id="thoi-gian">Thời gian thử việc tối đa</h2>
{tbl(['Loại công việc','Tối đa'],[
['Người quản lý doanh nghiệp (giám đốc, thành viên HĐQT…)','180 ngày'],
['Công việc cần trình độ cao đẳng trở lên','60 ngày'],
['Công việc cần trình độ trung cấp, công nhân kỹ thuật, nhân viên nghiệp vụ','30 ngày'],
['Công việc khác','6 ngày làm việc']])}
<p>Mỗi công việc chỉ được thử việc <strong>một lần</strong>. Hết thời gian thử việc mà công ty “gia hạn thử việc” hoặc ký thêm hợp đồng thử việc mới cho cùng công việc là trái luật.</p>

<h2 id="hinh-thuc">Hợp đồng thử việc hay thử việc trong hợp đồng lao động?</h2>
<p>Hai bên có thể chọn một trong hai cách:</p>
<ul>
<li><strong>Ghi nội dung thử việc trong hợp đồng lao động</strong>: thử việc đạt thì tiếp tục thực hiện hợp đồng đã ký.</li>
<li><strong>Ký hợp đồng thử việc riêng</strong>: thử việc đạt thì công ty phải ký hợp đồng lao động.</li>
</ul>
<p>Hợp đồng thử việc phải ghi rõ thời gian thử việc, công việc, địa điểm, mức lương, thời giờ làm việc…</p>

<h2 id="luong">Lương thử việc</h2>
<div class="calc"><p>Lương thử việc ≥ <b>85%</b> × mức lương của công việc đó</p>
<p>Ví dụ: lương chính thức 12.000.000 đ → lương thử việc tối thiểu 10.200.000 đ</p></div>

<h2 id="bao-hiem">Thử việc có phải đóng bảo hiểm không?</h2>
<ul>
<li><strong>Thử việc ghi trong hợp đồng lao động</strong> (từ 1 tháng trở lên): công ty phải đóng BHXH, BHYT, BHTN ngay từ tháng đầu.</li>
<li><strong>Ký hợp đồng thử việc riêng</strong>: hợp đồng thử việc không phải hợp đồng lao động, nên thường chưa thuộc diện đóng BHXH bắt buộc.</li>
<li>Thời gian thử việc không đóng BHTN, nếu sau đó làm chính thức cho cùng công ty, vẫn được tính để hưởng <a href="/bai-viet/tro-cap-thoi-viec-mat-viec/">trợ cấp thôi việc</a> và tính phép năm.</li>
</ul>

<h2 id="ket-thuc">Kết thúc thử việc</h2>
<ul>
<li>Hết thời gian thử việc, công ty <strong>phải thông báo kết quả</strong>.</li>
<li>Trong thời gian thử việc, <strong>mỗi bên đều có quyền hủy bỏ</strong> hợp đồng mà không cần báo trước và không phải bồi thường.</li>
<li>Thử việc không đạt thì chấm dứt hợp đồng thử việc hoặc hợp đồng lao động đã ký. Công ty vẫn phải trả lương cho những ngày đã làm.</li>
</ul>
''',
    faq=[('Công ty bắt thử việc 3 tháng cho nhân viên văn phòng có đúng không?', 'Với công việc cần trình độ cao đẳng trở lên, thời gian thử việc tối đa là 60 ngày. Thử việc 3 tháng là vượt mức luật cho phép, trừ vị trí quản lý doanh nghiệp.'),
         ('Thử việc có được tính thuế TNCN không?', 'Nếu ký hợp đồng thử việc riêng (dưới 3 tháng), công ty thường khấu trừ 10% khi trả từ 2 triệu đồng/lần trở lên. Bạn có thể làm cam kết theo mẫu nếu tổng thu nhập cả năm dưới mức phải nộp thuế. Nếu thử việc nằm trong hợp đồng lao động thì tính theo biểu lũy tiến.')]))

# 16 ─────────── Loại hợp đồng
A2.append(dict(
    slug='cac-loai-hop-dong-lao-dong', cat='lv', date=D,
    title='Các loại hợp đồng lao động: xác định thời hạn, không xác định thời hạn và những điều cần biết',
    desc='Bộ luật Lao động 2019 chỉ còn 2 loại hợp đồng lao động: không xác định thời hạn và xác định thời hạn (tối đa 36 tháng). Quy định ký tiếp, hình thức hợp đồng, nội dung bắt buộc.',
    lead='Bạn đang ký hợp đồng loại gì? Loại hợp đồng quyết định thời hạn báo trước khi nghỉ việc, khả năng bị chấm dứt khi hết hạn, và nhiều quyền lợi khác.',
    keys=['Chỉ có 2 loại: <strong>không xác định thời hạn</strong> và <strong>xác định thời hạn</strong> (không quá 36 tháng).',
          'Hợp đồng xác định thời hạn chỉ được ký thêm <strong>1 lần</strong>; lần sau phải ký không xác định thời hạn.',
          'Hết hạn mà vẫn làm tiếp quá 30 ngày không ký mới → tự động thành <strong>hợp đồng không xác định thời hạn</strong>.'],
    laws=[f'Bộ luật Lao động 2019 – {L("hop-dong-lao-dong","Điều 13, 14, 20, 21")}'],
    rel=['hop-dong-thu-viec', 'nghi-viec-dung-luat', 'tro-cap-thoi-viec-mat-viec'],
    body=f'''
<h2 id="hai-loai">Hai loại hợp đồng lao động</h2>
{tbl(['','Không xác định thời hạn','Xác định thời hạn'],[
['Thời hạn','Không ghi thời điểm kết thúc','Tối đa 36 tháng'],
['Báo trước khi nghỉ việc','Ít nhất 45 ngày','30 ngày (12–36 tháng) · 3 ngày làm việc (dưới 12 tháng)'],
['Hết hạn','Không có','Chấm dứt, hoặc ký tiếp (chỉ thêm 1 lần)']])}
<p>Hợp đồng “thời vụ”, hợp đồng “theo mùa vụ” trước đây nay đều thuộc loại <strong>xác định thời hạn</strong>.</p>
<div class="note"><b>Tên gọi không quan trọng bằng nội dung.</b> Theo Điều 13 BLLĐ, nếu hai bên ký “hợp đồng dịch vụ”, “hợp đồng cộng tác viên”… nhưng có nội dung về việc làm có trả công, tiền lương và sự quản lý, điều hành, giám sát của một bên, thì vẫn được coi là hợp đồng lao động. Công ty phải đóng bảo hiểm và thực hiện đầy đủ nghĩa vụ.</div>

<h2 id="ky-tiep">Hết hạn hợp đồng thì sao?</h2>
<ol>
<li>Trong <strong>30 ngày</strong> kể từ ngày hết hạn, nếu người lao động vẫn làm việc, hai bên phải ký hợp đồng mới. Trong thời gian chưa ký, quyền lợi thực hiện theo hợp đồng cũ.</li>
<li>Quá 30 ngày mà không ký → hợp đồng cũ <strong>trở thành hợp đồng không xác định thời hạn</strong>.</li>
<li>Nếu ký hợp đồng mới là loại xác định thời hạn thì <strong>chỉ được ký thêm 1 lần</strong>. Sau đó nếu vẫn làm tiếp phải ký hợp đồng không xác định thời hạn (trừ vài trường hợp đặc biệt như người cao tuổi, lao động nước ngoài, giám đốc doanh nghiệp vốn nhà nước).</li>
</ol>
<div class="calc"><p class="t">Ví dụ</p><p>Hợp đồng 1: 12 tháng → Hợp đồng 2: 36 tháng → Hợp đồng 3: <b>bắt buộc không xác định thời hạn</b> nếu tiếp tục làm việc.</p></div>

<h2 id="hinh-thuc">Hình thức hợp đồng</h2>
<ul>
<li>Phải <strong>bằng văn bản</strong>, làm 2 bản, mỗi bên giữ 1 bản. Hợp đồng điện tử có giá trị như văn bản.</li>
<li>Được ký <strong>bằng lời nói</strong> nếu thời hạn dưới 1 tháng (trừ một số trường hợp như lao động chưa đủ 15 tuổi, người giúp việc gia đình, nhóm lao động thông qua người đại diện).</li>
</ul>

<h2 id="noi-dung">Hợp đồng phải có những nội dung gì?</h2>
<p>Điều 21 BLLĐ yêu cầu các nội dung chủ yếu: thông tin hai bên; công việc và địa điểm làm việc; thời hạn hợp đồng; mức lương, hình thức trả lương, thời hạn trả lương, phụ cấp và các khoản bổ sung; chế độ nâng bậc, nâng lương; thời giờ làm việc, nghỉ ngơi; trang bị bảo hộ lao động; BHXH, BHYT, BHTN; đào tạo, bồi dưỡng.</p>
<div class="tip">Hãy giữ bản hợp đồng của mình. Đây là căn cứ quan trọng nhất khi có tranh chấp về lương, bảo hiểm hoặc trợ cấp.</div>
''',
    faq=[('Công ty không ký hợp đồng, chỉ thỏa thuận miệng có sao không?', 'Với công việc từ 1 tháng trở lên, hợp đồng phải bằng văn bản. Công ty không ký hợp đồng bằng văn bản là vi phạm, nhưng quan hệ lao động vẫn tồn tại và bạn vẫn có quyền đòi lương, bảo hiểm nếu chứng minh được.')]))

# 17 ─────────── Nghỉ việc đúng luật
A2.append(dict(
    slug='nghi-viec-dung-luat', cat='lv', date=D,
    title='Nghỉ việc đúng luật: báo trước bao nhiêu ngày, khi nào được nghỉ ngay?',
    desc='Thời hạn báo trước khi nghỉ việc theo Điều 35 Bộ luật Lao động 2019 (45 ngày, 30 ngày, 3 ngày làm việc), 7 trường hợp được nghỉ không cần báo trước, hậu quả nghỉ ngang và quyền lợi khi nghỉ việc.',
    lead='Người lao động có quyền nghỉ việc mà không cần lý do, chỉ cần báo trước đủ thời hạn. Nghỉ đúng luật giúp bạn giữ được trợ cấp thất nghiệp, trợ cấp thôi việc và tránh phải bồi thường.',
    keys=['Báo trước ít nhất <strong>45 ngày</strong> (HĐ không xác định thời hạn), <strong>30 ngày</strong> (HĐ 12–36 tháng), <strong>3 ngày làm việc</strong> (HĐ dưới 12 tháng).',
          'Được nghỉ <strong>không cần báo trước</strong> khi bị nợ lương, trả lương chậm, bị ngược đãi, quấy rối…',
          'Công ty phải thanh toán đủ các khoản trong <strong>14 ngày làm việc</strong> và chốt sổ BHXH.'],
    laws=[f'Bộ luật Lao động 2019 – {L("thoi-viec","Điều 35, 40, 48")}',
          'Luật Việc làm số 74/2025/QH15 – Điều 38 (điều kiện hưởng trợ cấp thất nghiệp)'],
    rel=['tro-cap-that-nghiep-2026', 'tro-cap-thoi-viec-mat-viec', 'nghi-phep-nam'],
    body=f'''
<h2 id="bao-truoc">Thời hạn báo trước khi nghỉ việc</h2>
{tbl(['Loại hợp đồng','Báo trước ít nhất'],[
['Không xác định thời hạn','<b>45 ngày</b>'],['Xác định thời hạn từ 12 đến 36 tháng','<b>30 ngày</b>'],
['Xác định thời hạn dưới 12 tháng','<b>3 ngày làm việc</b>'],['Một số ngành nghề đặc thù','Theo quy định của Chính phủ (có thể dài hơn)']])}
<p>Bạn chỉ cần <strong>thông báo</strong>, không cần công ty “duyệt đơn”. Nên làm bằng văn bản hoặc email, giữ lại bằng chứng ngày gửi.</p>

<h2 id="khong-bao-truoc">7 trường hợp được nghỉ ngay, không cần báo trước</h2>
<ol>
<li>Không được bố trí đúng công việc, địa điểm làm việc hoặc không được bảo đảm điều kiện làm việc như thỏa thuận (trừ trường hợp tạm điều chuyển hợp pháp);</li>
<li>Không được trả đủ lương hoặc trả lương không đúng thời hạn (trừ trường hợp bất khả kháng theo luật);</li>
<li>Bị ngược đãi, đánh đập, có lời nói, hành vi nhục mạ, ảnh hưởng sức khỏe, nhân phẩm, danh dự; bị cưỡng bức lao động;</li>
<li>Bị quấy rối tình dục tại nơi làm việc;</li>
<li>Lao động nữ mang thai phải nghỉ việc theo chỉ định của cơ sở y tế;</li>
<li>Đủ tuổi nghỉ hưu (trừ khi hai bên có thỏa thuận khác);</li>
<li>Công ty cung cấp thông tin không trung thực khi tuyển dụng, ảnh hưởng đến việc thực hiện hợp đồng.</li>
</ol>

<h2 id="nghi-ngang">Hậu quả của việc nghỉ ngang (trái luật)</h2>
<p>Theo Điều 40 BLLĐ, người lao động đơn phương chấm dứt hợp đồng trái luật thì:</p>
<ul>
<li><strong>Không được trợ cấp thôi việc</strong>;</li>
<li>Phải <strong>bồi thường nửa tháng tiền lương</strong> theo hợp đồng, cộng tiền lương của những ngày không báo trước;</li>
<li>Phải <strong>hoàn trả chi phí đào tạo</strong> (nếu có);</li>
<li><strong>Mất quyền hưởng trợ cấp thất nghiệp</strong> cho lần nghỉ việc này.</li>
</ul>
<div class="calc"><p class="t">Ví dụ: lương 13.000.000 đ, HĐ không xác định thời hạn, báo trước 15 ngày rồi nghỉ</p>
<p>Thiếu 30 ngày báo trước. Bồi thường: 6.500.000 (nửa tháng) + 13.000.000 ÷ 26 × số ngày làm việc trong 30 ngày thiếu</p>
<p>Chưa kể mất trợ cấp thất nghiệp, có thể vài chục triệu đồng.</p></div>

<h2 id="quyen-loi">Quyền lợi khi nghỉ việc đúng luật</h2>
<ul>
<li>Trong <strong>14 ngày làm việc</strong>, công ty phải thanh toán lương những ngày đã làm, <a href="/bai-viet/nghi-phep-nam/">tiền phép năm chưa nghỉ</a>, <a href="/bai-viet/tro-cap-thoi-viec-mat-viec/">trợ cấp thôi việc</a> (nếu có). Một số trường hợp đặc biệt được kéo dài, nhưng không quá 30 ngày.</li>
<li>Công ty phải <strong>chốt sổ BHXH</strong> (xác nhận thời gian đóng BHXH, BHTN) và trả lại giấy tờ gốc đã giữ.</li>
<li>Trong 3 tháng sau khi nghỉ, nộp hồ sơ hưởng <a href="/bai-viet/tro-cap-that-nghiep-2026/">trợ cấp thất nghiệp</a> nếu đủ điều kiện.</li>
</ul>
<div class="tip"><b>Mẫu thông báo nghỉ việc ngắn gọn:</b> “Tôi tên…, chức vụ…, bộ phận… Theo khoản 1 Điều 35 Bộ luật Lao động 2019, tôi thông báo đơn phương chấm dứt hợp đồng lao động số… kể từ ngày… (sau … ngày kể từ ngày thông báo này). Tôi sẽ bàn giao công việc đầy đủ trước ngày nghỉ. Đề nghị công ty thanh toán các khoản liên quan và chốt sổ BHXH theo quy định.”</div>
''',
    faq=[('Công ty không cho nghỉ, không nhận đơn thì sao?', 'Quyền nghỉ việc không phụ thuộc sự đồng ý của công ty. Bạn gửi thông báo bằng email hoặc thư bảo đảm để có bằng chứng; hết thời hạn báo trước là có quyền nghỉ.'),
         ('Công ty giữ bằng gốc, không trả có đúng không?', 'Không. Bộ luật Lao động cấm người sử dụng lao động giữ bản chính giấy tờ tùy thân, văn bằng, chứng chỉ của người lao động. Khi chấm dứt hợp đồng, công ty phải trả lại giấy tờ đã giữ.')]))

# 18 ─────────── Lương cơ sở
A2.append(dict(
    slug='luong-co-so-muc-tham-chieu-2026', cat='luong', date=D,
    title='Lương cơ sở 2.530.000 đ từ 01/7/2026: ảnh hưởng gì đến người lao động doanh nghiệp?',
    desc='Lương cơ sở tăng lên 2.530.000 đ/tháng từ 01/7/2026 theo Nghị định 161/2026. Lương cơ sở dùng để làm gì, khác lương tối thiểu vùng thế nào, và các khoản BHXH, BHYT thay đổi theo.',
    lead='Mỗi lần lương cơ sở tăng, nhiều người làm doanh nghiệp tư nhân nghĩ lương mình cũng tăng. Thực tế không phải vậy, nhưng lương cơ sở vẫn ảnh hưởng tới nhiều khoản liên quan đến bảo hiểm của bạn.',
    keys=['Từ <strong>01/7/2026</strong>, lương cơ sở là <strong>2.530.000 đ/tháng</strong> (trước đó 2.340.000 đ).',
          'Lương cơ sở dùng tính lương <strong>khu vực nhà nước</strong>; doanh nghiệp trả lương theo thỏa thuận với sàn là lương tối thiểu vùng.',
          'Lương cơ sở hiện cũng là <strong>mức tham chiếu</strong> của BHXH: trần đóng 50,6 triệu, trợ cấp sinh con 5,06 triệu…'],
    laws=[f'Nghị định 161/2026/NĐ-CP – {L("luong-co-so","Điều 3: Mức lương cơ sở")}',
          'Luật BHXH số 41/2024/QH15 – Điều 7 (mức tham chiếu), Điều 31, Điều 58',
          'Luật Công đoàn 2024 – đoàn phí'],
    rel=['luong-toi-thieu-vung-2026', 'ty-le-dong-bhxh-bhyt-bhtn-2026', 'che-do-thai-san-2026'],
    body=f'''
<h2 id="la-gi">Lương cơ sở là gì?</h2>
<p>Theo Điều 3 Nghị định 161/2026/NĐ-CP, mức lương cơ sở dùng làm căn cứ tính mức lương trong các bảng lương, phụ cấp và các chế độ khác cho cán bộ, công chức, viên chức, lực lượng vũ trang; tính hoạt động phí, sinh hoạt phí; và tính các khoản trích, chế độ được hưởng theo mức lương cơ sở.</p>
<div class="calc"><p class="t">Ví dụ với công chức</p><p>Lương = Hệ số lương × Lương cơ sở = 2,34 × 2.530.000 = <b>5.920.200 đ/tháng</b> (chưa kể phụ cấp)</p></div>

<h2 id="so-sanh">Khác lương tối thiểu vùng thế nào?</h2>
{tbl(['','Lương cơ sở','Lương tối thiểu vùng'],[
['Mức 2026','2.530.000 đ (từ 01/7/2026)','3.700.000 – 5.310.000 đ (từ 01/01/2026)'],
['Áp dụng cho','Khu vực nhà nước; căn cứ tính một số chế độ BHXH, BHYT','Người làm cho doanh nghiệp, tổ chức, cá nhân thuê lao động'],
['Vai trò','Đơn vị nhân với hệ số lương','Mức sàn, không được trả thấp hơn']])}

<h2 id="anh-huong">Các khoản thay đổi theo lương cơ sở</h2>
<p>Luật BHXH 2024 dùng khái niệm <strong>mức tham chiếu</strong> để tính một số mức đóng, mức hưởng. Khi chưa bỏ lương cơ sở, mức tham chiếu bằng lương cơ sở. Vì vậy từ 01/7/2026:</p>
{tbl(['Khoản','Cách tính','Mức từ 01/7/2026'],[
['Trần lương đóng BHXH, BHYT','20 × mức tham chiếu','50.600.000 đ'],
['Trợ cấp một lần khi sinh con (mỗi con)','2 × mức tham chiếu','5.060.000 đ'],
['Đoàn phí công đoàn tối đa','10% lương cơ sở','253.000 đ/tháng'],
['Ngưỡng cùng chi trả BHYT để được hưởng 100% (tham gia 5 năm liên tục)','6 × mức tham chiếu','15.180.000 đ/năm']],(2,))}
<p>Với người lương cao trên 46,8 triệu, trần đóng BHXH tăng từ 46.800.000 đ lên 50.600.000 đ nên tiền bảo hiểm bị trừ có thể tăng nhẹ từ tháng 7/2026.</p>
{TOOL_LUONG}
''',
    faq=[('Lương cơ sở tăng thì lương ở công ty tư nhân có tăng không?', 'Không tự động tăng. Lương ở doanh nghiệp do hai bên thỏa thuận. Thứ ảnh hưởng trực tiếp là lương tối thiểu vùng, vốn được điều chỉnh riêng (lần gần nhất từ 01/01/2026).')]))

# 19 ─────────── BHYT
A2.append(dict(
    slug='muc-huong-bhyt-2026', cat='bh', date=D,
    title='Mức hưởng bảo hiểm y tế 2026: khám đúng tuyến, trái tuyến được chi trả bao nhiêu?',
    desc='Mức hưởng BHYT của người lao động theo Luật BHYT sửa đổi 2024: 80% chi phí, 100% tại cơ sở cấp ban đầu, 100% khi đủ 5 năm liên tục và cùng chi trả vượt 6 lần mức tham chiếu, quy định khám không đúng nơi đăng ký.',
    lead='Mỗi tháng bạn đóng 1,5% lương cho BHYT, công ty đóng thêm 3%. Vậy khi đi khám, quỹ BHYT trả bao nhiêu? Luật BHYT sửa đổi năm 2024 thay đổi cách gọi “tuyến” thành “cấp” và mở rộng quyền lợi khi khám không đúng nơi đăng ký.',
    keys=['Người lao động được quỹ BHYT chi trả <strong>80%</strong> chi phí trong phạm vi hưởng, tự trả 20%.',
          '<strong>100%</strong> khi khám tại trạm y tế, cơ sở cấp ban đầu; khi chi phí một lần khám thấp hơn mức Chính phủ quy định; khi cấp cứu.',
          'Tham gia <strong>5 năm liên tục</strong> và tiền tự trả trong năm vượt <strong>6 lần mức tham chiếu</strong> (15.180.000 đ) → được 100% phần còn lại.'],
    laws=[f'Luật BHYT (sửa đổi bởi Luật số 51/2024/QH15) – {L("ty-le-dong-bh","Điều 22: Mức hưởng")}'],
    rel=['ty-le-dong-bhxh-bhyt-bhtn-2026', 'nghi-om-huong-bhxh-2026'],
    body=f'''
<h2 id="muc-huong">Mức hưởng BHYT của người lao động</h2>
{tbl(['Trường hợp','Quỹ BHYT chi trả'],[
['Khám chữa bệnh đúng quy định (người lao động thông thường)','<b>80%</b>'],
['Chi phí một lần khám thấp hơn mức do Chính phủ quy định','100%'],
['Khám tại trạm y tế, phòng khám y học gia đình, cơ sở cấp ban đầu','100%'],
['Tham gia 5 năm liên tục + tiền cùng chi trả trong năm > 6 lần mức tham chiếu','100% (phần vượt)'],
['Cấp cứu tại bất kỳ cơ sở nào','100% mức hưởng']])}

<h2 id="khong-dung-noi">Khám không đúng nơi đăng ký ban đầu</h2>
<p>Từ 01/01/2025, hệ thống khám chữa bệnh chia thành <strong>cấp ban đầu – cấp cơ bản – cấp chuyên sâu</strong> thay cho tuyến xã, huyện, tỉnh, trung ương. Nếu tự đi khám không đúng nơi đăng ký, quỹ BHYT vẫn trả theo tỷ lệ của mức hưởng:</p>
{tbl(['Nơi khám','Tỷ lệ của mức hưởng'],[
['Cơ sở cấp ban đầu','100%'],['Nội trú tại cơ sở cấp cơ bản','100%'],
['Cơ sở trước 01/01/2025 là tuyến huyện','100%'],
['Ngoại trú tại cấp cơ bản','50% – 100% theo lộ trình của Chính phủ'],
['Nội trú tại cấp chuyên sâu','40%'],
['Cấp chuyên sâu trước đây là tuyến tỉnh','100% nội trú; 50% ngoại trú (theo lộ trình)'],
['Bệnh hiếm, hiểm nghèo, cần phẫu thuật hoặc kỹ thuật cao (theo danh mục Bộ Y tế) tại cấp cơ bản, chuyên sâu','100%']])}
<div class="calc"><p class="t">Ví dụ: anh Bình nằm viện tại cơ sở cấp chuyên sâu không đúng nơi đăng ký, không có giấy chuyển, chi phí trong phạm vi BHYT 20.000.000 đ</p>
<p>Mức hưởng của anh: 80% · Tỷ lệ khi tự đi nội trú cấp chuyên sâu: 40%</p>
<p>Quỹ BHYT trả: 20.000.000 × 80% × 40% = <b>6.400.000 đ</b> · Anh Bình tự trả 13.600.000 đ</p>
<p>Nếu có giấy chuyển viện đúng quy định: quỹ trả 20.000.000 × 80% = <b>16.000.000 đ</b></p></div>

<h2 id="meo">Mẹo để được BHYT chi trả nhiều nhất</h2>
<ul>
<li>Đăng ký nơi khám ban đầu gần nhà hoặc gần nơi làm việc; có thể đổi vào đầu mỗi quý.</li>
<li>Khi cần lên cơ sở cao hơn, xin <strong>giấy chuyển cơ sở khám chữa bệnh</strong>.</li>
<li>Giữ thẻ BHYT liên tục, không để gián đoạn quá 3 tháng, để được tính “5 năm liên tục”.</li>
<li>Dùng thẻ BHYT trên ứng dụng VssID hoặc VNeID thay cho thẻ giấy.</li>
</ul>
''',
    faq=[('Nghỉ việc thì thẻ BHYT còn dùng được không?', 'Thẻ BHYT có giá trị đến hết tháng công ty đã đóng. Nếu đang hưởng trợ cấp thất nghiệp, bạn được cấp thẻ BHYT do quỹ BHTN đóng. Ngoài ra có thể mua BHYT hộ gia đình để không bị gián đoạn.')]))

# 20 ─────────── Trốn đóng BHXH
A2.append(dict(
    slug='cong-ty-no-tron-dong-bhxh', cat='bh', date=D,
    title='Công ty nợ, trốn đóng BHXH: cách kiểm tra và người lao động cần làm gì?',
    desc='Thế nào là trốn đóng BHXH theo Điều 39 Luật BHXH 2024, cách kiểm tra công ty có đóng đủ không qua VssID, quyền lợi bị ảnh hưởng và các bước khiếu nại, tố cáo.',
    lead='Bị trừ 10,5% lương mỗi tháng nhưng đến khi nghỉ việc mới phát hiện công ty không đóng hoặc đóng thiếu: đây là tình huống không hiếm. Bài này giúp bạn phát hiện sớm và biết cần làm gì.',
    keys=['Đăng ký lương đóng BHXH <strong>thấp hơn quy định</strong>, không đăng ký, hoặc không nộp tiền quá 60 ngày đều có thể bị coi là <strong>trốn đóng</strong>.',
          'Kiểm tra quá trình đóng trên ứng dụng <strong>VssID</strong> mỗi vài tháng.',
          'Có thể yêu cầu công ty, khiếu nại tới <strong>cơ quan BHXH</strong>, <strong>thanh tra lao động</strong>, hoặc khởi kiện.'],
    laws=[f'Luật BHXH số 41/2024/QH15 – {L("ty-le-dong-bh","Điều 39: Trốn đóng BHXH bắt buộc, BHTN")}; Điều 31 (căn cứ đóng)',
          'Bộ luật Lao động 2019 – Điều 48 (trách nhiệm chốt sổ khi chấm dứt hợp đồng)'],
    rel=['ty-le-dong-bhxh-bhyt-bhtn-2026', 'rut-bhxh-1-lan-2026', 'tro-cap-that-nghiep-2026'],
    body=f'''
<h2 id="the-nao-la">Thế nào là trốn đóng BHXH?</h2>
<p>Theo Điều 39 Luật BHXH 2024, công ty bị coi là trốn đóng BHXH, BHTN khi thuộc một trong các trường hợp:</p>
<ul>
<li>Sau 60 ngày kể từ hạn phải đăng ký mà <strong>không đăng ký</strong> hoặc đăng ký thiếu người phải tham gia;</li>
<li><strong>Đăng ký tiền lương đóng thấp hơn quy định</strong>, ví dụ lương thực tế 15 triệu (gồm lương và phụ cấp trả thường xuyên) nhưng chỉ khai 5 triệu;</li>
<li><strong>Không nộp hoặc nộp thiếu</strong> số tiền đã đăng ký sau 60 ngày kể từ hạn nộp chậm nhất, dù đã bị đôn đốc;</li>
<li>Các trường hợp khác do Chính phủ quy định.</li>
</ul>

<h2 id="kiem-tra">Cách kiểm tra công ty có đóng đủ không</h2>
<ol>
<li>Tải ứng dụng <strong>VssID – Bảo hiểm xã hội số</strong>, đăng nhập bằng mã số BHXH (thường là số CCCD) hoặc tài khoản định danh điện tử VNeID.</li>
<li>Vào mục <strong>Quá trình tham gia</strong> → xem từng tháng: đơn vị đóng, mức lương đóng, trạng thái.</li>
<li>So sánh mức lương đóng với hợp đồng và phiếu lương. Chú ý các tháng bị bỏ trống hoặc ghi “nợ”.</li>
</ol>

<h2 id="anh-huong">Bị đóng thiếu ảnh hưởng gì?</h2>
{tbl(['Quyền lợi','Ảnh hưởng'],[
['Thai sản, ốm đau','Tính theo lương đóng → thấp hơn; tháng nợ có thể chưa được giải quyết'],
['Trợ cấp thất nghiệp','60% lương đóng → thấp hơn; tháng chưa đóng không được tính'],
['BHXH một lần, lương hưu','Tính trên bình quân lương đóng → thấp hơn suốt đời'],
['Thẻ BHYT','Có thể bị gián đoạn khi công ty nợ']])}

<h2 id="lam-gi">Người lao động nên làm gì?</h2>
<ol>
<li><strong>Thu thập bằng chứng:</strong> hợp đồng lao động, phiếu lương có dòng trừ BHXH, sao kê lương, ảnh chụp VssID.</li>
<li><strong>Yêu cầu công ty bằng văn bản</strong> đóng bù và giải thích. Có thể nhờ công đoàn cơ sở hỗ trợ.</li>
<li><strong>Gửi đơn tới cơ quan BHXH</strong> cấp tỉnh hoặc cơ sở nơi công ty đóng. Cơ quan BHXH có quyền thanh tra chuyên ngành về đóng BHXH.</li>
<li><strong>Gửi đơn tới thanh tra lao động</strong> (Sở Nội vụ cấp tỉnh) hoặc gọi đường dây nóng của BHXH Việt Nam.</li>
<li><strong>Khởi kiện</strong> ra Tòa án nhân dân để buộc công ty đóng bù. Công ty trốn đóng có thể bị phạt hành chính, buộc đóng đủ cùng tiền lãi, và trong trường hợp nghiêm trọng có thể bị truy cứu trách nhiệm hình sự.</li>
</ol>
<div class="note"><b>Khi nghỉ việc:</b> Công ty có trách nhiệm hoàn thành thủ tục xác nhận thời gian đóng BHXH, BHTN (chốt sổ) theo Điều 48 BLLĐ. Công ty chưa đóng đủ thì việc chốt sổ bị chậm, ảnh hưởng đến hồ sơ thất nghiệp của bạn. Hãy kiểm tra sớm, đừng đợi đến khi nghỉ.</div>
''',
    faq=[('Công ty và nhân viên thỏa thuận đóng BHXH thấp để nhận lương cao hơn có được không?', 'Không. Thỏa thuận đóng thấp hơn mức luật định là trái pháp luật. Người lao động được nhận nhiều tiền hơn mỗi tháng nhưng thiệt về thai sản, thất nghiệp, lương hưu, còn công ty có thể bị xử phạt khi bị thanh tra.')]))
