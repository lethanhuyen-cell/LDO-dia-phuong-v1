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
   *   **Xử lý trùng lặp tên địa bàn (Ví dụ: Châu Thành - Long An vs Châu Thành - Tây Ninh)**: Đối chiếu chéo (Cross-reference) với các từ khóa bối cảnh phụ thuộc (Secondary Context Keywords) đặc trưng của tỉnh đi kèm để gán đúng tag Lớp 2.

### H. Kiến trúc Cấu trúc Mạng lưới Hub & Spoke Toàn Quốc (7 Văn phòng Thường trú)
Đồng bộ hóa sơ đồ ánh xạ quản lý địa giới hành chính giữa trang cổng (Hub) và trang địa phương (Spoke) cho toàn hệ thống:
1. **VP Tây Bắc Bộ (Hub)** ──► *Spokes:* Cao Bằng, Lạng Sơn, Lai Châu, Điện Biên, Sơn La, Lào Cai, Tuyên Quang, Phú Thọ, Thái Nguyên.
2. **VP Đông Bắc Bộ (Hub)** ──► *Spokes:* Quảng Ninh, Hải Phòng, Hưng Yên, Ninh Bình.
3. **VP Bắc Trung Bộ (Hub)** ──► *Spokes:* Thanh Hoá, Nghệ An, Hà Tĩnh, Thừa Thiên Huế, Quảng Trị.
4. **VP Miền Trung (Hub)** ──► *Spokes:* Quảng Ngãi, Đà Nẵng, Gia Lai.
5. **VP Tây Nguyên (Hub)** ──► *Spokes:* Lâm Đồng, Khánh Hoà, Đắk Lắk.
6. **VP ĐBSCL (Hub)** ──► *Spokes:* Vĩnh Long, Cần Thơ, Cà Mau, Đồng Tháp, An Giang.
7. **VP TPHCM & Đông Nam Bộ (Hub)** ──► *Spokes:* Tây Ninh, TP.HCM, Đồng Nai (cấu trúc sáp nhập mới).

*Quy tắc định tuyến (Routing Rule):* Mọi bài viết thuộc Spoke bất kỳ sẽ tự động được đồng bộ ngược lên Hub tương ứng thông qua quan hệ thừa kế Tag Lớp 4.

### I. Quy tắc Phân cấp & Kế thừa Địa giới sau Sáp nhập (Ông - Cha - Con - Cháu)
Hệ thống tự động nhận diện và kế thừa ngược (bubble up) theo cây thư mục hành chính mới sau sáp nhập:
- **Ông (Vùng thường trú/Hub)**: Đông Nam Bộ mới.
- **Cha (Địa phương cấp Tỉnh sau sáp nhập)**: TPHCM mới (đã gộp Bình Dương, BRVT), Đồng Nai mới, Tây Ninh mới.
- **Con (Quận/Huyện/Thành phố trực thuộc)**: Thủ Đức, Dĩ An, Biên Hòa, Trảng Bàng, Kiến Tường...
- **Cháu (Phường/Xã/Thị trấn/Tuyến đường/Địa danh cụ thể)**: Phường An Phú, Làng nổi Tân Lập, KDL Đại Nam...

*Cơ chế tự động hóa:* Khi bài viết được gắn tag ở cấp **Cháu** (Ví dụ: `KDL Đại Nam`), hệ thống tự động suy luận logic phân cấp để gán các tag ở cấp cao hơn: **Con** (`Bến Cát`) ──► **Cha** (`TPHCM`) ──► **Ông** (`Đông Nam Bộ`). Quy tắc này áp dụng đồng nhất cho tất cả các tỉnh thành đã sáp nhập trên cả nước để đảm bảo không bị sót tin bài và gom tag chính xác tuyệt đối.

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
  - **Mới:** Tích hợp thành công dữ liệu ẩm thực - du lịch Hà Nội thực tế từ laodong.vn qua script `scrape_hanoi_handbook.py` để thay thế toàn bộ tít giả lập và link rỗng `#` tại khối "Cẩm nang Hà Nội: Ăn gì - Chơi gì - Ở đâu?".
  - **Mới:** Đồng bộ hóa ảnh đại diện thực tế từ người dùng cho tin Công an Hà Nội, tích hợp hàng 3 bài viết dưới Main Cover và khắc phục lỗi co giãn ảnh bằng CSS Aspect-Ratio độc lập. Rà soát, ánh xạ lại toàn bộ ảnh gốc chất lượng cao cho các bài viết tiêu điểm.
* **Kinh nghiệm rút ra:** 
  - Khi gom tin và gắn tag địa bàn cấp xã/huyện, cần rà soát ngữ cảnh cụ thể để tránh việc gom nhầm các địa phương trùng tên ở các tỉnh thành khác không thuộc Hà Nội.
  - Sử dụng CSS Grid kết hợp inline CSS với thuộc tính `aspect-ratio` và `object-fit: cover` là giải pháp chống méo, kéo dài ảnh triệt để nhất khi làm việc với các hệ thống template động chịu ảnh hưởng bởi CSS ngoài từ CDN.
  - Định kỳ rà soát các tệp ảnh mockup để phát hiện các trường hợp Unsplash ghi đè nhầm lên ảnh địa phương thực tế đã tối ưu trước đó.

### Ngày 01/06/2026:
* **Nội dung:** Bắt đầu phiên làm việc ngày mới, sẵn sàng mở rộng và tiếp quản yêu cầu lập trình tiếp theo của người dùng.
* **Kinh nghiệm rút ra:** Luôn tự động mở đọc `session_state.md` khi bắt đầu phiên mới để đồng bộ trạng thái và tiếp quản To-Do list liền mạch.



