# 6. ĐẶC TẢ QUY TRÌNH TÒA SOẠN VÀ CƠ CHẾ SEO TAG CỦA BÁO LAO ĐỘNG

Tài liệu này mô tả chi tiết cơ chế hoạt động thực tế của Tòa soạn Báo Lao Động (quy trình xuất bản tin bài 5 bước) và cơ chế phối hợp gắn tag địa phương giữa Phóng viên, Thư ký tòa soạn và Ban CNTT. Đây là tài liệu nền tảng giúp "cấy não" và đồng bộ tư duy cho trợ lý AI.

---

## 1. QUY TRÌNH XUẤT BẢN TIN BÀI 5 BƯỚC (EDITORIAL WORKFLOW)

Mọi tin bài xuất bản trên Báo Lao Động (áp dụng thống nhất trên phạm vi toàn quốc và tất cả các ban chuyên môn/VPTT) đều phải tuân thủ nghiêm ngặt quy trình phê duyệt khép kín dưới đây:

```
[1. Phóng viên] (Viết & gắn tag v1)
       │
       ▼
[2. Lãnh đạo VPTT / Ban Chuyên môn] (Duyệt sơ bộ & định hướng)
       │
       ▼
[3. Biên tập viên] (Rà soát & tối ưu nội dung)
       │
       ▼
[4. Thư ký Tòa soạn] (Kiểm duyệt kỹ thuật, pháp lý & tiêu đề)
       │
       ▼
[5. Ban Biên tập / Lãnh đạo Báo] (Phê duyệt xuất bản)
       │
       ▼
[Xuất bản lên trang laodong.vn]
       │
       ▼
[Ban CNTT (IT)] (Hỗ trợ tối ưu SEO tag sau xuất bản)
```

### Chi tiết vai trò hành động trong quy trình:

1.  **Bước 1: Phóng viên (Tác giả)**
    *   **Nhiệm vụ**: Thu thập thông tin, viết bài.
    *   **Thao tác kỹ thuật**:
        *   Viết định danh địa bàn (Dateline) ở ngay đầu thân bài (ví dụ: *"NGHỆ AN - ..."*, *"HÀ NỘI - ..."*).
        *   Gắn các SEO tag ban đầu (Lớp 1: Headline place, Lớp 2: In-text places, Lớp 3: Affected areas) trên CMS.
2.  **Bước 2: Lãnh đạo VPTT / Lãnh đạo Ban chuyên môn**
    *   **Nhiệm vụ**: Duyệt tính thời sự, định hướng đề tài và xác định trách nhiệm địa bàn tác nghiệp.
    *   **Thao tác kỹ thuật**: Xác nhận hoặc chỉnh sửa trường `Responsible Office` (Lớp 4).
3.  **Bước 3: Biên tập viên**
    *   **Nhiệm vụ**: Biên sửa câu từ, sửa lỗi ngữ pháp, căn chỉnh hình ảnh đại diện đúng kích thước chuẩn (tối thiểu 1200px).
4.  **Bước 4: Thư ký Tòa soạn (TKTS)**
    *   **Nhiệm vụ**: Gác cổng pháp lý (Luật Báo chí, Luật Quảng cáo), kiểm duyệt tiêu đề phù hợp, rà soát tính nhất quán của hệ thống tag và canonical URL trước khi xuất bản.
5.  **Bước 5: Lãnh đạo Báo (Ban Biên tập)**
    *   **Nhiệm vụ**: Quyết định xuất bản chính thức lên trang chủ hoặc trang chuyên mục.
6.  **Sau xuất bản: Ban CNTT (IT) hỗ trợ**
    *   **Nhiệm vụ**: Quét lỗi kỹ thuật sau khi bài lên trang.
    *   **Thao tác kỹ thuật**: Tối ưu SEO tag (nếu phát hiện phóng viên gắn thiếu từ khóa hot hoặc sai thực thể), sửa lỗi redirect, giám sát Core Web Vitals của landing page chứa bài viết.

---

## 2. CƠ CHẾ GẮN ĐỊNH DANH ĐỊA PHƯƠNG (DATELINE) THỰC TẾ

Trên Báo Lao Động, mỗi bài viết thời sự địa phương luôn đi kèm tiền tố định danh địa danh viết hoa ở đầu bài viết để tạo thói quen tiếp nhận cho độc giả:

*   *Mẫu bài viết thực tế*:
    > **NGHỆ AN -** Sáng ngày 29.5, Liên đoàn Lao động tỉnh Nghệ An đã tổ chức chương trình đối thoại trực tiếp giữa người lao động và người sử dụng lao động...
*   *Cơ chế tự động hóa*: CMS sẽ quét tiền tố định danh địa phương này ở đầu bài viết để tự động gợi ý tag `Headline Place` tương ứng trong Taxonomy Service (Ví dụ: Chữ "NGHỆ AN -" sẽ tự động kích hoạt gợi ý tag `Nghệ An` với độ tin cậy Confidence Score = 99%).

---

## 3. PHÂN ĐỊNH TRÁCH NHIỆM SEO TAG GIỮA PHÓNG VIÊN VÀ IT

| Bộ phận thực hiện | Vai trò trong quy trình SEO Tag | Công cụ hỗ trợ trên CMS |
| :--- | :--- | :--- |
| **Phóng viên (Chủ động)** | - Gắn tag trực tiếp khi viết bài.<br>- Nắm rõ bối cảnh thực tế sự kiện để gắn các tag thuộc lớp `Affected areas` (Ví dụ: bão đổ bộ Nghệ An nhưng ảnh hưởng trực tiếp tới Hà Tĩnh, Thanh Hóa). | - Ô tìm kiếm tag thông minh (Auto-suggest).<br>- Checklist các thực thể địa phương thuộc VPTT phụ trách. |
| **Ban CNTT / IT (Hỗ trợ sau)** | - Quét tự động kho bài viết sau khi lên trang.<br>- Sửa đổi, bổ sung tag hàng loạt khi có chủ đề/sự kiện lớn (Topic Clustering).<br>- Tối ưu hóa metadata, thẻ canonical và schema cấu trúc JSON-LD. | - Dashboard kiểm toán SEO tag.<br>- Công cụ Audit lỗi trùng lặp URL.<br>- Tool đồng bộ thực thể Canonical Place Map. |
