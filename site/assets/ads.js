/*
 * CẤU HÌNH QUẢNG CÁO – Thư Viện Người Lao Động
 * Hiện TẮT. Các vị trí quảng cáo đã được chừa sẵn trên mọi trang (thẻ <div class="ad-slot" data-slot="...">),
 * đang ẩn hoàn toàn nên không ảnh hưởng giao diện.
 * Khi Google AdSense duyệt web:
 *   1. enabled: true
 *   2. client: mã nhà xuất bản dạng "ca-pub-XXXXXXXXXXXXXXXX"
 *   3. điền mã từng đơn vị quảng cáo (ad unit / data-ad-slot) vào slots; vị trí nào để trống sẽ không hiện.
 *   4. tạo tệp site/ads.txt theo hướng dẫn của AdSense.
 */
window.TVNLD_ADS = {
  enabled: true,   // bật từ 07/11/2026: Quảng cáo tự động của AdSense (chủ web yêu cầu)
  client: 'ca-pub-6036509094866269',
  slots: {
    'trang-chu-ket-qua': '',   // trang chủ: dưới kết quả tính lương
    'trang-chu-cuoi': '',      // mọi tab trang chủ: trên khung "Bài viết hữu ích"
    'bai-dau': '',             // bài viết: sau phần "Ý chính"
    'bai-giua': '',            // bài viết: giữa bài
    'bai-cuoi': '',            // bài viết: trước "Căn cứ pháp lý"
    'bai-ben-phai': '',        // bài viết: cột bên phải (máy tính)
    'danh-sach': ''            // trang danh sách bài viết
  }
};
(function () {
  var c = window.TVNLD_ADS;
  if (!c || !c.enabled || !/^ca-pub-\d+$/.test(c.client)) return;
  var s = document.createElement('script');
  s.async = true; s.crossOrigin = 'anonymous';
  s.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + c.client;
  document.head.appendChild(s);
  function fill() {
    document.querySelectorAll('.ad-slot[data-slot]').forEach(function (el) {
      var id = c.slots[el.getAttribute('data-slot')];
      if (!id || el.getAttribute('data-filled')) return;
      el.setAttribute('data-filled', '1'); el.hidden = false; el.classList.add('on');
      el.innerHTML = '<span class="ad-lb">Quảng cáo</span><ins class="adsbygoogle" style="display:block" data-ad-client="' + c.client +
        '" data-ad-slot="' + id + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fill); else fill();
})();
