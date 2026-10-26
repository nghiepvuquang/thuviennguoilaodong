# Thư Viện Người Lao Động – hướng dẫn cho Claude

Web tĩnh tại https://thuviennguoilaodong.com, chạy trên Netlify, **tự triển khai mỗi khi đẩy (push) lên nhánh `main`**. Thư mục được xuất bản là `site/` (xem `netlify.toml`). Không có bước build trên Netlify: mọi HTML trong `site/` phải được build sẵn và commit.

Chủ web: Vũ Quang Nghiệp (người Việt, không phải lập trình viên). Mọi nội dung và báo cáo viết bằng **tiếng Việt**, dễ hiểu.

## Cấu trúc
- `site/index.html` – trang chủ: công cụ tính lương Gross↔Net, BHXH 1 lần, tra cứu luật (nguyên văn). Tệp lớn, chỉnh bằng tay rất thận trọng. Khung "Bài viết hữu ích" được build tự cập nhật – không sửa tay.
- `site/bai-viet/<slug>/index.html`, `site/bai-viet/index.html`, `site/lien-he/`, `site/sitemap.xml`, `site/assets/blog.css` – **sinh tự động**, không sửa tay.
- `tools/build_blog.py` – build toàn bộ trang bài viết, trang danh sách, sitemap, khung bài trên trang chủ.
- `tools/articles.py`, `tools/articles2.py` – 20 bài đầu (Python).
- `content/bai-viet/<slug>.json` – **bài mới viết thêm đặt ở đây** (một tệp JSON/bài). Mẫu: `tools/example_article.json`.
- `tools/law_text.js` – kho **nguyên văn điều luật** (khóa dạng `'bhxh:70'`, `'bllđ:35'`, `'tncn:10'`…). Trang chủ cũng có bản sao dữ liệu này.
- `tools/law.py` – in nguyên văn: `python3 tools/law.py --list`, `python3 tools/law.py bhxh:70`.
- `tools/calc.py` – hàm tính lương Net 2026 (`g2n(gross, dep, reg, ins)`) để tính ví dụ.
- `tools/check.py` – kiểm tra liên kết, mục lục, sitemap, mã GA, JSON-LD. Phải ra "OK".
- `TOPICS.md` – danh sách chủ đề chờ viết / đã viết / tạm hoãn.

## Số liệu pháp lý chuẩn (năm 2026) – dùng thống nhất
- Lương tối thiểu vùng (NĐ 293/2025, từ 01/01/2026): I 5.310.000 · II 4.730.000 · III 4.140.000 · IV 3.700.000 đ/tháng; giờ 25.500 / 22.700 / 20.000 / 17.800.
- Lương cơ sở = mức tham chiếu BHXH: 2.530.000 đ từ 01/7/2026 (NĐ 161/2026); trước đó 2.340.000.
- Bảo hiểm NLĐ 10,5% (BHXH 8, BHYT 1,5, BHTN 1); DN 21,5% (14 + 3 + 0,5 + 3 + 1) + KPCĐ 2%. Trần BHXH/BHYT 20 × mức tham chiếu = 50.600.000; trần BHTN 20 × LTTV.
- Thuế TNCN (Luật 109/2025/QH15, áp dụng kỳ tính thuế 2026): 5 bậc 5/10/20/30/35% với ngưỡng 10/30/60/100 triệu/tháng; giảm trừ 15,5 triệu bản thân, 6,2 triệu/người phụ thuộc.
- Luật BHXH 41/2024/QH15 (từ 01/7/2025): lương hưu từ đủ 15 năm đóng; BHXH 1 lần Điều 70.
- Luật Việc làm 74/2025/QH15 (từ 01/01/2026): trợ cấp thất nghiệp 60%, tối đa 5 × LTTV.
- Tuổi nghỉ hưu 2026: nam 61 tuổi 6 tháng, nữ 57 tuổi.
Nếu phát hiện văn bản mới thay thế các số liệu trên, **không tự sửa hàng loạt**: ghi vào mục "Tạm hoãn" của TOPICS.md và báo trong báo cáo cuối để chủ web biết.

## Quy trình viết một bài mới (tác vụ tự động)
Mỗi lần chạy **viết đúng 1 bài**.

1. `git pull --rebase origin main`.
2. Chọn chủ đề theo thứ tự ưu tiên:
   a. Nếu lần chạy được giao một chủ đề cụ thể (tin nhắn thêm từ app quản trị) thì viết chủ đề đó.
   b. Nếu không, và phiên có công cụ `ArtifactData`: đọc hàng chờ của **app quản trị** — `ArtifactData` action `query`, url `https://claude.ai/artifact/Rvju7EjtWk7zTfZX9mHCvN`, collection `topics`, where `siteId == "thuviennguoilaodong-com"` và `status == "cho"`; lấy chủ đề có `createdAt` sớm nhất. Không có công cụ hoặc hàng chờ rỗng thì bỏ qua bước này.
   c. Nếu không có chủ đề nào ở trên: mở `TOPICS.md`, lấy chủ đề **đầu tiên** trong "Chờ viết". Kiểm tra chưa có bài trùng nội dung (xem tiêu đề trong `tools/articles*.py` và `content/bai-viet/`).
3. **Nghiên cứu căn cứ pháp lý**:
   - Ưu tiên nguyên văn trong `tools/law_text.js` (`python3 tools/law.py ...`).
   - Nếu cần điều luật chưa có, tìm nguyên văn từ nguồn chính thống (vbpl.vn, chinhphu.vn, luatvietnam.vn, thuvienphapluat.vn) bằng WebSearch/WebFetch. Chỉ dùng văn bản **đang có hiệu lực**; kiểm tra văn bản đã bị thay thế chưa.
   - **Không bao giờ bịa số liệu, số điều, số văn bản.** Chỗ nào không chắc thì viết ở mức chung ("theo hướng dẫn của Bộ…") và không nêu con số.
   - Nếu không đủ căn cứ để viết chính xác: chuyển chủ đề xuống "Tạm hoãn" kèm lý do, chọn chủ đề kế tiếp (tối đa thử 3 chủ đề; nếu cả 3 đều không được thì dừng, không đăng gì và báo cáo).
4. **Viết bài** vào `content/bai-viet/<slug>.json` theo mẫu `tools/example_article.json`:
   - `slug`: chữ thường không dấu, nối bằng gạch ngang, không trùng.
   - `cat`: một trong `luong`, `thue`, `bh`, `lv`.
   - `date`: ngày hôm nay theo giờ Việt Nam (YYYY-MM-DD).
   - `title` (55–75 ký tự, có từ khóa người ta hay tìm), `desc` (140–170 ký tự), `lead` (2–3 câu).
   - `keys`: 3 ý chính. `laws`: danh sách căn cứ, có thể chứa liên kết tới trang tra cứu nguyên văn `<a href="/#ma-muc">…</a>` – chỉ dùng mã mục có thật (check.py sẽ báo nếu sai).
   - `body`: HTML, 900–1.600 chữ, mỗi `<h2>` có `id` (mục lục tự sinh). Dùng các khối có sẵn: `<div class="tbl"><table>…</table></div>` (bảng > 3 cột thêm `class="w"` cho `<table>`), `<div class="calc">` (ví dụ tính), `<div class="note">` (lưu ý), `<div class="tip">`, và khối kêu gọi dùng công cụ `<div class="cta">…</div>` (chép từ bài mẫu).
   - Có **ít nhất 1 ví dụ tính tiền cụ thể**; mọi phép tính phải chạy bằng Python (ví dụ `tools/calc.py`) để chắc chắn đúng.
   - 2–4 liên kết nội bộ tới bài liên quan (`/bai-viet/<slug>/`) và `rel` gồm 2–4 slug.
   - `faq`: 2–3 cặp [câu hỏi, trả lời].
   - Văn phong tự nhiên, xưng "bạn"; không sao chép câu chữ từ trang khác (trừ trích nguyên văn điều luật có ghi rõ); không hứa hẹn, không quảng cáo.
5. `python3 tools/build_blog.py && python3 tools/check.py` – phải ra "OK". Sửa đến khi hết lỗi.
6. Tự rà lại trước khi đăng: từng con số đã khớp nguyên văn luật? ngày hiệu lực đúng? ví dụ tính đúng? không mâu thuẫn với 20 bài cũ và trang chủ?
7. Cập nhật `TOPICS.md`: chuyển chủ đề xuống "Đã viết" dạng `- [x] YYYY-MM-DD – <tiêu đề> (/bai-viet/<slug>/)`. Khi "Chờ viết" còn dưới 5 chủ đề, tự bổ sung 5 chủ đề mới hữu ích cho người lao động (không trùng).
8. Commit tất cả (`content/`, `site/`, `TOPICS.md`, `tools/law_text.js` nếu có thêm) với thông điệp `Bài mới: <tiêu đề>` rồi `git push origin main`. Netlify tự cập nhật web sau khoảng 1 phút.
9. Ghi vào app quản trị (chỉ khi phiên có công cụ `ArtifactData`; lỗi ở bước này không ảnh hưởng việc đăng bài):
   - `set` collection `posts`, doc_id = `<slug>`, data `{"siteId":"thuviennguoilaodong-com","title":<tiêu đề>,"url":"https://thuviennguoilaodong.com/bai-viet/<slug>/","date":<YYYY-MM-DD>,"cat":<cat>,"source":"auto"}`.
   - Nếu chủ đề lấy từ hàng chờ app (bước 2b) hoặc do app giao (2a, có bản ghi `topics` trạng thái `da-giao` trùng nội dung): `update` bản ghi đó thành `{"status":"da-viet","url":<link bài>,"updatedAt":<ISO time>}` (nhớ truyền `if_version` đã đọc).
   - Nếu chủ đề bị tạm hoãn vì thiếu căn cứ: `update` thành `{"status":"tam-hoan","note":<lý do>}`.
10. Báo cáo cuối (tiếng Việt, ngắn): tiêu đề, đường link `https://thuviennguoilaodong.com/bai-viet/<slug>/`, các căn cứ pháp lý đã đối chiếu, điểm nào còn chưa chắc chắn (nếu có).

## Không được làm
- Không xóa hay sửa nội dung bài cũ (trừ khi được yêu cầu), không đổi slug bài đã đăng.
- Không sửa mã Google Analytics (G-QXWRGDZ79R), không thêm mã quảng cáo/AdSense khi chưa được yêu cầu.
- Không push nếu `tools/check.py` còn lỗi.
- Không đăng quá 1 bài mỗi lần chạy.
