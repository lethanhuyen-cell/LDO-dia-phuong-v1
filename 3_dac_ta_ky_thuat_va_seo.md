# 3. ĐẶC TẢ KỸ THUẬT VÀ PHƯƠNG ÁN TỐI ƯU SEO

Tài liệu này cung cấp các hướng dẫn kỹ thuật chi tiết dành cho đội ngũ phát triển IT và chuyên gia SEO của Báo Lao Động để triển khai dự án **Lao Động – vùng miền**.

---

## 1. CẤU TRÚC ĐƯỜNG DẪN (URL CONVENTIONS) VÀ CANONICAL

### Quy ước đặt tên URL (URL Naming Rules)
Toàn bộ hệ thống landing page sử dụng chung một cấu trúc thư mục (namespace) trên domain chính để giữ sức mạnh liên kết:

*   **Landing Page Vùng miền**: `https://laodong.vn/vung-mien/[slug-vung]/`
    *   *Ví dụ*: `https://laodong.vn/vung-mien/bac-trung-bo/`
*   **Landing Page Tỉnh/Thành**: `https://laodong.vn/vung-mien/[slug-tinh]/`
    *   *Ví dụ*: `https://laodong.vn/vung-mien/nghe-an/`
    *   *Lưu ý*: Không lồng ghép dạng `/bac-trung-bo/nghe-an/` để tránh URL quá dài và vỡ cấu trúc khi thay đổi phân chia địa giới hành chính.
*   **URL Bài viết (Article URL)**: Giữ nguyên cấu trúc URL mặc định của Báo Lao Động.
    *   *Quy tắc cứng*: Một bài viết chỉ có một URL duy nhất và cố định suốt vòng đời. Không tạo thêm URL phụ khi bài viết hiển thị trên các landing page vùng miền khác nhau.

### Quy tắc Canonicalization (Rel="canonical")
Để tránh lỗi nội dung trùng lặp (Duplicate Content):

*   **Trên trang bài viết**: Thẻ `<link rel="canonical" href="[URL bài viết gốc]" />` tự trỏ về chính nó (Self-canonical).
*   **Trên các trang Landing Page**: Thẻ canonical trỏ về URL chuẩn của landing page đó.
*   **Tham số lọc / Phân trang**: Nếu có URL dạng `https://laodong.vn/vung-mien/nghe-an/?page=2` hoặc `?filter=cong-doan`, thẻ canonical bắt buộc phải trỏ về URL gốc: `https://laodong.vn/vung-mien/nghe-an/`.

---

## 2. ĐẶC TẢ CẤU TRÚC DỮ LIỆU (STRUCTURED DATA SCHEMAS)

CMS phải tự động nhúng các đoạn mã JSON-LD chuẩn dưới đây vào mã nguồn HTML trước khi xuất bản.

### A. Schema NewsArticle cho trang bài viết

```json
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://laodong.vn/cong-doan/tin-tuc-cong-doan-nghe-an-123456.ldo"
  },
  "headline": "Tiêu đề bài viết về công đoàn Nghệ An",
  "image": [
    "https://laodong.vn/images/size-16x9/anh-dai-dien-1200px.jpg"
  ],
  "datePublished": "2026-05-29T08:00:00+07:00",
  "dateModified": "2026-05-29T10:30:00+07:00",
  "author": {
    "@type": "Person",
    "name": "Nguyễn Văn A",
    "url": "https://laodong.vn/tac-gia/nguyen-van-a.ldo"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Báo Lao Động",
    "logo": {
      "@type": "ImageObject",
      "url": "https://laodong.vn/static/images/logo.png"
    }
  },
  "description": "Mô tả tóm tắt nội dung bài viết tin tức địa phương..."
}
```

### B. Schema BreadcrumbList cho trang Landing Page Tỉnh

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Trang chủ",
      "item": "https://laodong.vn/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Vùng miền",
      "item": "https://laodong.vn/vung-mien/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Nghệ An",
      "item": "https://laodong.vn/vung-mien/nghe-an/"
    }
  ]
}
```

---

## 3. KIẾN TRÚC HỆ THỐNG GỢI Ý (TECHNICAL ARCHITECTURE)

Hệ thống quản lý tin vùng miền được triển khai theo mô hình phân tách giữa nhập liệu và hiển thị:

```
[Phóng viên/BTV] ──► [CMS Editor UI (Tagging v4)] ──► [Taxonomy Service (Place DB)]
                                                              │
                                                              ▼
[Google Crawler] ◄── [Sitemap & HTML Generator] ◄── [Search/Index Layer (Elasticsearch)]
```

### Các thành phần cốt lõi:
1.  **Taxonomy Service**: Cơ sở dữ liệu lưu trữ cấu trúc cây địa danh (Vùng -> Tỉnh -> Huyện) và ánh xạ từ khóa đồng nghĩa (Aliases).
2.  **Tagging Pipeline**: Bộ lọc tự động quét nội dung bài viết và gợi ý tag địa lý (Confidence Score > 80%).
3.  **Override UI**: Giao diện trên CMS cho phép phóng viên hoặc thư ký tòa soạn gỡ bỏ tag sai hoặc thêm tag `Affected Areas` thủ công.
4.  **Sitemap Generator**: Tự động sinh file `sitemap-news.xml` chứa danh sách bài viết vùng miền xuất bản trong 48 giờ qua, phục vụ riêng cho Google News crawler.

---

## 4. THIẾT KẾ DASHBOARD GIÁM SÁT CHI TIẾT (KPI DASHBOARD)

Bộ chỉ số đo lường hiệu năng dự án bao gồm 5 nhóm chính:

| Nhóm KPI | Chỉ số thành phần | Tần suất | Mục tiêu kỹ thuật & Vận hành |
| :--- | :--- | :--- | :--- |
| **1. Quality (Chất lượng)** | - Độ chính xác của tag tự động gợi ý.<br>- % bài viết gắn đủ 4 lớp tag.<br>- Tỷ lệ landing page đạt chuẩn nội dung tối thiểu. | Hằng tuần | Đảm bảo hệ thống phân loại chính xác, giảm thiểu công sức chỉnh sửa thủ công. |
| **2. Impact (Hiệu năng)** | - Organic Sessions vào hệ thống landing page.<br>- Số lượt click từ Google News và Discover.<br>- Pages/Session và tỷ lệ click-through (CTR) nội bộ. | Hằng ngày | Đo lường mức độ tương tác và khả năng thu hút độc giả của sản phẩm mới. |
| **3. Commerce (Doanh thu)** | - Tỷ lệ lấp đầy (Fill rate) quảng cáo trên landing page.<br>- SOV (Share of Voice) bán được.<br>- Doanh thu bình quân trên mỗi địa bàn. | Hằng tháng | Đo lường hiệu quả thương mại hóa của dự án. |
| **4. Risk (Rủi ro)** | - Số lượng trang bị cảnh báo "thin content" (trang mỏng).<br>- Tỷ lệ lỗi 404 / Lỗi redirect vòng.<br>- Tốc độ tải trang di động (Core Web Vitals - LCP, CLS, FID). | Thời gian thực | Cảnh báo sớm các lỗi kỹ thuật và nguy cơ bị phạt thuật toán Google. |
| **5. Operations (Vận hành)** | - Thời gian trung bình để Trưởng VPTT duyệt bài tiêu điểm.<br>- Tỷ lệ phản hồi chỉnh sửa tag từ các văn phòng thường trú. | Hằng tuần | Đo lường mức độ thích nghi của tòa soạn với quy trình vận hành mới. |
