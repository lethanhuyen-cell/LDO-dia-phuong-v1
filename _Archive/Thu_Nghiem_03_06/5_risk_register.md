# 5. RISK REGISTER (BẢNG QUẢN TRỊ RỦI RO DỰ ÁN VÙNG MIỀN)

Tài liệu này tổng hợp toàn bộ các rủi ro kỹ thuật, pháp lý, vận hành và biên tập có thể phát sinh trong quá trình triển khai dự án **Lao Động – vùng miền**, cùng các biện pháp giảm thiểu tương ứng nhằm bảo vệ an toàn thương hiệu.

---

## 1. MA TRẬN PHÂN TÍCH RỦI RO (RISK MATRIX)

*   **Mức độ tác động (Impact - I)**: 1 (Thấp) đến 5 (Rất nghiêm trọng)
*   **Khả năng xảy ra (Likelihood - L)**: 1 (Hiếm khi) đến 5 (Rất dễ xảy ra)
*   **Điểm rủi ro (Score)** = I × L (Từ 1 đến 25)

| Mã | Tên Rủi ro | L | I | Điểm | Người chịu trách nhiệm | Biện pháp giảm thiểu & Hành động khắc phục |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **R-SEO-01** | **Án phạt Doorway Pages từ Google**<br>(Tạo hàng loạt trang tỉnh giống nhau chỉ khác tên địa danh). | 4 | 5 | **20** | IT Lead / SEO Specialist | - Khóa index mặc định (`noindex, follow`) đối với tất cả các tỉnh có mật độ bài thấp.<br>- Bắt buộc có mô tả biên tập viết tay khác biệt cho mỗi landing page tỉnh được index. |
| **R-SEO-02** | **Site Reputation Abuse**<br>(Bị Google phạt do đăng tải nội dung quảng cáo mỏng hoặc spam link trên domain uy tín). | 3 | 5 | **15** | Ban Biên tập / Thư ký Tòa soạn | - Quy định vùng cấm thương mại.<br>- Mọi bài viết PR phải qua quy trình kiểm duyệt chất lượng biên tập như tin thường.<br>- Sử dụng thuộc tính `rel="sponsored"` hoặc `rel="nofollow"` cho các link quảng cáo ngoài. |
| **R-NEWS-01**| **Mất hiển thị trên Google News / Top Stories**<br>(Do vi phạm các nguyên tắc về ngày giờ hoặc trùng lặp URL). | 3 | 4 | **12** | IT Lead | - Đảm bảo cấu trúc datePublished và dateModified chính xác.<br>- Giữ URL bài viết cố định, không tạo bản sao bài viết để đăng lại dưới URL mới. |
| **R-LEGAL-01**| **Vi phạm Luật Báo chí 2016/2025**<br>(Nhầm lẫn chuyên trang pháp lý với chuyên mục tổ chức nội dung nội bộ). | 2 | 5 | **10** | Thư ký Tòa soạn / Pháp chế | - Thống nhất gọi sản phẩm là "Chuyên mục Vùng miền" hoặc "Trang tin địa phương".<br>- Tránh thiết lập giao diện giống như một trang báo độc lập (subdomain riêng, ban biên tập riêng) nếu chưa đăng ký giấy phép chuyên trang. |
| **R-LEGAL-02**| **Vi phạm Luật Quảng cáo**<br>(Quảng cáo không có nhãn nhận diện rõ ràng, quảng cáo sai sự thật). | 3 | 4 | **12** | Trưởng Phòng Kinh doanh | - Bắt buộc hiển thị nhãn "Thông tin doanh nghiệp" rõ ràng trên mọi tin bài tài trợ.<br>- Thư ký tòa soạn rà soát nội dung bài PR trước khi xuất bản để chặn quảng cáo lừa đảo. |
| **R-PRIV-01** | **Vi phạm Luật Bảo vệ dữ liệu cá nhân 2025**<br>(Tracking vị trí địa lý của người dùng không xin phép). | 3 | 4 | **12** | IT Lead | - Khi áp dụng Geo-targeting để gợi ý tin tức, phải có popup thông báo thu thập vị trí và nút cho phép người dùng từ chối (Opt-out). |
| **R-EDIT-01** | **Bào mòn chất lượng biên tập (Editorial Capture)**<br>(Sản xuất bài viết theo đơn đặt hàng thương mại núp bóng tin biên tập). | 2 | 5 | **10** | Ban Biên tập | - Thiết lập ranh giới cứng: Phòng kinh doanh bán inventory quảng cáo, không bán nội dung bài viết biên tập.<br>- VPTT có quyền từ chối đưa bài PR của khách hàng vào khối Tiêu điểm (Top Stories). |
| **R-OP-01**   | **Quá tải vận hành thường trú**<br>(Trưởng văn phòng bận tác nghiệp, không cập nhật landing page). | 4 | 3 | **12** | Trưởng các VPTT | - Tự động hóa 80% luồng tin hiển thị trên landing page bằng thuật toán tag.<br>- Thiết lập ca trực cập nhật khối Tiêu điểm cố định hằng tuần. |

---

## 2. BIỆN PHÁP CHỦ ĐỘNG PHÒNG NGỪA THEO PHÂN NHÓM NHÂN SỰ

Để giảm thiểu các rủi ro trên một cách triệt để, từng bộ phận trong tòa soạn phải thực thi nghiêm ngặt các quy định phòng ngừa:

### Đội ngũ Kỹ thuật & IT
*   **Hành động phòng ngừa**: Lập trình công cụ tự động quét lỗi Schema và thẻ canonical hằng ngày. Thiết lập cơ chế tự động khóa index (noindex) cho bất kỳ landing page nào có Core Web Vitals rơi vào vùng Đỏ (LCP > 4s) hoặc có số bài viết mới dưới ngưỡng 10 bài/tháng.

### Ban Biên tập & Thư ký Tòa soạn
*   **Hành động phòng ngừa**: Tổ chức hội đồng nghiệm thu (UAT) chất lượng landing page trước khi cho phép IT mở index. Xây dựng bộ quy chế xử phạt nội bộ đối với các phóng viên cố tình gắn sai tag địa lý để chạy KPI sản lượng.

### Văn phòng Thường trú (VPTT)
*   **Hành động phòng ngừa**: Trưởng văn phòng thường trực tiếp ký duyệt danh sách bài viết tiêu điểm (Top Stories) hằng ngày trên landing page khu vực của mình. Chịu trách nhiệm trực tiếp trước Tổng biên tập về tính xác thực địa bàn của luồng tin hiển thị.

### Bộ phận Kinh doanh & Sales
*   **Hành động phòng ngừa**: Chỉ bán các gói sản phẩm quảng cáo dựa trên danh sách inventory đã được IT phê duyệt kỹ thuật. Không tự ý thương thảo thêm các điều khoản cam kết hiển thị ngoài luồng quy định (ví dụ: cam kết giữ bài PR trên mục Tiêu điểm 3 ngày liên tục).
