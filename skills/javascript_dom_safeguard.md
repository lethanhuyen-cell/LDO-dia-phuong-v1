# Bài học (Skill): Javascript DOM Elements Reference Safeguard

**Vấn đề (Lỗi cũ):**
Lỗi `ReferenceError: mostReadContainer is not defined` phát sinh khi Javascript cố tình truy cập vào một phần tử DOM trực tiếp thông qua ID của nó (ví dụ: `mostReadContainer.innerHTML = ...`) mà KHÔNG có bất kỳ khai báo biến nào.
Trong Javascript, nếu một ID HTML chứa dấu gạch nối (ví dụ: `<div id="most-read-container">`), trình duyệt sẽ **không tự động tạo biến global** với định dạng camelCase (như `mostReadContainer`). Cố tình gọi một biến chưa được định nghĩa (undefined) trong Strict Mode hoặc khi chạy thực tế sẽ lập tức tạo ra Exception (lỗi runtime). 
Khi xảy ra Exception, **toàn bộ luồng thực thi Javascript bị treo**, khiến các hàm render UI phía sau không được chạy (dẫn tới bị trống hoặc mất giao diện).

**Cách phòng tránh (Giải pháp):**
1. **LUÔN LUÔN** dùng `document.getElementById('id_cua_element')` để lấy tham chiếu tới phần tử HTML.
2. Lưu kết quả vào biến trước khi tác động: `let container = document.getElementById('most-read-container');`
3. Thêm bước **kiểm tra tính tồn tại (null check)** trước khi gán dữ liệu:
```javascript
let container = document.getElementById('most-read-container');
if (container) {
    container.innerHTML = "Dữ liệu HTML";
} else {
    console.warn("DOM Element 'most-read-container' không tồn tại!");
}
```
4. **Không bao giờ tin cậy vào Magic Global Variables** được trình duyệt tạo ra tự động từ các ID HTML. Luôn luôn khai báo tham chiếu rõ ràng.
