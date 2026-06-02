# Nhật ký Phiên làm việc (Session State & Context)

> [!IMPORTANT]
> **QUY TẮC TỰ ĐỘNG CẬP NHẬT:** 
> 1. Mỗi khi kết thúc một yêu cầu hoặc kết thúc phiên làm việc, **AI PHẢI tự động cập nhật** file [session_state.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/session_state.md) (về tiến độ) và [skills.md](file:///c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING%20PAGE%20THƯỜNG%20TRÚ/skills.md) (về kinh nghiệm kỹ thuật/bài học rút ra) mà không cần người dùng nhắc nhở.
> 2. Khi bắt đầu một phiên làm việc mới, bạn chỉ cần gõ: **`làm-tiếp`**. AI sẽ đọc file này để nắm bắt bối cảnh lập tức.

> [!CAUTION]
> **🔒 KHUNG CHAT CHÍNH DỰ ÁN (MASTER CHAT)**
> Conversation ID: `1be5f1f6-24da-484d-8983-4229c6fefd6f`
> Mọi cập nhật kỹ thuật, deploy, chỉnh sửa code, và cập nhật tài liệu dự án **CHỈ ĐƯỢC THỰC HIỆN** từ khung chat này. Không thực hiện thay đổi dự án từ bất kỳ conversation nào khác.

---

## 📅 Cập nhật cuối cùng
- Thời gian: 2026-06-02T11:55:00+07:00
- Trạng thái hiện tại: ✅ **ĐÃ KHẮC PHỤC LỖI HIỂN THỊ & DEPLOY AN TOÀN OPTION A**


---

## 🛠️ Trạng thái Dự án & Bối cảnh Hiện tại

### Vercel Production URLs
- **Hà Nội:** https://laodong-hanoi.vercel.app (= `index.html`)
- **TPHCM & Đông Nam Bộ:** https://laodong-hanoi.vercel.app/tphcm_index.html

### Các file cốt lõi:
| File | Vai trò | Trạng thái |
|------|---------|------------|
| `apply_ads_layout.py` | Script build trang Hà Nội | ✅ Cập nhật |
| `apply_tphcm_layout.py` | Script build trang TPHCM & ĐNB | ✅ Cập nhật |
| `demo_landing_page_hanoi_clean.html` | Template sạch Hà Nội | ✅ |
| `hanoi_final_consolidated.json` | Dữ liệu bài viết Hà Nội | ✅ |
| `tphcm_dongnambo_consolidated.json` | Dữ liệu bài viết TPHCM+ĐNB | ✅ |
| `index.html` | Production Hà Nội | ✅ Deployed |
| `tphcm_index.html` | Production TPHCM & ĐNB | ✅ Deployed |

---

## 📋 Tóm tắt buổi làm việc 01/06/2026 (hôm nay)

### Sáng: Triển khai Hub & Spoke TPHCM & Đông Nam Bộ
- ✅ Cào quét 64 bài viết thực tế từ TPHCM, Đồng Nai, Tây Ninh
- ✅ Xây dựng tab bar Hub & Spoke lọc theo tỉnh (all/tphcm/dongnai/tayninh)
- ✅ Provincial Profile Widget hiển thị thông tin lãnh đạo, dân số, kinh tế theo tab
- ✅ Lịch cắt điện liên kết động theo tỉnh đang xem

### Chiều: Tối ưu layout bố cục
- ✅ **Fix khoảng trắng lớn top giao diện** → Thêm `#left-column-feed-container` bổ sung 3 tin nhỏ kiểu sidebar bên dưới 3 tin bottom row để cân bằng chiều cao cột trái với sidebar phải
- ✅ **Cụm Đọc nhiều nhất**: Chuyển sang carousel 3 slide x 5 bài (gọn, tự chuyển mỗi 5 giây, có dots navigation) — bố trí NGANG bên dưới khối main cover trong `infra-block`
- ✅ **Tin mới nhất (News Ticker Bar)**: Dải marquee cuộn ngang vô hạn ngay DƯỚI dải breadcrumbs, kiểu CafeF
  - Tự động loại trừ bài đã hiển thị ở Tiêu điểm + Main Cover + Đọc nhiều
  - Click mở Local Reader Modal (không rời trang)
  - Dừng cuộn khi hover

### Tối: Đồng bộ sang Hà Nội & Deploy
- ✅ Áp dụng đầy đủ các skill TPHCM sang trang Hà Nội
- ✅ Rebuild cả 6 file HTML output
- ✅ Commit & Push → Vercel auto-deploy

---

## 🏗️ Kiến trúc Layout hiện tại (cả 2 trang)

```
[HEADER - Nav Báo Lao Động]
[BREADCRUMBS] ← [TICKER BAR cuộn ngang tin mới loại trừ trùng] →
[INTRO BADGE: "Trang thông tin địa bàn..."]
[HUB & SPOKE TAB BAR] (chỉ có ở TPHCM)
[AD SLOT 01: Billboard 970x250]
[BLOCK 1: MAIN COVER]
  ├─ CỘT TRÁI (.pl):
  │   ├─ subcover-container (2 tin stacked)
  │   ├─ main-cover-container (1 tin lớn)
  │   ├─ subcover-bottom-row (3 tin grid)
  │   └─ left-column-feed-container (3 tin nhỏ thumbnail bù chiều cao)
  └─ CỘT PHẢI (.pr):
      ├─ Tiêu điểm (4 tin spotlight)
      ├─ AD SLOT 02: Sidebar 300x250
      └─ Sự kiện bình luận + Người Việt tử tế
[INFRA BLOCK: Đọc nhiều nhất carousel 3 slide x 5 bài]
[BLOCK 2: Media Section]
[BLOCK 3: Category Columns]
[...]
[FOOTER]
```

---

## 📝 Việc cần làm buổi tiếp theo

- [ ] Kiểm tra trực tiếp trên Vercel: Ticker bar, Carousel đọc nhiều, left-column-feed
- [ ] Mở rộng test trên mobile (responsive)
- [ ] Thêm PCI Index / Governance Score widget vào trang địa phương (đã phê duyệt chiều nay)
- [ ] Triển khai thêm các trang spoke mới (Bình Dương, Bình Phước cho ĐNB)
- [ ] Tích hợp tính năng lưu vị trí đọc (scroll restoration) khi đóng mở Reader Modal
