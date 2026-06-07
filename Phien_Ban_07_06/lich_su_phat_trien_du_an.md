# NHẬT KÝ PHÁT TRIỂN DỰ ÁN CHUNG (MASTER PROJECT LOG)
## DỰ ÁN CỐT LÕI: CHUYÊN TRANG LAO ĐỘNG ĐỊA PHƯƠNG (LAODONG.VN)

Tài liệu này ghi nhận toàn bộ quá trình phát triển, tích hợp kỹ thuật và các cột mốc chiến lược thương mại của dự án qua từng buổi làm việc thực tế nhằm cung cấp góc nhìn toàn cảnh về quá trình xây dựng hệ sinh thái chuyên trang địa phương Lao Động.

---

## 📅 TIMELINE PHÁT TRIỂN & TÍCH HỢP CHI TIẾT

### 1. PHIÊN LÀM VIỆC NGÀY 29/05/2026: KHỞI ĐỘNG DỰ ÁN & THIẾT KẾ BẢN SẠCH
*   **Mục tiêu chính:** Xây dựng hạ tầng dữ liệu và thiết lập giao diện sạch (Original Layout) cho chuyên trang Hà Nội.
*   **Công việc kỹ thuật đã thực hiện:**
    *   **Lọc dữ liệu:** Viết mã cào dữ liệu tự động, thu thập và chuẩn hóa hơn 100 bài viết thực tế về Hà Nội từ Báo Lao Động thành tệp dữ liệu sạch [hanoi_final_consolidated.json](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/hanoi_final_consolidated.json).
    *   **Giao diện sạch:** Thiết lập trang chủ tĩnh sạch [demo_landing_page_hanoi.html](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/demo_landing_page_hanoi.html) và ánh xạ sang [index.html](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/index.html).
    *   **Cấu trúc dữ liệu phân loại 4 lớp (Taxonomy SEO):** Áp dụng cấu trúc phân tách sâu từ Vùng miền (Miền Bắc) -> Tỉnh/Thành (Hà Nội) -> Quận/Huyện (Hoàn Kiếm, Cầu Giấy...) -> Chuyên đề (Thời sự, Đô thị, Giáo dục...).
    *   **SEO & Schema:** Nhúng siêu dữ liệu chuẩn SEO và mã cấu trúc JSON-LD Breadcrumb & CollectionPage để Google dễ dàng index trang.
    *   **Xử lý hình ảnh:** Viết mã Python để khắc phục triệt để lỗi lazyload làm mất hình ảnh trên mã nguồn gốc; sử dụng AI tạo sinh để làm sạch và nâng cấp kho ảnh Hà Nội chất lượng cao cho các bài viết Tiêu điểm chính.
*   **Kết quả bàn giao:** Bản mẫu chuyên trang Hà Nội giao diện sạch hoàn toàn, hiển thị tin tức trơn tru, sẵn sàng cho công tác tối ưu hóa SEO.

---

### 2. PHIÊN LÀM VIỆC NGÀY 30/05/2026: QUY HOẠCH QUẢNG CÁO SỐ & BÁO CHÍ TƯƠNG TÁC (INTERACTIVE JOURNALISM)
*   **Mục tiêu chính:** Thương mại hóa chuyên trang và lập trình các tính năng tương tác hai chiều để giữ chân độc giả và thu hút hộ kinh doanh/nhãn hàng.
*   **Chi tiết các giải pháp và sản phẩm kỹ thuật đã tích hợp:**

#### A. Giả lập quy hoạch 5 vị trí Quảng cáo hiển thị tiêu chuẩn (IAB Standards)
Tích hợp các vị trí quảng cáo mô phỏng trên trang demo độc lập [demo_landing_page_hanoi_ads.html](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/demo_landing_page_hanoi_ads.html), tất cả đều mang tem nhãn đỏ **`QC GIẢ LẬP`** để bảo đảm tính thử nghiệm chuẩn mực:
1.  **Top Billboard (970x250):** Banner dải màu xanh navy chuyển sắc sang trọng ngay đầu trang (Thương hiệu: VinFast VF9).
2.  **Sidebar Medium Rectangle (300x250):** Hộp quảng cáo góc phải dưới Tiêu điểm (Thương hiệu: Vietcombank Priority).
3.  **Mid-Page Banner (728x90):** Banner cắt ngang chia cắt các khối tin bài lớn (Thương hiệu: Vinhomes Grand Park).
4.  **Catfish Floating Bottom Banner (970x90):** Banner bám sát chân màn hình có nút đóng `✕` tương tác thực tế (Thương hiệu: VinFast).
5.  **Wallpaper/Skin Ads (160x600 x 2):** Banner bọc dọc hai bên sườn trang trên màn hình Desktop rộng (>1400px).

#### B. Quy hoạch không gian nội dung PR tự nhiên (Native Ads)
*   **Chuyên đề đồng hành thương hiệu "HÀ NỘI 360°":** Khối tài trợ độc quyền bởi VinFast Xanh với 3 bài viết chuyên đề về Cẩm nang xanh, Ẩm thực du lịch và Hành trình di sản.
*   **Cẩm nang bản địa "Ăn gì - Chơi gì - Ở đâu":** Khối phân chia 3 cột nội dung lồng bài viết PR khéo léo:
    *   *Ăn gì:* Phở đêm phố cổ (PR), quán ốc vỉa hè ngon rẻ.
    *   *Chơi gì:* Điểm ngắm hoàng hôn Hồ Tây, tour xe đạp đêm di sản văn hóa (PR).
    *   *Ở đâu:* Biệt thự sinh thái nghỉ dưỡng Ba Vì (PR), khách sạn boutique Hoàn Kiếm.
*   **Sponsored Article Badge:** Ghi nhận thực tế việc gán nhãn thương mại **`TÀI TRỢ`** trực tiếp lên bài viết số 3 tại khối Tiêu điểm Hà Nội.

#### C. Thâm nhập tệp khách hàng "Đuôi Dài" (SMEs & Hộ kinh doanh)
*   **Khối "Kết nối Tiêu dùng" (Danh bạ số ngách):** Chuyển đổi từ danh bạ hộ kinh doanh tĩnh thành danh bạ dịch vụ ngách thiết thực đã qua xác thực tại Hà Nội:
    1.  *Nha khoa:* Nha khoa Quốc tế Hà Đông.
    2.  *Giáo dục:* Trung tâm gia sư sư phạm.
    3.  *Làng nghề:* Gốm sứ Bát Tràng chính gốc.
    4.  *Cứu hộ:* Cứu hộ giao thông Hà Nội 24/7.
    5.  *Dạy nghề:* Dạy nghề nấu ăn & pha chế Hanoi Cook.
    6.  *Thẩm mỹ:* Viện thẩm mỹ An Beauty.
    7.  *Y học cổ truyền:* Đông y Lãn Ông Đường.
    8.  *Tín dụng:* Vay ưu đãi hộ kinh doanh HDBank Cầu Giấy.
*   **Khối "Việc làm tại Hà Nội" (Tuyển dụng nhanh KCN):** Gợi ý việc làm của Canon Việt Nam và Tập đoàn Cơ khí Hà Nội.

#### D. Lập trình các tiện ích tương tác dữ liệu (Interactive Journalism)
*   **Bảng giá thực phẩm WinMart có bộ lọc Quận huyện:** Tích hợp bộ lọc dropdown 4 khu vực (Cầu Giấy, Hoàn Kiếm, Hà Đông, Ba Vì). Khi thay đổi quận, giá thực phẩm WinMart (được tài trợ) và giá chợ truyền thống tự động cập nhật động kèm link out WinMart Affiliate.
*   **Lịch biểu diễn nghệ thuật & Phim rạp:** Hiển thị giờ diễn kịch Nhà hát Lớn, xiếc TW, múa rối rối nước Thăng Long và suất chiếu phim rạp CGV/Lotte thời gian thực nhằm thu phí hoa hồng đại lý bán vé.
*   **Khảo sát dư luận xã hội (Interactive Poll):** Thao tác bình chọn ý kiến về phố đi bộ tự động hiển thị biểu đồ phần trăm thanh động mượt mà.
*   **Tự tính lương tăng ca (Labor Calculator):** Tiện ích nhập lương giờ và số giờ làm để công nhân KCN tự tính thù lao thêm giờ theo Luật Lao động 2019.

#### E. Tích hợp luồng phản ánh Hotline Chatbot & Feed Dân sinh
*   Tích hợp chatbot Hotline Dân sinh 24/7 ở góc phải dưới màn hình.
*   **Cơ chế liên kết 2 chiều động:** Khi độc giả nhập nội dung phản ánh dân sinh kèm số điện thoại và nhấn gửi trong Chatbot, hệ thống lập tức cập nhật một dòng trạng thái mới lên khối **Nhật ký Phản ánh Dân sinh** ngay trên trang chủ ở trạng thái nhấp nháy đỏ *"Đang xác minh"*, tạo cảm giác tương tác thực tế sống động.

#### F. Bảng điều khiển Tòa soạn & SEO (Dev Panel)
*   Collapsible drawer nằm sát mép phải cho phép biên tập viên:
    *   Thay đổi bài viết ghim nổi bật tại khối Tiêu điểm chính.
    *   Tăng giảm tần suất bài viết xuất bản mỗi tháng để bật/tắt trạng thái INDEXED/NOINDEX của trang.

#### G. Đóng gói & Phát hành (Deploy)
*   **Đóng gói tài liệu:** Tổng hợp toàn bộ 17 sản phẩm & widget thương mại hóa chi tiết tại [Ke_hoach_kinh_doanh_tong_the_v2.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/Ke_Hoach_Kinh_Doanh/Ke_hoach_kinh_doanh_tong_the_v2.md).
*   **Đồng bộ hóa giao diện gốc:**
    - Lưu trữ bản mẫu giao diện sạch nguyên bản thành [demo_landing_page_hanoi_clean.html](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/demo_landing_page_hanoi_clean.html) để làm mẫu sạch dự phòng.
    - Điều chỉnh trình biên dịch [apply_ads_layout.py](file:///C:/Users/Admin/.gemini/antigravity/brain/33ccafad-2fa8-4696-acbe-bb1db8c432c1/apply_ads_layout.py) đọc dữ liệu từ tệp sạch dự phòng và xuất kết quả đồng thời ra tất cả các tệp: `demo_landing_page_hanoi_ads.html`, `index_ads.html`, [demo_landing_page_hanoi.html](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/demo_landing_page_hanoi.html) (tệp gốc), và [index.html](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/index.html) (tệp trang chủ gốc).
    - Deploy Cloud đồng bộ thành công lên máy chủ Vercel. Địa chỉ gốc của tên miền **[https://laodong-hanoi.vercel.app](https://laodong-hanoi.vercel.app)** từ nay sẽ hiển thị trực tiếp giao diện đầy đủ nhất (Ads + Tương tác + Chatbot).
*   **Thiết lập cơ chế bảo vệ dữ liệu dự án (Data Protection & Backup):**
    - Tạo tệp tin tự động sao lưu [run_backup.py](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/run_backup.py) trong thư mục gốc.
    - Script tự động sao chép toàn bộ các tệp tin cốt lõi (HTML mẫu sạch, CSDL bài viết JSON, Lịch sử phát triển, Nhật ký hoạt động, Kế hoạch kinh doanh V2 và Script trình biên dịch) sang thư mục chuyên biệt [Sao_Luu_Du_Phong](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/Sao_Luu_Du_Phong).
    - Chạy thử nghiệm thành công tạo bản sao lưu snapshot đầu tiên.
*   **Nhật ký hoạt động:** Cập nhật chi tiết tiến trình tại [kinh_doanh_va_quang_cao_chuyen_trang.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/kinh_doanh_va_quang_cao_chuyen_trang.md).

---

### 3. PHIÊN LÀM VIỆC NGÀY 31/05/2026: TÍCH HỢP WIDGET THỜI TIẾT THỜI GIAN THỰC (REAL-TIME WEATHER WIDGET)
*   **Mục tiêu chính:** Tích hợp tiện ích Thời tiết Hà Nội cập nhật thời gian thực từ nguồn Open-Meteo uy tín vào thanh đầu trang.
*   **Công việc kỹ thuật đã thực hiện:**
    *   **Giao diện Widget:** Thiết kế một hộp tiện ích nhỏ gọn phong cách glassmorphism nằm ngay trên cùng, song hành với Breadcrumbs và Date Bar hiển thị thứ ngày tiêu chuẩn Việt Nam.
    *   **Tích hợp API thời gian thực:** Kết nối với API miễn phí và uy tín của Open-Meteo (`api.open-meteo.com`) lấy dữ liệu nhiệt độ, độ ẩm và mã thời tiết của tọa độ địa lý Hà Nội để tự động chuyển đổi thành trạng thái trực quan kèm biểu tượng emoji tương ứng (Trời quang ☀️, Nhiều mây ⛅, Mưa rào 🌦️, Mưa phùn 🌧️...).
    *   **Đồng bộ & Tự động chạy:** Hàm `fetchHanoiWeather()` tự động kích hoạt trên sự kiện `DOMContentLoaded` của trang.
    *   **Deploy Cloud:** Cập nhật và phát hành trực tuyến thành công lên Vercel.
*   **Kết quả bàn giao:** Trang chủ **[https://laodong-hanoi.vercel.app](https://laodong-hanoi.vercel.app)** hiển thị chính xác Thời tiết Hà Nội cập nhật thời gian thực.

---

### 4. PHIÊN LÀM VIỆC NGÀY 01/06/2026: TRIỂN KHAI HUB & SPOKE TP.HCM & ĐÔNG NAM BỘ & QUY TRÌNH URL REWRITE
*   **Mục tiêu chính:** Triển khai hạ tầng dữ liệu và giao diện Hub & Spoke cho TP.HCM & Đông Nam Bộ; biên soạn và lưu trữ quy trình kỹ thuật URL Rewrite hệ thống.
*   **Công việc kỹ thuật đã thực hiện:**
    *   **Cào quét & Hợp nhất Dữ liệu:** Viết mã [scrape_tphcm_real.py](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/scrape_tphcm_real.py) cào quét sâu 64 bài viết thực tế phân bổ qua 8 chuyên mục chính của khu vực TP.HCM, Đồng Nai, Tây Ninh.
    *   **Giao diện Hub & Spoke:** Xây dựng tab bar tương tác phía Client-side trên trang [demo_landing_page_tphcm.html](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/demo_landing_page_tphcm.html) cho phép chuyển đổi nhanh nội dung hiển thị giữa Hub (Toàn khu vực) và các Spoke (TP.HCM, Đồng Nai, Tây Ninh), tích hợp cơ chế fallback bù đắp tin bài tự động chống vỡ khung giao diện.
    *   **Carousel Đọc nhiều nhất:** Thiết kế carousel 3 slide xoay vòng tự động (mỗi slide 5 bài viết) thay thế cho sidebar tĩnh cũ.
    *   **Tích hợp Thời tiết & Tọa độ:** Cập nhật widget thời tiết đo đạc thời gian thực từ tọa độ TP.HCM và tích hợp bảng thông tin tag cắt điện vùng Đông Nam Bộ.
    *   **Quy trình Kỹ thuật URL Rewrite:** Thiết kế giải pháp định tuyến ảo tại tầng Web Server (Nginx) giúp ánh xạ đường dẫn cực ngắn `laodong.vn/[spoke]` sang cấu trúc SEO Silo vật lý `laodong.vn/vung-mien/[hub]/[spoke]/` mà không thay đổi địa chỉ trên trình duyệt và không làm mất điểm SEO của tòa soạn.

#### 📋 Quy trình Triển khai Kỹ thuật URL Rewrite ở tầng hệ thống
1.  **Thiết lập Cấu trúc Vật lý (SEO Silo):** CMS lưu trữ bài viết và trang danh mục thực tế tại đường dẫn chuẩn phân cấp: `laodong.vn/vung-mien/[hub]/[spoke]/`.
2.  **Áp dụng Định tuyến ảo (Short URL):** Cung cấp link ngắn `laodong.vn/[spoke]` (ví dụ: `laodong.vn/dongnai`) trên giao diện chia sẻ.
3.  **Cấu hình Nginx Proxy Map (Định tuyến ngầm):**
    *   Sử dụng cấu hình `map $uri $regional_spoke_uri` ở ngoài server block của Nginx để lưu trữ danh sách ánh xạ các Spoke thành đường dẫn vật lý dài. Việc này giúp Nginx biên dịch danh sách thành một bảng băm (Hash table), tối ưu hóa tốc độ tra cứu đạt mức $O(1)$.
    *   Sử dụng lệnh `rewrite` nội bộ bên trong `location /` để chuyển hướng ngầm mà không đổi URL hiển thị trên thanh địa chỉ của trình duyệt.
4.  **Khai báo Canonical & Breadcrumb JSON-LD:**
    *   Tại mã nguồn trả về của trang Spoke ảo, thêm thẻ `<link rel="canonical" href="https://laodong.vn/vung-mien/[hub]/[spoke]/" />` để hướng dòng chảy SEO về cấu trúc vật lý chuẩn mực của Google.
    *   Nhúng Schema JSON-LD BreadcrumbList đầy đủ 4 lớp nhằm khai báo chuẩn xác mối quan hệ phân cấp địa giới hành chính.
5.  **Cấu hình Vercel (`vercel.json`):** Sử dụng khóa `"rewrites"` để ánh xạ thử nghiệm link ảo đến tệp giao diện động truyền tham số truy vấn (ví dụ: `/dongnai` -> `/demo_landing_page_tphcm.html?spoke=dongnai`).


