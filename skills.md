# Kỹ năng & Kinh nghiệm Tích lũy (Skills & Knowledge Base)

> [!IMPORTANT]
> **QUY TẮC TỰ ĐỘNG CẬP NHẬT:**
> File này sẽ được AI chủ động cập nhật kinh nghiệm, quy trình kỹ thuật mới sau mỗi lần hoàn thành công việc hoặc thay đổi lớn trong dự án **mà không cần người dùng nhắc nhở**.

---

## 🧭 1. Tổng quan Dự án & Bối cảnh

- **Tên dự án:** Landing Page Thường Trú (Lao Động Vùng Miền).
- **Mục tiêu:** Xây dựng hệ thống trang thông tin địa phương tích hợp sâu với SEO, tối ưu giao diện độc giả (UX/UI), nâng cao trải nghiệm đọc báo vùng miền, phục vụ hoạt động tác nghiệp tòa soạn và định hướng thương mại hóa (ads, tài trợ, PR).
- **Cấu trúc tài liệu nền tảng:**
  - [1_chien_luoc_va_ke_hoach_pilot.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/1_chien_luoc_va_ke_hoach_pilot.md): Chiến lược triển khai giai đoạn thí điểm (Hà Nội).
  - [2_sop_bien_tap_va_van_hanh.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/2_sop_bien_tap_va_van_hanh.md): Quy trình tác nghiệp của Ban Biên tập và Phóng viên thường trú.
  - [3_dac_ta_ky_thuat_va_seo.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/3_dac_ta_ky_thuat_va_seo.md): Tiêu chuẩn kỹ thuật, tối ưu hóa tốc độ tải trang, cấu trúc URL, và Schema JSON-LD.
  - [4_mo_hinh_thuong_mai_hoa.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/4_mo_hinh_thuong_mai_hoa.md): Cách thức khai thác doanh thu (tài trợ chuyên mục, bài viết PR, e-commerce địa phương).
  - [5_risk_register.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/5_risk_register.md): Quản trị rủi ro về pháp lý, kỹ thuật, nhân sự và tài chính.
  - [6_quy_trinh_toa_soan_va_seo_tag.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/6_quy_trinh_toa_soan_va_seo_tag.md): Quy trình xuất bản nội dung và gắn thẻ tối ưu hóa SEO.
  - [7_tai_lieu_chuan_hoa_quy_trinh_trien_khai.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/7_tai_lieu_chuan_hoa_quy_trinh_trien_khai.md): Quy trình 8 bước chuẩn hóa từ khảo sát đến bàn giao.

---

## 🛠️ 2. Kỹ năng & Quy trình Kỹ thuật Tích lũy

### A. Tối ưu cấu trúc HTML & SEO Local (Landing Page Báo chí)
1. **Thiết kế Mobile-First & Responsive:** Luôn ưu tiên hiển thị trên di động vì lượng traffic báo chí địa phương chủ yếu đến từ mobile (thường chiếm >80%).
2. **Kỹ thuật tối ưu SEO:**
   - Đảm bảo thẻ Title có cấu trúc: `[Tên Địa Phương] - Tin tức mới nhất, nóng nhất | Báo Lao Động`.
   - Có đầy đủ các thẻ meta: `description`, `keywords`, `robots` và meta social (`og:title`, `og:description`, `og:image`).
   - Cấu trúc thẻ Heading (`h1` duy nhất cho tên chuyên mục/tỉnh thành, `h2` cho các khối tin lớn, `h3` cho tiêu đề bài viết con).
3. **Tích hợp Schema.org (JSON-LD):** 
   - Sử dụng `NewsArticle` cho trang chi tiết.
   - Sử dụng `CollectionPage` hoặc `ItemList` cho trang danh sách/chuyên mục để Google Index cấu trúc tin tốt nhất.

### B. Tổ chức Dữ liệu JSON & Cấu trúc Nội dung
* **Cấu trúc file Mockup Articles (`hanoi_articles.json`):** 
  * Lưu trữ cấu trúc phân tầng (Tin Tiêu Điểm, Tin Mới Nhất, Tin Theo Chuyên Mục: Đô Thị, Dân Sinh, Kinh Tế, Du Lịch).
  * Mỗi item bài viết cần có: `id`, `title`, `summary`, `thumbnail`, `published_date`, `author`, `slug`, `tags`, `views_count`.

### C. Quản lý Git & Triển khai Đa thiết bị (Cross-device Sync)
* **Kinh nghiệm đồng bộ Git:**
  * Luôn cấu hình `.gitignore` chuẩn xác để tránh đẩy các file rác (`node_modules`, `.env`, cache trình duyệt hoặc file hệ thống của hệ điều hành).
  * Quy trình thiết lập kết nối repo Github từ xa an toàn bằng SSH key hoặc HTTPS (sử dụng Personal Access Token).

---

### D. Kỹ thuật Quét Dữ liệu Báo chí & Vượt rào bảo mật (Scraping & Cookie Bypass)
1. **Bypass Cookie Gate:** Báo Lao Động sử dụng cơ chế bảo mật thiết lập cookie động thông qua JavaScript (`document.cookie="D1N=..."`). Để vượt qua, cần gửi một request khởi tạo, dùng Regex trích xuất chuỗi thiết lập cookie, đưa cookie này vào `http.cookiejar` và khởi tạo opener để sử dụng cho các request tải danh sách/chi tiết tiếp theo.
2. **Thuật toán quét tin tức địa phương mở rộng (Expanded Regional Scraper):**
   - **Tầng 1 (Tối ưu hóa tốc độ):** Lọc bài viết nhanh qua tiêu đề, tóm tắt (chapeau) và đường dẫn URL dựa trên danh sách từ khóa địa phương/địa danh. Nếu khớp, đánh dấu bài viết thuộc địa phương ngay lập tức và bỏ qua việc tải chi tiết để tiết kiệm băng thông và tránh bị chặn.
   - **Tầng 2 (Quét sâu nội dung):** Với các bài viết ứng viên không khớp ở Tầng 1, thực hiện tải nội dung trang chi tiết bài viết (detail page) và quét sâu văn bản bài viết để tìm kiếm các thực thể, địa danh, ban ngành cục bộ của địa phương đó.
3. **Cơ chế chống chặn (Anti-bot rate limiting):** Sử dụng thời gian dừng ngẫu nhiên hoặc tối thiểu `0.15s - 0.2s` giữa các request trang chi tiết để đảm bảo an toàn cho dải IP và tránh quá tải hệ thống nguồn.

### E. Xử lý hiển thị Layout dạng Lưới (Grid & Column Overlapping Resolution)
* Để khắc phục triệt để lỗi tràn/chồng chữ lên nhau (text overlapping) khi render dữ liệu động có độ dài tiêu đề khác nhau trong các cột lưới:
  - Thay thế `justify-content: space-between` bằng `justify-content: flex-start` trong thẻ cha của cột.
  - Sử dụng `min-height` cố định cho các khối tin bài trong cột chuyên mục.
  - Sử dụng CSS `-webkit-line-clamp` để giới hạn số dòng tiêu đề hiển thị đồng bộ (ví dụ: giới hạn 2-3 dòng cho tiêu đề bài viết phụ).

---

## 🧠 3. Kinh nghiệm Giải quyết Vấn đề & Best Practices

1. **Tính nhất quán của giao diện (UI Consistency):**
   - Khi chỉnh sửa template HTML (như `laodong_home_template.html`, `demo_landing_page_hanoi.html`), cần tuân thủ bảng mã màu thương hiệu của Báo Lao Động (đỏ chủ đạo `#c0392b` hoặc `#d35400`, font chữ chân phương có độ đọc cao như *Arial*, *Helvetica*, hoặc *Segoe UI*).
2. **Quản lý bối cảnh phiên làm việc (Session Context Management):**
   - Sử dụng file [session_state.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/session_state.md) làm "neo thông tin".
   - Mỗi khi kết thúc phiên, cập nhật tệp này. Khi bắt đầu phiên mới, AI chỉ cần đọc file này để nắm bắt tiến độ mà không cần hỏi lại người dùng hoặc quét toàn bộ tài liệu từ đầu.

---

## 📅 4. Nhật ký Học tập & Cải tiến Hàng ngày

### Ngày 29/05/2026:
* **Nội dung:** Khởi tạo hệ thống hóa tài liệu, đóng gói file kỹ năng (`skills.md`) và thiết lập cơ chế tự động ghi nhớ trạng thái qua `session_state.md`.
* **Kinh nghiệm rút ra:** Việc phân loại rõ ràng tài liệu thành các mảng (Chiến lược, Vận hành, Kỹ thuật, Thương mại) giúp giảm thiểu sự chồng chéo thông tin và dễ dàng mở rộng sang các địa phương tiếp theo ngoài Hà Nội (như TP.HCM, Đà Nẵng).
* **Nâng cấp cào tin:** Xây dựng thành công thuật toán cào bài viết Hà Nội mở rộng, tự động tải trang chi tiết để rà soát thực thể địa phương khi tiêu đề không chứa chữ "Hà Nội". Quét thành công hơn 1.500 bài viết và đồng bộ tự động lên Vercel. Ghi nhận bài học về chống tràn layout khi hiển thị text động.
