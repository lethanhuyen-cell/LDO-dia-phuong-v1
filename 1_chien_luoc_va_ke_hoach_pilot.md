# 1. CHIẾN LƯỢC PHÂN PHỐI NỘI DUNG VÀ KẾ HOẠCH PILOT 90 NGÀY

Dự án **Lao Động – vùng miền** được xây dựng nhằm mục đích tối ưu hóa tài nguyên nội dung địa phương sẵn có của tòa soạn mà không tăng tải sản xuất cơ bản, đồng thời thiết lập các landing page có tính cấu trúc cao nhằm phục vụ độc giả địa bàn và tạo dòng doanh thu mới.

---

## 1. PHÂN TÍCH ĐA CHIỀU (MÔ HÌNH 3 TẦNG × 5 GÓC NHÌN)

Để đảm bảo dự án thực thi hiệu quả và không trượt thành một dự án "SEO spam/doorway", tòa soạn sẽ áp dụng mô hình phân tầng địa lý:

*   **Tầng nền (Khu vực/VPTT)**: Mở mặc định, đại diện cho 6 Văn phòng thường trú (VPTT).
*   **Tầng tăng trưởng (Tỉnh/Thành pilot)**: Chỉ mở index khi có đủ mật độ bài viết (tối thiểu 15 bài/tháng) và có mô tả biên tập độc nhất.
*   **Tầng dữ liệu (Các tỉnh/thành còn lại)**: Gắn tag lưu trữ nội bộ, áp dụng `noindex` công khai cho đến khi đạt đủ độ dày dữ liệu.

### Bảng phân tích đa chiều 5 góc nhìn vận hành

| Tầng / Góc nhìn | Ban Lãnh đạo | Bộ phận Kinh doanh | Văn phòng Thường trú | Phóng viên Địa phương | IT & Kỹ thuật |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tầng nền** *(Khu vực)* | **KPI**: Tăng footprint thương hiệu & quản lý hiệu quả hoạt động vùng miền.<br>**Rủi ro**: Nội dung quá rộng, loãng bản sắc từng tỉnh. | **KPI**: Bán các gói thương mại vùng miền lớn (sponsorship lớn/SOV).<br>**Hạn chế**: Khó bán cho doanh nghiệp vừa và nhỏ chỉ có nhu cầu địa bàn tỉnh. | **KPI**: Chủ trì quản lý chất lượng chung toàn cụm.<br>**Ma sát**: Phân bổ tài nguyên curation giữa các tỉnh trong khu vực. | **Lợi ích**: Bài viết được phân phối diện rộng hơn.<br>**Thao tác**: Gắn tag VPTT mặc định theo cấu trúc tổ chức. | **Hệ thống**: Thiết lập template chung cho 6 khu vực.<br>**SEO**: Khai báo Breadcrumb và phân cấp logic nhất quán. |
| **Tầng tăng trưởng** *(Tỉnh pilot)* | **KPI**: Tăng trưởng traffic tự nhiên & chuyển đổi số địa phương.<br>**Ngưỡng**: Chỉ mở khi duyệt đủ chất lượng biên tập. | **KPI**: Khai thác gói tài trợ địa phương, quảng cáo du lịch, tuyển dụng, BĐS.<br>**Ràng buộc**: Tuyệt đối tách bạch nội dung tài trợ và biên tập. | **KPI**: Trực tiếp chịu trách nhiệm curate nội dung tiêu điểm (Top Stories) hằng ngày.<br>**Thao tác**: Duyệt bài thủ công lên vị trí Hero. | **Lợi ích**: Tăng uy tín cá nhân gắn với địa bàn tác nghiệp.<br>**Thao tác**: Gắn đủ 4 lớp tag cho từng bài viết. | **Hệ thống**: Tự động hóa việc gom feed theo tag. Cấp quyền Override UI cho Trưởng VPTT.<br>**SEO**: Bật index, quản lý canonical sạch. |
| **Tầng dữ liệu** *(Tỉnh còn lại)* | **KPI**: Tích lũy dữ liệu, theo dõi tín hiệu nhu cầu thị trường.<br>**Ràng buộc**: Khóa index để tránh án phạt doorway page. | **KPI**: Không thương mại hóa độc lập.<br>**Hành động**: Gom chung vào gói bán hàng vùng miền lớn. | **KPI**: Theo dõi chất lượng bài viết của tỉnh để chuẩn bị kế hoạch nâng cấp lên tầng 2. | **Lợi ích**: Bài viết được gom tự động, lưu trữ khoa học.<br>**Thao tác**: Gắn tag đầy đủ theo đúng thực tế. | **Hệ thống**: Áp dụng thẻ `noindex, follow` tự động cho toàn bộ landing page ở tầng này.<br>**SEO**: Đảm bảo crawler vẫn quét được liên kết. |

---

## 2. BẢNG PHÂN VAI TRÁCH NHIỆM RACI

Bảng phân định trách nhiệm cho các nhân sự chủ chốt trong dự án:

*   **R** (Responsible): Người thực hiện công việc.
*   **A** (Accountable): Người chịu trách nhiệm cuối cùng (duy nhất 1 vai trò).
*   **C** (Consulted): Người được tham vấn ý kiến.
*   **I** (Informed): Người nhận thông tin sau khi hoàn thành.

| Giai đoạn & Nhiệm vụ chính | Ban Lãnh đạo | Trưởng Ban Sản phẩm | Thư ký Tòa soạn / Pháp chế | Bộ phận IT | Trưởng VPTT | Đội ngũ Phóng viên | Bộ phận Kinh doanh |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Phê duyệt Taxonomy & Từ điển địa danh** | **A** | **R** | **C** | **I** | **C** | **I** | **I** |
| **2. Triển khai Tagging Pipeline & CMS Override** | **I** | **C** | **I** | **R** / **A** | **C** | **I** | **I** |
| **3. Biên soạn nội dung mô tả Landing Page** | **I** | **A** | **C** | **I** | **R** | **R** | **I** |
| **4. Duyệt mở index/noindex landing tỉnh** | **A** | **R** | **C** | **R** | **I** | **I** | **I** |
| **5. Cập nhật Tiêu điểm (Top Stories) hằng ngày** | **I** | **I** | **A** | **I** | **R** | **I** | **I** |
| **6. Gắn tag 4 lớp khi xuất bản bài viết** | **I** | **I** | **A** | **I** | **C** | **R** | **I** |
| **7. Thiết kế & Đóng gói Gói thương mại** | **A** | **C** | **C** | **I** | **I** | **I** | **R** |
| **8. Xử lý sửa bài / Đính chính thông tin** | **I** | **I** | **A** / **R** | **I** | **R** | **R** | **I** |

---

## 3. BACKLOG NHIỆM VỤ ƯU TIÊN (MUST / SHOULD / COULD)

### Must-Have (Bắt buộc phải làm ngay trong 30 ngày đầu)
- [ ] Thiết lập Từ điển thực thể địa danh chuẩn (Canonical Place Dictionary) để thống nhất định danh.
- [ ] Nâng cấp CMS hỗ trợ 4 lớp tag địa phương và tạo giao diện Override UI cho Biên tập viên.
- [ ] Áp dụng quy tắc Canonical URL duy nhất cho bài viết, cấm việc nhân bản URL bài viết dưới các danh mục khác nhau.
- [ ] Tự động hóa cơ chế `noindex` đối với các landing page tỉnh/thành chưa đạt chuẩn chất lượng.
- [ ] Soạn thảo quy chế phân tách rõ ràng giữa nội dung biên tập và nội dung quảng cáo/tài trợ, chuẩn hóa nhãn gắn (Labeling).

### Should-Have (Cần làm trong 60 ngày tiếp theo)
- [ ] Dựng Dashboard theo dõi hiệu quả theo thời gian thực (Organic traffic, Tỷ lệ lỗi index, Tốc độ Core Web Vitals).
- [ ] Tích hợp News Sitemap tự động cập nhật bài viết mới trong vòng 48 giờ.
- [ ] Tổ chức các buổi đào tạo quy chuẩn gắn tag cho 100% phóng viên và biên tập viên thường trú.
- [ ] Đóng gói tài liệu Media Kit chuẩn, loại bỏ các cam kết thao túng thứ hạng Google.

### Could-Have (Xem xét triển khai sau giai đoạn pilot)
- [ ] Thiết lập công cụ gợi ý nội dung tự động dựa trên địa lý người dùng (Geo-targeting recommendation).
- [ ] Triển khai bản tin email (Local Newsletter) hoặc thông báo đẩy (Push notification) phân cấp theo vùng.

---

## 4. CHI TIẾT LỘ TRÌNH PILOT 12 TUẦN (90 NGÀY)

### Chi tiết các mốc bàn giao và tiêu chí nghiệm thu (UAT)

#### Tuần 1 - 2: Audit dữ liệu và Thống nhất Taxonomy
*   **Hành động**: Audit kho bài viết 12 tháng gần nhất để đo lường mật độ bài viết theo từng tỉnh. Thống nhất danh sách địa danh chuẩn.
*   **Kết quả bàn giao**: Từ điển địa danh Canonical Place Dictionary v1.0. Danh sách 6 tỉnh pilot đã chốt (Hà Nội, TP.HCM, Nghệ An, Quảng Ninh, Đà Nẵng, Cần Thơ).
*   **Tiêu chí UAT**: 100% biến thể tên địa bàn (Ví dụ: "TP HCM", "Sài Gòn", "Thành phố Hồ Chí Minh") được map về duy nhất một ID thực thể.

#### Tuần 3 - 4: Nâng cấp CMS và Dựng Template
*   **Hành động**: Tích hợp 4 lớp tag vào giao diện soạn thảo. Lập trình 2 template landing page (Template Vùng và Template Tỉnh).
*   **Kết quả bàn giao**: Hệ thống CMS v2.0 (giao diện tag mới). Bản demo tĩnh của landing page.
*   **Tiêu chí UAT**: 
    1. Giao diện CMS không cho phép xuất bản bài viết nếu chưa chọn trường `Responsible Office`.
    2. URL của bài viết hiển thị đồng nhất ở dạng self-canonical.

#### Tuần 5 - 6: Cài đặt UAT nội bộ, Đào tạo & Kiểm duyệt Pháp lý
*   **Hành động**: Chạy thử nghiệm gắn tag tự động trên môi trường staging. Đào tạo nghiệp vụ cho phóng viên và VPTT. Rà soát pháp lý với Luật Báo chí mới.
*   **Kết quả bàn giao**: Tài liệu SOP hướng dẫn nhanh (1 trang cheat sheet). Báo cáo kiểm định pháp lý của Thư ký tòa soạn.
*   **Tiêu chí UAT**: 95% nhân sự VPTT vượt qua bài kiểm tra gắn tag thử nghiệm trên 10 bài viết mẫu.

#### Tuần 7 - 8: Launch mềm (Soft Launch)
*   **Hành động**: Mở public 6 landing page tỉnh pilot và 6 landing page vùng/VPTT. Giữ noindex cho 57 tỉnh còn lại.
*   **Kết quả bàn giao**: Hệ thống landing page chạy chính thức trên domain chính. XML News Sitemap riêng cho vùng miền hoạt động.
*   **Tiêu chí UAT**: 
    1. Công cụ Rich Results Test trả về kết quả 100% hợp lệ cho schema `NewsArticle` và `BreadcrumbList`.
    2. Điểm Core Web Vitals trên thiết bị di động của các landing page đạt > 80 điểm.

#### Tuần 9 - 10: Vận hành Kinh doanh và Tối ưu hóa
*   **Hành động**: VPTT bắt đầu cập nhật tiêu điểm hằng ngày. Phòng kinh doanh chào bán thử nghiệm gói sponsorship trên 6 địa bàn pilot.
*   **Kết quả bàn giao**: Hợp đồng sponsorship thử nghiệm. Dashboard theo dõi hiệu năng vùng miền đi vào hoạt động.
*   **Tiêu chí UAT**: Không có phản hồi tiêu cực nào từ độc giả về mật độ quảng cáo. Các quảng cáo xuất hiện đúng vị trí quy định và có nhãn rõ ràng.

#### Tuần 11 - 12: Đánh giá và Quyết định Scale-up
*   **Hành động**: Tổng hợp dữ liệu từ Dashboard. Rà soát rủi ro pháp lý thực tế. Lập tờ trình Tổng biên tập.
*   **Kết quả bàn giao**: Báo cáo tổng kết Pilot 90 ngày (Go/No-Go Memo).
*   **Tiêu chí UAT**: Đạt hoặc vượt tối thiểu 80% các chỉ số đo lường hiệu năng đề ra trong kế hoạch.
