# 2. SOP BIÊN TẬP VÀ QUY TRÌNH VẬN HÀNH NỘI DUNG ĐỊA PHƯƠNG

Tài liệu này đặc tả quy chuẩn tác nghiệp, phân loại (taxonomy) bài viết và vận hành nội dung số cho dự án **Lao Động – vùng miền**. Mục tiêu tối thượng là đảm bảo chất lượng thông tin, tăng tỷ lệ tuần hoàn (recirculation), ngăn ngừa rủi ro Doorway Pages và tuân thủ Luật Báo chí Việt Nam.

---

## 1. QUY CHUẨN GẮN TAG PHÂN LOẠI 4 LỚP

Mọi bài viết xuất bản liên quan đến yếu tố địa lý bắt buộc phải được gắn tag theo mô hình 4 lớp dưới đây. Không được bỏ sót hoặc gộp các lớp.

```
┌─────────────────────────────────────────────────────────────────┐
│                       BÀI VIẾT XUẤT BẢN                         │
└────────────────────────────────┬────────────────────────────────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Headline Place  │     │ In-text Places  │     │ Affected Areas  │
│ (1 thực thể)    │     │ (n thực thể)    │     │ (n thực thể)    │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │  Resp. Office   │
                        │ (1 Văn phòng)   │
                        └─────────────────┘
```

### Chi tiết định nghĩa và quy tắc áp dụng

| Lớp Tag | Đối tượng & Phạm vi | Quy tắc gắn bắt buộc | Mục tiêu SEO & Trải nghiệm |
| :--- | :--- | :--- | :--- |
| **1. Headline Place** | Địa danh trung tâm của bài viết, thường xuất hiện ở tiêu đề hoặc dòng đầu tiên (dateline). | **Tối đa 1 tag**. Chỉ gắn khi địa danh này quyết định bản chất của tin tức. | Xác định tiêu đề động cho module, định vị SEO meta title cho bài viết. |
| **2. In-text Places** | Các địa danh được nhắc đến trong nội dung thân bài nhưng không phải tiêu điểm chính. | **Không giới hạn**. Gắn tự động qua NER (Nhận diện thực thể) trên CMS, phóng viên rà soát lại. | Phục vụ các công cụ tìm kiếm nội bộ và widget liên kết bài viết liên quan. |
| **3. Affected Areas** | Vùng chịu tác động thực tế của sự kiện (dự án giao thông đi qua nhiều tỉnh, thiên tai...). | **Từ 0 đến 5 tag**. Có thể khác hoàn toàn với địa bàn viết bài (Headline Place). | Đẩy bài viết về landing page của các địa phương bị ảnh hưởng để phục vụ độc giả. |
| **4. Responsible Office** | Văn phòng thường trú (VPTT) hoặc Phòng ban chịu trách nhiệm tác nghiệp và nội dung. | **Bắt buộc duy nhất 1 tag** trong 6 VPTT của Báo Lao Động. | Phân định trách nhiệm xử lý, tính KPI sản lượng/chất lượng cho từng VPTT. |

---

## 2. QUY TẮC ĐỒNG NHẤT THỰC THỂ (CANONICAL PLACES DICTIONARY)

Để tránh hiện tượng chia nhỏ URL hoặc phân tán dòng traffic, CMS áp dụng bảng ánh xạ thực thể chuẩn dưới đây:

| ID Thực thể | Tên hiển thị chuẩn | Slug URL | VPTT Quản lý | Từ khóa đồng nghĩa (Aliases) được ánh xạ tự động |
| :--- | :--- | :--- | :--- | :--- |
| **PL-HAN** | Hà Nội | `ha-noi` | VPTT Hà Nội | Hà Thành, HN, Thủ đô Hà Nội, TP Hà Nội, Ha Noi |
| **PL-SGN** | TP. Hồ Chí Minh | `tp-hcm` | VPTT Miền Nam | Sài Gòn, TP.HCM, Thành phố Hồ Chí Minh, TPHCM |
| **PL-NAN** | Nghệ An | `nghe-an` | VPTT Bắc Trung Bộ | Vinh, Tỉnh Nghệ An, Nghe An |
| **PL-QNH** | Quảng Ninh | `quang-ninh` | VPTT Quảng Ninh | Hạ Long, Đất mỏ, Tỉnh Quảng Ninh, Quang Ninh |
| **PL-DAD** | Đà Nẵng | `da-nang` | VPTT Miền Trung | Đà Thành, TP Đà Nẵng, Da Nang |
| **PL-VLO** | Vĩnh Long | `vinh-long` | VPTT Đồng bằng Sông Cửu Long | Tỉnh Vĩnh Long, Vinh Long |

*Nguyên tắc hệ thống*: Khi phóng viên gõ bất kỳ từ khóa nào trong danh mục "Aliases", CMS sẽ tự động quy đổi về ID thực thể chuẩn.

---

## 3. SOP KIỂM SOÁT CHẤT LƯỢNG LANDING PAGE (CHỐNG DOORWAY PAGES)

Một landing page tỉnh/thành chỉ được phép công khai index lên Google khi và chỉ khi đạt đầy đủ các tiêu chuẩn cấu trúc nội dung dưới đây:

### Checklist Tiêu chuẩn Landing Page Địa phương

- [ ] **Mô tả biên tập độc nhất (Editorial Description)**: Có đoạn giới thiệu viết tay từ 120 đến 250 từ nêu rõ đặc điểm, nhịp tin cốt lõi của địa phương. **Cấm copy-paste** hoặc sử dụng AI spin content hàng loạt giữa các tỉnh.
- [ ] **Mô-đun Tiêu điểm (Top Stories) thủ công**: Có tối thiểu 3 bài viết tiêu điểm do Trưởng VPTT trực tiếp chọn lọc (không dùng cơ chế tự động lấy bài mới nhất).
- [ ] **Mật độ bài viết tối thiểu**: Landing page phải có tối thiểu **15 bài viết chất lượng** có tag tương ứng trong vòng 30 ngày gần nhất. Nếu thấp hơn, hệ thống tự động gán thẻ `noindex`.
- [ ] **Thanh điều hướng rõ ràng (Breadcrumb)**: Có Breadcrumb dạng: `Trang chủ > Vùng miền > [Tên Vùng] > [Tên Tỉnh/Thành]`.
- [ ] **Nhãn quảng cáo minh bạch**: Khu vực dành cho quảng cáo/tài trợ nằm ngoài luồng tin biên tập và ghi rõ nhãn "Thông tin doanh nghiệp".

---

## 4. QUY TRÌNH VÒNG ĐỜI NỘI DUNG VÀ REPUBLISHING (LIFECYCLE SOP)

Để đảm bảo tính toàn vẹn dữ liệu và tuân thủ Google News, tòa soạn quy định chặt chẽ cách xử lý các trường hợp cập nhật thông tin:

```
                  ┌──────────────────────────────┐
                  │ Yêu cầu cập nhật nội dung    │
                  └──────────────┬───────────────┘
                                 │
         ┌───────────────────────┴───────────────────────┐
         ▼                                               ▼
┌──────────────────────────────┐               ┌──────────────────────────────┐
│  Lỗi chính tả, lỗi nhỏ       │               │  Diễn biến mới / Sửa lớn     │
└────────┬─────────────────────┘               └────────┬─────────────────────┘
         │                                              │
         ▼                                              ▼
┌──────────────────────────────┐               ┌──────────────────────────────┐
│ - Giữ nguyên URL             │               │ - Giữ nguyên URL             │
│ - Sửa nội dung trực tiếp     │               │ - Cập nhật dateModified      │
│ - Không đổi ngày xuất bản    │               │ - Thêm dòng "Cập nhật lúc..."│
└──────────────────────────────┘               └──────────────────────────────┘
```

1.  **Sửa lỗi chính tả/Lỗi cú pháp**:
    *   Giữ nguyên URL. Sửa trực tiếp. Không thay đổi ngày giờ xuất bản và không khai báo `dateModified`.
2.  **Cập nhật thông tin quan trọng / Diễn biến mới**:
    *   **Giữ nguyên URL bài viết gốc**. Tuyệt đối không xóa bài cũ để đăng lại bài mới cùng nội dung (Republish).
    *   Cập nhật nội dung trong bài, thay đổi tag `dateModified` trong cấu trúc Schema JSON-LD.
    *   Ghi rõ ở đầu hoặc cuối bài viết: *"Bài viết được cập nhật lúc [Giờ] ngày [Ngày] để bổ sung thông tin về..."*
3.  **Xử lý thông tin sai sự thật (Đính chính / Cải chính)**:
    *   Tuân thủ nghiêm ngặt Luật Báo chí: Thực hiện cải chính, xin lỗi.
    *   Với báo điện tử, giữ nguyên URL bài viết cũ nhưng thay thế nội dung bằng văn bản đính chính chính thức hoặc gỡ bỏ thông tin sai lệch và ghi rõ lý do điều chỉnh. Không tự ý xóa trang (lỗi 404) khi chưa có phê duyệt từ Ban Biên tập.

---

## 5. QUY TRÌNH PHÊ DUYỆT VÀ ESCALATION PATH

Quy trình phối hợp giải quyết khi phát hiện lỗi hệ thống hoặc xung đột lợi ích:

*   **Lỗi gắn tag**: Phóng viên phát hiện sửa trực tiếp qua CMS -> Nếu bài đã xuất bản quá 24 giờ, phải báo Thư ký tòa soạn duyệt sửa để cập nhật sitemap.
*   **Yêu cầu gỡ bài / Sửa bài từ phía thương mại (Doanh nghiệp/Nhà tài trợ)**:
    *   *Quy tắc cứng*: Phòng Kinh doanh không được tự ý hứa hẹn hay yêu cầu gỡ/sửa nội dung biên tập.
    *   *Đường leo thang (Escalation Path)*: Yêu cầu từ đối tác -> Gửi đến Phòng Kinh doanh -> Trình Ban Biên tập duyệt -> Thư ký tòa soạn thực hiện nếu lý do hợp lý về mặt pháp lý/sự thật. Cấm tuyệt đối can thiệp kỹ thuật trực tiếp từ IT hoặc kinh doanh.
