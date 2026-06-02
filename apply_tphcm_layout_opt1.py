import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Read consolidated 100% Hanoi articles
with open('c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/tphcm_dongnambo_consolidated.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

js_all_articles_str = json.dumps(articles, ensure_ascii=False, indent=8)

# Read the HTML template
html_path = 'c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/demo_landing_page_hanoi_clean.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate header and footer
header_match = content.find('</header>')
if header_match == -1:
    print("Error: </header> not found")
    sys.exit(1)
header_part = content[:header_match + len('</header>')]

# Insert top billboard ad at the very top of body (above header/masthead)
body_tag = '<body ng-app="web-app">'
body_index = header_part.find(body_tag)
if body_index != -1:
    insert_pos = body_index + len(body_tag)
    top_billboard_html = """
    <!-- AD SLOT 01: TOP BILLBOARD (970x250) - PLACED ABOVE MASTHEAD -->
    <div style="width: 100%; max-width: 1000px; margin: 10px auto; text-align: center; font-family: Arial, sans-serif; position: relative; z-index: 1000;">
        <div style="position: absolute; top: 2px; left: 5px; font-size: 8px; color: #fff; background-color: #c00000; padding: 2px 5px; font-weight: bold; border-radius: 2px; z-index: 1005;">QC GIẢ LẬP</div>
        <a href="https://vinfastauto.com" target="_blank" style="text-decoration: none; display: block; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
            <div style="background: linear-gradient(90deg, #0b1a30 0%, #00458e 50%, #0b1a30 100%); height: 120px; display: flex; align-items: center; justify-content: space-between; padding: 0 40px; color: #fff; position: relative;">
                <div style="text-align: left;">
                    <h2 style="font-size: 22px; font-weight: 800; color: #fff; margin: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">VINFAST VF9</h2>
                    <p style="font-size: 11px; margin: 3px 0 0 0; color: #d0e1f9; font-weight: bold; letter-spacing: 0.5px;">ĐƯỜNG ĐẾN TƯƠNG LAI XANH - KIÊN TẠO VỊ THẾ DẪN ĐẦU</p>
                </div>
                <div style="border: 2px solid #fff; padding: 6px 15px; font-size: 12px; font-weight: bold; text-transform: uppercase; border-radius: 4px; background: rgba(255,255,255,0.1); cursor: pointer; transition: background 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'">Đăng ký lái thử</div>
            </div>
        </a>
    </div>
    """
    header_part = header_part[:insert_pos] + top_billboard_html + header_part[insert_pos:]

# Inject skin ads styling into header part
ad_styles = """
<style>
    @media (min-width: 1540px) {
        body {
            background-color: #f7f9fb !important;
            padding-left: 160px;
            padding-right: 160px;
        }
        .wallpaper-ad-left {
            position: fixed;
            top: 140px;
            left: calc(50% - 760px);
            width: 140px;
            height: 700px;
            background: linear-gradient(180deg, #0b1a30 0%, #002d62 100%);
            border: 2px dashed #c00000;
            color: #fff;
            font-family: Arial, sans-serif;
            padding: 15px 10px;
            box-sizing: border-box;
            border-radius: 6px;
            text-align: center;
            z-index: 99;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }
        .wallpaper-ad-right {
            position: fixed;
            top: 140px;
            right: calc(50% - 760px);
            width: 140px;
            height: 700px;
            background: linear-gradient(180deg, #0b1a30 0%, #002d62 100%);
            border: 2px dashed #c00000;
            color: #fff;
            font-family: Arial, sans-serif;
            padding: 15px 10px;
            box-sizing: border-box;
            border-radius: 6px;
            text-align: center;
            z-index: 99;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }
        .infra-block {
            background-color: #f9f9f9;
            border: 1px solid #eef1f5;
            border-radius: 8px;
            padding: 20px;
            font-family: Arial, sans-serif;
            margin-top: 20px;
        }
        .infra-heading-container {
            display: flex;
            align-items: center;
            border-bottom: 2px solid #e1251b;
            padding-bottom: 8px;
            margin-bottom: 15px;
        }
        .infra-heading-tag {
            background-color: #e1251b;
            color: #ffffff;
            font-size: 11px;
            font-weight: bold;
            padding: 3px 8px;
            border-radius: 3px;
            text-transform: uppercase;
            margin-right: 10px;
        }
        .infra-heading {
            font-size: 18px;
            font-weight: bold;
            color: #c00000;
            margin: 0;
            text-transform: uppercase;
        }
        .infra-grid {
            display: grid;
            grid-template-columns: 6fr 4fr;
            gap: 20px;
        }
        .infra-hero-card {
            position: relative;
            background-color: #ffffff;
            border: 1px solid #ddd;
            border-radius: 6px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        .infra-hero-img-container {
            position: relative;
            width: 100%;
            height: 280px;
            overflow: hidden;
        }
        .infra-hero-img-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s;
        }
        .infra-hero-img-container img:hover {
            transform: scale(1.03);
        }
        .infra-badge {
            position: absolute;
            top: 10px;
            left: 10px;
            background-color: rgba(192, 0, 0, 0.9);
            color: #ffffff;
            font-size: 11px;
            font-weight: bold;
            padding: 4px 8px;
            border-radius: 3px;
            z-index: 5;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        .infra-hero-body {
            padding: 15px;
        }
        .infra-hero-title {
            font-size: 16px;
            font-weight: bold;
            line-height: 1.4;
            margin: 0 0 8px 0;
        }
        .infra-hero-title a {
            color: #111;
            text-decoration: none;
        }
        .infra-hero-title a:hover {
            color: #c00000;
        }
        .infra-hero-excerpt {
            font-size: 13px;
            color: #555;
            line-height: 1.5;
            margin: 0;
        }
        .infra-list {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        .infra-list-item {
            border-bottom: 1px solid #eee;
            padding-bottom: 12px;
        }
        .infra-list-item:last-child {
            border-bottom: none;
            padding-bottom: 0;
        }
        .infra-list-title {
            font-size: 13.5px;
            font-weight: bold;
            line-height: 1.4;
            margin: 0 0 5px 0;
        }
        .infra-list-title a {
            color: #333;
            text-decoration: none;
        }
        .infra-list-title a:hover {
            color: #c00000;
        }
        .infra-list-meta {
            font-size: 11px;
            color: #888;
            display: flex;
            gap: 10px;
        }
        .infra-list-excerpt {
            font-size: 12px;
            color: #666;
            margin: 4px 0 0 0;
            line-height: 1.4;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        /* Mobile specific styles (Carousel) */
        @media (max-width: 850px) {
            .infra-grid {
                display: none !important;
            }
            .infra-carousel-container {
                display: flex !important;
                overflow-x: auto;
                scroll-snap-type: x mandatory;
                scroll-behavior: smooth;
                gap: 12px;
                padding-bottom: 10px;
                -webkit-overflow-scrolling: touch;
            }
            .infra-carousel-container::-webkit-scrollbar {
                display: none;
            }
            .infra-carousel-card {
                flex: 0 0 80%; /* Peek design: 15-20% cut-off */
                scroll-snap-align: start;
                background-color: #ffffff;
                border: 1px solid #ddd;
                border-radius: 6px;
                overflow: hidden;
                box-shadow: 0 2px 5px rgba(0,0,0,0.05);
                display: flex;
                flex-direction: column;
            }
            .infra-carousel-img-container {
                position: relative;
                width: 100%;
                height: 150px;
                overflow: hidden;
            }
            .infra-carousel-img-container img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
            .infra-carousel-body {
                padding: 12px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                flex-grow: 1;
            }
            .infra-carousel-title {
                font-size: 13px;
                font-weight: bold;
                line-height: 1.4;
                margin: 0 0 6px 0;
                display: -webkit-box;
                -webkit-line-clamp: 3;
                -webkit-box-orient: vertical;
                overflow: hidden;
            }
            .infra-carousel-title a {
                color: #111;
                text-decoration: none;
            }
        }
        @media (min-width: 851px) {
            .infra-carousel-container {
                display: none !important;
            }
        }
        
        /* Flexbox Overrides to prevent Float collapse and optimize layout alignment at the top */
        .blk-10-1 {
            display: flex !important;
            gap: 20px !important;
            width: 100% !important;
            clear: both !important;
            margin-bottom: 15px !important;
        }
        .blk-10-1 .pl.p-subcover {
            float: none !important;
            width: 300px !important;
            flex: 0 0 300px !important;
            box-sizing: border-box !important;
        }
        .blk-10-1 .pr.p-cover {
            float: none !important;
            flex: 1 1 auto !important;
            width: auto !important;
            box-sizing: border-box !important;
        }
        .blk-10::after {
            content: "";
            display: table;
            clear: both;
        }
        @media (max-width: 850px) {
            .most-read-slide {
                grid-template-columns: 1fr !important;
                gap: 10px !important;
            }
        }
    }
    @media (max-width: 768px) {
        #provincial-profile-widget {
            grid-template-columns: 1fr !important;
        }
        #provincial-profile-widget > div {
            border-right: none !important;
            padding-right: 0 !important;
            margin-bottom: 15px;
        }
    }
    #provincial-profile-widget table {
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
    }
    @media (max-width: 768px) {
        .columns-layout {
            grid-template-columns: 1fr !important;
            gap: 20px !important;
        }
        .nested-responsive-grid {
            grid-template-columns: 1fr !important;
        }
    }
    @media (max-width: 576px) {
        .job-item, [style*="border-left: 3px solid #ffc107"], [style*="border-left: 3px solid #28a745"] {
            flex-direction: column !important;
            align-items: flex-start !important;
            gap: 10px !important;
        }
        .job-item a, [style*="border-left: 3px solid #ffc107"] span:last-child, [style*="border-left: 3px solid #28a745"] span:last-child {
            align-self: flex-start !important;
        }
    }
</style>
<!-- WALLPAPER AD SLOTS -->
<div class="wallpaper-ad-left" style="display: none;">
    <div style="font-size: 8px; color: #fff; background-color: #c00000; padding: 2px 5px; font-weight: bold; border-radius: 2px; margin-bottom: 20px; display: inline-block;">QC GIẢ LẬP</div>
    <div style="font-weight: bold; font-size: 15px; margin-bottom: 30px; letter-spacing: 1px; color: #d4af37;">VINFAST VF9</div>
    <div style="font-size: 11px; line-height: 1.5; color: #d0e1f9;">Đẳng cấp SUV điện 7 chỗ hạng sang</div>
    <div style="margin-top: 100px; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px; font-size: 11px; color: #fff;">QUY HOẠCH SƯỜN TRÁI</div>
</div>
<div class="wallpaper-ad-right" style="display: none;">
    <div style="font-size: 8px; color: #fff; background-color: #c00000; padding: 2px 5px; font-weight: bold; border-radius: 2px; margin-bottom: 20px; display: inline-block;">QC GIẢ LẬP</div>
    <div style="font-weight: bold; font-size: 15px; margin-bottom: 30px; letter-spacing: 1px; color: #d4af37;">VINFAST VF9</div>
    <div style="font-size: 11px; line-height: 1.5; color: #d0e1f9;">Trải nghiệm công nghệ lái thông minh ADAS</div>
    <div style="margin-top: 100px; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px; font-size: 11px; color: #fff;">QUY HOẠCH SƯỜN PHẢI</div>
</div>
<script>
    document.addEventListener("DOMContentLoaded", () => {
        if(window.innerWidth >= 1540) {
            document.querySelector(".wallpaper-ad-left").style.display = "block";
            document.querySelector(".wallpaper-ad-right").style.display = "block";
        }
    });
</script>
"""

header_part = header_part + ad_styles

footer_match = content.find('<footer>')
if footer_match == -1:
    print("Error: <footer> not found")
    sys.exit(1)
footer_part = content[footer_match:]

# Construct the body with simulated ads integrated
middle_part = """
<div class="body-content">
    <div class="b-center">
        <div class="wrapper">
            
            <!-- BREADCRUMBS & WEATHER/DATE SUBBAR -->
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 12px 0 0 0; font-family: Arial, sans-serif; flex-wrap: wrap; gap: 10px;">
                <div class="breadcrumb-container" style="font-size: 13px; color: #666666; display: flex; align-items: center; gap: 5px;">
                    <a href="https://laodong.vn" style="color: #666666; text-decoration: none;">Trang chủ</a> 
                    <span style="color: #ccc;">/</span>
                    <a href="#" style="color: #666666; text-decoration: none;">Vùng miền</a> 
                    <span style="color: #ccc;">/</span>
                    <span id="dynamic-breadcrumb-spoke" style="color: #c00000; font-weight: bold;">TP.HCM & Đông Nam Bộ</span>
                </div>
                
                 <!-- Quick Links & Real-time TPHCM Weather Widget Grouped -->
                <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
                    <a id="dynamic-powercut-link" href="https://laodong.vn/tags/lich-cat-dien-tphcm-8542.ldo" target="_blank" style="text-decoration: none; font-size: 12px; color: #c00000; font-weight: bold; display: flex; align-items: center; gap: 3px;">⚡ Lịch cắt điện</a>
                    <span style="color: #ccc;">|</span>
                    <a href="https://laodong.vn/phap-luat/chinh-sach-moi" target="_blank" style="text-decoration: none; font-size: 12px; color: #002d62; font-weight: bold; display: flex; align-items: center; gap: 3px;">📋 Chính sách mới</a>
                    <span style="color: #ccc;">|</span>
                    <a href="https://laodong.vn/kinh-doanh/gia-vang" target="_blank" style="text-decoration: none; font-size: 12px; color: #b8860b; font-weight: bold; display: flex; align-items: center; gap: 3px;">🪙 Giá vàng</a>
                    <span style="color: #ccc;">|</span>
                    
                    <a href="https://weather.com/vi-VN/weather/today/l/VMXX0007:1:VM" target="_blank" title="Xem dự báo chi tiết tại Weather.com (Nguồn uy tín)" id="tphcm-weather-widget" style="text-decoration: none; display: flex; align-items: center; gap: 8px; background: rgba(240, 244, 248, 0.85); border: 1px solid #d0e1f9; padding: 4px 12px; border-radius: 20px; font-size: 12px; color: #002d62; box-shadow: 0 1px 3px rgba(0,0,0,0.05); font-weight: bold; transition: all 0.2s ease;" onmouseover="this.style.background='rgba(224, 235, 250, 0.95)'; this.style.transform='translateY(-1px)';" onmouseout="this.style.background='rgba(240, 244, 248, 0.85)'; this.style.transform='none';">
                        <span>📅 <span id="current-date-vietnam">Chủ nhật, 31/05/2026</span></span>
                        <span style="color: #ccc;">|</span>
                        <span id="weather-temp-span">📍 TP.HCM & Đông Nam Bộ: Đang tải...</span>
                    </a>
                </div>
            </div>

            <!-- NATIVE LAO DONG BREADCRUMBS / TITLE SECTION -->
            <div class="breadcrums" style="border-bottom: 2px solid #eee; padding-bottom: 10px; margin-top: 15px;">
                <h1 style="margin: 0; font-size: 22px; font-weight: bold; font-family: Arial, sans-serif;">
                    <a class="main-cat-lnk" href="#" style="color: #000000; text-decoration: none;" id="dynamic-page-title">TP.HCM & Đông Nam Bộ</a>
                </h1>
                <div class="children-cats" style="margin-top: 10px;">
                    <div class="list" id="hub-spoke-tabs" style="display: flex; gap: 15px; flex-wrap: wrap; font-family: Arial, sans-serif; font-size: 13px;">
                        <a href="#" class="item active" onclick="filterSpokeProvince('all'); return false;" style="color: #c00000; font-weight: bold; text-decoration: none; padding-bottom: 2px; border-bottom: 2px solid #c00000;">Toàn bộ khu vực</a>
                        <a href="#" class="item" onclick="filterSpokeProvince('tphcm'); return false;" style="color: #555; text-decoration: none; padding-bottom: 2px;">TP. Hồ Chí Minh</a>
                        <a href="#" class="item" onclick="filterSpokeProvince('dongnai'); return false;" style="color: #555; text-decoration: none; padding-bottom: 2px;">Đồng Nai</a>
                        <a href="#" class="item" onclick="filterSpokeProvince('tayninh'); return false;" style="color: #555; text-decoration: none; padding-bottom: 2px;">Tây Ninh</a>
                    </div>
                </div>
            </div>

            <!-- COLLAPSIBLE PROVINCIAL PROFILE ACCORDION -->
            <div style="margin-top: 15px; font-family: Arial, sans-serif;">
                <div onclick="toggleProvincialProfile()" style="background-color: #f7f9fb; border: 1px solid #e3e3e3; padding: 10px 15px; border-radius: 4px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none;">
                    <span style="font-weight: bold; color: #002d62; font-size: 13px; display: flex; align-items: center; gap: 8px;">
                        📊 THÔNG TIN HỒ SƠ & CHỈ SỐ CẢI CÁCH ĐỊA PHƯƠNG
                    </span>
                    <span id="profile-toggle-icon" style="font-weight: bold; color: #888; font-size: 14px;">Mở rộng ▾</span>
                </div>
                <div id="provincial-profile-widget" style="background-color: #ffffff; border: 1px solid #e3e3e3; border-top: none; border-left: 4px solid #002d62; padding: 15px 20px; font-family: Arial, sans-serif; border-bottom-left-radius: 4px; border-bottom-right-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); display: none; grid-template-columns: 1.2fr 1.8fr; gap: 20px; align-items: start; box-sizing: border-box;">
                    <!-- JS populated dynamically -->
                </div>
            </div>



            <!-- BLOCK 1: MAIN COVER GRID -->
            <div class="blk-10 main-cover m-top-20">
                <div class="pl">
                    <div class="blk-10-1">
                        <!-- Left Subcover: 2 stacked stories -->
                        <div class="pl p-subcover" id="subcover-container">
                            <!-- JS populated -->
                        </div>
                        
                        <!-- Center Main Cover: 1 giant spotlight story -->
                        <div class="pr p-cover" id="main-cover-container">
                            <!-- JS populated -->
                        </div>
                    </div>
                    <!-- Row of 3 bottom stories -->
                    <div class="subcover-bottom-row" id="subcover-bottom-row" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 15px; padding-top: 15px; border-top: 1px solid #eee;">
                        <!-- JS populated -->
                    </div>
                </div>
                
                <!-- Right Side: Spotlight stories + Sidebar Ad -->
                <div class="pr">
                    <div class="p-tieudiem">
                        <div style="font-size: 13px; font-weight: bold; color: #c00000; text-transform: uppercase; margin-bottom: 12px; border-bottom: 2px solid #c00000; padding-bottom: 5px;">Tiêu điểm TP.HCM & Đông Nam Bộ</div>
                        <div id="spotlight-container">
                            <!-- JS populated -->
                        </div>
                        
                        <!-- AD SLOT 02: SIDEBAR RECTANGLE (300x250) -->
                        <div style="width: 100%; margin: 15px 0; font-family: Arial, sans-serif; position: relative;">
                            <div style="position: absolute; top: 2px; left: 5px; font-size: 8px; color: #fff; background-color: #c00000; padding: 2px 5px; font-weight: bold; border-radius: 2px; z-index: 5;">QC GIẢ LẬP</div>
                            <a href="https://vietcombank.com.vn" target="_blank" style="text-decoration: none; display: block; border-radius: 4px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.1); border: 1px solid #d4af37;">
                                <div style="background: linear-gradient(135deg, #113824 0%, #1c5c3c 100%); height: 250px; display: flex; flex-direction: column; justify-content: space-between; padding: 20px; color: #fff; box-sizing: border-box; text-align: center;">
                                    <div style="font-size: 10px; color: #d4af37; letter-spacing: 2px; font-weight: bold; text-transform: uppercase;">Vietcombank Priority</div>
                                    <div style="font-size: 15px; font-weight: bold; line-height: 1.4; color: #fff; margin-top: 10px;">ĐẲNG CẤP DẪN ĐẦU<br><span style="color: #d4af37; font-size: 12px;">Đặc quyền xứng tầm Thượng khách tại Thủ đô</span></div>
                                    <div style="background-color: #d4af37; color: #113824; font-size: 11px; font-weight: bold; padding: 8px 15px; border-radius: 2px; align-self: center; cursor: pointer; text-transform: uppercase; width: fit-content; margin-top: 15px;">Tìm hiểu ngay</div>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- DYNAMIC FULL-WIDTH MOST READ CAROUSEL (Balances page flow) -->
            <div style="background-color: #fcfcfc; border: 1px solid #eef1f5; border-radius: 8px; padding: 15px 20px; margin-top: 20px; font-family: Arial, sans-serif; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; border-bottom: 2px solid #c00000; padding-bottom: 6px;">
                    <span style="font-size: 14px; font-weight: bold; color: #c00000; text-transform: uppercase; letter-spacing: 0.5px;">Đọc nhiều nhất</span>
                    <div id="most-read-dots" style="display: flex; gap: 6px; align-items: center;">
                        <!-- Populated dynamically -->
                    </div>
                </div>
                <div id="most-read-container" style="position: relative; min-height: 110px; overflow: hidden;">
                    <!-- JS populated dynamically -->
                </div>
            </div>

            <!-- BLOCK 2: MEDIA SECTION -->
            <div class="blk-media m-top-20" style="background-color: #eee; border-radius: 8px; padding: 20px; font-family: Arial, sans-serif;">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #c00000; padding-bottom: 8px; margin-bottom: 15px;">
                    <h2 style="font-size: 20px; font-weight: bold; color: #c00000; margin: 0; text-transform: uppercase;">Media TP.HCM & Đông Nam Bộ</h2>
                    <div style="display: flex; gap: 15px; font-size: 12px; font-weight: bold;">
                        <span style="color:#555;">Lao Động TV</span>
                        <span style="color:#555;">Hyper Text</span>
                        <span style="color:#555;">Photo</span>
                        <span style="color:#555;">Podcast</span>
                    </div>
                </div>
                
                <div style="display: grid; grid-template-columns: 1.2fr 1fr 1fr; gap: 15px;" class="columns-layout">
                    <!-- Left: TV Frame -->
                    <div style="background-color: #ffffff; padding: 15px; border-radius: 6px; border: 1px solid #ddd; display: flex; flex-direction: column; justify-content: space-between;">
                        <div style="background: linear-gradient(135deg, #ccc 0%, #999 50%, #bbb 100%); padding: 10px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
                            <div style="background-color: #000; width: 100%; height: 180px; border-radius: 6px; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center;">
                                <img src="https://media-cdn-v2.laodong.vn/laodong/2.0.0.35/images/logo/ldo_red.png" height="50" style="opacity: 0.8;" id="tv-player-img">
                                <div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.7); color: #fff; padding: 2px 6px; font-size: 10px; border-radius: 3px; font-weight: bold;">LIVE</div>
                            </div>
                            <div style="text-align: center; color: #333; font-size: 10px; font-weight: bold; margin-top: 5px; text-shadow: 1px 1px 1px #fff; letter-spacing: 2px;">LAODONG TV</div>
                        </div>
                        <div style="margin-top: 10px; border-top: 1px solid #eee; padding-top: 10px;">
                            <span style="font-size: 11px; background-color: #c00000; color: #fff; font-weight: bold; padding: 2px 6px; text-transform: uppercase;">Lịch phát sóng:</span>
                            <marquee style="font-size: 12px; color: #333; margin-top: 5px; font-weight: bold;" scrollamount="3">09:00 - Tin tức cập nhật sáng Thủ đô  |  12:00 - Bản tin Lao động Công đoàn TP.HCM & Đông Nam Bộ  |  20:00 - Bản tin Thời sự Tổng hợp TP.HCM & Đông Nam Bộ 24h</marquee>
                        </div>
                    </div>
                    
                    <!-- Middle & Right: Media Cards -->
                    <div style="display: flex; flex-direction: column; gap: 10px;" id="media-col-1">
                        <!-- JS populated -->
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 10px;" id="media-col-2">
                        <!-- JS populated -->
                    </div>
                </div>
            </div>

            PLACEHOLDER_STATIC_INFRASTRUCTURE

            <!-- AD SLOT 03: MID-PAGE BANNER (728x90) -->
            <div style="width: 100%; max-width: 1000px; margin: 20px auto; text-align: center; font-family: Arial, sans-serif; position: relative;">
                <div style="position: absolute; top: 2px; left: 5px; font-size: 8px; color: #fff; background-color: #c00000; padding: 2px 5px; font-weight: bold; border-radius: 2px; z-index: 5;">QC GIẢ LẬP</div>
                <a href="https://vinhomes.vn" target="_blank" style="text-decoration: none; display: block; border-radius: 6px; overflow: hidden; box-shadow: 0 3px 8px rgba(0,0,0,0.1);">
                    <div style="background: linear-gradient(90deg, #b8860b 0%, #e8c35b 50%, #b8860b 100%); height: 90px; display: flex; align-items: center; justify-content: space-between; padding: 0 30px; color: #7f0000;">
                        <div style="text-align: left;">
                            <h3 style="font-size: 18px; font-weight: bold; color: #7f0000; margin: 0;">VINHOMES GRAND PARK</h3>
                            <p style="font-size: 12px; margin: 2px 0 0 0; color: #7f0000; font-weight: bold;">ĐÔ THỊ THÔNG MINH XANH ĐÁNG SỐNG BẬC NHẤT</p>
                        </div>
                        <div style="background-color: #7f0000; color: #fff; font-size: 11px; padding: 8px 16px; font-weight: bold; border-radius: 4px; text-transform: uppercase; cursor: pointer;">Nhận bảng giá</div>
                    </div>
                </a>
            </div>

            <!-- BLOCK 4: SỰ KIỆN RIBBON -->
            <div class="m-top-20" style="background-color: #002d62; color: #ffffff; padding: 12px 20px; border-radius: 4px; display: flex; align-items: center; gap: 20px; flex-wrap: wrap; font-family: Arial, sans-serif;">
                <span style="font-weight: bold; font-size: 14px; letter-spacing: 1.5px; border-right: 2px solid rgba(255,255,255,0.3); padding-right: 20px; text-transform: uppercase;">Sự kiện</span>
                <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                    <span style="background-color: #ffffff; color: #002d62; padding: 4px 12px; border-radius: 4px; font-size: 11px; font-weight: bold; cursor: pointer;">Đại hội XIV Công đoàn VN</span>
                    <span style="background-color: rgba(255,255,255,0.15); color: #fff; padding: 4px 12px; border-radius: 4px; font-size: 11px; font-weight: bold; cursor: pointer;">Quy hoạch TP.HCM & Đông Nam Bộ</span>
                    <span style="background-color: rgba(255,255,255,0.15); color: #fff; padding: 4px 12px; border-radius: 4px; font-size: 11px; font-weight: bold; cursor: pointer;">Tuyển sinh lớp 10 TP.HCM & Đông Nam Bộ</span>
                    <span style="background-color: rgba(255,255,255,0.15); color: #fff; padding: 4px 12px; border-radius: 4px; font-size: 11px; font-weight: bold; cursor: pointer;">Vành đai 4 Thủ đô</span>
                </div>
            </div>

            <!-- BLOCK 4.5: SPONSORED SPECIAL HUBS -->
            <div class="m-top-20" style="background-color: #fcf9f2; border: 1px solid #e5d3b3; border-top: 3px solid #b8860b; border-radius: 8px; padding: 20px; font-family: Arial, sans-serif;">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #b8860b; padding-bottom: 8px; margin-bottom: 15px;">
                    <h2 style="font-size: 16px; font-weight: bold; color: #7f0000; margin: 0; text-transform: uppercase; display: flex; align-items: center; gap: 8px;">
                        <span>💎 Chuyên đề Đồng hành: TP.HCM & ĐÔNG NAM BỘ 360°</span>
                    </h2>
                    <span style="font-size: 11px; color: #666; font-weight: bold;">
                        Đồng hành bởi: <span style="color: #00458e; font-weight: 800;">VINFAST XANH</span>
                    </span>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px;" class="columns-layout">
                    <!-- Card 1 -->
                    <div style="background-color: #ffffff; border: 1px solid #eee; padding: 10px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between; position: relative;">
                        <span style="position: absolute; top: 15px; left: 15px; background: rgba(192,0,0,0.85); color: #fff; font-size: 8px; font-weight: bold; padding: 2px 5px; border-radius: 2px; z-index: 2;">QC GIẢ LẬP</span>
                        <div style="height: 120px; overflow: hidden; border-radius: 3px;">
                            <img src="https://images.unsplash.com/photo-1509060464153-4466739f88c0?auto=format&fit=crop&w=400&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <h4 style="margin: 10px 0 0 0; font-size: 12.5px; font-weight: bold; line-height: 1.4; color: #111;">
                            <span style="color: #b8860b; font-size: 10px; font-weight: bold; display: block; text-transform: uppercase; margin-bottom: 2px;">Cẩm nang xanh</span>
                            Khám phá 5 cung đường mùa thu lãng mạn nhất Thủ đô bằng xe máy điện VinFast
                        </h4>
                    </div>
                    <!-- Card 2 -->
                    <div style="background-color: #ffffff; border: 1px solid #eee; padding: 10px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between; position: relative;">
                        <span style="position: absolute; top: 15px; left: 15px; background: rgba(192,0,0,0.85); color: #fff; font-size: 8px; font-weight: bold; padding: 2px 5px; border-radius: 2px; z-index: 2;">QC GIẢ LẬP</span>
                        <div style="height: 120px; overflow: hidden; border-radius: 3px;">
                            <img src="https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=400&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <h4 style="margin: 10px 0 0 0; font-size: 12.5px; font-weight: bold; line-height: 1.4; color: #111;">
                            <span style="color: #b8860b; font-size: 10px; font-weight: bold; display: block; text-transform: uppercase; margin-bottom: 2px;">Ẩm thực du lịch</span>
                            Bản đồ ẩm thực phố cổ: Những món ăn sáng gia truyền nhất định phải thử tại TP.HCM & Đông Nam Bộ
                        </h4>
                    </div>
                    <!-- Card 3 -->
                    <div style="background-color: #ffffff; border: 1px solid #eee; padding: 10px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between; position: relative;">
                        <span style="position: absolute; top: 15px; left: 15px; background: rgba(192,0,0,0.85); color: #fff; font-size: 8px; font-weight: bold; padding: 2px 5px; border-radius: 2px; z-index: 2;">QC GIẢ LẬP</span>
                        <div style="height: 120px; overflow: hidden; border-radius: 3px;">
                            <img src="https://images.unsplash.com/photo-1569154941061-e231b4725ef1?auto=format&fit=crop&w=400&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <h4 style="margin: 10px 0 0 0; font-size: 12.5px; font-weight: bold; line-height: 1.4; color: #111;">
                            <span style="color: #b8860b; font-size: 10px; font-weight: bold; display: block; text-transform: uppercase; margin-bottom: 2px;">Hành trình di sản</span>
                            Check-in những công trình kiến trúc Pháp cổ kính biểu tượng tại Thủ đô
                        </h4>
                    </div>
                </div>
            </div>

            <!-- BLOCK 5: MULTI-COLUMN CATEGORY GRIDS -->
            <div class="m-top-20" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;" id="categories-grid-row1">
                <!-- JS populated Row 1 (4 columns) -->
            </div>
            
            <div class="m-top-20" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;" id="categories-grid-row2">
                <!-- JS populated Row 2 (4 columns) -->
            </div>

            <!-- BLOCK 5.5: HỆ SINH THÁI DÂN SINH & DANH BẠ HỘ KINH DOANH (MÔ PHỎNG CHIẾN LƯỢC ĐUÔI DÀI) -->
            <div class="m-top-20 columns-layout" style="display: grid; grid-template-columns: 2fr 1fr; gap: 20px; font-family: Arial, sans-serif;">
                <!-- Left: Worker Life, Weekend Escapes & Job Board -->
                <div style="background-color: #ffffff; border: 1px solid #e3e3e3; border-radius: 8px; padding: 20px; display: flex; flex-direction: column; justify-content: space-between;">
                    <div style="font-size: 14px; font-weight: bold; color: #002d62; text-transform: uppercase; border-bottom: 2px solid #002d62; padding-bottom: 6px; margin-bottom: 15px;">Dân sinh & Đời sống TP.HCM & Đông Nam Bộ</div>
                    <div class="nested-responsive-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
                        <!-- Item 1: Worker Life -->
                        <div style="border: 1px solid #eee; border-radius: 4px; padding: 10px; position: relative;">
                            <span style="position: absolute; top: 12px; left: 12px; background: rgba(192,0,0,0.85); color: #fff; font-size: 7px; font-weight: bold; padding: 2px 4px; border-radius: 2px; z-index: 2;">QC GIẢ LẬP</span>
                            <div style="height: 100px; overflow: hidden; border-radius: 3px;">
                                <img src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=400&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <h4 style="margin: 8px 0 0 0; font-size: 12px; font-weight: bold; line-height: 1.3;">
                                <span style="color: #002d62; font-size: 9px; font-weight: bold; display: block; text-transform: uppercase; margin-bottom: 2px;">Cẩm nang Công nhân KCN</span>
                                Danh sách nhà trọ an toàn, giá rẻ cho công nhân tại KCN Biên Hòa 2 & Amata năm 2026
                            </h4>
                        </div>
                        <!-- Item 2: Weekend Escape -->
                        <div style="border: 1px solid #eee; border-radius: 4px; padding: 10px; position: relative;">
                            <span style="position: absolute; top: 12px; left: 12px; background: rgba(192,0,0,0.85); color: #fff; font-size: 7px; font-weight: bold; padding: 2px 4px; border-radius: 2px; z-index: 2;">QC GIẢ LẬP</span>
                            <div style="height: 100px; overflow: hidden; border-radius: 3px;">
                                <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <h4 style="margin: 8px 0 0 0; font-size: 12px; font-weight: bold; line-height: 1.3;">
                                <span style="color: #28a745; font-size: 9px; font-weight: bold; display: block; text-transform: uppercase; margin-bottom: 2px;">Trốn phố cuối tuần</span>
                                Top 5 địa điểm camping, khu sinh thái xanh mát mắt tại Đồng Nai lý tưởng cuối tuần
                            </h4>
                        </div>
                    </div>
                    
                    <!-- JOB BOARD: VIỆC LÀM TP.HCM & ĐÔNG NAM BỘ -->
                    <div style="border-top: 1px solid #eee; padding-top: 15px; margin-bottom: 15px;">
                        <div style="font-size: 13px; font-weight: bold; color: #c00000; text-transform: uppercase; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center;">
                            <span>💼 Việc làm tại TP.HCM & Đông Nam Bộ (Tuyển dụng nhanh)</span>
                            <span style="font-size: 9.5px; color: #666; font-weight: normal; text-transform: none;">Liên kết: Trung tâm Dịch vụ việc làm TP.HCM & Đông Nam Bộ</span>
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 8px;">
                            <!-- Job 1 -->
                            <div class="job-item" style="display: flex; justify-content: space-between; align-items: center; background-color: #fcfcfc; border: 1px solid #eee; padding: 8px 12px; border-radius: 4px; position: relative;">
                                <span style="position: absolute; right: 85px; top: 12px; font-size: 7.5px; color: #d71920; border: 1px solid #d71920; padding: 1px 3px; border-radius: 2px; font-weight: bold; text-transform: uppercase;">Gấp</span>
                                <div style="text-align: left;">
                                    <strong style="font-size: 11.5px; color: #333; display: block;">Nhân viên lắp ráp linh kiện điện tử (KCN Amata, Biên Hòa)</strong>
                                    <span style="font-size: 9.5px; color: #666;">Công ty TNHH Changshin Việt Nam | Thu nhập: 8.5 - 11 triệu VNĐ</span>
                                </div>
                                <a href="#" style="background-color: #c00000; color: #fff; text-decoration: none; font-size: 10px; font-weight: bold; padding: 5px 10px; border-radius: 3px;">Nộp hồ sơ</a>
                            </div>
                            <!-- Job 2 -->
                            <div class="job-item" style="display: flex; justify-content: space-between; align-items: center; background-color: #fcfcfc; border: 1px solid #eee; padding: 8px 12px; border-radius: 4px;">
                                <div style="text-align: left;">
                                    <strong style="font-size: 11.5px; color: #333; display: block;">Kỹ thuật viên vận hành máy tiện cơ khí CNC</strong>
                                    <span style="font-size: 9.5px; color: #666;">Tập đoàn Cơ khí Tân Bình (KCN Tân Bình, TP.HCM) | Thu nhập: 10 - 13.5 triệu VNĐ</span>
                                </div>
                                <a href="#" style="background-color: #c00000; color: #fff; text-decoration: none; font-size: 10px; font-weight: bold; padding: 5px 10px; border-radius: 3px;">Nộp hồ sơ</a>
                            </div>
                        </div>
                    </div>

                    <!-- CITIZEN REPORTS FEED: NHẬT KÝ PHẢN ÁNH DÂN SINH -->
                    <div style="border-top: 1px solid #eee; padding-top: 15px;">
                        <div style="font-size: 13px; font-weight: bold; color: #002d62; text-transform: uppercase; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center;">
                            <span>📢 Nhật ký Phản ánh Dân sinh (Từ Độc giả)</span>
                            <span style="font-size: 9.5px; color: #28a745; font-weight: bold; text-transform: uppercase;">Live Feed</span>
                        </div>
                        <div id="citizen-reports-feed-container" style="display: flex; flex-direction: column; gap: 8px; max-height: 180px; overflow-y: auto;">
                            <!-- Seed Report 1 -->
                            <div style="background-color: #fafbfc; border: 1px solid #e9ecef; border-left: 3px solid #ffc107; padding: 8px 12px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <strong style="font-size: 11px; color: #333; display: block;">Hố ga mất nắp gây nguy hiểm tại ngã tư Nguyễn Thị Minh Khai - Cách Mạng Tháng Tám</strong>
                                    <span style="font-size: 9px; color: #666;">Độc giả 098****321 | ⏰ 15 phút trước</span>
                                </div>
                                <span style="background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; font-size: 9px; padding: 2px 6px; border-radius: 3px; font-weight: bold; flex-shrink: 0;">Đang xử lý</span>
                            </div>
                            <!-- Seed Report 2 -->
                            <div style="background-color: #fafbfc; border: 1px solid #e9ecef; border-left: 3px solid #28a745; padding: 8px 12px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <strong style="font-size: 11px; color: #333; display: block;">Rác thải sinh hoạt ùn ứ gây mùi hôi thối cạnh chợ Phạm Văn Hai, Tân Bình</strong>
                                    <span style="font-size: 9px; color: #666;">Độc giả 090****888 | ⏰ 2 giờ trước</span>
                                </div>
                                <span style="background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; font-size: 9px; padding: 2px 6px; border-radius: 3px; font-weight: bold; flex-shrink: 0;">Đã giải quyết</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                                <!-- Right: Local Business Directory -->
                <div style="background-color: #fdfdfd; border: 1px solid #e3e3e3; border-radius: 8px; padding: 20px; display: flex; flex-direction: column; box-sizing: border-box;">
                    <div style="font-size: 14px; font-weight: bold; color: #b8860b; text-transform: uppercase; border-bottom: 2px solid #b8860b; padding-bottom: 6px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 5px;">
                        <span>Kết nối Tiêu dùng</span>
                        <div style="display: flex; align-items: center; gap: 6px; user-select: none;">
                            <button onclick="prevDirectoryPage()" style="background: #fff; border: 1px solid #ccc; width: 22px; height: 22px; border-radius: 50%; font-size: 10px; cursor: pointer; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #b8860b; transition: all 0.2s;" onmouseover="this.style.background='#f0f0f0';" onmouseout="this.style.background='#fff';">◀</button>
                            <span id="directory-page-indicator" style="font-size: 11px; color: #666; font-weight: bold;">1/3</span>
                            <button onclick="nextDirectoryPage()" style="background: #fff; border: 1px solid #ccc; width: 22px; height: 22px; border-radius: 50%; font-size: 10px; cursor: pointer; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #b8860b; transition: all 0.2s;" onmouseover="this.style.background='#f0f0f0';" onmouseout="this.style.background='#fff';">▶</button>
                        </div>
                    </div>
                    <div style="display: flex; flex-direction: column; gap: 8px; min-height: 480px;" id="local-directory-list">
                        <!-- Loaded dynamically via JS -->
                    </div>
                </div>
                

            <!-- BLOCK 5.7: BẢNG GIÁ THỊ TRƯỜNG DÂN SINH TP.HCM & ĐÔNG NAM BỘ (MÔ PHỎNG TIẾP THỊ LIÊN KẾT & TÀI TRỢ SIÊU THỊ) -->
            <div class="m-top-20 columns-layout" style="display: grid; grid-template-columns: 2fr 1.2fr; gap: 20px; font-family: Arial, sans-serif;">
                <!-- Left: Interactive Price Table -->
                <div style="background-color: #ffffff; border: 1px solid #e3e3e3; border-radius: 8px; padding: 20px; box-sizing: border-box;">
                    <div style="font-size: 14px; font-weight: bold; color: #002d62; text-transform: uppercase; border-bottom: 2px solid #002d62; padding-bottom: 6px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                        <span>📊 Bảng giá thị trường dân sinh TP.HCM & Đông Nam Bộ</span>
                        <div style="display: flex; align-items: center; gap: 5px;">
                            <span style="font-size: 11px; color: #555; font-weight: normal; text-transform: none;">Khu vực:</span>
                            <select id="price-district-select" onchange="changeDistrictPrices(this.value)" style="padding: 3px 8px; font-size: 11.5px; border: 1px solid #ccc; border-radius: 3px; font-weight: bold; color: #002d62;">
                                <option value="quan1" selected>Quận 1 (TP.HCM)</option>
                                <option value="thuduc">TP. Thủ Đức</option>
                                <option value="bienhoa">TP. Biên Hòa</option>
                                <option value="tayninh">TP. Tây Ninh</option>
                            </select>
                        </div>
                    </div>
                    
                    <table style="width: 100%; border-collapse: collapse; font-size: 12px; text-align: left;">
                        <thead>
                            <tr style="background-color: #f7f9fb; border-bottom: 2px solid #eee;">
                                <th style="padding: 10px; color: #555;">Mặt hàng (Sạch/OCOP)</th>
                                <th style="padding: 10px; color: #555; text-align: center;">Chợ truyền thống</th>
                                <th style="padding: 10px; color: #d71920; font-weight: bold; text-align: center; background-color: #fff9fa;">Giá ưu đãi WinMart (Tài trợ)</th>
                                <th style="padding: 10px; color: #555; text-align: center;">Liên kết mua</th>
                            </tr>
                        </thead>
                        <tbody id="market-prices-tbody">
                            <!-- JS Populated dynamically based on district selection -->
                        </tbody>
                    </table>
                </div>
                
                <!-- Right: Supermarket Sponsorship Hub -->
                <div style="background-color: #ffffff; border: 1px solid #e3e3e3; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; position: relative; min-height: 380px; box-sizing: border-box;">
                    <span style="position: absolute; top: 10px; left: 10px; background: rgba(192,0,0,0.85); color: #fff; font-size: 7px; font-weight: bold; padding: 2px 5px; border-radius: 2px; z-index: 10;">QC GIẢ LẬP</span>
                    <div style="position: relative; height: 180px; overflow: hidden; width: 100%;">
                        <img src="winmart_summer_banner.png" alt="Khuyến mãi mùa hè 2026" style="width: 100%; height: 100%; object-fit: cover;">
                        <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 60%; background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.8) 100%); z-index: 2;"></div>
                        <div style="position: absolute; bottom: 12px; left: 15px; z-index: 5; color: #fff;">
                            <span style="font-size: 9px; font-weight: bold; color: #ffeb3b; text-transform: uppercase; letter-spacing: 0.5px;">Chương trình đặc biệt</span>
                            <h4 style="margin: 3px 0 0 0; font-size: 15px; font-weight: bold; line-height: 1.2; text-shadow: 0 1px 3px rgba(0,0,0,0.5);">KHUYẾN MÃI MÙA HÈ 2026</h4>
                        </div>
                    </div>
                    <div style="padding: 15px; display: flex; flex-direction: column; gap: 8px; flex-grow: 1; justify-content: space-between;">
                        <div>
                            <div style="font-size: 11px; font-weight: bold; color: #d71920; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5px;">Đồng hành chuyên mục</div>
                            <p style="margin: 0; font-size: 12px; color: #444; line-height: 1.45;">Đón hè rực rỡ cùng hàng ngàn ưu đãi giải nhiệt từ siêu thị WinMart TP.HCM & Đông Nam Bộ! Tiết kiệm lên tới 20% các mặt hàng tươi sống, thịt sạch & rau sạch mỗi ngày!</p>
                        </div>
                        <a href="https://winmart.vn" target="_blank" style="background-color: #d71920; color: #ffffff; text-decoration: none; font-size: 11px; font-weight: bold; padding: 10px 0; border-radius: 4px; text-transform: uppercase; text-align: center; display: block; box-shadow: 0 2px 5px rgba(215,25,32,0.2); transition: all 0.2s;" onmouseover="this.style.backgroundColor='#bd141b';" onmouseout="this.style.backgroundColor='#d71920';">Đăng ký hội viên miễn phí</a>
                    </div>
                </div>
            </div>

            <!-- BLOCK 5.75: LỊCH BIỂU DIỄN & GIẢI TRÍ TP.HCM & ĐÔNG NAM BỘ (MÔ PHỎNG KẾT NỐI API THỜI GIAN THỰC) -->
            <div class="m-top-20" style="display: grid; grid-template-columns: 1.8fr 1.2fr; gap: 20px; font-family: Arial, sans-serif;" class="columns-layout">
                <!-- Left: Theatre, Circus, Shows -->
                <div style="background-color: #ffffff; border: 1px solid #e3e3e3; border-radius: 8px; padding: 20px;">
                    <div style="font-size: 14px; font-weight: bold; color: #002d62; text-transform: uppercase; border-bottom: 2px solid #002d62; padding-bottom: 6px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                        <span>🎭 Lịch biểu diễn & Nghệ thuật TP.HCM & Đông Nam Bộ</span>
                        <span style="font-size: 9px; color: #28a745; font-weight: bold; border: 1px solid #28a745; padding: 2px 5px; border-radius: 2px;">LIVE API CONNECTED</span>
                    </div>
                    
                    <div style="display: flex; flex-direction: column; gap: 12px;">
                        <!-- Show 1 -->
                        <div style="display: flex; gap: 12px; align-items: center; border-bottom: 1px solid #f5f5f5; padding-bottom: 10px;">
                            <div style="background-color: #ffeef0; color: #d71920; font-size: 10px; font-weight: bold; padding: 8px; text-align: center; border-radius: 4px; width: 50px; flex-shrink: 0; line-height: 1.2;">
                                30<br><span style="font-size: 8px; font-weight: normal;">Th5</span>
                            </div>
                            <div style="flex-grow: 1;">
                                <span style="background-color: #f5f5f5; color: #888; border: 1px solid #ddd; padding: 0 3px; font-size: 8px; font-weight: bold; border-radius: 2px; margin-right: 4px;">PR Pinned</span>
                                <h4 style="margin: 0 0 3px 0; font-size: 12px; font-weight: bold; color: #111;">Hòa nhạc giao hưởng: "Giai điệu Sài Gòn xanh"</h4>
                                <span style="font-size: 10.5px; color: #666; display: block;">📍 Nhà hát Thành phố TP.HCM | ⏰ 19:30 Tối nay</span>
                            </div>
                            <a href="https://ticketbox.vn" target="_blank" style="background-color: #002d62; color: #fff; text-decoration: none; padding: 5px 10px; border-radius: 3px; font-size: 10px; font-weight: bold; flex-shrink: 0;">Đặt vé</a>
                        </div>
                        <!-- Show 2 -->
                        <div style="display: flex; gap: 12px; align-items: center; border-bottom: 1px solid #f5f5f5; padding-bottom: 10px;">
                            <div style="background-color: #e5f1ff; color: #00458e; font-size: 10px; font-weight: bold; padding: 8px; text-align: center; border-radius: 4px; width: 50px; flex-shrink: 0; line-height: 1.2;">
                                31<br><span style="font-size: 8px; font-weight: normal;">Th5</span>
                            </div>
                            <div style="flex-grow: 1;">
                                <h4 style="margin: 0 0 3px 0; font-size: 12px; font-weight: bold; color: #111;">Kịch xiếc nghệ thuật: "Vòng quay diệu kỳ"</h4>
                                <span style="font-size: 10.5px; color: #666; display: block;">📍 Rạp xiếc Công viên Gia Định | ⏰ 10:00 & 20:00 Ngày mai</span>
                            </div>
                            <a href="https://ticketbox.vn" target="_blank" style="background-color: #002d62; color: #fff; text-decoration: none; padding: 5px 10px; border-radius: 3px; font-size: 10px; font-weight: bold; flex-shrink: 0;">Đặt vé</a>
                        </div>
                        <!-- Show 3 -->
                        <div style="display: flex; gap: 12px; align-items: center; padding-bottom: 5px;">
                            <div style="background-color: #f6f0ff; color: #7a22ff; font-size: 10px; font-weight: bold; padding: 8px; text-align: center; border-radius: 4px; width: 50px; flex-shrink: 0; line-height: 1.2;">
                                01<br><span style="font-size: 8px; font-weight: normal;">Th6</span>
                            </div>
                            <div style="flex-grow: 1;">
                                <h4 style="margin: 0 0 3px 0; font-size: 12px; font-weight: bold; color: #111;">Biểu diễn Múa rối nước cổ truyền (Dành cho 1/6)</h4>
                                <span style="font-size: 10.5px; color: #666; display: block;">📍 Nhà hát Múa rối nước Rồng Vàng | ⏰ 15:00 & 17:00</span>
                            </div>
                            <a href="https://ticketbox.vn" target="_blank" style="background-color: #002d62; color: #fff; text-decoration: none; padding: 5px 10px; border-radius: 3px; font-size: 10px; font-weight: bold; flex-shrink: 0;">Đặt vé</a>
                        </div>
                    </div>
                </div>
                
                <!-- Right: Cinema Cinema / Showtimes -->
                <div style="background-color: #ffffff; border: 1px solid #e3e3e3; border-radius: 8px; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="font-size: 14px; font-weight: bold; color: #c00000; text-transform: uppercase; border-bottom: 2px solid #c00000; padding-bottom: 6px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
                            <span>🎬 Suất chiếu phim rạp TP.HCM & Đông Nam Bộ</span>
                            <span style="font-size: 9px; color: #888; font-weight: normal; text-transform: none;">CGV & Lotte</span>
                        </div>
                        
                        <div style="display: flex; flex-direction: column; gap: 8px;">
                            <!-- Movie 1 -->
                            <div style="border: 1px solid #eee; padding: 6px 10px; border-radius: 3px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <strong style="font-size: 11px; color: #333; display: block;">🎬 Điệp vụ bất khả thi: Tái sinh</strong>
                                    <span style="font-size: 9px; color: #888;">CGV Vincom Đồng Khởi | Suất: 18:30, 20:45</span>
                                </div>
                                <span style="background-color: #28a745; color: #fff; font-size: 8px; padding: 2px 4px; border-radius: 2px; font-weight: bold;">Còn vé</span>
                            </div>
                            <!-- Movie 2 -->
                            <div style="border: 1px solid #eee; padding: 6px 10px; border-radius: 3px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <strong style="font-size: 11px; color: #333; display: block;">🎬 Kẻ hủy diệt mới (2D Vietsub)</strong>
                                    <span style="font-size: 9px; color: #888;">Lotte Cinema Cộng Hòa | Suất: 19:00, 21:30</span>
                                </div>
                                <span style="background-color: #dc3545; color: #fff; font-size: 8px; padding: 2px 4px; border-radius: 2px; font-weight: bold;">Sắp cháy vé</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Partnership info -->
                    <div style="font-size: 9.5px; color: #666; margin-top: 10px; border-top: 1px solid #eee; padding-top: 8px; text-align: center;">
                        Dữ liệu tự động đồng bộ thời gian thực từ <strong style="color: #c00000;">TicketBox & CGV Cinema</strong>
                    </div>
                </div>
            </div>

            <!-- BLOCK 5.76: GÓC TƯƠNG TÁC ĐỘC GIẢ (BÁO CHÍ TƯƠNG TÁC DỰ LIỆU) -->
            <div class="m-top-20" style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 20px; font-family: Arial, sans-serif;" class="columns-layout">
                <!-- Left: Interactive Poll (Khảo sát dư luận) -->
                <div style="background-color: #ffffff; border: 1px solid #e3e3e3; border-radius: 8px; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="font-size: 14px; font-weight: bold; color: #002d62; text-transform: uppercase; border-bottom: 2px solid #002d62; padding-bottom: 6px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                            <span>📊 Khảo sát Dư luận Thủ đô</span>
                            <span style="font-size: 9px; color: #c00000; font-weight: bold; border: 1px solid #c00000; padding: 2px 5px; border-radius: 2px;">VOTE</span>
                        </div>
                        
                        <div id="poll-container">
                            <h4 style="margin: 0 0 12px 0; font-size: 13.5px; font-weight: bold; color: #333; line-height: 1.45;">Bạn ủng hộ việc tiếp tục mở rộng thêm các tuyến phố đi bộ vào cuối tuần tại TP.HCM & Đông Nam Bộ không?</h4>
                            <div style="display: flex; flex-direction: column; gap: 8px;">
                                <button onclick="submitPollVote('yes')" style="background: #ffffff; border: 1px solid #ddd; padding: 10px; border-radius: 4px; text-align: left; font-size: 12px; cursor: pointer; font-weight: bold; color: #333; transition: all 0.2s;" onmouseover="this.style.borderColor='#002d62'; this.style.backgroundColor='#f7f9fb';" onmouseout="this.style.borderColor='#ddd'; this.style.backgroundColor='#fff';">👍 Đồng ý, cần nhân rộng mô hình này</button>
                                <button onclick="submitPollVote('no')" style="background: #ffffff; border: 1px solid #ddd; padding: 10px; border-radius: 4px; text-align: left; font-size: 12px; cursor: pointer; font-weight: bold; color: #333; transition: all 0.2s;" onmouseover="this.style.borderColor='#002d62'; this.style.backgroundColor='#f7f9fb';" onmouseout="this.style.borderColor='#ddd'; this.style.backgroundColor='#fff';">👎 Không đồng ý, gây ùn tắc giao thông cục bộ</button>
                                <button onclick="submitPollVote('neutral')" style="background: #ffffff; border: 1px solid #ddd; padding: 10px; border-radius: 4px; text-align: left; font-size: 12px; cursor: pointer; font-weight: bold; color: #333; transition: all 0.2s;" onmouseover="this.style.borderColor='#002d62'; this.style.backgroundColor='#f7f9fb';" onmouseout="this.style.borderColor='#ddd'; this.style.backgroundColor='#fff';">😐 Đồng ý nhưng cần quy hoạch bãi đỗ xe hợp lý</button>
                            </div>
                        </div>
                    </div>
                    <div style="font-size: 9.5px; color: #888; margin-top: 15px; border-top: 1px solid #eee; padding-top: 8px; text-align: center;">
                        Khảo sát mang tính chất tham khảo dư luận phục vụ bài viết chuyên đề.
                    </div>
                </div>

                <!-- Right: Labor Overtime Pay Calculator (Tính lương tăng ca tự động) -->
                <div style="background-color: #ffffff; border: 1px solid #e3e3e3; border-radius: 8px; padding: 20px; box-sizing: border-box;">
                    <div style="font-size: 14px; font-weight: bold; color: #c00000; text-transform: uppercase; border-bottom: 2px solid #c00000; padding-bottom: 6px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                        <span>⚖️ Tự tính Lương tăng ca (Luật LĐ 2019)</span>
                        <span style="font-size: 9px; color: #28a745; font-weight: bold; border: 1px solid #28a745; padding: 2px 5px; border-radius: 2px;">TIỆN ÍCH LAO ĐỘNG</span>
                    </div>
                    
                    <div style="display: flex; flex-direction: column; gap: 12px; font-size: 12px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <label style="font-weight: bold; color: #333;">Lương cơ bản (đồng/giờ):</label>
                            <input type="number" id="labor-hourly-wage" value="30000" style="width: 100px; padding: 4px; border: 1px solid #ccc; border-radius: 3px; font-weight: bold; text-align: right; color: #002d62;">
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <label style="font-weight: bold; color: #333;">Số giờ làm thêm:</label>
                            <input type="number" id="labor-overtime-hours" value="4" style="width: 100px; padding: 4px; border: 1px solid #ccc; border-radius: 3px; font-weight: bold; text-align: right; color: #002d62;">
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <label style="font-weight: bold; color: #333;">Thời điểm tăng ca:</label>
                            <select id="labor-overtime-type" style="width: 120px; padding: 4px; border: 1px solid #ccc; border-radius: 3px; font-weight: bold; color: #002d62;">
                                <option value="weekday">Ngày thường (+150%)</option>
                                <option value="weekend">Ngày chủ nhật (+200%)</option>
                                <option value="holiday">Ngày lễ, Tết (+300%)</option>
                            </select>
                        </div>
                        <button onclick="calculateLaborOvertime()" style="background-color: #c00000; color: #ffffff; border: none; padding: 8px; border-radius: 4px; font-weight: bold; cursor: pointer; text-transform: uppercase;">Tính toán quyền lợi</button>
                        
                        <div id="labor-calc-result" style="background-color: #f7f9fb; border: 1px dashed #ccc; padding: 10px; border-radius: 4px; display: none;">
                            <!-- Calculated result populated here -->
                        </div>
                    </div>
                </div>
            </div>

            <!-- BLOCK 5.8: CẨM NANG TP.HCM & ĐÔNG NAM BỘ: ĂN GÌ - CHƠI GÌ - Ở ĐÂU? (MÔ PHỎNG NATIVE PR ĐỊA PHƯƠNG) -->
            <div class="m-top-20" style="background-color: #ffffff; border: 1px solid #e3e3e3; border-radius: 8px; padding: 20px; font-family: Arial, sans-serif;">
                <div style="font-size: 14px; font-weight: bold; color: #c00000; text-transform: uppercase; border-bottom: 2px solid #c00000; padding-bottom: 6px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <span>🗺️ Cẩm nang TP.HCM & Đông Nam Bộ: Ăn gì - Chơi gì - Ở đâu?</span>
                    <span style="font-size: 11px; color: #888; font-weight: normal; text-transform: none;">Tin cậy • Thực tế • Bản địa</span>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;" class="columns-layout">
                    <!-- Column 1: ĂN GÌ? -->
                    <div style="border-right: 1px solid #eee; padding-right: 15px;">
                        <h3 style="font-size: 13.5px; font-weight: bold; color: #002d62; text-transform: uppercase; margin: 0 0 10px 0; border-left: 3px solid #002d62; padding-left: 8px;">🍽️ Ăn gì?</h3>
                        <div style="display: flex; flex-direction: column; gap: 12px;">
                            <div style="display: flex; gap: 8px; align-items: center; position: relative;">
                                <div style="width: 50px; height: 35px; overflow: hidden; border-radius: 2px; flex-shrink: 0;">
                                    <img src="https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=100&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                                </div>
                                <div style="flex-grow: 1;">
                                    <span style="background-color: #f5f5f5; color: #888; border: 1px solid #ddd; padding: 0 3px; font-size: 8px; font-weight: bold; border-radius: 2px; margin-right: 4px;">PR</span>
                                    <a href="#" style="font-size: 11.5px; font-weight: bold; color: #333; text-decoration: none; line-height: 1.3;">5 quán phở đêm trứ danh phố cổ làm ấm lòng thực khách Thủ đô</a>
                                </div>
                            </div>
                            <div style="display: flex; gap: 8px; align-items: center;">
                                <div style="width: 50px; height: 35px; overflow: hidden; border-radius: 2px; flex-shrink: 0;">
                                    <img src="https://images.unsplash.com/photo-1473163928189-364b2c4e1135?auto=format&fit=crop&w=100&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                                </div>
                                <div>
                                    <a href="#" style="font-size: 11.5px; font-weight: bold; color: #333; text-decoration: none; line-height: 1.3;">Bản đồ các quán ốc vỉa hè ngon rẻ thu hút đông đảo giới trẻ TP.HCM & Đông Nam Bộ</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Column 2: CHƠI GÌ? -->
                    <div style="border-right: 1px solid #eee; padding-right: 15px;">
                        <h3 style="font-size: 13.5px; font-weight: bold; color: #002d62; text-transform: uppercase; margin: 0 0 10px 0; border-left: 3px solid #002d62; padding-left: 8px;">🚴 Chơi gì?</h3>
                        <div style="display: flex; flex-direction: column; gap: 12px;">
                            <div style="display: flex; gap: 8px; align-items: center;">
                                <div style="width: 50px; height: 35px; overflow: hidden; border-radius: 2px; flex-shrink: 0;">
                                    <img src="https://images.unsplash.com/photo-1508672019048-805c876b67e2?auto=format&fit=crop&w=100&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                                </div>
                                <div>
                                    <a href="#" style="font-size: 11.5px; font-weight: bold; color: #333; text-decoration: none; line-height: 1.3;">Những tọa độ ngắm hoàng hôn Hồ Tây lãng mạn và yên bình ít người biết</a>
                                </div>
                            </div>
                            <div style="display: flex; gap: 8px; align-items: center; position: relative;">
                                <div style="width: 50px; height: 35px; overflow: hidden; border-radius: 2px; flex-shrink: 0;">
                                    <img src="https://images.unsplash.com/photo-1513407030348-c983a97b98d8?auto=format&fit=crop&w=100&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                                </div>
                                <div style="flex-grow: 1;">
                                    <span style="background-color: #f5f5f5; color: #888; border: 1px solid #ddd; padding: 0 3px; font-size: 8px; font-weight: bold; border-radius: 2px; margin-right: 4px;">PR</span>
                                    <a href="#" style="font-size: 11.5px; font-weight: bold; color: #333; text-decoration: none; line-height: 1.3;">Trải nghiệm tour xe đạp đêm khám phá các di tích văn hóa lịch sử trung tâm</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Column 3: Ở ĐÂU? -->
                    <div>
                        <h3 style="font-size: 13.5px; font-weight: bold; color: #002d62; text-transform: uppercase; margin: 0 0 10px 0; border-left: 3px solid #002d62; padding-left: 8px;">🏨 Ở đâu?</h3>
                        <div style="display: flex; flex-direction: column; gap: 12px;">
                            <div style="display: flex; gap: 8px; align-items: center; position: relative;">
                                <div style="width: 50px; height: 35px; overflow: hidden; border-radius: 2px; flex-shrink: 0;">
                                    <img src="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=100&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                                </div>
                                <div style="flex-grow: 1;">
                                    <span style="background-color: #f5f5f5; color: #888; border: 1px solid #ddd; padding: 0 3px; font-size: 8px; font-weight: bold; border-radius: 2px; margin-right: 4px;">PR</span>
                                    <a href="#" style="font-size: 11.5px; font-weight: bold; color: #333; text-decoration: none; line-height: 1.3;">Review khu nghỉ dưỡng sinh thái xanh mát cực chill tại Trảng Bom, Đồng Nai</a>
                                </div>
                            </div>
                            <div style="display: flex; gap: 8px; align-items: center;">
                                <div style="width: 50px; height: 35px; overflow: hidden; border-radius: 2px; flex-shrink: 0;">
                                    <img src="https://images.unsplash.com/photo-1569154941061-e231b4725ef1?auto=format&fit=crop&w=100&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                                </div>
                                <div>
                                    <a href="#" style="font-size: 11.5px; font-weight: bold; color: #333; text-decoration: none; line-height: 1.3;">Top khách sạn boutique sang trọng mang đậm kiến trúc Đông Dương giữa lòng Quận 1</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- BLOCK 6: THÔNG TIN DOANH NGHIỆP -->
            <div class="m-top-20" style="background-color: #f7f7f7; padding: 20px; border-radius: 8px; border: 1px solid #e3e3e3; font-family: Arial, sans-serif;">
                <div style="font-size: 14px; font-weight: bold; color: #8b0000; text-transform: uppercase; border-bottom: 2px solid #8b0000; padding-bottom: 6px; margin-bottom: 15px;">Thông tin doanh nghiệp</div>
                <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px;" class="columns-layout" id="enterprise-grid-container">
                    <!-- JS populated (5 PR cards) -->
                </div>
            </div>

        </div>
    </div>
</div>

<!-- AD SLOT 04: CATFISH FLOATING BOTTOM (970x90) -->
<div id="catfish-ad-container" style="position: fixed; bottom: 0; left: 0; width: 100%; background: rgba(11,26,48,0.95); border-top: 3px solid #c00000; box-shadow: 0 -4px 15px rgba(0,0,0,0.3); z-index: 999999; display: flex; align-items: center; justify-content: center; padding: 12px 0; font-family: Arial, sans-serif;">
    <div style="width: 100%; max-width: 1000px; display: flex; align-items: center; justify-content: space-between; padding: 0 20px; box-sizing: border-box; position: relative;">
        <div style="position: absolute; top: -20px; left: 20px; font-size: 8px; color: #fff; background-color: #c00000; padding: 2px 5px; font-weight: bold; border-radius: 2px; z-index: 5;">QC GIẢ LẬP</div>
        <button onclick="document.getElementById('catfish-ad-container').style.display='none'; document.body.style.marginBottom='0'" style="position: absolute; right: 10px; top: -25px; background: #c00000; color: #fff; border: none; width: 22px; height: 22px; border-radius: 50%; font-weight: bold; cursor: pointer; font-size: 10px; display: flex; align-items: center; justify-content: center;">✕</button>
        <a href="https://vinfastauto.com" target="_blank" style="text-decoration: none; display: flex; align-items: center; justify-content: space-between; width: 100%; color: #fff;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <div style="background-color: #d4af37; color: #0b1a30; font-weight: bold; font-size: 10px; padding: 4px 8px; border-radius: 3px; text-transform: uppercase;">ƯU ĐÃI THỦ ĐÔ</div>
                <div style="font-size: 13px; font-weight: bold; color: #fff;">Sở hữu xe điện thông minh VinFast hôm nay - Hỗ trợ 100% lệ phí trước bạ & Sạc pin miễn phí 1 năm tại TP.HCM & Đông Nam Bộ!</div>
            </div>
            <div style="background-color: #fff; color: #002d62; font-size: 11px; font-weight: bold; padding: 7px 16px; border-radius: 4px; text-transform: uppercase;">Đăng ký ngay</div>
        </a>
    </div>
</div>
<script>
    document.addEventListener("DOMContentLoaded", () => {
        document.body.style.marginBottom = "60px";
    });
</script>

<!-- COLLAPSIBLE DEV PANEL / ADMIN SIMULATOR -->
<div id="dev-console-widget" style="position: fixed; bottom: 75px; right: 15px; z-index: 999999; font-family: sans-serif;">
    <button onclick="toggleDevConsole()" style="background-color: #002d62; color: #ffffff; border: none; padding: 8px 15px; border-radius: 20px; font-size: 12px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.2); display: flex; align-items: center; gap: 5px;">
        🔧 <span>Giả lập Tòa soạn & SEO (Demo)</span>
    </button>
    
    <div id="dev-console-drawer" style="display: none; width: 320px; background: #ffffff; border: 1px solid #ccc; border-radius: 8px; padding: 15px; margin-bottom: 8px; box-shadow: 0 5px 20px rgba(0,0,0,0.15); flex-direction: column; gap: 12px; position: absolute; bottom: 40px; right: 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee; padding-bottom: 8px;">
            <strong style="font-size: 13px; color: #002d62;">BẢNG ĐIỀU KHIỂN DEMO</strong>
            <button onclick="toggleDevConsole()" style="background: none; border: none; font-size: 16px; cursor: pointer; color: #999;">&times;</button>
        </div>
        
        <div>
            <label style="display: block; font-size: 11.5px; font-weight: bold; margin-bottom: 5px; color: #555;">Ghim bài Tiêu điểm chính (VPTT):</label>
            <select id="curator-select" style="width: 100%; padding: 6px; border: 1px solid #ccc; border-radius: 4px; font-size: 11.5px;" onchange="pinFeaturedStory(this.value)">
                <!-- populated dynamically -->
            </select>
        </div>

        <div>
            <label style="display: block; font-size: 11.5px; font-weight: bold; margin-bottom: 5px; color: #555; display: flex; justify-content: space-between;">
                <span>Tần suất bài viết:</span>
                <span id="threshold-val" style="color: #c00000; font-weight: bold;">120 bài/tháng</span>
            </label>
            <input type="range" id="threshold-slider" min="30" max="150" value="120" style="width: 100%; accent-color: #c00000;" oninput="updateThresholdDemo(this.value)">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 5px;">
                <span style="font-size: 10px; color: #888;">Ngưỡng an toàn: 100 bài</span>
                <span id="index-badge-status" style="background-color: #28a745; color: #ffffff; font-size: 9px; font-weight: bold; padding: 2px 6px; border-radius: 3px;">INDEXED</span>
            </div>
        </div>

        <div>
            <button onclick="openSchemaModal()" style="width: 100%; background-color: #c00000; color: #fff; border: none; padding: 7px; border-radius: 4px; font-size: 11px; font-weight: bold; cursor: pointer;">
                Xem cấu trúc 4 lớp Tag & JSON-LD
            </button>
        </div>
    </div>
</div>

</div>

<!-- FLOATING CHATBOT / CITIZEN HOTLINE INTERACTIVE WIDGET (MÔ PHỎNG QUẢN TRỊ DƯ LUẬN & DỊCH VỤ CÔNG) -->
<div id="hotline-chatbot-widget" style="position: fixed; bottom: 130px; right: 15px; z-index: 999999; font-family: sans-serif;">
    <!-- Pulsing Action Button -->
    <button onclick="toggleHotlineChat()" style="background: linear-gradient(135deg, #c00000 0%, #a00000 100%); color: #ffffff; border: none; padding: 10px 18px; border-radius: 25px; font-size: 12px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 15px rgba(192,0,0,0.3); display: flex; align-items: center; gap: 8px; position: relative;">
        <span style="position: absolute; top: -3px; right: -3px; display: flex; h: 10px; w: 10px; height: 10px; width: 10px;">
            <span style="animate-ping: absolute; inline-flex: 100%; height: 100%; width: 100%; border-radius: 9999px; background-color: #ffd700; opacity: 0.75;" class="pulsing-notification"></span>
        </span>
        📞 <span>Đường dây nóng Dân sinh 24/7</span>
    </button>
    
    <!-- Chat Window Container -->
    <div id="hotline-chat-window" style="display: none; width: 330px; height: 420px; background: #ffffff; border: 1px solid #ccc; border-radius: 12px; box-shadow: 0 5px 25px rgba(0,0,0,0.2); position: absolute; bottom: 45px; right: 0; flex-direction: column; overflow: hidden; font-family: Arial, sans-serif;">
        <!-- Header -->
        <div style="background: linear-gradient(90deg, #002d62 0%, #0b1a30 100%); color: #fff; padding: 12px 15px; display: flex; justify-content: space-between; align-items: center;">
            <div>
                <strong style="font-size: 13px; display: block;">Trợ lý Dân sinh & Công đoàn</strong>
                <span style="font-size: 9px; color: #28a745; font-weight: bold;">● AI tự động kết nối Tòa soạn</span>
            </div>
            <button onclick="toggleHotlineChat()" style="background: none; border: none; color: #fff; font-size: 18px; cursor: pointer;">&times;</button>
        </div>
        
        <!-- Chat body area -->
        <div id="chat-messages-container" style="flex-grow: 1; padding: 15px; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; background-color: #f7f9fb; font-size: 12px; line-height: 1.4;">
            <!-- System message -->
            <div style="background-color: #e5f1ff; color: #002d62; padding: 10px; border-radius: 8px; border: 1px solid #b6d4ff;">
                <strong>Kính chào độc giả Thủ đô!</strong><br>
                Đây là cổng tiếp nhận phản ánh dân sinh và tư vấn pháp luật Lao động tự động của Báo Lao Động TP.HCM & Đông Nam Bộ.
            </div>
            <!-- AI message -->
            <div style="align-self: flex-start; background-color: #fff; border: 1px solid #e3e3e3; padding: 10px; border-radius: 8px; max-width: 85%; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                Bạn cần trợ giúp hoặc phản ánh vấn đề gì hôm nay? Vui lòng chọn danh mục:
            </div>
            <!-- Option buttons -->
            <div id="chat-options-block" style="display: flex; flex-direction: column; gap: 8px; margin-top: 5px;">
                <button onclick="selectChatOption('report')" style="background-color: #fff; border: 1px solid #c00000; color: #c00000; padding: 8px 12px; border-radius: 20px; font-size: 11px; font-weight: bold; text-align: left; cursor: pointer; display: flex; align-items: center; justify-content: space-between;">
                    <span>📢 Phản ánh Dân sinh (Ngập lụt, rác thải, ô nhiễm)</span> <span>➔</span>
                </button>
                <button onclick="selectChatOption('union')" style="background-color: #fff; border: 1px solid #002d62; color: #002d62; padding: 8px 12px; border-radius: 20px; font-size: 11px; font-weight: bold; text-align: left; cursor: pointer; display: flex; align-items: center; justify-content: space-between;">
                    <span>⚖️ Bảo vệ quyền lợi Lao động (Bảo hiểm, Lương)</span> <span>➔</span>
                </button>
                <button onclick="selectChatOption('jobs')" style="background-color: #fff; border: 1px solid #28a745; color: #28a745; padding: 8px 12px; border-radius: 20px; font-size: 11px; font-weight: bold; text-align: left; cursor: pointer; display: flex; align-items: center; justify-content: space-between;">
                    <span>💼 Tra cứu Việc làm TP.HCM & Đông Nam Bộ mới nhất</span> <span>➔</span>
                </button>
            </div>
        </div>
    </div>
</div>

<style>
    @keyframes pulse-ad {
        0% { transform: scale(0.95); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 0.4; }
        100% { transform: scale(0.95); opacity: 0.8; }
    }
    .pulsing-notification {
        animation: pulse-ad 1.5s infinite ease-in-out;
    }
</style>

<script>
    function toggleHotlineChat() {
        const win = document.getElementById('hotline-chat-window');
        win.style.display = win.style.display === 'none' || win.style.display === '' ? 'flex' : 'none';
    }

    function selectChatOption(optionType) {
        const container = document.getElementById('chat-messages-container');
        const options = document.getElementById('chat-options-block');
        
        // Remove options
        if(options) options.remove();

        if (optionType === 'report') {
            container.innerHTML += `
                <div style="align-self: flex-end; background-color: #c00000; color: #fff; padding: 8px 12px; border-radius: 8px; max-width: 80%; margin-top: 5px;">
                    Tôi muốn Phản ánh vấn đề Dân sinh
                </div>
                <div style="align-self: flex-start; background-color: #fff; border: 1px solid #e3e3e3; padding: 10px; border-radius: 8px; max-width: 85%; margin-top: 5px;">
                    Cảm ơn bạn. Hãy mô tả ngắn gọn vấn đề (Ví dụ: "Hố ga mất nắp gây nguy hiểm tại Phố Huế") và đính kèm số điện thoại để phóng viên liên hệ:
                    <div style="margin-top: 10px; display: flex; flex-direction: column; gap: 8px;">
                        <textarea id="report-text" placeholder="Nhập nội dung phản ánh..." style="width: 100%; border: 1px solid #ccc; border-radius: 4px; padding: 5px; font-size: 11px; resize: none; height: 50px; font-family: Arial;"></textarea>
                        <input type="text" id="report-phone" placeholder="Số điện thoại liên hệ..." style="width: 100%; border: 1px solid #ccc; border-radius: 4px; padding: 5px; font-size: 11px;">
                        <button onclick="submitReportDemo()" style="background-color: #c00000; color: #fff; border: none; padding: 6px; border-radius: 4px; font-size: 11px; font-weight: bold; cursor: pointer;">Gửi phản ánh</button>
                    </div>
                </div>
            `;
        } else if (optionType === 'union') {
            container.innerHTML += `
                <div style="align-self: flex-end; background-color: #002d62; color: #fff; padding: 8px 12px; border-radius: 8px; max-width: 80%; margin-top: 5px;">
                    Tôi muốn tư vấn Bảo vệ quyền lợi Lao động
                </div>
                <div style="align-self: flex-start; background-color: #fff; border: 1px solid #e3e3e3; padding: 10px; border-radius: 8px; max-width: 85%; margin-top: 5px;">
                    💡 <strong>Trợ lý AI trả lời tự động:</strong> Theo Bộ luật Lao động Việt Nam năm 2019, người sử dụng lao động có nghĩa vụ đóng bảo hiểm xã hội bắt buộc cho người lao động có hợp đồng từ 1 tháng trở lên. Nếu công ty chậm đóng quá 30 ngày, bạn có quyền phản ánh lên Liên đoàn Lao động quận/huyện sở tại để được hỗ trợ can thiệp pháp lý.
                </div>
            `;
        } else if (optionType === 'jobs') {
            container.innerHTML += `
                <div style="align-self: flex-end; background-color: #28a745; color: #fff; padding: 8px 12px; border-radius: 8px; max-width: 80%; margin-top: 5px;">
                    Tôi muốn tìm kiếm Việc làm TP.HCM & Đông Nam Bộ
                </div>
                <div style="align-self: flex-start; background-color: #fff; border: 1px solid #e3e3e3; padding: 10px; border-radius: 8px; max-width: 85%; margin-top: 5px;">
                    🔍 Tìm thấy <strong>2 việc làm khẩn cấp</strong> trên địa bàn TP.HCM & Đông Nam Bộ hôm nay:
                    <ul style="padding-left: 15px; margin: 5px 0;">
                        <li><strong>Canon Việt Nam</strong> (KCN Bắc Thăng Long) - Lắp ráp linh kiện điện tử (8.5 - 11 triệu)</li>
                        <li><strong>Tập đoàn Cơ khí TP.HCM & Đông Nam Bộ</strong> (CNC Thạch Thất) - Vận hành máy tiện (10 - 13.5 triệu)</li>
                    </ul>
                    Bạn có thể nộp hồ sơ trực tiếp tại bảng "Việc làm tại TP.HCM & Đông Nam Bộ" nằm ở giữa trang!
                </div>
            `;
        }
        
        container.scrollTop = container.scrollHeight;
    }

    function submitReportDemo() {
        const text = document.getElementById('report-text').value;
        const phone = document.getElementById('report-phone').value;
        const container = document.getElementById('chat-messages-container');
        
        if(!text || !phone) {
            alert("Vui lòng điền đầy đủ thông tin!");
            return;
        }

        container.innerHTML += `
            <div style="align-self: flex-start; background-color: #e2f0d9; border: 1.5px dashed #28a745; padding: 10px; border-radius: 8px; margin-top: 5px; color: #1e4620;">
                ✔ <strong>Gửi phản ánh thành công!</strong><br>
                Hệ thống đã chuyển thông tin đến <strong>Văn phòng đại diện Báo Lao Động tại TP.HCM & Đông Nam Bộ</strong> và đồng gửi đến cơ quan quản lý địa bàn. Cảm ơn sự cộng tác dân sinh của bạn.
            </div>
        `;
        container.scrollTop = container.scrollHeight;

        // Dynamic update to the Feed widget on the landing page
        const feedContainer = document.getElementById('citizen-reports-feed-container');
        if(feedContainer) {
            const maskedPhone = phone.substring(0, 3) + "****" + phone.substring(phone.length - 3);
            const newReportHtml = `
                <div style="background-color: #fff8f8; border: 1px solid #ffccd0; border-left: 3px solid #dc3545; padding: 8px 12px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; animation: highlight-new 2s ease-out;">
                    <div>
                        <strong style="font-size: 11px; color: #333; display: block;">${text}</strong>
                        <span style="font-size: 9px; color: #666;">Độc giả ${maskedPhone} | ⏰ Vừa xong</span>
                    </div>
                    <span style="background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; font-size: 9px; padding: 2px 6px; border-radius: 3px; font-weight: bold; flex-shrink: 0;">Đang xác minh</span>
                </div>
            `;
            feedContainer.insertAdjacentHTML('afterbegin', newReportHtml);
            feedContainer.scrollTop = 0;
        }
    }

    function submitPollVote(option) {
        const container = document.getElementById('poll-container');
        if(!container) return;
        
        let votes = { yes: 64, no: 18, neutral: 18 };
        if(option === 'yes') votes.yes += 1;
        else if(option === 'no') votes.no += 1;
        else if(option === 'neutral') votes.neutral += 1;
        
        const total = votes.yes + votes.no + votes.neutral;
        const pctYes = Math.round((votes.yes / total) * 100);
        const pctNo = Math.round((votes.no / total) * 100);
        const pctNeutral = Math.round((votes.neutral / total) * 100);
        
        container.innerHTML = `
            <h4 style="margin: 0 0 15px 0; font-size: 13.5px; font-weight: bold; color: #333; line-height: 1.45;">Kết quả khảo sát dư luận:</h4>
            <div style="display: flex; flex-direction: column; gap: 12px; font-size: 11.5px;">
                <div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px; font-weight: bold;">
                        <span>👍 Đồng ý, cần nhân rộng:</span>
                        <span>${pctYes}% (${votes.yes} phiếu)</span>
                    </div>
                    <div style="background-color: #eee; border-radius: 4px; height: 10px; overflow: hidden;">
                        <div style="background-color: #28a745; width: ${pctYes}%; height: 100%; transition: width 1s ease-in-out;"></div>
                    </div>
                </div>
                <div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px; font-weight: bold;">
                        <span>👎 Không đồng ý, gây ùn tắc:</span>
                        <span>${pctNo}% (${votes.no} phiếu)</span>
                    </div>
                    <div style="background-color: #eee; border-radius: 4px; height: 10px; overflow: hidden;">
                        <div style="background-color: #dc3545; width: ${pctNo}%; height: 100%; transition: width 1s ease-in-out;"></div>
                    </div>
                </div>
                <div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px; font-weight: bold;">
                        <span>😐 Cần quy hoạch đỗ xe:</span>
                        <span>${pctNeutral}% (${votes.neutral} phiếu)</span>
                    </div>
                    <div style="background-color: #eee; border-radius: 4px; height: 10px; overflow: hidden;">
                        <div style="background-color: #ffc107; width: ${pctNeutral}%; height: 100%; transition: width 1s ease-in-out;"></div>
                    </div>
                </div>
            </div>
            <div style="margin-top: 15px; text-align: center; color: #28a745; font-weight: bold; font-size: 11px;">
                ✔ Cảm ơn bạn đã tham gia khảo sát ý kiến!
            </div>
        `;
    }

    function calculateLaborOvertime() {
        const hourlyWage = parseFloat(document.getElementById('labor-hourly-wage').value);
        const hours = parseFloat(document.getElementById('labor-overtime-hours').value);
        const type = document.getElementById('labor-overtime-type').value;
        const resultDiv = document.getElementById('labor-calc-result');
        
        if(isNaN(hourlyWage) || isNaN(hours) || hourlyWage <= 0 || hours <= 0) {
            alert("Vui lòng nhập mức lương và số giờ hợp lệ!");
            return;
        }
        
        let multiplier = 1.5;
        let typeText = "Ngày thường (+150%)";
        if(type === 'weekend') {
            multiplier = 2.0;
            typeText = "Ngày chủ nhật (+200%)";
        } else if(type === 'holiday') {
            multiplier = 3.0;
            typeText = "Ngày lễ, Tết (+300%)";
        }
        
        const overtimePay = hourlyWage * hours * multiplier;
        
        resultDiv.style.display = 'block';
        resultDiv.innerHTML = `
            <div style="color: #002d62; font-weight: bold; margin-bottom: 5px;">✔ Kết quả tính toán:</div>
            <div style="line-height: 1.5; font-size: 11.5px; color: #333;">
                • Lương giờ cơ bản: <strong>${hourlyWage.toLocaleString()} đ</strong><br>
                • Hệ số áp dụng: <strong>x${multiplier}</strong> (${typeText})<br>
                • Tổng tiền tăng ca nhận được:<br>
                <span style="font-size: 14px; color: #c00000; font-weight: 800;">${overtimePay.toLocaleString()} đ</span><br>
                <span style="font-size: 9.5px; color: #666; display: block; margin-top: 3px;">(Căn cứ theo Điều 98 - Bộ luật Lao động năm 2019)</span>
            </div>
        `;
    }

    const districtPricesData = {
        quan1: [
            { name: "🥩 Thịt ba rọi heo sạch MEATDeli", normal: "135.000 đ/kg", winmart: "119.000 đ/kg", discount: "12%" },
            { name: "🥬 Rau muống sạch VietGAP Củ Chi", normal: "15.000 đ/kg", winmart: "12.000 đ/kg", discount: "20%" },
            { name: "🐟 Cá lóc bông tươi sống Trị An", normal: "110.000 đ/kg", winmart: "98.000 đ/kg", discount: "11%" },
            { name: "🍚 Gạo thơm ST25 Sóc Trăng (Túi 5kg)", normal: "145.000 đ/túi", winmart: "128.000 đ/túi", discount: "12%" }
        ],
        thuduc: [
            { name: "🥩 Thịt ba rọi heo sạch MEATDeli", normal: "140.000 đ/kg", winmart: "122.000 đ/kg", discount: "13%" },
            { name: "🥬 Rau muống sạch VietGAP Củ Chi", normal: "16.000 đ/kg", winmart: "13.000 đ/kg", discount: "18%" },
            { name: "🐟 Cá lóc bông tươi sống Trị An", normal: "115.000 đ/kg", winmart: "102.000 đ/kg", discount: "11%" },
            { name: "🍚 Gạo thơm ST25 Sóc Trăng (Túi 5kg)", normal: "148.000 đ/túi", winmart: "130.000 đ/túi", discount: "12%" }
        ],
        bienhoa: [
            { name: "🥩 Thịt ba rọi heo sạch MEATDeli", normal: "130.000 đ/kg", winmart: "115.000 đ/kg", discount: "11%" },
            { name: "🥬 Rau muống sạch VietGAP Củ Chi", normal: "14.000 đ/kg", winmart: "11.000 đ/kg", discount: "21%" },
            { name: "🐟 Cá lóc bông tươi sống Trị An", normal: "105.000 đ/kg", winmart: "92.000 đ/kg", discount: "12%" },
            { name: "🍚 Gạo thơm ST25 Sóc Trăng (Túi 5kg)", normal: "140.000 đ/túi", winmart: "125.000 đ/túi", discount: "10%" }
        ],
        tayninh: [
            { name: "🥩 Thịt ba rọi heo sạch MEATDeli", normal: "125.000 đ/kg", winmart: "110.000 đ/kg", discount: "12%" },
            { name: "🥬 Rau muống sạch VietGAP Củ Chi", normal: "13.000 đ/kg", winmart: "10.000 đ/kg", discount: "23%" },
            { name: "🐟 Cá lóc bông tươi sống Trị An", normal: "100.000 đ/kg", winmart: "88.000 đ/kg", discount: "12%" },
            { name: "🍚 Gạo thơm ST25 Sóc Trăng (Túi 5kg)", normal: "138.000 đ/túi", winmart: "122.000 đ/túi", discount: "11%" }
        ]
    };

    function changeDistrictPrices(district) {
        const tbody = document.getElementById('market-prices-tbody');
        if(!tbody) return;
        
        const data = districtPricesData[district] || districtPricesData.quan1;
        let html = '';
        data.forEach(item => {
            html += `
                <tr style="border-bottom: 1px solid #eee;">
                    <td style="padding: 10px; font-weight: bold;">${item.name}</td>
                    <td style="padding: 10px; text-align: center; color: #666;">${item.normal}</td>
                    <td style="padding: 10px; text-align: center; font-weight: bold; color: #d71920; background-color: #fff9fa;">${item.winmart} <span style="font-size:9px; display:block; color:#888;">(Giảm ${item.discount})</span></td>
                    <td style="padding: 10px; text-align: center;">
                        <a href="https://winmart.vn" target="_blank" style="background-color: #d71920; color: #fff; text-decoration: none; padding: 4px 8px; border-radius: 3px; font-size: 10px; font-weight: bold; display: inline-block;">Mua tại WinMart</a>
                    </td>
                </tr>
            `;
        });
        tbody.innerHTML = html;
    }
</script>

<!-- DIAGNOSTIC SCHEMA MODAL -->
<div id="schema-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 9999999; justify-content: center; align-items: center; padding: 20px;">
    <div style="background: #ffffff; border-radius: 8px; width: 100%; max-width: 750px; max-height: 85vh; overflow-y: auto; box-shadow: 0 5px 25px rgba(0,0,0,0.25);">
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 12px 18px; border-bottom: 1px solid #eee; background-color: #002d62; color: #ffffff; border-top-left-radius: 8px; border-top-right-radius: 8px;">
            <h3 style="margin: 0; font-size: 14px; font-weight: bold;">CẤU TRÚC PHÂN PHỐI SEO & DỮ LIỆU CÓ CẤU TRÚC</h3>
            <button onclick="closeSchemaModal()" style="background: none; border: none; color: #fff; font-size: 20px; cursor: pointer;">&times;</button>
        </div>
        <div style="padding: 15px;">
            <h4 style="margin: 0 0 8px 0; font-size: 13px; color: #333;">1. Mô hình Phân Loại 4 Lớp Tag (Taxonomy Model)</h4>
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 15px; font-size: 11.5px;">
                <thead>
                    <tr style="background-color: #f5f5f5;">
                        <th style="border: 1px solid #ddd; padding: 6px; text-align: left;">Lớp Phân Loại</th>
                        <th style="border: 1px solid #ddd; padding: 6px; text-align: left;">Giá Trị Khai Báo</th>
                        <th style="border: 1px solid #ddd; padding: 6px; text-align: left;">Nguyên Tắc SEO</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 6px; font-weight: bold;">Lớp 1: Vùng Miền</td>
                        <td style="border: 1px solid #ddd; padding: 6px;">Đông Nam Bộ</td>
                        <td style="border: 1px solid #ddd; padding: 6px;">Chỉ mục toàn bộ trang</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 6px; font-weight: bold;">Lớp 2: Tỉnh/Thành</td>
                        <td style="border: 1px solid #ddd; padding: 6px;">TP.HCM & Đông Nam Bộ (Trọng điểm Tầng 1)</td>
                        <td style="border: 1px solid #ddd; padding: 6px;">Canonical cố định tại laodong.vn/vung-mien/tphcm-va-dong-nam-bo/</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 6px; font-weight: bold;">Lớp 3: Quận/Huyện</td>
                        <td style="border: 1px solid #ddd; padding: 6px;" id="schema-district">Quận 1 / TP. Thủ Đức / Biên Hòa...</td>
                        <td style="border: 1px solid #ddd; padding: 6px;">Bản đồ Entity cục bộ</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 6px; font-weight: bold;">Lớp 4: Chuyên Đề</td>
                        <td style="border: 1px solid #ddd; padding: 6px;" id="schema-category">Đô thị | Quy hoạch</td>
                        <td style="border: 1px solid #ddd; padding: 6px;">Liên kết ngang (Internal link silo)</td>
                    </tr>
                </tbody>
            </table>

            <h4 style="margin: 0 0 8px 0; font-size: 13px; color: #333;">2. JSON-LD Breadcrumb & CollectionPage Schema</h4>
            <pre id="json-schema-output" style="background-color: #272822; color: #f8f8f2; padding: 12px; border-radius: 5px; font-family: Consolas, Monaco, monospace; font-size: 11px; overflow-x: auto; margin: 0; max-height: 200px;"></pre>
        </div>
        <div style="padding: 10px 15px; border-top: 1px solid #eee; text-align: right;">
            <button onclick="closeSchemaModal()" style="background-color: #eee; color: #333; border: 1px solid #ccc; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-size: 12px;">Đóng</button>
        </div>
    </div>
</div>

<script>
    const originalTphcmArticles = PLACEHOLDER_RAW_ARTICLES;
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
        const leftSubPool = tphcmArticles.filter(a => a.id !== centerArt.id);
        const sub1 = getSafeArticle(leftSubPool, 0, 1);
        const sub2 = getSafeArticle(leftSubPool, 1, 2);
        const rightPool = tphcmArticles.filter(a => a.id !== centerArt.id && a.id !== sub1.id && a.id !== sub2.id);
        const bottom1 = getSafeArticle(rightPool, 0, 3);
        const bottom2 = getSafeArticle(rightPool, 1, 4);
        const bottom3 = getSafeArticle(rightPool, 2, 5);
        const spot1 = getSafeArticle(rightPool, 3, 6);
        const spot2 = getSafeArticle(rightPool, 4, 7);
        const spot3 = getSafeArticle(rightPool, 5, 8);
        const spot4 = getSafeArticle(rightPool, 6, 9);

        // Gather all featured/cover/spotlight IDs to exclude them from other sections
        const displayedIds = new Set([centerArt.id, sub1.id, sub2.id, bottom1.id, bottom2.id, bottom3.id, spot1.id, spot2.id, spot3.id, spot4.id]);

        // Most Read Pool (15 items) - Must not duplicate featured/spotlight articles
        const mostReadPool = tphcmArticles.filter(a => !displayedIds.has(a.id)).slice(0, 15);
        const mostReadIds = new Set(mostReadPool.map(a => a.id));

        // Latest News Feed (3 items) - Must not duplicate featured/spotlight AND must not duplicate most read
        const latestNewsPool = tphcmArticles.filter(a => !displayedIds.has(a.id) && !mostReadIds.has(a.id));
        const feed1 = getSafeArticle(latestNewsPool, 0, 10);
        const feed2 = getSafeArticle(latestNewsPool, 1, 11);
        const feed3 = getSafeArticle(latestNewsPool, 2, 12);

        document.getElementById('main-cover-container').innerHTML = `
            <article class="v4 cv-001">
                <a class="link-img" href="` + centerArt.url + `" target="_blank">
                    <figure class="_thumb">
                        <img src="` + centerArt.image + `" class="img-art" alt="` + centerArt.title + `" width="560" height="348">
                    </figure>
                </a>
                <a class="link-title" href="` + centerArt.url + `" target="_blank">
                    <h2 class="title cover prefix-icon">` + centerArt.title + `</h2>
                </a>
                <div class="chapeau ellipsis fade-out">` + centerArt.excerpt + `</div>
            </article>
        `;

        document.getElementById('subcover-container').innerHTML = `
            <article class="v4 nm-001 item n-1">
                <a class="link-img" href="` + sub1.url + `" target="_blank">
                    <figure class="_thumb">
                        <img src="` + sub1.image + `" class="img-art" alt="` + sub1.title + `" width="300" height="186">
                    </figure>
                </a>
                <a class="link-title" href="` + sub1.url + `" target="_blank">
                    <h2 class="title prefix-icon">` + sub1.title + `</h2>
                </a>
            </article>
            <article class="v4 nm-001 item n-2">
                <a class="link-img" href="` + sub2.url + `" target="_blank">
                    <figure class="_thumb">
                        <img src="` + sub2.image + `" class="img-art" alt="` + sub2.title + `" width="300" height="186">
                    </figure>
                </a>
                <a class="link-title" href="` + sub2.url + `" target="_blank">
                    <h2 class="title prefix-icon">` + sub2.title + `</h2>
                </a>
            </article>
        `;

        document.getElementById('subcover-bottom-row').innerHTML = `
            <div style="display: flex; flex-direction: column; width: 100%; box-sizing: border-box;">
                <a href="` + bottom1.url + `" target="_blank" style="display: block; width: 100%; aspect-ratio: 16/10; overflow: hidden; border-radius: 4px; background-color: #f0f0f0;">
                    <img src="` + bottom1.image + `" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='none'">
                </a>
                <a href="` + bottom1.url + `" target="_blank" style="text-decoration: none; display: block; margin-top: 8px;">
                    <h3 style="font-family: Arial, sans-serif; font-size: 14px; line-height: 1.4; font-weight: bold; color: #111; margin: 0; transition: color 0.2s;" onmouseover="this.style.color='#c00000'" onmouseout="this.style.color='#111'">
                        ` + bottom1.title + `
                    </h3>
                </a>
            </div>
            <div style="display: flex; flex-direction: column; width: 100%; box-sizing: border-box;">
                <a href="` + bottom2.url + `" target="_blank" style="display: block; width: 100%; aspect-ratio: 16/10; overflow: hidden; border-radius: 4px; background-color: #f0f0f0;">
                    <img src="` + bottom2.image + `" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='none'">
                </a>
                <a href="` + bottom2.url + `" target="_blank" style="text-decoration: none; display: block; margin-top: 8px;">
                    <h3 style="font-family: Arial, sans-serif; font-size: 14px; line-height: 1.4; font-weight: bold; color: #111; margin: 0; transition: color 0.2s;" onmouseover="this.style.color='#c00000'" onmouseout="this.style.color='#111'">
                        ` + bottom2.title + `
                    </h3>
                </a>
            </div>
            <div style="display: flex; flex-direction: column; width: 100%; box-sizing: border-box;">
                <a href="` + bottom3.url + `" target="_blank" style="display: block; width: 100%; aspect-ratio: 16/10; overflow: hidden; border-radius: 4px; background-color: #f0f0f0;">
                    <img src="` + bottom3.image + `" style="width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='none'">
                </a>
                <a href="` + bottom3.url + `" target="_blank" style="text-decoration: none; display: block; margin-top: 8px;">
                    <h3 style="font-family: Arial, sans-serif; font-size: 14px; line-height: 1.4; font-weight: bold; color: #111; margin: 0; transition: color 0.2s;" onmouseover="this.style.color='#c00000'" onmouseout="this.style.color='#111'">
                        ` + bottom3.title + `
                    </h3>
                </a>
            </div>
        `;


        document.getElementById('spotlight-container').innerHTML = `
            <article class="v4 p2c m001 n-1">
                <div class="pl">
                    <a class="link-img" href="` + spot1.url + `" target="_blank">
                        <figure class="_thumb">
                            <img src="` + spot1.image + `" class="img-art" alt="` + spot1.title + `" width="159" height="93">
                        </figure>
                    </a>
                </div>
                <div class="pr">
                    <a class="link-title" href="` + spot1.url + `" target="_blank">
                        <h2 class="title prefix-icon">` + spot1.title + `</h2>
                    </a>
                </div>
            </article>
            <article class="v4 p2c m001 n-2">
                <div class="pl">
                    <a class="link-img" href="` + spot2.url + `" target="_blank">
                        <figure class="_thumb">
                            <img src="` + spot2.image + `" class="img-art" alt="` + spot2.title + `" width="159" height="93">
                        </figure>
                    </a>
                </div>
                <div class="pr">
                    <a class="link-title" href="` + spot2.url + `" target="_blank">
                        <h2 class="title prefix-icon">` + spot2.title + `</h2>
                    </a>
                </div>
            </article>
            <article class="v4 p2c m001 n-3">
                <div class="pl">
                    <a class="link-img" href="` + spot3.url + `" target="_blank">
                        <figure class="_thumb">
                            <img src="` + spot3.image + `" class="img-art" alt="` + spot3.title + `" width="159" height="93">
                        </figure>
                    </a>
                </div>
                <div class="pr">
                    <a class="link-title" href="` + spot3.url + `" target="_blank">
                        <h2 class="title prefix-icon"><span style="background-color: #ffeef0; color: #d71920; border: 1px solid #ffccd0; padding: 1px 4px; font-size: 9px; margin-right: 5px; border-radius: 2px; font-weight: bold; vertical-align: middle;">TÀI TRỢ</span>` + spot3.title + `</h2>
                    </a>
                </div>
            </article>
            <article class="v4 p2c m001 n-4">
                <div class="pl">
                    <a class="link-img" href="` + spot4.url + `" target="_blank">
                        <figure class="_thumb">
                            <img src="` + spot4.image + `" class="img-art" alt="` + spot4.title + `" width="159" height="93">
                        </figure>
                    </a>
                </div>
                <div class="pr">
                    <a class="link-title" href="` + spot4.url + `" target="_blank">
                        <h2 class="title prefix-icon">` + spot4.title + `</h2>
                    </a>
                </div>
            </article>
        `;


        let containerHtml = '';
        let dotsHtml = '';
        const slideCount = Math.ceil(mostReadPool.length / 5);
        
        for (let s = 0; s < slideCount; s++) {
            const slideArticles = mostReadPool.slice(s * 5, (s + 1) * 5);
            let slideItemsHtml = '';
            slideArticles.forEach((item, idx) => {
                const globalIdx = s * 5 + idx + 1;
                slideItemsHtml += `
                    <div style="display: flex; gap: 10px; align-items: flex-start; padding: 10px; background: #ffffff; border: 1px solid #eef1f5; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.02); height: 100%; box-sizing: border-box;">
                        <span style="font-size: 16px; font-weight: 800; color: #c00000; line-height: 1.1; min-width: 18px;">` + globalIdx + `</span>
                        <a href="` + item.url + `" target="_blank" style="font-size: 12px; color: #333; text-decoration: none; font-weight: bold; line-height: 1.4; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; height: 3.6em;" onmouseover="this.style.color='#c00000'" onmouseout="this.style.color='#333'">` + item.title + `</a>
                    </div>
                `;
            });
            
            containerHtml += `
                <div id="most-read-slide-` + s + `" class="most-read-slide" style="display: ` + (s === 0 ? 'grid' : 'none') + `; grid-template-columns: repeat(5, 1fr); gap: 15px; opacity: ` + (s === 0 ? '1' : '0') + `; transition: opacity 0.4s ease;">
                    ` + slideItemsHtml + `
                </div>
            `;
            
            dotsHtml += `
                <span id="most-read-dot-` + s + `" onclick="switchMostReadSlide(` + s + `)" style="width: 8px; height: 8px; border-radius: 50%; background-color: ` + (s === 0 ? '#c00000' : '#ccc') + `; display: inline-block; cursor: pointer; transition: background-color 0.2s;"></span>
            `;
        }
        
        document.getElementById('most-read-container').innerHTML = containerHtml;
        document.getElementById('most-read-dots').innerHTML = dotsHtml;
        
        if (!window.switchMostReadSlide) {
            window.currentMostReadSlide = 0;
            window.switchMostReadSlide = function(slideIndex) {
                const slides = document.querySelectorAll('.most-read-slide');
                slides.forEach((slide, idx) => {
                    const el = document.getElementById('most-read-slide-' + idx);
                    const dot = document.getElementById('most-read-dot-' + idx);
                    if (idx === slideIndex) {
                        el.style.display = window.innerWidth <= 850 ? 'block' : 'grid';
                        setTimeout(() => { el.style.opacity = '1'; }, 20);
                        if (dot) dot.style.backgroundColor = '#c00000';
                    } else {
                        el.style.opacity = '0';
                        el.style.display = 'none';
                        if (dot) dot.style.backgroundColor = '#ccc';
                    }
                });
                window.currentMostReadSlide = slideIndex;
            };
            
            setInterval(() => {
                let nextSlide = (window.currentMostReadSlide + 1) % slideCount;
                window.switchMostReadSlide(nextSlide);
            }, 5000);
        }
    }

    function renderMediaSection() {
        let mediaPool = tphcmArticles.filter(a => a.category === "Xã hội" || a.category === "Thời sự").slice(5, 10);
        if (mediaPool.length < 4) {
            mediaPool = originalTphcmArticles.filter(a => a.category === "Xã hội" || a.category === "Thời sự").slice(5, 10);
        }
        if (mediaPool.length < 4) return;

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
        `;
        
        document.getElementById('media-col-2').innerHTML = `
            <div style="background-color:#ffffff; border:1px solid #ddd; border-radius:4px; padding:10px; display:flex; gap:10px;">
                <div style="width:100px; height:65px; overflow:hidden; border-radius:3px; flex-shrink:0; position:relative;">
                    <img src="` + mediaPool[2].image + `" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; bottom:3px; left:3px; color:red; font-size:12px;"><i class="fa fa-video-camera"></i></div>
                </div>
                <a href="` + mediaPool[2].url + `" target="_blank" style="text-decoration:none; font-size:12px; font-weight:bold; color:#111; line-height:1.3; display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical; overflow:hidden;">` + mediaPool[2].title + `</a>
            </div>
            <div style="background-color:#ffffff; border:1px solid #ddd; border-radius:4px; padding:10px; display:flex; gap:10px;">
                <div style="width:100px; height:65px; overflow:hidden; border-radius:3px; flex-shrink:0; position:relative;">
                    <img src="` + mediaPool[3].image + `" style="width:100%; height:100%; object-fit:cover;">
                    <div style="position:absolute; bottom:3px; left:3px; color:red; font-size:12px;"><i class="fa fa-video-camera"></i></div>
                </div>
                <a href="` + mediaPool[3].url + `" target="_blank" style="text-decoration:none; font-size:12px; font-weight:bold; color:#111; line-height:1.3; display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical; overflow:hidden;">` + mediaPool[3].title + `</a>
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
                    <div style="display:flex; gap:8px; border-top:1px solid #eee; padding-top:8px; margin-top:8px; min-height: 48px; line-height: 1.45;">
                        <a href="` + item.url + `" target="_blank" style="width: 50px; height: 35px; overflow:hidden; display:block; flex-shrink:0; border-radius: 2px;">
                            <img src="` + item.image + `" style="width:100%; height:100%; object-fit:cover;">
                        </a>
                        <a href="` + item.url + `" target="_blank" style="font-size:11.5px; color:#333; text-decoration:none; font-weight:bold; line-height:1.35; display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical; overflow:hidden; flex-grow: 1;">` + item.title + `</a>
                    </div>
                `;
            });
            
            return `
                <div style="background-color:#ffffff; border:1px solid #e3e3e3; border-radius:4px; padding:12px; font-family:Arial, sans-serif; display:flex; flex-direction:column; justify-content:flex-start; min-height: 380px; box-sizing: border-box;">
                    <div style="background-color:#f5f5f5; border-bottom:2px solid #c00000; padding:6px 10px; display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <span style="font-size:12px; font-weight:bold; color:#c00000; text-transform:uppercase;">` + categoryName + `</span>
                        <span style="color:#888; font-weight:bold; font-size:11px;">&gt;</span>
                    </div>
                    <a href="` + mainCat.url + `" target="_blank" style="display:block; overflow:hidden; height:105px; border-radius:3px; flex-shrink: 0; margin-bottom: 8px;">
                        <img src="` + mainCat.image + `" style="width:100%; height:100%; object-fit:cover; transition:transform 0.2s;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
                    </a>
                    <a href="` + mainCat.url + `" target="_blank" style="text-decoration:none; display:block; margin-bottom:10px; flex-shrink: 0;">
                        <h4 style="margin:0; font-size:13px; font-weight:bold; color:#111; line-height:1.4;">` + mainCat.title + `</h4>
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
                <h4 style="margin: 0 0 10px 0; font-size: 12px; font-weight: bold; color: #002d62; text-transform: uppercase; letter-spacing: 0.5px; display: flex; align-items: center; gap: 6px;">
                    📌 ${profile.title}
                </h4>
                ${profile.profileHtml}
            </div>
            <div>
                <h4 style="margin: 0 0 10px 0; font-size: 12px; font-weight: bold; color: #c00000; text-transform: uppercase; letter-spacing: 0.5px; display: flex; align-items: center; gap: 6px;">
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
                <div style="background: #fff; border: 1px solid #eee; border-left: 3px solid #b8860b; padding: 6px 10px; border-radius: 3px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); transition: all 0.2s;" onmouseover="this.style.transform='translateX(2px)'; this.style.borderColor='#b8860b';" onmouseout="this.style.transform='none'; this.style.borderColor='#eee';">
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
        changeDistrictPrices('caugiay');
        fetchHanoiWeather();
        updateProvincialProfileWidget('all');
        initInfraCarouselAutoplay();
        renderDirectoryPage();
    });
</script>
"""

# Replace placeholder
# Filter infrastructure articles
infra_keywords = ["vành đai", "cầu", "đường", "thi công", "quy hoạch", "hạ tầng", "giao thông", "gpmb", "giải phóng mặt bằng"]
infra_articles = []
for a in articles:
    title_lower = a['title'].lower()
    excerpt_lower = a['excerpt'].lower()
    if any(k in title_lower or k in excerpt_lower for k in infra_keywords):
        # Avoid duplicating the main featured story
        if a['id'] != articles[0]['id']:
            infra_articles.append(a)

# Fallbacks if database has too few matches
if len(infra_articles) < 5:
    for a in articles:
        if a not in infra_articles and a['id'] != articles[0]['id']:
            infra_articles.append(a)

infra_hero = infra_articles[0]
infra_list = infra_articles[1:4]

# Hero format badge (alternating Video / Infographic based on ID)
hero_badge = "📹 Video" if infra_hero['id'] % 2 == 0 else "📊 Infographic"

# Generate Desktop Left Hero Column
static_hero_html = f"""
                    <div class="infra-hero-card">
                        <div class="infra-hero-img-container">
                            <span class="infra-badge">{hero_badge}</span>
                            <a href="{infra_hero['url']}" target="_blank">
                                <img src="{infra_hero['image']}" alt="{infra_hero['title']}">
                            </a>
                        </div>
                        <div class="infra-hero-body">
                            <h3 class="infra-hero-title">
                                <a href="{infra_hero['url']}" target="_blank">{infra_hero['title']}</a>
                            </h3>
                            <p class="infra-hero-excerpt">{infra_hero['excerpt']}</p>
                        </div>
                    </div>
"""

# Generate Desktop Right List Column
static_list_items_html = ""
for item in infra_list:
    static_list_items_html += f"""
                        <div class="infra-list-item">
                            <h4 class="infra-list-title">
                                <a href="{item['url']}" target="_blank">{item['title']}</a>
                            </h4>
                            <div class="infra-list-meta">
                                <span>📅 {item['date']}</span>
                                <span>📍 {item['district']}</span>
                            </div>
                            <p class="infra-list-excerpt">{item['excerpt']}</p>
                        </div>
"""

# Generate Mobile Carousel slides (right-most peeks by 15-20% through class widths)
static_carousel_html = ""
for i, item in enumerate(infra_articles[:4]):
    badge_label = "📹 Video" if i % 2 == 0 else "📊 Infographic"
    static_carousel_html += f"""
                <div class="infra-carousel-card">
                    <div class="infra-carousel-img-container">
                        <span class="infra-badge">{badge_label}</span>
                        <a href="{item['url']}" target="_blank">
                            <img src="{item['image']}" alt="{item['title']}">
                        </a>
                    </div>
                    <div class="infra-carousel-body">
                        <h4 class="infra-carousel-title">
                            <a href="{item['url']}" target="_blank">{item['title']}</a>
                        </h4>
                    </div>
                </div>
"""

# Assemble full block HTML
static_infra_html = f"""
            <!-- CHUYỂN ĐỘNG HẠ TẦNG MODULE -->
            <div class="infra-block">
                <div class="infra-heading-container">
                    <span class="infra-heading-tag">Đô thị</span>
                    <h2 class="infra-heading">Chuyển động Hạ tầng</h2>
                </div>
                
                <!-- Desktop Grid Layout (6:4 Split) -->
                <div class="infra-grid">
                    <div class="pl">
                        {static_hero_html}
                    </div>
                    <div class="pr">
                        <div class="infra-list">
                            {static_list_items_html}
                        </div>
                    </div>
                </div>
                
                <!-- Mobile Carousel Layout -->
                <div class="infra-carousel-container" style="display: none;">
                    {static_carousel_html}
                </div>
            </div>
"""

middle_part = middle_part.replace("PLACEHOLDER_STATIC_INFRASTRUCTURE", static_infra_html)
middle_part = middle_part.replace("PLACEHOLDER_RAW_ARTICLES", js_all_articles_str)

# Combine HTML parts
full_html_content = header_part + middle_part + footer_part

# Save as tphcm_index_opt1_ads.html
ads_html_path = 'c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/tphcm_index_opt1_ads.html'
with open(ads_html_path, 'w', encoding='utf-8') as f:
    f.write(full_html_content)

# Save as tphcm_index_opt1_ads2.html for easy Vercel routing
index_ads_path = 'c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/tphcm_index_opt1_ads2.html'
with open(index_ads_path, 'w', encoding='utf-8') as f:
    f.write(full_html_content)

# Overwrite original root page tphcm_index_opt1_demo.html
orig_html_path = 'c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/tphcm_index_opt1_demo.html'
with open(orig_html_path, 'w', encoding='utf-8') as f:
    f.write(full_html_content)

# Overwrite tphcm_index_opt1.html for default Vercel routing
index_path = 'c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/tphcm_index_opt1.html'
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(full_html_content)

print("Demo TPHCM & Dong Nam Bo landing page compiled successfully!")
