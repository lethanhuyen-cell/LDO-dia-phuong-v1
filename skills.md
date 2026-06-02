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

### F. Phân loại địa giới hành chính & Loại trừ trùng lặp địa danh (Local Geotagging & Ambiguity Resolution)
1. **Phân cấp hành chính Hà Nội (Sau sắp xếp):** 
   - Tổng cộng có **126 đơn vị hành chính cấp xã** (gồm 51 phường và 75 xã).
   - Danh sách các địa bàn trọng điểm của Hà Nội cần ghi nhớ để gom tin bài & gắn tag:
     * *Khu vực trung tâm/nội thành:* Hoàn Kiếm, Cửa Nam, Ba Đình, Ngọc Hà, Giảng Võ, Hai Bà Trưng, Vĩnh Tuy, Bạch Mai, Đống Đa, Kim Liên, Văn Miếu - Quốc Tử Giám, Láng, Ô Chợ Dừa, Hồng Hà, Lĩnh Nam, Hoàng Mai, Vĩnh Hưng, Tương Mai, Định Công, Hoàng Liệt, Yên Sở, Thanh Xuân, Khương Đình, Phương Liệt, Cầu Giấy, Nghĩa Đô, Yên Hòa, Tây Hồ, Phú Thượng.
     * *Khu vực mở rộng/ngoại thành:* Tây Tựu, Phú Diễn, Xuân Đỉnh, Đông Ngạc, Thượng Cát, Từ Liêm, Xuân Phương, Tây Mỗ, Đại Mỗ, Long Biên, Bồ Đề, Việt Hưng, Phúc Lợi, Hà Đông, Dương Nội, Yên Nghĩa, Phú Lương, Kiến Hưng, Thanh Liệt, Chương Mỹ, Sơn Tây, Tùng Thiện.
2. **Nguyên tắc loại trừ trùng lặp địa danh (Disambiguation Rules):**
   - Khi quét nội dung hoặc gắn tag theo địa bàn cấp xã/huyện, **bắt buộc phải đối chiếu ngữ cảnh tỉnh thành đi kèm (Hà Nội)** để loại trừ các địa phương trùng tên ở các tỉnh khác.
   - *Ví dụ thực tế:* 
     * Phường **Việt Hưng** (Hà Nội) phân biệt với xã **Việt Hưng** (Hải Dương, Quảng Ninh...).
     * Phường **Hồng Hà** (Hà Nội) phân biệt với phường **Hồng Hà** (Yên Bái, Hạ Long...).
     * Huyện **Chương Mỹ** (Hà Nội) không được nhầm lẫn trong các ngữ cảnh tin bài vùng miền khác.
   - *Thuật toán xử lý:* Chỉ ghi nhận tag địa bàn Hà Nội khi bài viết có tiền tố địa danh (Dateline) là `HÀ NỘI -` hoặc trong nội dung bài viết xuất hiện từ khóa xác nhận ngữ cảnh liên quan đến Hà Nội (như: các tuyến đường ở Hà Nội, các cơ quan ban ngành của Hà Nội, các địa danh lân cận thuộc Hà Nội).

### G. Kỹ năng Gom & Định vị Tag Tự động 4 Lớp Kết hợp Thuật toán Phân loại
Quy trình tối ưu kết hợp đặc tả kỹ thuật PRD (Cơ chế 4 lớp tag) và thuật toán phân loại tự động:

1. **Khớp và Phân bổ Tag theo 4 Lớp Chính thức (PRD)**:
   *   **Lớp 1: Headline place**: Quét Dateline viết hoa đầu bài (ví dụ: `HÀ NỘI -`, `TPHCM -`) để gợi ý tag địa phương chính (Confidence Score = 99%).
   *   **Lớp 2: In-text places**: Quét nội dung bài viết và đối chiếu với danh sách các quận, huyện, thị xã trực thuộc tỉnh để tự động điền các tag địa bàn nhỏ.
   *   **Lớp 3: Affected areas**: Dựa trên quy tắc liên đới địa lý (ví dụ: các tỉnh giáp ranh hoặc dự án hạ tầng liên tỉnh như Vành đai 4, Cao tốc Biên Hòa - Vũng Tàu) để tự động bổ sung tag khu vực ảnh hưởng giáp ranh.
   *   **Lớp 4: Responsible Office / VPTT**: Tự động gán tag cơ quan văn phòng thường trú phụ trách theo địa bàn hành chính sáp nhập mới (ví dụ: bài viết có tag thuộc TPHCM, Bình Dương, BRVT sẽ tự động nhận tag `VPTT Đông Nam Bộ`).

2. **Công thức Điểm số liên quan ($S$) & Giải quyết Trùng lặp (Entity Disambiguation)**:
   *   **Công thức tính điểm**:
       $$S = 10.0 \cdot C_{title} + 8.0 \cdot C_{tag} + 5.0 \cdot C_{summary} + 1.0 \cdot C_{body}$$
       *(Với $C$ là tần suất xuất hiện của từ khóa địa lý trong từng phần của bài viết. Ngưỡng tự động duyệt là $S \ge 15$).*
   *   **Xử lý trùng lặp tên địa bàn (Ví dụ: Châu Thành - Long An vs Châu Thành - Tây Ninh)**: Đối chiếu chéo (Cross-reference) với các từ khóa bối cảnh phụ thuộc (Secondary Context Keywords) đặc trưng của tỉnh đi kèm để gán đúng.

---

### J. Cơ chế Cấu hình URL Rewrite & Định tuyến ảo cho Hub & Spoke
Để giải quyết mâu thuẫn giữa việc giữ cấu trúc thư mục SEO phân cấp chuẩn mực cho Google và hiển thị URL ngắn gọn thân thiện cho độc giả:
1.  **Phân mục vật lý (Physical SEO Silo):** Toàn bộ cấu trúc được lưu trữ dưới dạng `laodong.vn/vung-mien/[hub]/[spoke]/` (ví dụ: `laodong.vn/vung-mien/dong-nam-bo/dong-nai/`). Đây là đường dẫn thực tế duy nhất mà Google quét được, giúp bảo toàn cấu trúc phân cấp địa giới hành chính và tối ưu cấu trúc Silo.
2.  **Định tuyến ảo rút ngắn (Short Virtual URL):** Độc giả truy cập qua link ảo cực ngắn `laodong.vn/[spoke]` (ví dụ: `laodong.vn/dongnai`).
3.  **Quy trình định tuyến Web Server (Nginx Proxy Rewrite):**
    *   **Nginx Map Table:** Sử dụng khối cấu hình `map $uri $regional_spoke_uri` bên ngoài khối `server` để lưu danh sách route ảo. Cơ chế này biên dịch dữ liệu thành bảng băm giúp tra cứu với tốc độ $O(1)$.
    *   **Internal Rewrite:** Sử dụng chỉ thị `rewrite` trong khối `location /` của Nginx để chuyển hướng ngầm mà không đổi địa chỉ hiển thị trên trình duyệt (`PAGER` hoặc đổi URL hiển thị).
    *   **Thẻ Canonical:** Trên các trang Spoke được trả về, bắt buộc nhúng thẻ `<link rel="canonical" href="https://laodong.vn/vung-mien/[hub]/[spoke]/" />` để chỉ định tuyệt đối cho Googlebot về trang vật lý chính thức, phòng ngừa lỗi trùng lặp nội dung (duplicate content).
    *   **Breadcrumb JSON-LD:** Cung cấp BreadcrumbList 4 lớp rõ ràng trong Schema để Google nhận diện phân cấp địa lý.

---

### K. Tích hợp Chỉ số Cạnh tranh (PCI) & Đồng bộ Tiện ích Spoke (Spoke Context Sync)
Để củng cố uy tín nội dung (EEAT) và đảm bảo tính nhất quán của giao diện khi người dùng chuyển đổi giữa các Spoke:
1.  **Thiết kế Khung Chân dung Địa phương (Local Profile Card):** Tích hợp thông tin diện tích, dân số, GRDP tăng trưởng và số lượng KCN để vẽ chân dung địa bàn.
2.  **Bộ chỉ số hành chính công chính thống:** Tải và trình diễn điểm số/vị trí xếp hạng PCI, PAPI, PAR Index để cung cấp dữ liệu tham chiếu xã hội chất lượng cao cho độc giả.
3.  **Thuật toán Đồng bộ Khung Tiện ích khi Click Tab (Context Syncing):**
    *   *Breadcrumbs:* Cập nhật thẻ breadcrumbs HTML dynamically phản ánh đúng phân cấp địa giới hành chính của Spoke được chọn.
    *   *Weather:* Thay đổi tọa độ địa lý truyền vào hàm gọi API thời tiết (Ví dụ: Biên Hòa cho Đồng Nai, TP.HCM cho TP.HCM) và cập nhật hiển thị địa danh.
    *   *Lịch cắt điện & Tags:* Đổi liên kết trỏ về tag chuyên đề "Lịch cắt điện [Tỉnh]" tương ứng trên domain chính laodong.vn.
    *   *Profile Widget:* Cập nhật nội dung mô tả cấu trúc kinh tế và khuyến nghị cải thiện cho từng Spoke.

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

### Ngày 31/05/2026:
* **Nội dung:** 
  - Cập nhật thông tin phân cấp hành chính Hà Nội mới nhất sau khi sắp xếp (126 xã/phường, gồm 51 phường và 75 xã) và các quy tắc lọc loại trừ trùng lặp thực thể địa danh (Disambiguation Rules).
  - Viết và chạy thành công script cào bài viết tự động theo địa danh cấp xã/phường Hà Nội (`scrape_hanoi_local.py`).
  - Tích hợp thành công dữ liệu ẩm thực - du lịch Hà Nội thực tế từ laodong.vn qua script `scrape_hanoi_handbook.py` để thay thế toàn bộ tít giả lập và link rỗng `#` tại khối "Cẩm nang Hà Nội: Ăn gì - Chơi gì - Ở đâu?".
  - Đồng bộ hóa ảnh đại diện thực tế từ người dùng cho tin Công an Hà Nội, tích hợp hàng 3 bài viết dưới Main Cover và khắc phục lỗi co giãn ảnh bằng CSS Aspect-Ratio độc lập. Rà soát, ánh xạ lại toàn bộ ảnh gốc chất lượng cao cho các bài viết tiêu điểm.
* **Kinh nghiệm rút ra:** 
  - Khi gom tin và gắn tag địa bàn cấp xã/huyện, cần rà soát ngữ cảnh cụ thể để tránh việc gom nhầm các địa phương trùng tên ở các tỉnh thành khác không thuộc Hà Nội.
  - Sử dụng CSS Grid kết hợp inline CSS với thuộc tính `aspect-ratio` và `object-fit: cover` là giải pháp chống méo, kéo dài ảnh triệt để nhất khi làm việc với các hệ thống template động chịu ảnh hưởng bởi CSS ngoài từ CDN.
  - Định kỳ rà soát các tệp ảnh mockup để phát hiện các trường hợp Unsplash ghi đè nhầm lên ảnh địa phương thực tế đã tối ưu trước đó.

### Ngày 01/06/2026:
* **Nội dung:** 
  - Triển khai thành công kiến trúc Hub & Spoke bằng cơ chế Tab Bar động tại giao diện [demo_landing_page_tphcm.html](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/demo_landing_page_tphcm.html) cho TP.HCM & Đông Nam Bộ.
  - Tối ưu hóa scraper quét tin bài thực tế và tích hợp carousel slide "Đọc nhiều nhất" gọn gàng ở sidebar (3 slide xoay vòng tự động).
  - Thiết kế quy trình định tuyến ảo hệ thống bằng cơ chế URL Rewrite (tầng Nginx Proxy Map) và giải thích trực quan hóa mô hình Hub & Spoke URL.
  - Tích hợp bộ số liệu Chỉ số cạnh tranh cấp tỉnh (PCI), PAPI, PAR Index và thông tin KCN vào cấu trúc "Chân dung Địa phương" ngay dưới thanh lọc địa bàn.
  - Triển khai cơ chế đồng bộ khung tiện ích Spoke (Context Syncing) thay đổi đồng thời breadcrumbs, thời tiết và link chuyên đề cắt điện theo vị trí địa lý của Spoke đang hoạt động.
  - **Mới (Nâng cấp tin mới nhất):** Thiết kế dải Tin mới nhất (Latest News Ticker Bar) nằm ngay dưới thanh Breadcrumbs theo phong cách CafeF. Sử dụng CSS Keyframe animation (`translateX(0)` sang `translateX(-50%)`) kết hợp nhân bản kép nội dung HTML danh sách 7 bài viết mới nhất để tạo hiệu ứng cuộn ngang vô hạn (seamless infinite marquee CSS) và dừng lại khi hover. Tích hợp trực tiếp sự kiện click trên thanh tin để mở bài đọc nhanh qua Local Reader Modal (Modal Overlay) giúp độc giả không bị điều hướng ra khỏi trang địa phương.
* **Kinh nghiệm rút ra:**
  - Đối với các Spoke có dữ liệu ít hơn Hub (như Tây Ninh, Đồng Nai), cơ chế trộn gộp (merge fallback) là rất cần thiết để đảm bảo hiển thị đủ nội dung lưới tin bài.
  - Sử dụng `map` định tuyến trong Nginx thay thế `if` lồng nhau giúp cải thiện hiệu năng và bảo trì dễ dàng khi mở rộng ra 63 tỉnh thành.
  - Thiết kế Spoke Context Sync đồng bộ thời gian thực giúp nâng cao độ chính xác về mặt logic địa lý, tạo cảm giác chuyên nghiệp khi người dùng tương tác chuyển đổi vùng.
  - Sử dụng giải pháp Event Listener đánh chặn (Click Event Interceptor) ở cấp `document` giúp kiểm soát toàn bộ lượt click mà không cần can thiệp chỉnh sửa hàng chục chuỗi template HTML sinh động.
  - Nên đưa trực tiếp các thẻ HTML & JavaScript bổ trợ cho Modal và Ticker vào template sạch (`demo_landing_page_hanoi_clean.html`) để khi biên dịch layout tự động (chạy `apply_ads_layout.py` hoặc `apply_tphcm_layout.py`) không bị ghi đè mất mã nguồn tính năng.
  - Cần chạy bypass execution policy của PowerShell (`powershell -ExecutionPolicy Bypass -Command "..."`) khi triển khai lệnh Node CLI (như `npx vercel`) trên hệ điều hành Windows để tránh lỗi phân quyền.
  - Để đảm bảo hiệu ứng marquee chạy vô hạn không bị giật (jump) khi lặp lại, tổng chiều rộng nội dung của container con phải khớp chính xác với bước dịch chuyển của Keyframe (dịch chuyển đúng `-50%` của chiều rộng nhân bản kép).
  - Tải tin và sắp xếp theo mốc thời gian thực tế giúp giao diện sống động và cập nhật liên tục đúng với tôn chỉ "Tin mới nhất".

### Ngày 02/06/2026:
* **Nội dung:** 
  - Khắc phục triệt để lỗi hiển thị vỡ khung layout trên toàn bộ các trang địa phương do việc replace chuỗi `<style>` không an toàn trước đó.
  - Thiết kế patcher Option A tối ưu hóa giao diện an toàn bằng cách định vị và chèn quy tắc CSS mobile chính xác thông qua Regex neo biên giới (anchor) `</style>\s*<!-- WALLPAPER AD SLOTS -->`.
  - Thay đổi an toàn breakpoint wallpaper ads và JS checks từ `1400px` lên `1540px`, cùng tăng font size bài viết từ `11.5px` lên `13px`.
  - **Sửa lỗi hiển thị cuối trang (Mobile Responsiveness & Grid Squishing):** Khắc phục lỗi hiển thị co quắp/móp méo các khối "Dân sinh & Đời sống", "Kết nối Tiêu dùng" và "Bảng giá thị trường" trên di động. Đồng thời, tìm và sửa lỗi thiếu thẻ đóng `</div>` ở khối 5.5 trong `apply_tphcm_layout.py` khiến các khối bên dưới bị lồng sai lệch và hiển thị co rúm thành cột dọc hẹp trên desktop.
  - **Tích hợp Banner tiếp thị:** Thiết kế hình ảnh và tích hợp banner quảng cáo giả lập cho siêu thị WinMart về chương trình Khuyến mãi mùa hè 2026, cải tiến thiết kế thẻ đồng hành chuyên mục thành cấu trúc card sang trọng kết hợp ảnh nền sắc nét và overlay text gradient.
  - **Quy hoạch thiết kế Premium nửa cuối trang:** Loại bỏ các hộp thô cứng, viền thô và các khối inline-style xám thô tĩnh. Giới thiệu các class thiết kế chuyên nghiệp như `.premium-card` (có bóng mờ tinh tế, border nhẹ nhàng, hover nâng nhẹ chiều sâu), `.category-card` (tiêu đề chuyên mục phân tuyến dạng line tối giản tinh tế), và cấu trúc bảng biểu `.interactive-table` mượt mà có highlight hover. Sửa triệt để các lỗi thẻ `div` lồng nhau bị unclosed bằng cách đóng chính xác `wrapper` và `b-center` trước thẻ `<script>` cũng như đóng đúng vị trí `BLOCK 5.5`.


* **Kinh nghiệm rút ra:**
  - Tuyệt đối không sử dụng replace chuỗi tĩnh quá chung chung (như `<style>`) trên mã nguồn Python để tiêm CSS vào mẫu HTML, vì điều đó dễ trùng khớp với các biến chuỗi HTML định nghĩa ở đầu tệp.
  - Luôn sử dụng Regex neo biên giới kết hợp với các bình luận HTML đặc thù (ví dụ: `<!-- WALLPAPER AD SLOTS -->`) để định vị điểm tiêm mã cực kỳ chính xác.
  - Tránh khai báo lặp lại thuộc tính `class` trên cùng một thẻ HTML vì trình duyệt sẽ bỏ qua thuộc tính khai báo sau.
  - Mọi bố cục Grid/Flexbox dạng cột ghép đôi (như bảng giá đi kèm banner tài trợ) bắt buộc phải tích hợp sẵn quy tắc thu gọn (stacking) bằng CSS `@media` để đảm bảo trải nghiệm hiển thị an toàn trên thiết bị cầm tay.
  - **Quan trọng về HTML Tag Closures:** Chỉ cần thiếu 1 thẻ đóng `</div>` ở phần trên có thể phá hủy hoàn toàn hiển thị của phần dưới trang bằng cách kéo các container con cấp dưới lồng vào trong grid layout có tỉ lệ nhỏ của container cha. Luôn xác thực tính hợp lệ của cây DOM khi xảy ra các lỗi co quắp layout kỳ lạ.









