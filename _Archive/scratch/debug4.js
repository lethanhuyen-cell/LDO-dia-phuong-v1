const document = { getElementById: function(id) { return {style:{}, classList:{add:function(){}, remove:function(){}}, appendChild:function(){}}; }, querySelectorAll: function() { return []; }, addEventListener: function(e, cb) { cb(); }, createElement: function() { return {appendChild:function(){}}; } };
const window = { addEventListener: function(e, cb) { cb(); } };
const IntersectionObserver = class { constructor() {} observe() {} };

    const originalTphcmArticles = [
        {
                "id": 0,
                "title": "TPHCM điều động, bổ nhiệm cán bộ lãnh đạo chủ chốt",
                "excerpt": "TPHCM điều động, bổ nhiệm cán bộ lãnh đạo chủ chốt",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1711741/Can-Bo-Tphcm.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/thoi-su/tphcm-dieu-dong-bo-nhiem-can-bo-lanh-dao-chu-chot-1711741.ldo",
                "date": "01/06/2026 13:33",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Thời sự"
                ],
                "category": "Thời sự",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 1,
                "title": "Tổng Bí thư, Chủ tịch nước dâng hoa tại Tượng đài Chủ tịch Hồ Chí Minh ở Philippines",
                "excerpt": "Tổng Bí thư, Chủ tịch nước dâng hoa tại Tượng đài Chủ tịch Hồ Chí Minh ở Philippines",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711342/To-Lam5.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/thoi-su/tong-bi-thu-chu-tich-nuoc-dang-hoa-tai-tuong-dai-chu-tich-ho-chi-minh-o-philippines-1711342.ldo",
                "date": "31/05/2026 17:06",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Thời sự"
                ],
                "category": "Thời sự",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 2,
                "title": "Tổng Bí thư, Chủ tịch nước Tô Lâm dâng hoa tưởng niệm Chủ tịch Hồ Chí Minh tại Singapore",
                "excerpt": "Tổng Bí thư, Chủ tịch nước Tô Lâm dâng hoa tưởng niệm Chủ tịch Hồ Chí Minh tại Singapore",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/30/1710631/Rsz_To-Lam.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/thoi-su/tong-bi-thu-chu-tich-nuoc-to-lam-dang-hoa-tuong-niem-chu-tich-ho-chi-minh-tai-singapore-1710631.ldo",
                "date": "30/05/2026 11:26",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Thời sự"
                ],
                "category": "Thời sự",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 3,
                "title": "Chủ tịch Quốc hội đề nghị TPHCM khẩn trương hoàn thiện dự thảo Luật Đô thị đặc biệt",
                "excerpt": "Chủ tịch Quốc hội đề nghị TPHCM khẩn trương hoàn thiện dự thảo Luật Đô thị đặc biệt",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/29/1710423/Chu-Tich-Quoc-Hoi.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/thoi-su/chu-tich-quoc-hoi-de-nghi-tphcm-khan-truong-hoan-thien-du-thao-luat-do-thi-dac-biet-1710423.ldo",
                "date": "29/05/2026 20:10",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Thời sự"
                ],
                "category": "Thời sự",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 4,
                "title": "Chủ tịch Quốc hội chúc mừng Đại lễ Phật đản tại TPHCM",
                "excerpt": "Chủ tịch Quốc hội chúc mừng Đại lễ Phật đản tại TPHCM",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/29/1710091/Chua2.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/thoi-su/chu-tich-quoc-hoi-chuc-mung-dai-le-phat-dan-tai-tphcm-1710091.ldo",
                "date": "29/05/2026 14:46",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Thời sự"
                ],
                "category": "Thời sự",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 5,
                "title": "Vũng Tàu tổ chức lại giao thông tuyến đường lên núi Nhỏ, núi Lớn",
                "excerpt": "Vũng Tàu tổ chức lại giao thông tuyến đường lên núi Nhỏ, núi Lớn",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711360/Giao-Thong-1.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/giao-thong/vung-tau-to-chuc-lai-giao-thong-tuyen-duong-len-nui-nho-nui-lon-1711360.ldo",
                "date": "31/05/2026 17:46",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 6,
                "title": "10 bước sắp xếp gần 6.000 khu phố, ấp, khu dân cư ở TPHCM",
                "excerpt": "10 bước sắp xếp gần 6.000 khu phố, ấp, khu dân cư ở TPHCM",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1711995/Sap-Xep-Khu-Pho-1-1.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/10-buoc-sap-xep-gan-6000-khu-pho-ap-khu-dan-cu-o-tphcm-1711995.ldo",
                "date": "01/06/2026 18:50",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 7,
                "title": "Nóng Sài Gòn: Các cửa hàng ở TPHCM chính thức bán đại trà xăng E10",
                "excerpt": "Nóng Sài Gòn: Các cửa hàng ở TPHCM chính thức bán đại trà xăng E10",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1711819/XANG.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/video/nong-sai-gon-cac-cua-hang-o-tphcm-chinh-thuc-ban-dai-tra-xang-e10-1711819.ldo",
                "date": "01/06/2026 19:00",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Kinh tế"
                ],
                "category": "Kinh tế",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 8,
                "title": "TPHCM phát hiện nhiều thực phẩm và hàng hóa không rõ nguồn gốc",
                "excerpt": "TPHCM phát hiện nhiều thực phẩm và hàng hóa không rõ nguồn gốc",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1711701/2.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/kinh-doanh/tphcm-phat-hien-nhieu-thuc-pham-va-hang-hoa-khong-ro-nguon-goc-1711701.ldo",
                "date": "01/06/2026 11:24",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Kinh tế"
                ],
                "category": "Kinh tế",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 9,
                "title": "TPHCM thúc đẩy “số hóa” chợ truyền thống để hút khách",
                "excerpt": "TPHCM thúc đẩy “số hóa” chợ truyền thống để hút khách",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711462/3-Tphcm.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/kinh-doanh/tphcm-thuc-day-so-hoa-cho-truyen-thong-de-hut-khach-1711462.ldo",
                "date": "01/06/2026 11:00",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Kinh tế"
                ],
                "category": "Kinh tế",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 10,
                "title": "Hàng loạt cửa hàng ở TPHCM chính thức bán đại trà xăng E10",
                "excerpt": "Hàng loạt cửa hàng ở TPHCM chính thức bán đại trà xăng E10",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1711593/Xang2.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/kinh-doanh/hang-loat-cua-hang-o-tphcm-chinh-thuc-ban-dai-tra-xang-e10-1711593.ldo",
                "date": "01/06/2026 09:51",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Kinh tế"
                ],
                "category": "Kinh tế",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 11,
                "title": "Đề thi, đáp án môn Toán thi vào lớp 10 tại TPHCM năm 2026",
                "excerpt": "Đề thi, đáp án môn Toán thi vào lớp 10 tại TPHCM năm 2026",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/2/1712137/P.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/giao-duc/de-thi-dap-an-mon-toan-thi-vao-lop-10-tai-tphcm-nam-2026-1712137.ldo",
                "date": "02/06/2026 08:52",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Giáo dục"
                ],
                "category": "Giáo dục",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 12,
                "title": "Thí sinh ở TPHCM tự tin bước vào môn thi cuối cùng trong kỳ thi vào lớp 10",
                "excerpt": "Thí sinh ở TPHCM tự tin bước vào môn thi cuối cùng trong kỳ thi vào lớp 10",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/2/1712122/Thpt-Hv.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/video/thi-sinh-o-tphcm-tu-tin-buoc-vao-mon-thi-cuoi-cung-trong-ky-thi-vao-lop-10-1712122.ldo",
                "date": "02/06/2026 08:11",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Giáo dục"
                ],
                "category": "Giáo dục",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 13,
                "title": "Thí sinh lo ngại dạng toán thực tế trong đề thi Toán lớp 10 tại TPHCM",
                "excerpt": "Thí sinh lo ngại dạng toán thực tế trong đề thi Toán lớp 10 tại TPHCM",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1712077/MON-TOAN-1.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/giao-duc/thi-sinh-lo-ngai-dang-toan-thuc-te-trong-de-thi-toan-lop-10-tai-tphcm-1712077.ldo",
                "date": "02/06/2026 07:44",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Giáo dục"
                ],
                "category": "Giáo dục",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 14,
                "title": "Sáng nay, thí sinh tại TPHCM tiếp tục dự thi môn Toán trong kỳ thi lớp 10",
                "excerpt": "Sáng nay, thí sinh tại TPHCM tiếp tục dự thi môn Toán trong kỳ thi lớp 10",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1712063/THI-TIENG-ANH.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/giao-duc/sang-nay-thi-sinh-tai-tphcm-tiep-tuc-du-thi-mon-toan-trong-ky-thi-lop-10-1712063.ldo",
                "date": "02/06/2026 06:00",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Giáo dục"
                ],
                "category": "Giáo dục",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 15,
                "title": "Ngày đầu thi lớp 10 ở TPHCM: Phát sinh sự cố đề thi tại một số điểm thi",
                "excerpt": "Ngày đầu thi lớp 10 ở TPHCM: Phát sinh sự cố đề thi tại một số điểm thi",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1711960/Thi-Ngu-Van.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/giao-duc/ngay-dau-thi-lop-10-o-tphcm-phat-sinh-su-co-de-thi-tai-mot-so-diem-thi-1711960.ldo",
                "date": "01/06/2026 17:38",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Giáo dục"
                ],
                "category": "Giáo dục",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 16,
                "title": "Chấn chỉnh việc xếp hàng qua đêm nộp hồ sơ nhà ở xã hội CT-02 An Bình Tân",
                "excerpt": "Chấn chỉnh việc xếp hàng qua đêm nộp hồ sơ nhà ở xã hội CT-02 An Bình Tân",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711144/1Wupukykncwksdnvnxrb.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/chan-chinh-viec-xep-hang-qua-dem-nop-ho-so-nha-o-xa-hoi-ct-02-an-binh-tan-1711144.ldo",
                "date": "31/05/2026 20:02",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 17,
                "title": "Công an Khánh Hòa giám sát xét duyệt hồ sơ nhà ở xã hội An Bình Tân",
                "excerpt": "Công an Khánh Hòa giám sát xét duyệt hồ sơ nhà ở xã hội An Bình Tân",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/30/1710794/DJI_0895_11Zon.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/cong-an-khanh-hoa-giam-sat-xet-duyet-ho-so-nha-o-xa-hoi-an-binh-tan-1710794.ldo",
                "date": "30/05/2026 15:04",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 18,
                "title": "TPHCM dự chi hơn 9.800 tỉ đồng thu hồi đất làm Metro Bến Thành - Cần Giờ",
                "excerpt": "TPHCM dự chi hơn 9.800 tỉ đồng thu hồi đất làm Metro Bến Thành - Cần Giờ",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/29/1710453/Nguyen-Tat-Thanh.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/tphcm-du-chi-hon-9800-ti-dong-thu-hoi-dat-lam-metro-ben-thanh-can-gio-1710453.ldo",
                "date": "29/05/2026 20:18",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 19,
                "title": "Thanh niên công nhân sôi nổi tham gia sân chơi văn hóa tinh thần ở TPHCM",
                "excerpt": "Thanh niên công nhân sôi nổi tham gia sân chơi văn hóa tinh thần ở TPHCM",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1711578/Thanh-Nien-Cong-Nhan.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/cong-doan/thanh-nien-cong-nhan-soi-noi-tham-gia-san-choi-van-hoa-tinh-than-o-tphcm-1711578.ldo",
                "date": "01/06/2026 11:23",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Công đoàn"
                ],
                "category": "Công đoàn",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 20,
                "title": "Tặng quà cho 810 cháu thiếu nhi là con em công nhân lao động ở TPHCM",
                "excerpt": "Tặng quà cho 810 cháu thiếu nhi là con em công nhân lao động ở TPHCM",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711403/Tang-Qua-Thieu-Nhi-3.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/cong-doan/tang-qua-cho-810-chau-thieu-nhi-la-con-em-cong-nhan-lao-dong-o-tphcm-1711403.ldo",
                "date": "31/05/2026 18:38",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Công đoàn"
                ],
                "category": "Công đoàn",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 21,
                "title": "Khai thác hiệu quả tiềm năng du lịch đêm của TPHCM",
                "excerpt": "Khai thác hiệu quả tiềm năng du lịch đêm của TPHCM",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711253/Dem.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/video/khai-thac-hieu-qua-tiem-nang-du-lich-dem-cua-tphcm-1711253.ldo",
                "date": "31/05/2026 14:35",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Văn hóa - Giải trí"
                ],
                "category": "Văn hóa - Giải trí",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 22,
                "title": "Tiến Linh ghi bàn cuối trận, đội Công an TPHCM chia điểm với Thể Công Viettel",
                "excerpt": "Tiến Linh ghi bàn cuối trận, đội Công an TPHCM chia điểm với Thể Công Viettel",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711475/Cong-An-27-1.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/the-thao/tien-linh-ghi-ban-cuoi-tran-doi-cong-an-tphcm-chia-diem-voi-the-cong-viettel-1711475.ldo",
                "date": "31/05/2026 21:42",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Thể thao"
                ],
                "category": "Thể thao",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 23,
                "title": "Becamex TPHCM đua trụ hạng cùng Đà Nẵng và PVF-CAND",
                "excerpt": "Becamex TPHCM đua trụ hạng cùng Đà Nẵng và PVF-CAND",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711465/Bfc-2.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/the-thao/becamex-tphcm-dua-tru-hang-cung-da-nang-va-pvf-cand-1711465.ldo",
                "date": "31/05/2026 21:32",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Thể thao"
                ],
                "category": "Thể thao",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 24,
                "title": "Link xem trực tiếp bóng đá Công an Hà Nội vs Becamex TPHCM tại V.League",
                "excerpt": "Link xem trực tiếp bóng đá Công an Hà Nội vs Becamex TPHCM tại V.League",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711319/1920X1080-6.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bong-da/link-xem-truc-tiep-bong-da-cong-an-ha-noi-vs-becamex-tphcm-tai-vleague-1711319.ldo",
                "date": "31/05/2026 15:56",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Thể thao"
                ],
                "category": "Thể thao",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 25,
                "title": "TPHCM khôi phục tuyến tàu khách cao tốc đi Côn Đảo",
                "excerpt": "TPHCM khôi phục tuyến tàu khách cao tốc đi Côn Đảo",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1711671/1780285234711_177620.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/tphcm-khoi-phuc-tuyen-tau-khach-cao-toc-di-con-dao-1711671.ldo",
                "date": "01/06/2026 11:45",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 26,
                "title": "TPHCM xây dựng hệ sinh thái sản xuất - phân phối thực phẩm an toàn",
                "excerpt": "TPHCM xây dựng hệ sinh thái sản xuất - phân phối thực phẩm an toàn",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/29/1710107/Tickxanh2.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/kinh-doanh/tphcm-xay-dung-he-sinh-thai-san-xuat-phan-phoi-thuc-pham-an-toan-1710107.ldo",
                "date": "29/05/2026 11:04",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Kinh tế"
                ],
                "category": "Kinh tế",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 27,
                "title": "Cao tốc dài 45 km ở TPHCM phải giải phóng mặt bằng xong trước tháng 10.2026",
                "excerpt": "Cao tốc dài 45 km ở TPHCM phải giải phóng mặt bằng xong trước tháng 10.2026",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/28/1709446/Cao-Toc-TPHCM-37.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/cao-toc-dai-45-km-o-tphcm-phai-giai-phong-mat-bang-xong-truoc-thang-102026-1709446.ldo",
                "date": "28/05/2026 21:11",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 28,
                "title": "Chỉ đạo mới của UBND TPHCM về khu Mả Lạng và chợ Gà - Gạo",
                "excerpt": "Chỉ đạo mới của UBND TPHCM về khu Mả Lạng và chợ Gà - Gạo",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/28/1709450/Khu-Ma-Lang-3.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/chi-dao-moi-cua-ubnd-tphcm-ve-khu-ma-lang-va-cho-ga-gao-1709450.ldo",
                "date": "28/05/2026 09:29",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 29,
                "title": "TPHCM xây dựng đề án công nhận loại đô thị, thúc đẩy nâng cấp xã lên phường",
                "excerpt": "TPHCM xây dựng đề án công nhận loại đô thị, thúc đẩy nâng cấp xã lên phường",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/25/1708087/Can-Gio-Tphcm-3.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/tphcm-xay-dung-de-an-cong-nhan-loai-do-thi-thuc-day-nang-cap-xa-len-phuong-1708087.ldo",
                "date": "26/05/2026 15:39",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 30,
                "title": "3 phường ở TPHCM giải tỏa hơn 15.700 căn nhà, gấp rút xây 4.058 nhà tái định cư",
                "excerpt": "3 phường ở TPHCM giải tỏa hơn 15.700 căn nhà, gấp rút xây 4.058 nhà tái định cư",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/23/1706713/Kenh-Doi-Tphcm-3.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/3-phuong-o-tphcm-giai-toa-hon-15700-can-nha-gap-rut-xay-4058-nha-tai-dinh-cu-1706713.ldo",
                "date": "23/05/2026 11:50",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tphcm",
                "province_label": "TP.HCM",
                "tags": [
                        "TP.HCM",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_tphcm": true,
                "district": "TP.HCM"
        },
        {
                "id": 31,
                "title": "Đồng Nai khởi công xây mới tuyến đường dài hơn 42km trong tháng 6",
                "excerpt": "Đồng Nai khởi công xây mới tuyến đường dài hơn 42km trong tháng 6",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/2/1712133/San-Bay-Long-Thanh.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/dong-nai-khoi-cong-xay-moi-tuyen-duong-dai-hon-42km-trong-thang-6-1712133.ldo",
                "date": "02/06/2026 08:29",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 32,
                "title": "Mưa lớn kéo dài khiến nhiều tuyến đường ở Đồng Nai ngập sâu",
                "excerpt": "Mưa lớn kéo dài khiến nhiều tuyến đường ở Đồng Nai ngập sâu",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1712039/Ngap.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/mua-lon-keo-dai-khien-nhieu-tuyen-duong-o-dong-nai-ngap-sau-1712039.ldo",
                "date": "01/06/2026 19:41",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 33,
                "title": "Tăng tốc 180 ngày đêm hoàn thành và khai thác sân bay Long Thành",
                "excerpt": "Tăng tốc 180 ngày đêm hoàn thành và khai thác sân bay Long Thành",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1711990/Long-Thanh-3.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/tang-toc-180-ngay-dem-hoan-thanh-va-khai-thac-san-bay-long-thanh-1711990.ldo",
                "date": "01/06/2026 18:59",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 34,
                "title": "Nguyên nhân 250 tấn cá chết hàng loạt trên hồ Trị An ở Đồng Nai",
                "excerpt": "Nguyên nhân 250 tấn cá chết hàng loạt trên hồ Trị An ở Đồng Nai",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1711975/Ca-3.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/nguyen-nhan-250-tan-ca-chet-hang-loat-tren-ho-tri-an-o-dong-nai-1711975.ldo",
                "date": "01/06/2026 18:10",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 35,
                "title": "Đồng Nai công khai phương án bồi thường dự án mở rộng đường 25B",
                "excerpt": "Đồng Nai công khai phương án bồi thường dự án mở rộng đường 25B",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/1/1711957/25B.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/dong-nai-cong-khai-phuong-an-boi-thuong-du-an-mo-rong-duong-25b-1711957.ldo",
                "date": "01/06/2026 17:22",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 36,
                "title": "Đồng Nai thu hồi hơn 1.164 ha đất gần sân bay Long Thành",
                "excerpt": "Đồng Nai thu hồi hơn 1.164 ha đất gần sân bay Long Thành",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711321/Long-Thanh-4-01.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/dong-nai-thu-hoi-hon-1164-ha-dat-gan-san-bay-long-thanh-1711321.ldo",
                "date": "31/05/2026 16:01",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 37,
                "title": "Đồng Nai chuẩn bị khởi công nhà ở cho thuê quy mô lớn gần khu công nghiệp",
                "excerpt": "Đồng Nai chuẩn bị khởi công nhà ở cho thuê quy mô lớn gần khu công nghiệp",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/29/1710253/Nha-O-Xa-Hoi.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/dong-nai-chuan-bi-khoi-cong-nha-o-cho-thue-quy-mo-lon-gan-khu-cong-nghiep-1710253.ldo",
                "date": "29/05/2026 17:17",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 38,
                "title": "Đồng Nai công khai phương án bồi thường dự án mở rộng 9 km đường nối sân bay",
                "excerpt": "Đồng Nai công khai phương án bồi thường dự án mở rộng 9 km đường nối sân bay",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/26/1708505/25B-1.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/dong-nai-cong-khai-phuong-an-boi-thuong-du-an-mo-rong-9-km-duong-noi-san-bay-1708505.ldo",
                "date": "26/05/2026 15:57",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 39,
                "title": "Đồng Nai thu hồi đất ở siêu phường để thực hiện dự án khu đô thị 72.000 tỉ đồng",
                "excerpt": "Đồng Nai thu hồi đất ở siêu phường để thực hiện dự án khu đô thị 72.000 tỉ đồng",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/26/1708438/Hiep-Hoa.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/dong-nai-thu-hoi-dat-o-sieu-phuong-de-thuc-hien-du-an-khu-do-thi-72000-ti-dong-1708438.ldo",
                "date": "26/05/2026 14:48",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 40,
                "title": "Thu hồi 1.738 ha đất tại TPHCM, Đồng Nai, Tây Ninh làm đường lớn nhất Đông Nam Bộ",
                "excerpt": "Thu hồi 1.738 ha đất tại TPHCM, Đồng Nai, Tây Ninh làm đường lớn nhất Đông Nam Bộ",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/16/1703038/Vanh-Dai-4-TPHCM-16.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/thu-hoi-1738-ha-dat-tai-tphcm-dong-nai-tay-ninh-lam-duong-lon-nhat-dong-nam-bo-1703038.ldo",
                "date": "16/05/2026 19:02",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 41,
                "title": "Đề thi, đáp án môn Ngữ văn thi vào lớp 10 tại Tây Ninh năm 2026",
                "excerpt": "Đề thi, đáp án môn Ngữ văn thi vào lớp 10 tại Tây Ninh năm 2026",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/6/2/1712184/Thi-Lop-10-2019-64.jpeg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/giao-duc/de-thi-dap-an-mon-ngu-van-thi-vao-lop-10-tai-tay-ninh-nam-2026-1712184.ldo",
                "date": "02/06/2026 09:15",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tayninh",
                "province_label": "Tây Ninh",
                "tags": [
                        "Tây Ninh",
                        "Giáo dục"
                ],
                "category": "Giáo dục",
                "is_tayninh": true,
                "district": "Tây Ninh"
        },
        {
                "id": 42,
                "title": "Tin sáng 1.6: Dự án mở rộng Quốc lộ 50 nối TPHCM với Tây Ninh sắp về đích",
                "excerpt": "Tin sáng 1.6: Dự án mở rộng Quốc lộ 50 nối TPHCM với Tây Ninh sắp về đích",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711335/Tin-Sang-1.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/podcast-tin-tuc/tin-sang-16-du-an-mo-rong-quoc-lo-50-noi-tphcm-voi-tay-ninh-sap-ve-dich-1711335.ldo",
                "date": "01/06/2026 06:30",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tayninh",
                "province_label": "Tây Ninh",
                "tags": [
                        "Tây Ninh",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_tayninh": true,
                "district": "Tây Ninh"
        },
        {
                "id": 43,
                "title": "Nóng Sài Gòn: Tuyến đường gần 1.500 tỉ đồng nối TPHCM - Tây Ninh sắp về đích",
                "excerpt": "Nóng Sài Gòn: Tuyến đường gần 1.500 tỉ đồng nối TPHCM - Tây Ninh sắp về đích",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711312/Q1.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/video-xa-hoi/nong-sai-gon-tuyen-duong-gan-1500-ti-dong-noi-tphcm-tay-ninh-sap-ve-dich-1711312.ldo",
                "date": "31/05/2026 19:00",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tayninh",
                "province_label": "Tây Ninh",
                "tags": [
                        "Tây Ninh",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_tayninh": true,
                "district": "Tây Ninh"
        },
        {
                "id": 44,
                "title": "Tuyến đường gần 1.500 tỉ đồng nối TPHCM - Tây Ninh sắp về đích",
                "excerpt": "Tuyến đường gần 1.500 tỉ đồng nối TPHCM - Tây Ninh sắp về đích",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711138/Quoc-Lo-50-5.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/tuyen-duong-gan-1500-ti-dong-noi-tphcm-tay-ninh-sap-ve-dich-1711138.ldo",
                "date": "31/05/2026 11:49",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tayninh",
                "province_label": "Tây Ninh",
                "tags": [
                        "Tây Ninh",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_tayninh": true,
                "district": "Tây Ninh"
        },
        {
                "id": 45,
                "title": "TPHCM cấp bách xây 3 nút giao nghìn tỉ kết nối cao tốc Bến Lức - Long Thành",
                "excerpt": "TPHCM cấp bách xây 3 nút giao nghìn tỉ kết nối cao tốc Bến Lức - Long Thành",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/25/1707860/Nut-Giao-Rung-Sac-Ca.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/tphcm-cap-bach-xay-3-nut-giao-nghin-ti-ket-noi-cao-toc-ben-luc-long-thanh-1707860.ldo",
                "date": "25/05/2026 15:41",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tayninh",
                "province_label": "Tây Ninh",
                "tags": [
                        "Tây Ninh",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_tayninh": true,
                "district": "Tây Ninh"
        },
        {
                "id": 46,
                "title": "Tìm nguồn hơn 11,7 triệu mét khối cát cho dự án Vành đai 4 TPHCM đoạn qua Tây Ninh",
                "excerpt": "Tìm nguồn hơn 11,7 triệu mét khối cát cho dự án Vành đai 4 TPHCM đoạn qua Tây Ninh",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/25/1707857/Tay-Ninh-2.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/tim-nguon-hon-117-trieu-met-khoi-cat-cho-du-an-vanh-dai-4-tphcm-doan-qua-tay-ninh-1707857.ldo",
                "date": "25/05/2026 15:37",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tayninh",
                "province_label": "Tây Ninh",
                "tags": [
                        "Tây Ninh",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_tayninh": true,
                "district": "Tây Ninh"
        },
        {
                "id": 47,
                "title": "Tây Ninh lập điều chỉnh quy hoạch tỉnh đến năm 2030, tầm nhìn 2050",
                "excerpt": "Tây Ninh lập điều chỉnh quy hoạch tỉnh đến năm 2030, tầm nhìn 2050",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/4/28/1693064/Tay-Ninh-2.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/tay-ninh-lap-dieu-chinh-quy-hoach-tinh-den-nam-2030-tam-nhin-2050-1693064.ldo",
                "date": "28/04/2026 18:41",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "tayninh",
                "province_label": "Tây Ninh",
                "tags": [
                        "Tây Ninh",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_tayninh": true,
                "district": "Tây Ninh"
        },
        {
                "id": 48,
                "title": "Cá nuôi lồng bè chết trên hồ Trị An lên hơn 200 tấn",
                "excerpt": "Cá nuôi lồng bè chết trên hồ Trị An lên hơn 200 tấn",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/31/1711341/Ca-2.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/ca-nuoi-long-be-chet-tren-ho-tri-an-len-hon-200-tan-1711341.ldo",
                "date": "31/05/2026 16:35",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 49,
                "title": "Thành phố Đồng Nai phát triển nhà ở xã hội cho thuê gần các khu công nghiệp",
                "excerpt": "Thành phố Đồng Nai phát triển nhà ở xã hội cho thuê gần các khu công nghiệp",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/27/1709069/4-4.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/thanh-pho-dong-nai-phat-trien-nha-o-xa-hoi-cho-thue-gan-cac-khu-cong-nghiep-1709069.ldo",
                "date": "27/05/2026 14:39",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 50,
                "title": "Thành phố Đồng Nai động thổ xây dựng hơn 2.800 căn nhà ở",
                "excerpt": "Thành phố Đồng Nai động thổ xây dựng hơn 2.800 căn nhà ở",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/27/1708913/Bcons-Dn.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/thanh-pho-dong-nai-dong-tho-xay-dung-hon-2800-can-nha-o-1708913.ldo",
                "date": "27/05/2026 11:18",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 51,
                "title": "Công nhân ở Đồng Nai trúng thưởng nhẫn vàng, xe máy",
                "excerpt": "Công nhân ở Đồng Nai trúng thưởng nhẫn vàng, xe máy",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/30/1710946/Nhan-Vang.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/cong-doan/cong-nhan-o-dong-nai-trung-thuong-nhan-vang-xe-may-1710946.ldo",
                "date": "30/05/2026 18:22",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Công đoàn"
                ],
                "category": "Công đoàn",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 52,
                "title": "Đồng Nai quy hoạch khu đô thị ở cửa ngõ phía Tây sân bay Long Thành",
                "excerpt": "Đồng Nai quy hoạch khu đô thị ở cửa ngõ phía Tây sân bay Long Thành",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/12/1700680/San-Bay-Long-Thanh-1.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/dong-nai-quy-hoach-khu-do-thi-o-cua-ngo-phia-tay-san-bay-long-thanh-1700680.ldo",
                "date": "12/05/2026 16:32",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 53,
                "title": "75 căn hộ chung cư phục vụ công nhân ở Đồng Nai sắp mở bán",
                "excerpt": "75 căn hộ chung cư phục vụ công nhân ở Đồng Nai sắp mở bán",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/4/18/1687583/Chung-Cu-Cong-Nhan.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/bat-dong-san/75-can-ho-chung-cu-phuc-vu-cong-nhan-o-dong-nai-sap-mo-ban-1687583.ldo",
                "date": "18/04/2026 16:15",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Bất động sản"
                ],
                "category": "Bất động sản",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 54,
                "title": "Đồng Nai duyệt phương án bồi thường hỗ trợ 834 hộ dân dự án đường Vành đai 4",
                "excerpt": "Đồng Nai duyệt phương án bồi thường hỗ trợ 834 hộ dân dự án đường Vành đai 4",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/5/30/1710933/Cau-Thu-Bien.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/dong-nai-duyet-phuong-an-boi-thuong-ho-tro-834-ho-dan-du-an-duong-vanh-dai-4-1710933.ldo",
                "date": "30/05/2026 19:14",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 55,
                "title": "Doanh nghiệp mong muốn thành phố Đồng Nai đầu tư đồng bộ hạ tầng logistics",
                "excerpt": "Doanh nghiệp mong muốn thành phố Đồng Nai đầu tư đồng bộ hạ tầng logistics",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/4/25/1691565/Cang-Phuoc-An-Dn.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/kinh-doanh/doanh-nghiep-mong-muon-thanh-pho-dong-nai-dau-tu-dong-bo-ha-tang-logistics-1691565.ldo",
                "date": "25/04/2026 16:57",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Kinh tế"
                ],
                "category": "Kinh tế",
                "is_dongnai": true,
                "district": "Đồng Nai"
        },
        {
                "id": 56,
                "title": "Sân bay Long Thành tuyển lao động đến hết năm 2026 với mức lương hấp dẫn",
                "excerpt": "Sân bay Long Thành tuyển lao động đến hết năm 2026 với mức lương hấp dẫn",
                "image": "https://media-cdn-v2.laodong.vn/storage/newsportal/2026/4/21/1689070/San-Bay-13.jpg?w=800&amp;h=420&amp;crop=auto&amp;scale=both",
                "url": "https://laodong.vn/xa-hoi/san-bay-long-thanh-tuyen-lao-dong-den-het-nam-2026-voi-muc-luong-hap-dan-1689070.ldo",
                "date": "21/04/2026 14:23",
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "province": "dongnai",
                "province_label": "Đồng Nai",
                "tags": [
                        "Đồng Nai",
                        "Xã hội"
                ],
                "category": "Xã hội",
                "is_dongnai": true,
                "district": "Đồng Nai"
        }
];
    let tphcmArticles = [...originalTphcmArticles];

    // Helper to safely fetch articles from the filtered list (looping if we run out)
    function getSafeArticle(pool, index, globalFallbackIndex) {
        if (pool && pool.length > 0) {
            return pool[index % pool.length];
        }
        return originalTphcmArticles[globalFallbackIndex % originalTphcmArticles.length];
    }

    let featuredArticleId = tphcmArticles[0].id;
    let articlesVolume = 120;
    let isIndexedStatus = true;

    function toggleDevConsole() {
        const drawer = document.getElementById('dev-console-drawer');
        drawer.style.display = drawer.style.display === 'none' || drawer.style.display === '' ? 'flex' : 'none';
    }

    function populateCuratorOptions() {
        const select = document.getElementById('curator-select');
        select.innerHTML = '';
        tphcmArticles.forEach(a => {
            const opt = document.createElement('option');
            opt.value = a.id;
            opt.innerText = a.title.substring(0, 50) + "...";
            select.appendChild(opt);
        });
    }

    function renderMainCover() {
        const centerArt = tphcmArticles.find(a => a.id === featuredArticleId) || getSafeArticle(tphcmArticles, 0, 0);
        const pool = tphcmArticles.filter(a => a.id !== centerArt.id);
        const sub1 = getSafeArticle(pool, 0, 1);
        const sub2 = getSafeArticle(pool, 1, 2);
        const sub3 = getSafeArticle(pool, 2, 3);
        const spot1 = getSafeArticle(pool, 3, 4);
        const spot2 = getSafeArticle(pool, 4, 5);
        const spot3 = getSafeArticle(pool, 5, 6);
        const spot4 = getSafeArticle(pool, 6, 7);

        displayedIds.add(centerArt.id);
        displayedIds.add(sub1.id); displayedIds.add(sub2.id); displayedIds.add(sub3.id);
        displayedIds.add(spot1.id); displayedIds.add(spot2.id); displayedIds.add(spot3.id); displayedIds.add(spot4.id);

        document.getElementById('main-cover-container').innerHTML = `
            <article class="v4 cv-001 hero-main-article" style="display: block;">
                <a class="link-img" href="` + centerArt.url + `" target="_blank">
                    <figure class="_thumb" style="margin-bottom: 12px; width: 100%;">
                        <img src="` + centerArt.image + `" class="img-art" alt="` + centerArt.title + `" style="width: 100%; border-radius: 6px; aspect-ratio: 16/9; object-fit: cover;">
                    </figure>
                </a>
                <a class="link-title" href="` + centerArt.url + `" target="_blank" style="text-decoration: none;">
                    <h2 class="title cover prefix-icon" style="font-size: 26px; line-height: 1.3; margin-bottom: 10px; font-weight: 800; color: #111; letter-spacing: -0.5px;">` + centerArt.title + `</h2>
                </a>
                <div class="chapeau ellipsis fade-out" style="font-size: 14.5px; line-height: 1.5; color: #444; -webkit-line-clamp: 4; display: -webkit-box; -webkit-box-orient: vertical; overflow: hidden;">` + centerArt.excerpt + `</div>
            </article>
        `;

        document.getElementById('subcover-bottom-row').innerHTML = `
            ${[sub1, sub2, sub3].map(art => `
                <article class="v4 p2c" style="display: flex; flex-direction: column; gap: 8px;">
                    <a class="link-img" href="${art.url}" target="_blank">
                        <figure class="_thumb" style="margin: 0; width: 100%;">
                            <img src="${art.image}" class="img-art" alt="${art.title}" style="width: 100%; aspect-ratio: 16/10; object-fit: cover; border-radius: 4px;">
                        </figure>
                    </a>
                    <a class="link-title" href="${art.url}" target="_blank" style="text-decoration: none;">
                        <h2 class="title prefix-icon" style="font-size: 14.5px; line-height: 1.3; font-weight: 700; color: #111; margin: 0; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">${art.title}</h2>
                    </a>
                </article>
            `).join('')}
        `;

        const spotStyles = ['border-bottom: 1px dashed #ddd; padding-bottom: 15px; margin-bottom: 15px;','border-bottom: 1px dashed #ddd; padding-bottom: 15px; margin-bottom: 15px;','border-bottom: 1px dashed #ddd; padding-bottom: 15px; margin-bottom: 15px;',''];
        document.getElementById('spotlight-container').innerHTML = `
            ${[spot1, spot2, spot3, spot4].map((art, i) => `
                <article class="v4 p2c" style="display: flex; gap: 12px; align-items: flex-start; ${spotStyles[i]}">
                    <a class="link-img" href="${art.url}" target="_blank" style="flex: 0 0 110px;">
                        <img src="${art.image}" class="img-art" alt="${art.title}" style="width: 110px; height: 82px; object-fit: cover; border-radius: 4px;">
                    </a>
                    <a class="link-title" href="${art.url}" target="_blank" style="text-decoration: none; flex: 1;">
                        <h2 class="title prefix-icon" style="font-size: 13.5px; line-height: 1.4; color: #111; font-weight: bold; margin: 0; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden;">${art.title}</h2>
                    </a>
                </article>
            `).join('')}
        `;
    }

    function renderMediaSection() {
        let mediaPool = tphcmArticles.filter(a => a.category === "Xã hội" || a.category === "Thời sự").slice(5, 11);
        if (mediaPool.length < 6) {
            mediaPool = originalTphcmArticles.filter(a => a.category === "Xã hội" || a.category === "Thời sự").slice(5, 11);
        }
        if (mediaPool.length < 6) return;

        document.getElementById('media-col-1').innerHTML = `
            <div style="background-color:#ffffff; border:1px solid #ddd; border-radius:4px; padding:10px; display:flex; gap:10px;">
                <div style="width:100px; height:65px; overflow:hidden; border-radius:3px; flex-shrink:0; position:relative;">
                    <img src="` + mediaPool[0].image + `" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; bottom:3px; left:3px; color:red; font-size:12px;"><i class="fa fa-video-camera"></i></div>
                </div>
                <a href="` + mediaPool[0].url + `" target="_blank" style="text-decoration:none; font-size:12px; font-weight:bold; color:#111; line-height:1.3; display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical; overflow:hidden;">` + mediaPool[0].title + `</a>
            </div>
            <div style="background-color:#ffffff; border:1px solid #ddd; border-radius:4px; padding:10px; display:flex; gap:10px;">
                <div style="width:100px; height:65px; overflow:hidden; border-radius:3px; flex-shrink:0; position:relative;">
                    <img src="` + mediaPool[1].image + `" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; bottom:3px; left:3px; color:red; font-size:12px;"><i class="fa fa-video-camera"></i></div>
                </div>
                <a href="` + mediaPool[1].url + `" target="_blank" style="text-decoration:none; font-size:12px; font-weight:bold; color:#111; line-height:1.3; display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical; overflow:hidden;">` + mediaPool[1].title + `</a>
            </div>
            <div style="background-color:#ffffff; border:1px solid #ddd; border-radius:4px; padding:10px; display:flex; gap:10px;">
                <div style="width:100px; height:65px; overflow:hidden; border-radius:3px; flex-shrink:0; position:relative;">
                    <img src="` + mediaPool[2].image + `" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; bottom:3px; left:3px; color:red; font-size:12px;"><i class="fa fa-video-camera"></i></div>
                </div>
                <a href="` + mediaPool[2].url + `" target="_blank" style="text-decoration:none; font-size:12px; font-weight:bold; color:#111; line-height:1.3; display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical; overflow:hidden;">` + mediaPool[2].title + `</a>
            </div>
        `;
        
        document.getElementById('media-col-2').innerHTML = `
            <div style="background-color:#ffffff; border:1px solid #ddd; border-radius:4px; padding:10px; display:flex; gap:10px;">
                <div style="width:100px; height:65px; overflow:hidden; border-radius:3px; flex-shrink:0; position:relative;">
                    <img src="` + mediaPool[3].image + `" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; bottom:3px; left:3px; color:red; font-size:12px;"><i class="fa fa-video-camera"></i></div>
                </div>
                <a href="` + mediaPool[3].url + `" target="_blank" style="text-decoration:none; font-size:12px; font-weight:bold; color:#111; line-height:1.3; display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical; overflow:hidden;">` + mediaPool[3].title + `</a>
            </div>
            <div style="background-color:#ffffff; border:1px solid #ddd; border-radius:4px; padding:10px; display:flex; gap:10px;">
                <div style="width:100px; height:65px; overflow:hidden; border-radius:3px; flex-shrink:0; position:relative;">
                    <img src="` + mediaPool[4].image + `" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; bottom:3px; left:3px; color:red; font-size:12px;"><i class="fa fa-video-camera"></i></div>
                </div>
                <a href="` + mediaPool[4].url + `" target="_blank" style="text-decoration:none; font-size:12px; font-weight:bold; color:#111; line-height:1.3; display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical; overflow:hidden;">` + mediaPool[4].title + `</a>
            </div>
            <div style="background-color:#ffffff; border:1px solid #ddd; border-radius:4px; padding:10px; display:flex; gap:10px;">
                <div style="width:100px; height:65px; overflow:hidden; border-radius:3px; flex-shrink:0; position:relative;">
                    <img src="` + mediaPool[5].image + `" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; bottom:3px; left:3px; color:red; font-size:12px;"><i class="fa fa-video-camera"></i></div>
                </div>
                <a href="` + mediaPool[5].url + `" target="_blank" style="text-decoration:none; font-size:12px; font-weight:bold; color:#111; line-height:1.3; display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical; overflow:hidden;">` + mediaPool[5].title + `</a>
            </div>
        `;
        
        let activeIdx = 0;
        setInterval(() => {
            activeIdx = (activeIdx + 1) % mediaPool.length;
            document.getElementById('tv-player-img').src = mediaPool[activeIdx].image;
        }, 5000);
    }

    function renderCategoryColumns() {
        const row1Categories = ["Thời sự", "Xã hội", "Giáo dục", "Kinh tế"];
        const row2Categories = ["Công đoàn", "Bất động sản", "Văn hóa - Giải trí", "Thể thao"];

        function makeColumnHtml(categoryName) {
            let catPool = tphcmArticles.filter(a => a.category === categoryName);
            if (catPool.length < 5) {
                // Only fall back to articles within the filtered province to prevent leakage
                const generalCatPool = tphcmArticles;
                catPool = catPool.concat(generalCatPool.filter(ga => !catPool.some(ca => ca.id === ga.id))).slice(0, 5);
            }
            const mainCat = getSafeArticle(catPool, 0, 12);
            const secondaryList = catPool.slice(1, 5);
            
            let listHtml = '';
            secondaryList.forEach(item => {
                listHtml += `
                    <div class="category-list-item">
                        <a href="` + item.url + `" target="_blank" style="width: 50px; height: 35px; overflow:hidden; display:block; flex-shrink:0; border-radius: 2px;">
                            <img src="` + item.image + `" style="width:100%; height:100%; object-fit:cover;">
                        </a>
                        <a href="` + item.url + `" target="_blank" class="category-list-link" style="display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical; overflow:hidden; flex-grow: 1;">` + item.title + `</a>
                    </div>
                `;
            });
            
            return `
                <div class="category-card">
                    <div class="category-header">
                        <span>` + categoryName + `</span>
                        <span>&gt;</span>
                    </div>
                    <a href="` + mainCat.url + `" target="_blank" style="display:block; overflow:hidden; height:120px; border-radius:6px; flex-shrink: 0; margin-bottom: 8px;">
                        <img src="` + mainCat.image + `" style="width:100%; height:100%; object-fit:cover; transition:transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
                    </a>
                    <a href="` + mainCat.url + `" target="_blank" style="text-decoration:none; display:block; margin-bottom:10px; flex-shrink: 0;">
                        <h4 class="category-title">` + mainCat.title + `</h4>
                    </a>
                    <div style="display:flex; flex-direction:column; gap:4px; margin-top:auto;">
                        ` + listHtml + `
                    </div>
                </div>
            `;
        }

        let row1Html = '';
        row1Categories.forEach(cat => { row1Html += makeColumnHtml(cat); });
        document.getElementById('categories-grid-row1').innerHTML = row1Html;

        let row2Html = '';
        row2Categories.forEach(cat => { row2Html += makeColumnHtml(cat); });
        document.getElementById('categories-grid-row2').innerHTML = row2Html;
    }

    function renderEnterpriseBlock() {
        let prPool = tphcmArticles.filter(a => a.category === "Kinh tế").slice(0, 5);
        if (prPool.length < 5) {
            const generalPrPool = tphcmArticles.filter(a => a.category === "Kinh tế");
            prPool = prPool.concat(generalPrPool.filter(gp => !prPool.some(p => p.id === gp.id))).slice(0, 5);
        }
        let html = '';
        
        prPool.forEach(item => {
            html += `
                <div style="background-color:#ffffff; border:1px solid #e3e3e3; padding:10px; border-radius:4px; display:flex; flex-direction:column; justify-content:space-between; min-height: 150px;">
                    <a href="` + item.url + `" target="_blank" style="display:block; height:90px; overflow:hidden; border-radius:2px;">
                        <img src="` + item.image + `" style="width:100%; height:100%; object-fit:cover;">
                    </a>
                    <a href="` + item.url + `" target="_blank" style="text-decoration:none; display:block; margin-top:8px;">
                        <h5 style="margin:0; font-size:11.5px; font-weight:bold; color:#111; line-height:1.4; display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical; overflow:hidden;">` + item.title + `</h5>
                    </a>
                </div>
            `;
        });
        document.getElementById('enterprise-grid-container').innerHTML = html;
    }

    function pinFeaturedStory(idStr) {
        featuredArticleId = parseInt(idStr);
        renderMainCover();
        updateSchemaMarkup();
    }

    function updateThresholdDemo(val) {
        articlesVolume = parseInt(val);
        document.getElementById('threshold-val').innerText = val + " bài/tháng";
        const badge = document.getElementById('index-badge-status');
        if (articlesVolume >= 100) {
            isIndexedStatus = true;
            badge.innerText = "INDEXED";
            badge.style.backgroundColor = "#28a745";
        } else {
            isIndexedStatus = false;
            badge.innerText = "NOINDEX";
            badge.style.backgroundColor = "#6c757d";
        }
        updateSchemaMarkup();
    }

    function updateSchemaMarkup() {
        const curFeatured = tphcmArticles.find(a => a.id === featuredArticleId) || tphcmArticles[0];
        const schema = {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "Lao Động TP.HCM & Đông Nam Bộ - Trang tin tức vùng Đông Nam Bộ",
            "url": "https://laodong.vn/vung-mien/tphcm-va-dong-nam-bo/",
            "description": "Trang tin tức của Báo Lao Động về TP.HCM & Đông Nam Bộ, cập nhật tin thời sự, xã hội, công đoàn.",
            "isPartOf": {
                "@type": "WebSite",
                "name": "Báo Lao Động",
                "url": "https://laodong.vn"
            },
            "breadcrumb": {
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
                        "name": "TP.HCM & Đông Nam Bộ",
                        "item": "https://laodong.vn/vung-mien/tphcm-va-dong-nam-bo/"
                    }
                ]
            },
            "publishingPolicy": {
                "active_robots_meta": isIndexedStatus ? "index, follow" : "noindex, follow",
                "monthly_articles_count": articlesVolume,
                "indexing_threshold_required": 100
            },
            "mainEntity": {
                "@type": "NewsArticle",
                "headline": curFeatured.title,
                "url": curFeatured.url,
                "datePublished": curFeatured.date,
                "publisher": {
                    "@type": "NewsMediaOrganization",
                    "name": "Báo Lao Động",
                    "logo": "https://media-cdn-v2.laodong.vn/laodong-logo.png"
                }
            }
        };
        document.getElementById('json-schema-output').innerText = JSON.stringify(schema, null, 2);
    }

    function fetchTPHCMWeather(lat = 10.7769, lon = 106.7009, name = "TP.HCM & Đông Nam Bộ") {
        const options = { weekday: 'long', year: 'numeric', month: '2-digit', day: '2-digit' };
        const today = new Date();
        document.getElementById('current-date-vietnam').innerText = today.toLocaleDateString('vi-VN', options);

        const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=temperature_2m,relative_humidity_2m,weather_code`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                if (data && data.current) {
                    const temp = Math.round(data.current.temperature_2m);
                    const humidity = data.current.relative_humidity_2m;
                    const code = data.current.weather_code;
                    
                    let condition = "Trời nhiều mây";
                    let emoji = "⛅";
                    
                    if (code === 0) { condition = "Trời quang"; emoji = "☀️"; }
                    else if (code >= 1 && code <= 3) { condition = "Ít mây / Nhiều mây"; emoji = "⛅"; }
                    else if (code >= 45 && code <= 48) { condition = "Sương mù"; emoji = "🌫️"; }
                    else if (code >= 51 && code <= 55) { condition = "Mưa phùn"; emoji = "🌧️"; }
                    else if (code >= 61 && code <= 65) { condition = "Có mưa"; emoji = "🌧️"; }
                    else if (code >= 80 && code <= 82) { condition = "Mưa rào"; emoji = "🌦️"; }
                    else if (code >= 95) { condition = "Có giông bão"; emoji = "⛈️"; }
                    
                    document.getElementById('weather-temp-span').innerHTML = `
                        ${name}: ${emoji} <strong>${temp}°C</strong> (${condition}) <span style="font-weight: normal; color: #666; margin-left: 5px;">💧 ${humidity}% ẩm</span>
                    `;
                }
            })
            .catch(err => {
                console.error("Lỗi khi tải thời tiết:", err);
                document.getElementById('weather-temp-span').innerHTML = `${name}: ⛅ 28°C`;
            });
    }

    const provincialProfiles = {
        all: {
            title: "TP.HCM & ĐÔNG NAM BỘ - ĐẦU TÀU KINH TẾ",
            profileHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Tổng diện tích:</strong> 23.590 km² (Khu vực Đông Nam Bộ)<br>
                    • <strong>Tổng dân số:</strong> 18.5 triệu người (Vùng công nghiệp lớn nhất cả nước)<br>
                    • <strong>Quy mô kinh tế:</strong> Đóng góp khoảng 30% GDP và hơn 40% ngân sách quốc gia.<br>
                    • <strong>Khu công nghiệp (KCN):</strong> Trên 80 KCN tập trung, thu hút dòng vốn FDI hàng đầu.
                </div>
            `,
            indicatorHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Năng lực cạnh tranh (PCI):</strong> Dẫn đầu cả nước (Bà Rịa - Vũng Tàu, TP.HCM, Bình Dương nằm trong nhóm Rất tốt/Tốt).<br>
                    • <strong>Hiệu quả quản trị hành chính công (PAPI):</strong> Đa số các tỉnh nằm trong nhóm Trung bình Cao trở lên.<br>
                    • <strong>Thế mạnh:</strong> Hạ tầng kết nối cảng biển nước sâu, logistics quốc tế, công nghệ cao, thu hút đầu tư nước ngoài.
                </div>
            `
        },
        tphcm: {
            title: "TP. HỒ CHÍ MINH - ĐÔ THỊ ĐẶC BIỆT",
            profileHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Diện tích:</strong> 2.061 km² (Trung tâm kinh tế, văn hóa cả nước)<br>
                    • <strong>Dân số thực tế:</strong> Hơn 9.4 triệu người (Mật độ dân số cao nhất cả nước)<br>
                    • <strong>Quy mô kinh tế (GRDP):</strong> Dẫn đầu cả nước, chiếm tỷ trọng cao nhất trong các vùng kinh tế.<br>
                    • <strong>Hạ tầng công nghiệp:</strong> 17 khu chế xuất, khu công nghiệp và khu công nghệ cao Thủ Đức.
                </div>
            `,
            indicatorHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Chỉ số cạnh tranh cấp tỉnh (PCI 2025):</strong> Hạng 15/63 tỉnh thành (68.45 điểm) - Nhóm Tốt.<br>
                    • <strong>Chỉ số hiệu quả quản trị (PAPI):</strong> Nằm trong nhóm Cao (Đánh giá tốt về cung ứng dịch vụ công).<br>
                    • <strong>Cải cách hành chính (PAR Index):</strong> Xếp hạng 5 cả nước.<br>
                    • <strong>Khuyến nghị cải thiện:</strong> Thủ tục tiếp cận đất đai cho DN, giảm thời gian giải quyết hồ sơ quy hoạch, giảm ùn tắc giao thông đô thị.
                </div>
            `
        },
        dongnai: {
            title: "TỈNH ĐỒNG NAI - THỦ PHỦ CÔNG NGHIỆP MIỀN NAM",
            profileHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Diện tích:</strong> 5.907 km² (Cửa ngõ kết nối Nam Trung Bộ và Tây Nguyên)<br>
                    • <strong>Dân số:</strong> 3.3 triệu người (Hạng 2 toàn khu vực miền Nam)<br>
                    • <strong>Quy mô kinh tế (GRDP):</strong> Nền kinh tế quy mô công nghiệp chế biến, chế tạo trọng điểm.<br>
                    • <strong>Khu công nghiệp (KCN):</strong> 32 KCN đang hoạt động (Khu vực Biên Hòa, Long Thành, Nhơn Trạch, Trảng Bom).
                </div>
            `,
            indicatorHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Chỉ số cạnh tranh cấp tỉnh (PCI 2025):</strong> Hạng 22/63 tỉnh thành (66.50 điểm) - Nhóm Khá.<br>
                    • <strong>Chỉ số hiệu quả quản trị (PAPI):</strong> Nhóm Trung bình Cao.<br>
                    • <strong>Cải cách hành chính (PAR Index):</strong> Xếp thứ 18 toàn quốc.<br>
                    • <strong>Khuyến nghị cải thiện:</strong> Rút ngắn "Chi phí thời gian" thực hiện thủ tục hành chính, tối ưu quy trình cấp phép xây dựng cho dự án FDI.
                </div>
            `
        },
        tayninh: {
            title: "TỈNH TÂY NINH - CỬA NGÕ GIAO THƯƠNG ĐÔNG TÂY",
            profileHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Diện tích:</strong> 4.041 km² (Giáp ranh trực tiếp vương quốc Campuchia)<br>
                    • <strong>Dân số:</strong> 1.2 triệu người (Mật độ dân số ở mức vừa phải)<br>
                    • <strong>Đặc thù kinh tế:</strong> Nông nghiệp công nghệ cao kết hợp du lịch tâm linh di tích quốc gia Núi Bà Đen.<br>
                    • <strong>Khu công nghiệp (KCN):</strong> 6 KCN quy mô lớn (KCN Phước Đông, KCN Trảng Bàng).
                </div>
            `,
            indicatorHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Chỉ số cạnh tranh cấp tỉnh (PCI 2025):</strong> Hạng 19/63 tỉnh thành (67.10 điểm) - Nhóm Khá.<br>
                    • <strong>Chỉ số hiệu quả quản trị (PAPI):</strong> Nhóm Trung bình Thấp.<br>
                    • <strong>Cải cách hành chính (PAR Index):</strong> Xếp thứ 25 toàn quốc.<br>
                    • <strong>Khuyến nghị cải thiện:</strong> Nâng cao hiệu quả chính sách "Hỗ trợ doanh nghiệp", tăng tính công khai minh bạch thông tin quy hoạch sử dụng đất đai.
                </div>
            `
        }
    };

    function updateProvincialProfileWidget(province) {
        const widget = document.getElementById('provincial-profile-widget');
        if (!widget) return;
        const profile = provincialProfiles[province] || provincialProfiles.all;
        
        widget.innerHTML = `
            <div style="border-right: 1px solid #eee; padding-right: 20px;">
                <h4 style="margin: 0 0 10px 0; font-size: 12px; font-weight: bold; color: #002d62; text-transform: uppercase; letter-spacing: 0.5px; display: flex; align-items: center; gap: 4px;">
                    📌 ${profile.title}
                </h4>
                ${profile.profileHtml}
            </div>
            <div>
                <h4 style="margin: 0 0 10px 0; font-size: 12px; font-weight: bold; color: #c00000; text-transform: uppercase; letter-spacing: 0.5px; display: flex; align-items: center; gap: 4px;">
                    📊 CHỈ SỐ CẢI CÁCH & CẠNH TRANH CHÍNH THỐNG
                </h4>
                ${profile.indicatorHtml}
            </div>
        `;
    }

    function openSchemaModal() {
        document.getElementById('schema-modal').style.display = 'flex';
        updateSchemaMarkup();
    }
    function closeSchemaModal() {
        document.getElementById('schema-modal').style.display = 'none';
    }

    window.toggleProvincialProfile = function() {
        const widget = document.getElementById('provincial-profile-widget');
        const icon = document.getElementById('profile-toggle-icon');
        if (widget.style.display === 'none' || widget.style.display === '') {
            widget.style.display = 'grid';
            icon.innerText = 'Thu gọn ▴';
        } else {
            widget.style.display = 'none';
            icon.innerText = 'Mở rộng ▾';
        }
    }

    window.filterSpokeProvince = function(province) {
        const tabs = document.querySelectorAll('#hub-spoke-tabs .item');
        tabs.forEach(tab => {
            tab.style.color = '#555';
            tab.style.fontWeight = 'normal';
            tab.style.borderBottom = 'none';
            tab.classList.remove('active');
        });
        
        const eventTarget = window.event ? window.event.target : null;
        if (eventTarget) {
            eventTarget.style.color = '#c00000';
            eventTarget.style.fontWeight = 'bold';
            eventTarget.style.borderBottom = '2px solid #c00000';
            eventTarget.classList.add('active');
        }

        const pageTitle = document.getElementById('dynamic-page-title');
        if (province === 'all') {
            tphcmArticles = [...originalTphcmArticles];
            if (pageTitle) pageTitle.innerText = "TP.HCM & Đông Nam Bộ";
            document.getElementById('dynamic-breadcrumb-spoke').innerHTML = 'TP.HCM & Đông Nam Bộ';
            document.getElementById('dynamic-powercut-link').href = 'https://laodong.vn/tags/lich-cat-dien-tphcm-8542.ldo';
            document.getElementById('tphcm-weather-widget').href = 'https://weather.com/vi-VN/weather/today/l/VMXX0007:1:VM';
            fetchTPHCMWeather(10.7769, 106.7009, 'TP.HCM & Đông Nam Bộ');
        } else if (province === 'tphcm') {
            tphcmArticles = originalTphcmArticles.filter(a => a.is_tphcm);
            if (pageTitle) pageTitle.innerText = "TP. Hồ Chí Minh";
            document.getElementById('dynamic-breadcrumb-spoke').innerHTML = `<a href="#" onclick="filterSpokeProvince('all')" style="color: #666666; text-decoration: none;">TP.HCM & Đông Nam Bộ</a> <span style="color: #ccc;">/</span> TP. Hồ Chí Minh`;
            document.getElementById('dynamic-powercut-link').href = 'https://laodong.vn/tags/lich-cat-dien-tphcm-8542.ldo';
            document.getElementById('tphcm-weather-widget').href = 'https://weather.com/vi-VN/weather/today/l/VMXX0007:1:VM';
            fetchTPHCMWeather(10.7769, 106.7009, 'TP. Hồ Chí Minh');
        } else if (province === 'dongnai') {
            tphcmArticles = originalTphcmArticles.filter(a => a.is_dongnai);
            if (pageTitle) pageTitle.innerText = "Tỉnh Đồng Nai";
            document.getElementById('dynamic-breadcrumb-spoke').innerHTML = `<a href="#" onclick="filterSpokeProvince('all')" style="color: #666666; text-decoration: none;">TP.HCM & Đông Nam Bộ</a> <span style="color: #ccc;">/</span> Đồng Nai`;
            document.getElementById('dynamic-powercut-link').href = 'https://laodong.vn/tags/lich-cat-dien-dong-nai-8588.ldo';
            document.getElementById('tphcm-weather-widget').href = 'https://weather.com/vi-VN/weather/today/l/VMXX0004:1:VM';
            fetchTPHCMWeather(10.9575, 106.8427, 'Đồng Nai');
        } else if (province === 'tayninh') {
            tphcmArticles = originalTphcmArticles.filter(a => a.is_tayninh);
            if (pageTitle) pageTitle.innerText = "Tỉnh Tây Ninh";
            document.getElementById('dynamic-breadcrumb-spoke').innerHTML = `<a href="#" onclick="filterSpokeProvince('all')" style="color: #666666; text-decoration: none;">TP.HCM & Đông Nam Bộ</a> <span style="color: #ccc;">/</span> Tây Ninh`;
            document.getElementById('dynamic-powercut-link').href = 'https://laodong.vn/tags/lich-cat-dien-tay-ninh-8622.ldo';
            document.getElementById('tphcm-weather-widget').href = 'https://weather.com/vi-VN/weather/today/l/VMXX0030:1:VM';
            fetchTPHCMWeather(11.3121, 106.1009, 'Tây Ninh');
        }

        updateProvincialProfileWidget(province);
        featuredArticleId = getSafeArticle(tphcmArticles, 0, 0).id;
        
        populateCuratorOptions();
        renderMainCover();
        renderMediaSection();
        renderCategoryColumns();
        renderEnterpriseBlock();
        updateSchemaMarkup();
        
        if (window.switchMostReadSlide) {
            window.switchMostReadSlide(0);
        }
    };

    function initInfraCarouselAutoplay() {
        const carousel = document.querySelector('.infra-carousel-container');
        if (!carousel) return;
        let slideIndex = 0;
        
        setInterval(() => {
            const cards = carousel.querySelectorAll('.infra-carousel-card');
            if (cards.length <= 1) return;
            slideIndex = (slideIndex + 1) % cards.length;
            const cardWidth = cards[0].offsetWidth + 12; // width + gap
            carousel.scrollTo({
                left: cardWidth * slideIndex,
                behavior: 'smooth'
            });
        }, 5000);
    }

    const directoryListings = [
        { name: "Nha khoa Quốc tế Sài Gòn", address: "189 Nguyễn Thị Minh Khai, Quận 1", phone: "0988.xxx.xxx" },
        { name: "Trung tâm Gia sư Sư phạm thủ khoa TPHCM", address: "290 Điện Biên Phủ, Bình Thạnh", phone: "0912.xxx.xxx" },
        { name: "Gốm sứ Bình Dương Minh Long chính gốc", address: "12 Đại lộ Bình Dương, Thuận An", phone: "0945.xxx.xxx" },
        { name: "Cứu hộ Giao thông Đông Nam Bộ 24/7 (Thủ Đức - Biên Hòa)", address: "102 Xa lộ Hà Nội, Thủ Đức", phone: "0904.xxx.xxx" },
        { name: "Trường Dạy nghề ẩm thực & pha chế Netspace", address: "30 Nguyễn Văn Thủ, Quận 1", phone: "0916.xxx.xxx" },
        { name: "Viện Thẩm mỹ Công nghệ cao SeoulCenter", address: "375 Nguyễn Thượng Hiền, Quận 10", phone: "0989.xxx.xxx" },
        { name: "Phòng khám Đông y gia truyền Vạn An Đường", address: "Trần Hưng Đạo, Quận 5", phone: "0973.xxx.xxx" },
        { name: "Gói vay ưu đãi hộ kinh doanh - HDBank Quận 1", address: "Nguyễn Thị Minh Khai, Quận 1", phone: "0903.xxx.xxx" },
        { name: "Sửa chữa máy tính & Laptop lấy ngay Phong Vũ", address: "264 Nguyễn Thị Minh Khai, Quận 3", phone: "0985.xxx.xxx" },
        { name: "Thiết kế thi công nội thất hiện đại Lộc Phát", address: "32 Song Hành, Quận 2", phone: "0942.xxx.xxx" },
        { name: "Nhà hàng chay Mandala Quận 1", address: "110 Sương Nguyệt Ánh, Quận 1", phone: "0967.xxx.xxx" },
        { name: "Cửa hàng hoa tươi Sài Gòn Flower", address: "45 Hồ Thị Kỷ, Quận 10", phone: "0918.xxx.xxx" },
        { name: "Giặt ủi công nghiệp siêu tốc Quận 7", address: "12 Nguyễn Thị Thập, Quận 7", phone: "0936.xxx.xxx" },
        { name: "Nha khoa nụ cười duyên (Smile Dental)", address: "321 Nguyễn Tri Phương, Quận 10", phone: "0977.xxx.xxx" },
        { name: "Sửa xe máy phân khối lớn & tay ga Gia Huy", address: "88 Ung Văn Khiêm, Bình Thạnh", phone: "0909.xxx.xxx" },
        { name: "Vận tải & chuyển nhà trọn gói Thành Hưng Sài Gòn", address: "40/12 Võ Thị Sáu, Quận 1", phone: "0915.xxx.xxx" },
        { name: "Đại lý vé máy bay & du lịch Saigontourist", address: "45 Lê Lợi, Quận 1", phone: "0981.xxx.xxx" },
        { name: "Phòng khám đa khoa hoàn mỹ Sài Gòn", address: "60A Phan Xích Long, Phú Nhuận", phone: "0982.xxx.xxx" },
        { name: "Cà phê rang xay nguyên chất Đất Sài Gòn", address: "145 Võ Văn Tần, Quận 3", phone: "0947.xxx.xxx" },
        { name: "Cửa hàng đặc sản bánh tráng phơi sương Tây Ninh chính gốc", address: "32 Lê Văn Sỹ, Tân Bình", phone: "0914.xxx.xxx" },
        { name: "Salon tóc & Làm đẹp chuyên nghiệp Lê Hiếu", address: "339 Lê Văn Sỹ, Quận 3", phone: "0983.xxx.xxx" },
        { name: "Lớp học vẽ & Mỹ thuật thiếu nhi Art Land", address: "45 Phạm Ngọc Thạch, Quận 3", phone: "0941.xxx.xxx" },
        { name: "Đại lý yến sào Khánh Hòa chính gốc Quận 1", address: "120 Cách Mạng Tháng Tám, Quận 3", phone: "0911.xxx.xxx" },
        { name: "Cửa hàng thực phẩm sạch & rau hữu cơ Nam An Market", address: "21 Thảo Điền, Quận 2", phone: "0984.xxx.xxx" },
        { name: "Sửa điện lạnh & Máy giặt Gia Định", address: "250 Bạch Đằng, Bình Thạnh", phone: "0902.xxx.xxx" },
        { name: "Cho thuê áo dài cưới & Trang điểm cô dâu Quỳnh Anh", address: "152 Võ Thị Sáu, Quận 3", phone: "0917.xxx.xxx" },
        { name: "Lớp học tiếng Anh giao tiếp chuẩn KTDC", address: "9 Mai Thị Lựu, Quận 1", phone: "0938.xxx.xxx" },
        { name: "Dịch vụ hút hầm cầu & Thông nghẹt đô thị Sài Gòn", address: "112 Điện Biên Phủ, Bình Thạnh", phone: "0906.xxx.xxx" },
        { name: "Cơm văn phòng ngon sạch & Giao hàng tận nơi Saigon Bento", address: "88 Lê Thị Hồng Gấm, Quận 1", phone: "0975.xxx.xxx" },
        { name: "Vàng bạc đá quý PNJ Bến Thành", address: "12 Nguyễn An Ninh, Quận 1", phone: "0986.xxx.xxx" }
    ];

    let currentDirectoryPage = 0;
    const itemsPerDirectoryPage = 10;

    function renderDirectoryPage() {
        const start = currentDirectoryPage * itemsPerDirectoryPage;
        const end = start + itemsPerDirectoryPage;
        const itemsToShow = directoryListings.slice(start, end);
        const listContainer = document.getElementById('local-directory-list');
        if (!listContainer) return;
        
        let html = '';
        itemsToShow.forEach(item => {
            html += `
                <div style="background: #fff; border: 1px solid #eee; border-left: 3px solid #b8860b; padding: 3px 6px; border-radius: 3px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); transition: all 0.2s;" onmouseover="this.style.transform='translateX(2px)'; this.style.borderColor='#b8860b';" onmouseout="this.style.transform='none'; this.style.borderColor='#eee';">
                    <strong style="font-size: 11.5px; color: #333; display: block; margin-bottom: 2px;">${item.name}</strong>
                    <span style="font-size: 10px; color: #666; display: block; line-height: 1.3;">📍 ${item.address} | ☎ ${item.phone}</span>
                </div>
            `;
        });
        listContainer.innerHTML = html;
        
        const indicator = document.getElementById('directory-page-indicator');
        if (indicator) {
            indicator.innerText = `${currentDirectoryPage + 1}/3`;
        }
    }

    window.prevDirectoryPage = function() {
        if (currentDirectoryPage > 0) {
            currentDirectoryPage--;
        } else {
            currentDirectoryPage = 2;
        }
        renderDirectoryPage();
    };

    window.nextDirectoryPage = function() {
        if (currentDirectoryPage < 2) {
            currentDirectoryPage++;
        } else {
            currentDirectoryPage = 0;
        }
        renderDirectoryPage();
    };

    window.addEventListener('DOMContentLoaded', () => {
        populateCuratorOptions();
        renderMainCover();
        renderMediaSection();
        renderCategoryColumns();
        renderEnterpriseBlock();
        updateSchemaMarkup();
        changeDistrictPrices('quan1');
        fetchTPHCMWeather(10.7769, 106.7009, 'TP.HCM & Đông Nam Bộ');
        updateProvincialProfileWidget('all');
        initInfraCarouselAutoplay();
        renderDirectoryPage();
        initLandPriceWidget('tphcm');
    });
