# 7. TÀI LIỆU CHUẨN HÓA QUY TRÌNH TRIỂN KHAI DỰ ÁN "LAO ĐỘNG – VÙNG MIỀN"

Bộ khung quy trình triển khai chi tiết này được thiết kế đặc thù để Nhóm nội dung số đa nền tảng có thể trực tiếp giám sát, giao việc cho các bộ phận liên quan (Công nghệ, Văn phòng thường trú, Kinh doanh) và kiểm soát rủi ro hệ thống.

---

### 1. Decision Log (Hồ sơ Quyết định & Giả định đầu vào)

Trước khi khởi động, dự án sẽ vận hành trên các giả định và quyết định cứng sau đây để tránh rủi ro "scaled content" (sản xuất nội dung hàng loạt kém chất lượng):

| Hạng mục | Trạng thái | Chi tiết quyết định / Giả định |
| :--- | :--- | :--- |
| **Phạm vi triển khai** | **Chốt cứng** | Không phủ toàn bản đồ ngay. Áp dụng chiến lược "density-first", đi theo mô hình 3 tầng (Tầng nền, Tầng tăng trưởng, Tầng dữ liệu). |
| **Địa bàn Pilot** | *Giả định* | Lựa chọn 6–12 tỉnh/thành có mật độ bài viết hiện hữu cao nhất và nhu cầu độc giả lớn để chạy thử nghiệm. |
| **Hệ thống CMS** | **Chốt cứng** | CMS tự phát triển (In-house) hoặc mã nguồn mở có toàn quyền can thiệp code (PHP/NodeJS/Go), cho phép tùy biến sâu giao diện soạn thảo và schemas. |
| **Cơ chế gắn tag** | **Chốt cứng** | Gắn tag hoàn toàn bằng tay: Phóng viên tự tìm kiếm và chọn tag từ danh sách có sẵn trên CMS, không sử dụng thuật toán tự động. |
| **Cấu trúc URL** | **Chốt cứng** | Bài viết giữ nguyên URL duy nhất, vĩnh viễn (Self-canonical). Không republish bài dưới URL mới. |
| **Phân quyền hiển thị** | **Chốt cứng** | Trưởng Văn phòng Thường trú (VPTT) được phân quyền chủ động chọn và duyệt hiển thị Top Stories của tỉnh/vùng mình quản lý. |
| **Ngưỡng mở Index** | **Chốt cứng** | Chỉ mở index cho các landing page tỉnh đạt tối thiểu **100 tin bài/tháng** để đảm bảo tính tươi mới và tránh rủi ro Doorway Pages. |
| **Ranh giới thương mại** | **Chốt cứng** | Inventory quảng cáo độc lập hoàn toàn với luồng tin chính. Bắt buộc có nhãn "Tài trợ" theo quy định pháp luật hiện hành. |

---

### 2. Lộ trình Triển khai Pilot 90 ngày (SOP Cốt lõi)

Quy trình này chia làm 4 giai đoạn, bám sát vòng đời phát triển từ dữ liệu, kỹ thuật đến thương mại hóa.

#### Giai đoạn 1: Thiết lập nền móng dữ liệu (Tuần 1–2)
*   **Audit bài viết**: Quét toàn bộ kho dữ liệu hiện tại để đánh giá mật độ bài viết theo địa phương.
*   **Chốt Taxonomy**: Ban hành từ điển thực thể địa danh (Canonical Place Dictionary) với các trường bắt buộc (place_id, slug, display_name, aliases).
*   **Chốt danh sách Pilot**: Quyết định 6-12 địa bàn (Tầng tăng trưởng) và thiết lập mô tả biên tập tối thiểu 120-250 từ cho từng landing.

#### Giai đoạn 2: Tích hợp Kỹ thuật & Tagging UI (Tuần 3–6)
*   **Xây dựng Tagging UI trên CMS**: Tích hợp các trường chọn 4 lớp tag (Headline place, In-text places, Affected areas, Responsible office) thân thiện và dễ tìm kiếm nhất cho phóng viên.
*   **Phát triển Template**: Dựng 2-3 landing page template tích hợp BreadcrumbList schema, đảm bảo tối ưu Core Web Vitals (CWV) trên mobile.
*   **UAT (User Acceptance Testing)**: Chạy thử nghiệm quy trình gắn tag thủ công, kiểm tra luồng phân phối tự động lên landing mockup.

#### Giai đoạn 3: Soft Launch & Tối ưu (Tuần 7–10)
*   **Go-live giới hạn**: Mở index cho các landing Tầng nền (Khu vực) và Tầng tăng trưởng (Pilot) đạt tối thiểu **100 tin bài/tháng** và đạt đủ tiêu chuẩn biên tập. Các trang dưới 100 bài bị khóa bằng thẻ `noindex, follow`.
*   **Kiểm soát chất lượng (Editorial QA)**: Trưởng VP thường trú vận hành cơ chế chọn Top Stories thủ công hằng ngày cho địa bàn của mình.
*   **Thương mại hóa thử nghiệm**: Khởi chạy 2-3 gói tài trợ an toàn (Brand-safe local context) tại các vị trí đã quy hoạch, đo lường Viewability và rủi ro ad-clutter.

#### Giai đoạn 4: Đánh giá & Phán quyết (Tuần 11–12)
*   **Review Dashboard**: Đối chiếu KPI (Organic sessions, Recirculation, Tag precision).
*   **Go/No-go Memo**: Ban lãnh đạo quyết định duy trì, mở rộng thêm tỉnh/thành mới, hoặc cắt bỏ các trang không đạt chuẩn.

---

### 3. Ma trận Phân quyền Trách nhiệm (RACI)

Mọi đầu việc phải được xác định rõ người chịu trách nhiệm, tránh dẫm chân lên nhau.

| Hạng mục Công việc | Lãnh đạo BBT | Nhóm ND Số (Product/SEO) | VP Thường trú | CNTT (Dev/IT) | Kinh doanh (Sales) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Phê duyệt danh sách Landing Pilot** | **A** (Accountable) | **R** (Responsible) | **C** (Consulted) | I (Informed) | I |
| **Xây dựng Taxonomy & Tagging Rules** | I | **R/A** | C | **C** | I |
| **Phát triển Landing Template & Schema** | I | **C** | I | **R/A** | I |
| **Chọn bài Top Stories trên Landing** | I | C | **R/A** | I | I |
| **Bán gói Sponsorship theo địa bàn** | I | C | I | I | **R/A** |
| **Phê duyệt duyệt ngoại lệ (Vùng cấm)** | **R/A** | C | C | I | C |

*(R: Chịu trách nhiệm làm; A: Có quyền quyết định cuối cùng; C: Được tham vấn; I: Được thông báo)*

---

### 4. Phản biện & Quản trị Điểm mù Hệ thống

Để hệ thống không trượt khỏi quỹ đạo chất lượng, cần thiết lập ngay các chốt chặn sau:

*   **Lỗ hổng "Over-tagging" của phóng viên**: Phóng viên có xu hướng gắn mọi tag địa danh xuất hiện trong bài để tăng view. **Khắc phục**: Hệ thống CMS chỉ tự động lấy địa danh ở đầu câu (Headline place) làm phân loại chính. Mọi can thiệp bằng tay vào *Affected areas* phải được cảnh báo nội bộ nếu tỷ lệ sai lệch (bounce rate trên landing) tăng vọt.
*   **Sức ép từ Kinh doanh mở "Trang mỏng"**: Khi khách hàng muốn tài trợ ở một tỉnh chưa đủ lượng tin bài (Tầng dữ liệu). **Khắc phục**: Nguyên tắc chốt cứng - Tuyệt đối không mở index landing vì lý do Sales. Nếu có cam kết, khách hàng chỉ được mua Inventory ở Tầng nền (Khu vực lớn).
*   **Xung đột Tag cập nhật muộn (SEO Lag)**: Nếu khâu gắn tag phụ thuộc vào độ trễ của kỹ thuật hậu kiểm, landing địa phương sẽ toàn tin cũ. **Khắc phục**: Shift-left SEO. Buộc module Tagging Pipeline phải đề xuất tag tự động ngay trên màn hình soạn thảo của phóng viên trước khi bấm gửi duyệt.
