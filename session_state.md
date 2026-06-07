# Nhật ký Phiên làm việc (Session State & Context)

> [!IMPORTANT]
> **QUY TẮC TỰ ĐỘNG CẬP NHẬT:** 
> 1. Mỗi khi kết thúc một yêu cầu hoặc kết thúc phiên làm việc, **AI PHẢI tự động cập nhật** file [session_state.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/session_state.md) và [skills.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/skills.md).
> 2. Khi bắt đầu một phiên làm việc mới, bạn chỉ cần gõ: **`làm-tiếp`**. AI sẽ đọc file này để nắm bắt bối cảnh lập tức.

---

## 📌 Cập nhật cuối cùng
- Thời gian: 2026-06-07
- Trạng thái hiện tại: ✅ **ĐÃ TÁCH KHỐI TIỆN ÍCH DÂN SINH VÀ KHÔNG GIAN SỐNG. ĐÃ XỬ LÝ LỖI CACHE/SAI LINK VERCEL.**

---

## 🌐 Trạng thái Dự án & Bối cảnh Hiện tại

### Vercel Production URLs
> [!WARNING]
> **LƯU Ý QUAN TRỌNG VỀ DEPLOYMENT URL:** 
> Dự án Vercel tự động nhận code từ branch `main` của repo `LDO-dia-phuong-v1` là **`laodong-hanoi.vercel.app`** (không có hậu tố `-v2`). 
> **Tuyệt đối KHÔNG GỬI link `laodong-hanoi-v2.vercel.app` cho user** vì đó là một deployment thủ công cũ, không tự động cập nhật code mới, dẫn đến việc user không thấy thay đổi.

- **HÀ NỘI:** https://laodong-hanoi.vercel.app (= `index.html`)
- **TPHCM & Đông Nam Bộ:** https://laodong-hanoi.vercel.app/tphcm_index.html

### Các file cốt lõi:
| File | Vai trò | Trạng thái |
|------|---------|------------|
| `apply_ads_layout.py` | Script build trang Hà Nội | ✅ Cập nhật |
| `apply_tphcm_layout.py` | Script build trang TPHCM & ĐNB | ✅ Cập nhật |
| `index.html` | Production Hà Nội | ✅ Deployed |
| `tphcm_index.html` | Production TPHCM & ĐNB | ✅ Deployed |
| `vercel.json` | Cấu hình Vercel chống cache | ✅ Đã thêm |

---

## 📝 Tóm tắt buổi làm việc 07/06/2026

### Cấu trúc lại giao diện (Refactor 2-Column Layout)
- ✅ Chuyển toàn bộ giao diện sang cấu trúc 2 cột rõ ràng từ trên xuống dưới (`main-content-col` 2.2fr và `sidebar-col` 1fr).
- ✅ Dời toàn bộ các widget Tiện ích (Tra cứu phạt nguội, Giá đất, Lịch biểu diễn, Chợ Công đoàn, Lịch cắt điện) sang `sidebar-col`.
- ✅ **Bốc tách Khối 5.5**: 
  - Khối **Không gian sống** (tin bài) được đưa trở lại `main-content-col` (cột trái).
  - Khối **Tiện ích dân sinh** (Nhật ký phản ánh, Kết nối tiêu dùng) được dời hẳn sang `sidebar-col` (cột phải thứ 3).

### Xử lý sự cố hiển thị Vercel
- Phát hiện user xem nhầm link `laodong-hanoi-v2` (bản deploy tay cũ) khiến giao diện không thay đổi.
- Chạy manual deploy `npx vercel --prod` và cung cấp link chuẩn `laodong-hanoi.vercel.app`.
- Bổ sung `vercel.json` với header `Cache-Control: no-cache` để đảm bảo luôn load HTML mới nhất từ Edge Network.

---

## 🏗️ Kiến trúc Layout hiện tại

```
[HEADER - Nav Báo Lao Động]
[BREADCRUMBS]
[INTRO BADGE]
[HUB & SPOKE TAB BAR] (chỉ có ở TPHCM)

<div class="two-col-layout">
  <!-- CỘT TRÁI (Tin tức chính) -->
  <div class="main-content-col">
    [BLOCK 1: MAIN COVER]
    [INFRA BLOCK: Đọc nhiều nhất carousel]
    [BLOCK 2: Media Section]
    [BLOCK 3: Category Columns]
    [BLOCK 4: Thời sự, Xã hội, Pháp luật, Bạn đọc]
    [BLOCK 5: Bất động sản, Nhịp sống, Việc làm]
    [KHÔNG GIAN SỐNG: Cẩm nang KCN, Trốn phố]
    [BLOCK 5.8: Cẩm nang ăn chơi]
    [THÔNG TIN DOANH NGHIỆP]
  </div>

  <!-- CỘT PHẢI (Tiện ích & Tương tác) -->
  <div class="sidebar-col">
    [DANH MỤC TIỆN ÍCH TỔNG HỢP]
    [TRUNG TÂM TRA CỨU NHANH]
    [CHỢ CÔNG ĐOÀN - DEAL HOT]
    [LỊCH BIỂU DIỄN & GIẢI TRÍ]
    [LỊCH CẮT ĐIỆN]
    [TIỆN ÍCH DÂN SINH: Nhật ký phản ánh, Kết nối tiêu dùng]
  </div>
</div>
[FOOTER]
```
