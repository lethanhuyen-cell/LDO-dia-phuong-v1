# Quy Trình Chuẩn: Thu Thập & Tích Hợp Tin Bài Cho Hệ Thống Hub & Spoke Địa Phương

Tài liệu này chuẩn hóa quy trình 5 bước để tự động cào quét dữ liệu thật, rà soát phân loại địa bàn hành chính sâu (Deep Geotagging), áp dụng cơ chế bù đắp dữ liệu (Fallback) và cập nhật giao diện tự động cho các chuyên trang vùng miền.

---

## 🛠️ Quy Trình 5 Bước Triển Khai

### 1. Thiết lập Cấu hình Địa phương & Từ khóa Phân cấp
Mỗi vùng thường trú (Hub) được cấu trúc gồm nhiều tỉnh/thành thành viên (Spoke). Ta cần định nghĩa cấu trúc từ khóa cho từng Spoke:
*   **Keywords:** Danh sách các từ khóa địa danh cấp Tỉnh, Quận/Huyện, Thị xã, các địa danh du lịch, di tích lịch sử nổi bật.
*   **Trình tự khớp:** Luôn kiểm tra từ Spoke nhỏ/ngách trước, sau đó mới khớp đến Spoke trung tâm để đảm bảo phân loại đúng.

### 2. Thu thập Tin bài Đa tầng (Multi-tier Scraping)
Để khắc phục tình trạng thiếu tin bài cục bộ do tần suất cập nhật không đều giữa các tỉnh thành:
*   **Tầng 1 (Scan Chỉ mục):** Quét qua index trang của 8 chuyên mục chính (`Thời sự`, `Xã hội`, `Kinh tế`, `Giáo dục`, `Bất động sản`, `Công đoàn`, `Văn hóa - Giải trí`, `Thể thao`) ngược dòng thời gian (quét từ 30 đến 50 trang).
*   **Tầng 2 (Bypass Cookie Gate):** Sử dụng cơ chế khởi tạo session JavaScript của Báo Lao Động để nạp Cookie `D1N` tự động vào CookieJar trước khi thực hiện request chi tiết.

### 3. Phân loại Địa lý Sâu (Deep Geotagging & Classification)
Không chỉ kiểm tra tiêu đề hay URL, hệ thống phải truy cập trang chi tiết bài viết và kiểm tra toàn bộ nội dung HTML (Body text) để tìm từ khóa đặc trưng:
*   Nếu bài viết khớp từ khóa của Spoke nào (ví dụ: `Tây Ninh`), gán cờ `is_tayninh = true`.
*   Nếu không khớp bất kỳ Spoke nào, bài viết được định danh là **Tin Chung (Hub Article)**. Tin này sẽ được gán đồng thời `is_tphcm = true`, `is_dongnai = true`, `is_tayninh = true` để sẵn sàng làm dữ liệu bù đắp (Fallback) khi hiển thị.

### 4. Cơ chế Bù đắp Dữ liệu Tự động (Client-side Fallback & Merge)
Tại tầng Frontend, khi người dùng lọc tin theo Spoke:
*   Lấy toàn bộ tin bài thuộc Spoke đó: `pool = articles.filter(a => a.is_[spoke])`.
*   Nếu số lượng tin bài trong chuyên mục của Spoke không đạt tối thiểu (ví dụ: 5 bài viết):
    *   Hệ thống tự động thực hiện phép gộp `concat` với danh sách tin thuộc chuyên mục tương ứng của Hub.
    *   Sử dụng hàm loại bỏ trùng lặp ID (`!pool.some(existing => existing.id === hubArt.id)`) để đảm bảo không bị trùng tin trên giao diện.
    *   Cắt (`slice`) lấy đúng số lượng bài viết quy định để giữ nguyên cấu trúc lưới của template.

### 5. Biên dịch & Xuất Giao diện Tự động (Build Compiler)
*   Chạy script Python (ví dụ: `apply_tphcm_layout.py`) để đọc tệp JSON tổng hợp dữ liệu thật (`tphcm_dongnambo_consolidated.json`) và nhúng trực tiếp chuỗi JSON vào trang HTML.
*   Trang HTML sử dụng JavaScript thuần để render danh sách tin bài theo Tab Spoke được chọn thời gian thực, đảm bảo tốc độ phản hồi < 100ms.

---

## 📝 Ví dụ Cấu hình Python cho Địa phương mới (Mẫu)
```python
# Cấu hình từ khóa vùng ĐBSCL
REGION_CFG = {
    "cantho": {
        "tag": "Cần Thơ",
        "keywords": ["cần thơ", "ninh kiều", "cái răng", "bình thủy", "phong điền", "ô môn", "thốt nốt"],
    },
    "longan": {
        "tag": "Long An",
        "keywords": ["long an", "tân an", "bến lức", "đức hòa", "cần giuộc", "cần đước"],
    }
}
```
*Áp dụng quy trình trên giúp tự động hóa 100% khâu xây dựng nội dung sạch, đồng bộ hóa trải nghiệm cho tất cả các chuyên trang địa phương tiếp theo.*
