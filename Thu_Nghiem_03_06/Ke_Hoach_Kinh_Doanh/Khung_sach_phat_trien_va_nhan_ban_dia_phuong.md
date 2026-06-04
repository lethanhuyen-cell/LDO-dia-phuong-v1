# KHUNG SÁCH PHÁT TRIỂN VÀ NHÂN BẢN TRANG ĐỊA PHƯƠNG TOÀN QUỐC
## CÔNG THỨC CHUNG ĐỂ BẢN ĐỊA HÓA VÀ THƯƠNG MẠI HÓA (LOCAL SATELLITE BLUEPRINT)

Tài liệu này đóng vai trò là cẩm nang hướng dẫn chuẩn hóa (SOP) giúp tòa soạn nhanh chóng nhân bản mô hình chuyên trang vùng miền/địa phương ra 63 tỉnh thành trên cả nước, đảm bảo tính đồng bộ về hạ tầng công nghệ và chiến lược thương mại số.

---

## 1. CÔNG THỨC NỘI DUNG BẢN ĐỊA HÓA (LOCALIZATION FORMULA)

Để biến một trang tin tổng hợp thành chuyên trang địa phương thực thụ, bộ lọc dữ liệu phải tuân thủ công thức phân loại 4 lớp (Taxonomy Model):

```
┌──────────────────────────────────────────────────────────┐
│ LỚP 1: VÙNG MIỀN (Ví dụ: Đồng bằng sông Hồng, Đông Nam Bộ)│
└────────────────────────────┬─────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────┐
│ LỚP 2: TỈNH / THÀNH PHỐ (Ví dụ: Hải Phòng, Bình Dương)    │
└────────────────────────────┬─────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────┐
│ LỚP 3: QUẬN / HUYỆN CỤ THỂ (Dùng làm từ khóa lọc sâu)    │
└────────────────────────────┬─────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────┐
│ LỚP 4: CHUYÊN ĐỀ DÂN SINH (Thời sự, Công đoàn, Đô thị...)│
└──────────────────────────────────────────────────────────┘
```

### Thuật toán lọc bài viết địa phương tự động:
1.  **Dữ liệu đầu vào**: RSS/API toàn bộ bài viết mới của Báo Lao Động.
2.  **Bộ lọc từ khóa (Keyword Filter)**: Lọc tiêu đề chứa tên các địa danh hành chính trực thuộc tỉnh (tên Quận, Huyện, Phố, Đường, Công trình hạ tầng trọng điểm).
3.  **Loại bỏ nhiễu (Negative Filter)**: Tự động loại bỏ các bài viết chứa từ khóa vĩ mô, trung ương, quốc tế hoặc các bài tin tức giải trí không có tính địa bàn rõ rệt.

---

## 2. CÔNG THỨC THƯƠNG MẠI HÓA ĐẶC THÙ THEO NHÓM ĐỊA PHƯƠNG

Tùy thuộc vào đặc điểm kinh tế - xã hội của từng địa phương, cơ cấu doanh thu từ 5 dòng tiền sẽ được điều chỉnh trọng số (Weighting) cho phù hợp:

### NHÓM A: Tỉnh/Thành công nghiệp & dịch vụ (Ví dụ: Bình Dương, Đồng Nai, Quảng Ninh, Hải Phòng)
*   **Trọng tâm doanh thu**: Dòng tiền **Công nhân & KCN** (50%) + **Truyền thông Doanh nghiệp lớn** (30%).
*   **Chiến dịch mẫu**: Gói tuyển dụng lao động lớn cho KCN, quảng cáo nhà trọ an toàn, bảo hiểm tai nạn lao động và các sản phẩm FMCG phục vụ đời sống công nhân.

### NHÓM B: Tỉnh/Thành thế mạnh du lịch & dịch vụ (Ví dụ: Đà Nẵng, Khánh Hòa, Lâm Đồng, Kiên Giang)
*   **Trọng tâm doanh thu**: Dòng tiền **Quảng cáo địa bàn** (40%) + **Làng nghề & Ẩm thực, Homestay** (40%).
*   **Chiến dịch mẫu**: Cẩm nang du lịch nghỉ dưỡng cuối tuần, bản đồ ẩm thực đặc sản, gói tài trợ độc quyền từ các chuỗi khách sạn/resort địa phương.

### NHÓM C: Tỉnh/Thành đang phát triển (Ví dụ: Nghệ An, Thanh Hóa, Đắk Lắk, Cần Thơ)
*   **Trọng tâm doanh thu**: Dòng tiền **Truyền thông chính sách** (40%) + **Giáo dục & Y tế tư nhân** (30%).
*   **Chiến dịch mẫu**: Hướng dẫn thủ tục hành chính công, chuyển đổi số nông thôn mới, tuyển sinh trường tư thục, quảng bá nông sản đạt chuẩn OCOP địa phương.

---

## 3. QUY TRÌNH NHÂN BẢN 5 BƯỚC (5-STEP REPLICATION PIPELINE)

Khi muốn mở rộng sang một tỉnh mới (Ví dụ: Nghệ An), đội ngũ kỹ thuật và nội dung thực hiện theo đúng quy trình sau:

### Bước 1: Khởi tạo cơ sở dữ liệu địa phương
*   Cấu hình từ khóa lọc cho tỉnh mục tiêu (Ví dụ: Nghệ An: *Vinh, Cửa Lò, Diễn Châu, Quỳnh Lưu, Đô Lương...*).
*   Chạy script cào tự động để chọn ra danh sách ~100 bài viết đặc thù.

### Bước 2: Thiết kế bộ tài nguyên đồ họa địa phương (Local Visuals)
*   Sử dụng AI tạo ra 6-8 hình ảnh phong cảnh, văn hóa, đời sống xã hội tiêu biểu có độ nét cao đại diện cho địa phương đó để lắp vào các bài viết nổi bật.
*   Thay thế toàn bộ ảnh placeholder chất lượng thấp bằng kho ảnh này.

### Bước 3: Quy hoạch Bản quảng cáo giả lập (Ads Mockup)
*   Thay thế các nhãn hàng demo trong file mẫu bằng các thương hiệu nổi bật có thế mạnh hoặc chi nhánh lớn tại địa phương đó (Ví dụ: Nghệ An: Ngân hàng Bắc Á, Bia Sao Vàng; Bình Dương: Becamex IDC).
*   Đảm bảo tem nhãn "QC GIẢ LẬP" hiển thị chính xác.

### Bước 4: Biên dịch trang tĩnh (HTML Static Generation)
*   Chạy script Python tổng hợp dữ liệu để sinh ra file HTML tĩnh độc lập (Ví dụ: `demo_landing_page_nghean.html` và phiên bản Ads tương ứng).
*   Đẩy lên thư mục chứa và cấu hình định tuyến (Routing) trên Vercel/Web Server.

### Bước 5: Bàn giao tài liệu kinh doanh và tiếp cận khách hàng (Go-to-Market)
*   Bản địa hóa tài liệu kinh doanh theo đúng nhóm đặc thù (A, B hoặc C) của tỉnh đó.
*   Bàn giao cho văn phòng đại diện hoặc văn phòng thường trú của Báo Lao Động tại địa bàn để bắt đầu tiếp cận khách hàng trực tiếp.
