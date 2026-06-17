import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Read consolidated 100% Hanoi articles
with open('c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/hanoi_final_consolidated.json', 'r', encoding='utf-8') as f:
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
            <div class="top-billboard-ad" style="background: linear-gradient(90deg, #0b1a30 0%, #00458e 50%, #0b1a30 100%); height: 120px; display: flex; align-items: center; justify-content: space-between; padding: 0 40px; color: #fff; position: relative;">
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
    /* Premium Design overrides for the lower half of the page */
    .premium-card {
        background: #ffffff !important;
        border: 1px solid #eef1f6 !important;
        border-radius: 12px !important;
        padding: 24px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02) !important;
        transition: all 0.3s ease !important;
        box-sizing: border-box;
    }
    .premium-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05) !important;
        border-color: #d1d8e0 !important;
    }
    .premium-header {
        font-family: Arial, sans-serif;
        font-size: 15px !important;
        font-weight: 800 !important;
        color: #002d62 !important;
        text-transform: uppercase;
        border-bottom: 2px solid #002d62 !important;
        padding-bottom: 10px !important;
        margin-bottom: 20px !important;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 10px;
    }
    .premium-header.red-theme {
        color: #c00000 !important;
        border-bottom-color: #c00000 !important;
    }
    .premium-header.gold-theme {
        color: #b8860b !important;
        border-bottom-color: #b8860b !important;
    }
    
    /* Category Columns Premium Styling */
    .category-card {
        background: #ffffff !important;
        border: 1px solid #eef1f6 !important;
        border-radius: 12px !important;
        padding: 16px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02) !important;
        transition: all 0.3s ease !important;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        min-height: 400px !important;
        box-sizing: border-box;
    }
    .category-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05) !important;
        border-color: #d1d8e0 !important;
    }
    .category-header {
        background: linear-gradient(90deg, #f8f9fa 0%, #ffffff 100%) !important;
        border-left: 3px solid #c00000 !important;
        border-bottom: 1px solid #eef1f6 !important;
        padding: 8px 12px !important;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px !important;
        border-radius: 0 4px 4px 0;
    }
    .category-header span:first-child {
        font-size: 13px !important;
        font-weight: 800 !important;
        color: #111 !important;
    }
    .category-header span:last-child {
        color: #c00000 !important;
    }
    .category-title {
        font-size: 14px !important;
        font-weight: 800 !important;
        color: #111 !important;
        line-height: 1.45 !important;
        margin-top: 5px !important;
        transition: color 0.2s;
    }
    .category-title:hover {
        color: #c00000 !important;
    }
    .category-list-item {
        display: flex;
        gap: 10px;
        border-top: 1px dashed #eef1f6 !important;
        padding-top: 10px !important;
        margin-top: 10px !important;
        min-height: 48px;
        align-items: center;
    }
    .category-list-link {
        font-size: 13px !important;
        color: #333 !important;
        text-decoration: none !important;
        font-weight: 700 !important;
        line-height: 1.4 !important;
        transition: color 0.2s;
    }
    .category-list-link:hover {
        color: #c00000 !important;
    }
    
    /* Interactive Market Table */
    .interactive-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 13px !important;
        text-align: left;
    }
    .interactive-table th {
        padding: 12px 10px !important;
        color: #444 !important;
        font-weight: 800 !important;
        background-color: #f8f9fa !important;
        border-bottom: 2px solid #eef1f6 !important;
    }
    .interactive-table td {
        padding: 12px 10px !important;
        border-bottom: 1px solid #f1f3f7 !important;
        color: #333 !important;
    }
    .interactive-table tr:hover td {
        background-color: #fafbfc !important;
    }
    
    .interactive-select {
        padding: 6px 12px !important;
        font-size: 12.5px !important;
        border: 1px solid #d1d8e0 !important;
        border-radius: 6px !important;
        font-weight: bold !important;
        color: #002d62 !important;
        background-color: #ffffff !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        outline: none;
        cursor: pointer;
        transition: border-color 0.2s;
    }
    .interactive-select:focus {
        border-color: #002d62 !important;
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
                    <span style="color: #c00000; font-weight: bold;">Hà Nội</span>
                </div>
                
                <!-- Quick Links & Real-time Hanoi Weather Widget Grouped -->
                <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
                    <a href="https://laodong.vn/tags/lich-cat-dien-ha-noi-8541.ldo" target="_blank" style="text-decoration: none; font-size: 12px; color: #c00000; font-weight: bold; display: flex; align-items: center; gap: 3px;">⚡ Lịch cắt điện</a>
                    <span style="color: #ccc;">|</span>
                    <a href="https://laodong.vn/phap-luat/chinh-sach-moi" target="_blank" style="text-decoration: none; font-size: 12px; color: #002d62; font-weight: bold; display: flex; align-items: center; gap: 3px;">📋 Chính sách mới</a>
                    <span style="color: #ccc;">|</span>
                    <a href="https://laodong.vn/kinh-doanh/gia-vang" target="_blank" style="text-decoration: none; font-size: 12px; color: #b8860b; font-weight: bold; display: flex; align-items: center; gap: 3px;">🪙 Giá vàng</a>
                    <span style="color: #ccc;">|</span>
                    
                    <a href="https://weather.com/vi-VN/weather/today/l/VMXX0006:1:VM" target="_blank" title="Xem dự báo chi tiết tại Weather.com (Nguồn uy tín)" id="hanoi-weather-widget" style="text-decoration: none; display: flex; align-items: center; gap: 8px; background: rgba(240, 244, 248, 0.85); border: 1px solid #d0e1f9; padding: 4px 12px; border-radius: 20px; font-size: 12px; color: #002d62; box-shadow: 0 1px 3px rgba(0,0,0,0.05); font-weight: bold; transition: all 0.2s ease;" onmouseover="this.style.background='rgba(224, 235, 250, 0.95)'; this.style.transform='translateY(-1px)';" onmouseout="this.style.background='rgba(240, 244, 248, 0.85)'; this.style.transform='none';">
                        <span>📅 <span id="current-date-vietnam">Chủ nhật, 31/05/2026</span></span>
                        <span style="color: #ccc;">|</span>
                        <span id="weather-temp-span">📍 Hà Nội: Đang tải...</span>
                    </a>
                </div>
            </div>

            <!-- NATIVE LAO DONG BREADCRUMBS / TITLE SECTION -->
            <div class="breadcrums" style="border-bottom: 2px solid #eee; padding-bottom: 10px; margin-top: 15px;">
                <h1 style="margin: 0; font-size: 22px; font-weight: bold; font-family: Arial, sans-serif;">
                    <a class="main-cat-lnk" href="#" style="color: #000000; text-decoration: none;" id="dynamic-page-title">Trang Hà Nội</a>
                </h1>
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
                        <div style="font-size: 13px; font-weight: bold; color: #c00000; text-transform: uppercase; margin-bottom: 12px; border-bottom: 2px solid #c00000; padding-bottom: 5px;">Tiêu điểm Hà Nội</div>
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

                        <!-- Interactive Poll (Khảo sát dư luận) -->
                        <div class="premium-card" style="box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between; margin-top: 15px;">
                            <div>
                                <div style="font-size: 13.5px; font-weight: bold; color: #002d62; text-transform: uppercase; border-bottom: 2px solid #002d62; padding-bottom: 6px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
                                    <span>📊 Khảo sát Dư luận Thủ đô</span>
                                    <span style="font-size: 9px; color: #c00000; font-weight: bold; border: 1px solid #c00000; padding: 2px 5px; border-radius: 2px;">VOTE</span>
                                </div>
                                
                                <div id="poll-container">
                                    <h4 style="margin: 0 0 12px 0; font-size: 12.5px; font-weight: bold; color: #333; line-height: 1.45;">Bạn ủng hộ việc tiếp tục mở rộng thêm các tuyến phố đi bộ vào cuối tuần tại Hà Nội không?</h4>
                                    <div style="display: flex; flex-direction: column; gap: 8px;">
                                        <button onclick="submitPollVote('yes')" style="background: #ffffff; border: 1px solid #ddd; padding: 10px; border-radius: 4px; text-align: left; font-size: 11.5px; cursor: pointer; font-weight: bold; color: #333; transition: all 0.2s;" onmouseover="this.style.borderColor='#002d62'; this.style.backgroundColor='#f7f9fb';" onmouseout="this.style.borderColor='#ddd'; this.style.backgroundColor='#fff';">👍 Đồng ý, cần nhân rộng mô hình này</button>
                                        <button onclick="submitPollVote('no')" style="background: #ffffff; border: 1px solid #ddd; padding: 10px; border-radius: 4px; text-align: left; font-size: 11.5px; cursor: pointer; font-weight: bold; color: #333; transition: all 0.2s;" onmouseover="this.style.borderColor='#002d62'; this.style.backgroundColor='#f7f9fb';" onmouseout="this.style.borderColor='#ddd'; this.style.backgroundColor='#fff';">👎 Không đồng ý, gây ùn tắc giao thông cục bộ</button>
                                        <button onclick="submitPollVote('neutral')" style="background: #ffffff; border: 1px solid #ddd; padding: 10px; border-radius: 4px; text-align: left; font-size: 11.5px; cursor: pointer; font-weight: bold; color: #333; transition: all 0.2s;" onmouseover="this.style.borderColor='#002d62'; this.style.backgroundColor='#f7f9fb';" onmouseout="this.style.borderColor='#ddd'; this.style.backgroundColor='#fff';">😐 Đồng ý nhưng cần quy hoạch bãi đỗ xe hợp lý</button>
                                    </div>
                                </div>
                            </div>
                            <div style="font-size: 9px; color: #888; margin-top: 15px; border-top: 1px solid #eee; padding-top: 8px; text-align: center;">
                                Khảo sát mang tính chất tham khảo dư luận phục vụ bài viết chuyên đề.
                            </div>
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
                    <h2 style="font-size: 20px; font-weight: bold; color: #c00000; margin: 0; text-transform: uppercase;">Media Hà Nội</h2>
                    <div style="display: flex; gap: 15px; font-size: 12px; font-weight: bold;">
                        <span style="color:#555;">Lao Động TV</span>
                        <span style="color:#555;">Hyper Text</span>
                        <span style="color:#555;">Photo</span>
                        <span style="color:#555;">Podcast</span>
                    </div>
                </div>
                
                <div style="display: grid; grid-template-columns: 1.2fr 2fr; gap: 15px;" class="columns-layout">
                    <!-- Left: TV Frame -->
                    <div style="background-color: #ffffff; padding: 15px; border-radius: 6px; border: 1px solid #ddd; display: flex; flex-direction: column; justify-content: space-between; box-sizing: border-box; min-height: 280px;" class="premium-card">
                        <div style="background: linear-gradient(135deg, #ccc 0%, #999 50%, #bbb 100%); padding: 10px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
                            <div style="background-color: #000; width: 100%; height: 180px; border-radius: 6px; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center;">
                                <img src="https://media-cdn-v2.laodong.vn/laodong/2.0.0.35/images/logo/ldo_red.png" height="50" style="opacity: 0.8;" id="tv-player-img">
                                <div style="position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,0.7); color: #fff; padding: 2px 6px; font-size: 10px; border-radius: 3px; font-weight: bold;">LIVE</div>
                            </div>
                            <div style="text-align: center; color: #333; font-size: 10px; font-weight: bold; margin-top: 5px; text-shadow: 1px 1px 1px #fff; letter-spacing: 2px;">LAODONG TV</div>
                        </div>
                        <div style="margin-top: 10px; border-top: 1px solid #eee; padding-top: 10px;">
                            <span style="font-size: 11px; background-color: #c00000; color: #fff; font-weight: bold; padding: 2px 6px; text-transform: uppercase;">Lịch phát sóng:</span>
                            <marquee style="font-size: 12px; color: #333; margin-top: 5px; font-weight: bold;" scrollamount="3">09:00 - Tin tức cập nhật sáng Thủ đô  |  12:00 - Bản tin Lao động Công đoàn Hà Nội  |  20:00 - Bản tin Thời sự Tổng hợp Hà Nội 24h</marquee>
                        </div>
                    </div>
                    
                    <!-- Right: Media Cards Wrapper -->
                    <div style="background-color: #ffffff; padding: 15px; border-radius: 6px; border: 1px solid #ddd; display: grid; grid-template-columns: 1fr 1fr; gap: 15px; box-sizing: border-box; height: 100%;" class="premium-card">
                        <div style="display: flex; flex-direction: column; gap: 10px; justify-content: space-between; height: 100%;" id="media-col-1">
                            <!-- JS populated -->
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 10px; justify-content: space-between; height: 100%;" id="media-col-2">
                            <!-- JS populated -->
                        </div>
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
                    <span style="background-color: rgba(255,255,255,0.15); color: #fff; padding: 4px 12px; border-radius: 4px; font-size: 11px; font-weight: bold; cursor: pointer;">Quy hoạch Hà Nội</span>
                    <span style="background-color: rgba(255,255,255,0.15); color: #fff; padding: 4px 12px; border-radius: 4px; font-size: 11px; font-weight: bold; cursor: pointer;">Tuyển sinh lớp 10 Hà Nội</span>
                    <span style="background-color: rgba(255,255,255,0.15); color: #fff; padding: 4px 12px; border-radius: 4px; font-size: 11px; font-weight: bold; cursor: pointer;">Vành đai 4 Thủ đô</span>
                </div>
            </div>

            <!-- BLOCK 4.5: SPONSORED SPECIAL HUBS -->
            <div class="m-top-20" style="background-color: #fcf9f2; border: 1px solid #e5d3b3; border-top: 3px solid #b8860b; border-radius: 8px; padding: 20px; font-family: Arial, sans-serif;">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #b8860b; padding-bottom: 8px; margin-bottom: 15px;">
                    <h2 style="font-size: 16px; font-weight: bold; color: #7f0000; margin: 0; text-transform: uppercase; display: flex; align-items: center; gap: 8px;">
                        <span>💎 Chuyên đề Đồng hành: HÀ NỘI 360°</span>
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
                            Bản đồ ẩm thực phố cổ: Những món ăn sáng gia truyền nhất định phải thử tại Hà Nội
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
                <div class="premium-card" style="display: flex; flex-direction: column; justify-content: space-between;">
                    <div style="font-size: 14px; font-weight: bold; color: #002d62; text-transform: uppercase; border-bottom: 2px solid #002d62; padding-bottom: 6px; margin-bottom: 15px;">Dân sinh & Đời sống Hà Nội</div>
                    <div class="nested-responsive-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
                        <!-- Item 1: Worker Life -->
                        <div style="border: 1px solid #eee; border-radius: 4px; padding: 10px; position: relative;">
                            <span style="position: absolute; top: 12px; left: 12px; background: rgba(192,0,0,0.85); color: #fff; font-size: 7px; font-weight: bold; padding: 2px 4px; border-radius: 2px; z-index: 2;">QC GIẢ LẬP</span>
                            <div style="height: 100px; overflow: hidden; border-radius: 3px;">
                                <img src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=400&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                            </div>
                            <h4 style="margin: 8px 0 0 0; font-size: 12px; font-weight: bold; line-height: 1.3;">
                                <span style="color: #002d62; font-size: 9px; font-weight: bold; display: block; text-transform: uppercase; margin-bottom: 2px;">Cẩm nang Công nhân KCN</span>
                                Danh sách nhà trọ an toàn, giá rẻ cho công nhân tại KCN Bắc Thăng Long năm 2026
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
                                Top 5 khu cắm trại và homestay dịch vụ xanh cực đẹp tại Ba Vì cho gia đình
                            </h4>
                        </div>
                    </div>
                    
                    <!-- JOB BOARD: VIỆC LÀM HÀ NỘI -->
                    <div style="border-top: 1px solid #eee; padding-top: 15px; margin-bottom: 15px;">
                        <div style="font-size: 13px; font-weight: bold; color: #c00000; text-transform: uppercase; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center;">
                            <span>💼 Việc làm tại Hà Nội (Tuyển dụng nhanh)</span>
                            <span style="font-size: 9.5px; color: #666; font-weight: normal; text-transform: none;">Liên kết: Trung tâm Dịch vụ việc làm Hà Nội</span>
                        </div>
                        <div style="display: flex; flex-direction: column; gap: 8px;">
                            <!-- Job 1 -->
                            <div class="job-item" style="display: flex; justify-content: space-between; align-items: center; background-color: #fcfcfc; border: 1px solid #eee; padding: 8px 12px; border-radius: 4px; position: relative;">
                                <span style="position: absolute; right: 85px; top: 12px; font-size: 7.5px; color: #d71920; border: 1px solid #d71920; padding: 1px 3px; border-radius: 2px; font-weight: bold; text-transform: uppercase;">Gấp</span>
                                <div style="text-align: left;">
                                    <strong style="font-size: 11.5px; color: #333; display: block;">Nhân viên lắp ráp linh kiện điện tử (KCN Bắc Thăng Long)</strong>
                                    <span style="font-size: 9.5px; color: #666;">Công ty TNHH Canon Việt Nam | Thu nhập: 8.5 - 11 triệu VNĐ</span>
                                </div>
                                <a href="#" style="background-color: #c00000; color: #fff; text-decoration: none; font-size: 10px; font-weight: bold; padding: 5px 10px; border-radius: 3px;">Nộp hồ sơ</a>
                            </div>
                            <!-- Job 2 -->
                            <div class="job-item" style="display: flex; justify-content: space-between; align-items: center; background-color: #fcfcfc; border: 1px solid #eee; padding: 8px 12px; border-radius: 4px;">
                                <div style="text-align: left;">
                                    <strong style="font-size: 11.5px; color: #333; display: block;">Kỹ thuật viên vận hành máy tiện cơ khí CNC</strong>
                                    <span style="font-size: 9.5px; color: #666;">Tập đoàn Cơ khí Hà Nội (KCN Thạch Thất) | Thu nhập: 10 - 13.5 triệu VNĐ</span>
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
                                    <strong style="font-size: 11px; color: #333; display: block;">Hố ga mất nắp gây nguy hiểm tại ngã tư Lê Văn Lương - Hoàng Minh Giám</strong>
                                    <span style="font-size: 9px; color: #666;">Độc giả 098****321 | ⏰ 15 phút trước</span>
                                </div>
                                <span style="background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; font-size: 9px; padding: 2px 6px; border-radius: 3px; font-weight: bold; flex-shrink: 0;">Đang xử lý</span>
                            </div>
                            <!-- Seed Report 2 -->
                            <div style="background-color: #fafbfc; border: 1px solid #e9ecef; border-left: 3px solid #28a745; padding: 8px 12px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <strong style="font-size: 11px; color: #333; display: block;">Rác thải sinh hoạt ùn ứ gây mùi hôi thối cạnh trường Tiểu học Dịch Vọng</strong>
                                    <span style="font-size: 9px; color: #666;">Độc giả 090****888 | ⏰ 2 giờ trước</span>
                                </div>
                                <span style="background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; font-size: 9px; padding: 2px 6px; border-radius: 3px; font-weight: bold; flex-shrink: 0;">Đã giải quyết</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Right: Local Business Directory -->
                <div class="premium-card" style="display: flex; flex-direction: column; box-sizing: border-box;">
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
            </div>

            <!-- BLOCK 5.7: BẢNG GIÁ THỊ TRƯỜNG DÂN SINH HÀ NỘI (MÔ PHỎNG TIẾP THỊ LIÊN KẾT & TÀI TRỢ SIÊU THỊ) -->
            <div class="m-top-20 columns-layout" style="display: grid; grid-template-columns: 2fr 1.2fr; gap: 20px; font-family: Arial, sans-serif;">
                <!-- Left: Interactive Price Table -->
                <div class="premium-card" style="box-sizing: border-box;">
                    <div style="font-size: 14px; font-weight: bold; color: #002d62; text-transform: uppercase; border-bottom: 2px solid #002d62; padding-bottom: 6px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                        <span>📊 Bảng giá thị trường dân sinh Hà Nội</span>
                        <div style="display: flex; align-items: center; gap: 5px;">
                            <span style="font-size: 11px; color: #555; font-weight: normal; text-transform: none;">Khu vực:</span>
                            <select id="price-district-select" onchange="changeDistrictPrices(this.value)" class="interactive-select">
                                <option value="hoankiem">Quận Hoàn Kiếm</option>
                                <option value="caugiay" selected>Quận Cầu Giấy</option>
                                <option value="hadong">Quận Hà Đông</option>
                                <option value="bavi">Huyện Ba Vì</option>
                            </select>
                        </div>
                    </div>
                    
                    <table class="interactive-table">
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
                            <p style="margin: 0; font-size: 12px; color: #444; line-height: 1.45;">Đón hè rực rỡ cùng hàng ngàn ưu đãi giải nhiệt từ siêu thị WinMart Hà Nội! Tiết kiệm lên tới 20% các mặt hàng tươi sống, thịt sạch & rau sạch mỗi ngày!</p>
                        </div>
                        <a href="https://winmart.vn" target="_blank" style="background-color: #d71920; color: #ffffff; text-decoration: none; font-size: 11px; font-weight: bold; padding: 10px 0; border-radius: 4px; text-transform: uppercase; text-align: center; display: block; box-shadow: 0 2px 5px rgba(215,25,32,0.2); transition: all 0.2s;" onmouseover="this.style.backgroundColor='#bd141b';" onmouseout="this.style.backgroundColor='#d71920';">Đăng ký hội viên miễn phí</a>
                    </div>
                </div>
            </div>

            <!-- BLOCK 5.75: LỊCH BIỂU DIỄN & GIẢI TRÍ HÀ NỘI (MÔ PHỎNG KẾT NỐI API THỜI GIAN THỰC) -->
            <div class="m-top-20 columns-layout" style="display: grid; grid-template-columns: 1.8fr 1.2fr; gap: 20px; font-family: Arial, sans-serif;">
                <!-- Left: Theatre, Circus, Shows + Exhibitions & Events -->
                <div class="premium-card">
                    <div style="font-size: 14px; font-weight: bold; color: #002d62; text-transform: uppercase; border-bottom: 2px solid #002d62; padding-bottom: 6px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                        <span>🎭 Lịch biểu diễn & Triển lãm Hà Nội</span>
                        <span style="font-size: 9px; color: #28a745; font-weight: bold; border: 1px solid #28a745; padding: 2px 5px; border-radius: 2px;">LIVE API CONNECTED</span>
                    </div>
                    
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;" class="columns-layout">
                        <!-- Column 1: Sân khấu & Nghệ thuật -->
                        <div style="border-right: 1px solid #eee; padding-right: 15px;">
                            <div style="font-size: 11.5px; font-weight: bold; color: #c00000; text-transform: uppercase; margin-bottom: 10px;">🎭 Sân khấu & Ca nhạc</div>
                            <div style="display: flex; flex-direction: column; gap: 12px;">
                                <!-- Show 1 -->
                                <div style="display: flex; gap: 10px; align-items: center; border-bottom: 1px solid #f9f9f9; padding-bottom: 8px;">
                                    <div style="background-color: #ffeef0; color: #d71920; font-size: 9.5px; font-weight: bold; padding: 6px; text-align: center; border-radius: 4px; width: 42px; flex-shrink: 0; line-height: 1.2;">
                                        30<br><span style="font-size: 7.5px; font-weight: normal;">Th5</span>
                                    </div>
                                    <div style="flex-grow: 1;">
                                        <span style="background-color: #f5f5f5; color: #888; border: 1px solid #ddd; padding: 0 3px; font-size: 7.5px; font-weight: bold; border-radius: 2px; margin-right: 4px;">PR Pinned</span>
                                        <h4 style="margin: 0 0 2px 0; font-size: 11.5px; font-weight: bold; color: #111; line-height: 1.3;">Hòa nhạc: "Đêm mùa thu Hà Nội"</h4>
                                        <span style="font-size: 9.5px; color: #666; display: block;">📍 Nhà hát Lớn | ⏰ 19:30</span>
                                    </div>
                                    <a href="https://ticketbox.vn" target="_blank" style="background-color: #002d62; color: #fff; text-decoration: none; padding: 4px 8px; border-radius: 3px; font-size: 9.5px; font-weight: bold; flex-shrink: 0;">Đặt vé</a>
                                </div>
                                <!-- Show 2 -->
                                <div style="display: flex; gap: 10px; align-items: center; border-bottom: 1px solid #f9f9f9; padding-bottom: 8px;">
                                    <div style="background-color: #e5f1ff; color: #00458e; font-size: 9.5px; font-weight: bold; padding: 6px; text-align: center; border-radius: 4px; width: 42px; flex-shrink: 0; line-height: 1.2;">
                                        31<br><span style="font-size: 7.5px; font-weight: normal;">Th5</span>
                                    </div>
                                    <div style="flex-grow: 1;">
                                        <h4 style="margin: 0 0 2px 0; font-size: 11.5px; font-weight: bold; color: #111; line-height: 1.3;">Kịch xiếc: "Vòng quay diệu kỳ"</h4>
                                        <span style="font-size: 9.5px; color: #666; display: block;">📍 Rạp xiếc TW | ⏰ 10:00 & 20:00</span>
                                    </div>
                                    <a href="https://ticketbox.vn" target="_blank" style="background-color: #002d62; color: #fff; text-decoration: none; padding: 4px 8px; border-radius: 3px; font-size: 9.5px; font-weight: bold; flex-shrink: 0;">Đặt vé</a>
                                </div>
                                <!-- Show 3 -->
                                <div style="display: flex; gap: 10px; align-items: center;">
                                    <div style="background-color: #f6f0ff; color: #7a22ff; font-size: 9.5px; font-weight: bold; padding: 6px; text-align: center; border-radius: 4px; width: 42px; flex-shrink: 0; line-height: 1.2;">
                                        01<br><span style="font-size: 7.5px; font-weight: normal;">Th6</span>
                                    </div>
                                    <div style="flex-grow: 1;">
                                        <h4 style="margin: 0 0 2px 0; font-size: 11.5px; font-weight: bold; color: #111; line-height: 1.3;">Múa rối nước cổ truyền (Dành cho 1/6)</h4>
                                        <span style="font-size: 9.5px; color: #666; display: block;">📍 Rạp Thăng Long | ⏰ 15:00 & 17:00</span>
                                    </div>
                                    <a href="https://ticketbox.vn" target="_blank" style="background-color: #002d62; color: #fff; text-decoration: none; padding: 4px 8px; border-radius: 3px; font-size: 9.5px; font-weight: bold; flex-shrink: 0;">Đặt vé</a>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Column 2: Triển lãm & Sự kiện khác -->
                        <div>
                            <div style="font-size: 11.5px; font-weight: bold; color: #002d62; text-transform: uppercase; margin-bottom: 10px;">🖼️ Triển lãm & Sự kiện khác</div>
                            <div style="display: flex; flex-direction: column; gap: 12px;">
                                <!-- Event 1 -->
                                <div style="display: flex; gap: 10px; align-items: center; border-bottom: 1px solid #f9f9f9; padding-bottom: 8px;">
                                    <div style="background-color: #eafaf1; color: #2ecc71; font-size: 9.5px; font-weight: bold; padding: 6px; text-align: center; border-radius: 4px; width: 42px; flex-shrink: 0; line-height: 1.2;">
                                        30<br><span style="font-size: 7.5px; font-weight: normal;">Th5</span>
                                    </div>
                                    <div style="flex-grow: 1;">
                                        <span style="background-color: #e8f5e9; color: #2e7d32; padding: 0 4px; font-size: 7.5px; font-weight: bold; border-radius: 2px; margin-right: 4px;">Free Entry</span>
                                        <h4 style="margin: 0 0 2px 0; font-size: 11.5px; font-weight: bold; color: #111; line-height: 1.3;">Triển lãm tranh: "Sắc màu Hà Nội"</h4>
                                        <span style="font-size: 9.5px; color: #666; display: block;">📍 Bảo tàng Mỹ thuật VN | ⏰ 9:00 - 17:00</span>
                                    </div>
                                    <a href="https://ticketbox.vn" target="_blank" style="background-color: #002d62; color: #fff; text-decoration: none; padding: 4px 8px; border-radius: 3px; font-size: 9.5px; font-weight: bold; flex-shrink: 0;">Chi tiết</a>
                                </div>
                                <!-- Event 2 -->
                                <div style="display: flex; gap: 10px; align-items: center; border-bottom: 1px solid #f9f9f9; padding-bottom: 8px;">
                                    <div style="background-color: #fff9db; color: #f59f00; font-size: 9.5px; font-weight: bold; padding: 6px; text-align: center; border-radius: 4px; width: 42px; flex-shrink: 0; line-height: 1.2;">
                                        31<br><span style="font-size: 7.5px; font-weight: normal;">Th5</span>
                                    </div>
                                    <div style="flex-grow: 1;">
                                        <h4 style="margin: 0 0 2px 0; font-size: 11.5px; font-weight: bold; color: #111; line-height: 1.3;">Lễ hội ẩm thực: "Hương vị Thủ đô"</h4>
                                        <span style="font-size: 9.5px; color: #666; display: block;">📍 CV Thống Nhất | ⏰ 8:00 - 22:00</span>
                                    </div>
                                    <a href="https://ticketbox.vn" target="_blank" style="background-color: #002d62; color: #fff; text-decoration: none; padding: 4px 8px; border-radius: 3px; font-size: 9.5px; font-weight: bold; flex-shrink: 0;">Đăng ký</a>
                                </div>
                                <!-- Event 3 -->
                                <div style="display: flex; gap: 10px; align-items: center;">
                                    <div style="background-color: #fff0f6; color: #d6336c; font-size: 9.5px; font-weight: bold; padding: 6px; text-align: center; border-radius: 4px; width: 42px; flex-shrink: 0; line-height: 1.2;">
                                        02<br><span style="font-size: 7.5px; font-weight: normal;">Th6</span>
                                    </div>
                                    <div style="flex-grow: 1;">
                                        <h4 style="margin: 0 0 2px 0; font-size: 11.5px; font-weight: bold; color: #111; line-height: 1.3;">Triển lãm ảnh: "Ký ức Hà Nội xưa"</h4>
                                        <span style="font-size: 9.5px; color: #666; display: block;">📍 Triển lãm Đinh Tiên Hoàng | ⏰ 8:30</span>
                                    </div>
                                    <a href="https://ticketbox.vn" target="_blank" style="background-color: #002d62; color: #fff; text-decoration: none; padding: 4px 8px; border-radius: 3px; font-size: 9.5px; font-weight: bold; flex-shrink: 0;">Chi tiết</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Right: Cinema Cinema / Showtimes -->
                <div class="premium-card" style="box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="font-size: 14px; font-weight: bold; color: #c00000; text-transform: uppercase; border-bottom: 2px solid #c00000; padding-bottom: 6px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
                            <span>🎬 Suất chiếu phim rạp Hà Nội</span>
                            <span style="font-size: 9px; color: #888; font-weight: normal; text-transform: none;">CGV & Lotte</span>
                        </div>
                        
                        <div style="display: flex; flex-direction: column; gap: 8px;">
                            <!-- Movie 1 -->
                            <div style="border: 1px solid #eee; padding: 6px 10px; border-radius: 3px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <strong style="font-size: 11px; color: #333; display: block;">🎬 Điệp vụ bất khả thi: Tái sinh</strong>
                                    <span style="font-size: 9px; color: #888;">CGV Vincom Bà Triệu | Suất: 18:30, 20:45</span>
                                </div>
                                <span style="background-color: #28a745; color: #fff; font-size: 8px; padding: 2px 4px; border-radius: 2px; font-weight: bold;">Còn vé</span>
                            </div>
                            <!-- Movie 2 -->
                            <div style="border: 1px solid #eee; padding: 6px 10px; border-radius: 3px; display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <strong style="font-size: 11px; color: #333; display: block;">🎬 Kẻ hủy diệt mới (2D Vietsub)</strong>
                                    <span style="font-size: 9px; color: #888;">Trung tâm Chiếu phim Quốc gia | Suất: 19:00, 21:30</span>
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
            <div class="m-top-20 columns-layout" style="font-family: Arial, sans-serif; display: grid; grid-template-columns: 1.2fr 1fr; gap: 20px;">
                <!-- Labor Overtime Pay Calculator (Tính lương tăng ca tự động) -->
                <div class="premium-card" style="box-sizing: border-box; max-width: 100%;">
                    <div style="font-size: 14px; font-weight: bold; color: #c00000; text-transform: uppercase; border-bottom: 2px solid #c00000; padding-bottom: 6px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                        <span>⚖️ Tự tính Lương tăng ca (Luật LĐ 2019)</span>
                        <span style="font-size: 9px; color: #28a745; font-weight: bold; border: 1px solid #28a745; padding: 2px 5px; border-radius: 2px;">TIỆN ÍCH LAO ĐỘNG</span>
                    </div>
                    
                    <div style="display: flex; flex-direction: column; gap: 12px; font-size: 12px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <label style="font-weight: bold; color: #333;">Lương cơ bản (đồng/giờ):</label>
                            <input type="number" id="labor-hourly-wage" value="30000" style="width: 120px; padding: 4px; border: 1px solid #ccc; border-radius: 3px; font-weight: bold; text-align: right; color: #002d62;">
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <label style="font-weight: bold; color: #333;">Số giờ làm thêm:</label>
                            <input type="number" id="labor-overtime-hours" value="4" style="width: 120px; padding: 4px; border: 1px solid #ccc; border-radius: 3px; font-weight: bold; text-align: right; color: #002d62;">
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <label style="font-weight: bold; color: #333;">Thời điểm tăng ca:</label>
                            <select id="labor-overtime-type" style="width: 140px; padding: 4px; border: 1px solid #ccc; border-radius: 3px; font-weight: bold; color: #002d62;">
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

                <!-- Land Price Lookup widget -->
                <div class="premium-card" style="box-sizing: border-box; max-width: 100%;">
                    <div style="font-size: 14px; font-weight: bold; color: #c00000; text-transform: uppercase; border-bottom: 2px solid #c00000; padding-bottom: 6px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                        <span>📍 Tra cứu giá đất địa phương</span>
                        <span style="font-size: 9px; color: #002d62; font-weight: bold; border: 1px solid #002d62; padding: 2px 5px; border-radius: 2px;">BATDONGSAN.COM.VN COOP</span>
                    </div>
                    
                    <div style="display: flex; flex-direction: column; gap: 12px; font-size: 12px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <label style="font-weight: bold; color: #333;">Chọn Quận/Huyện:</label>
                            <select id="land-district" onchange="updateLandStreets()" style="width: 150px; padding: 4px; border: 1px solid #ccc; border-radius: 3px; font-weight: bold; color: #002d62;">
                                <!-- Will populate dynamically -->
                            </select>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <label style="font-weight: bold; color: #333;">Chọn tuyến đường:</label>
                            <select id="land-street" onchange="showLandPrice()" style="width: 150px; padding: 4px; border: 1px solid #ccc; border-radius: 3px; font-weight: bold; color: #002d62;">
                                <!-- Will populate dynamically -->
                            </select>
                        </div>
                        
                        <div id="land-price-result" style="background-color: #f7f9fb; border: 1px dashed #ccc; padding: 10px; border-radius: 4px; display: none;">
                            <!-- Calculated result populated here -->
                        </div>
                    </div>
                </div>
            </div>

            <!-- BLOCK 5.8: CẨM NANG HÀ NỘI: ĂN GÌ - CHƠI GÌ - Ở ĐÂU? (MÔ PHỎNG NATIVE PR ĐỊA PHƯƠNG) -->
            <div class="m-top-20" style="background-color: #ffffff; border: 1px solid #e3e3e3; border-radius: 8px; padding: 20px; font-family: Arial, sans-serif;">
                <div style="font-size: 14px; font-weight: bold; color: #c00000; text-transform: uppercase; border-bottom: 2px solid #c00000; padding-bottom: 6px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <span>🗺️ Cẩm nang Hà Nội: Ăn gì - Chơi gì - Ở đâu?</span>
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
                                    <a href="#" style="font-size: 11.5px; font-weight: bold; color: #333; text-decoration: none; line-height: 1.3;">Bản đồ các quán ốc vỉa hè ngon rẻ thu hút đông đảo giới trẻ Hà Nội</a>
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
                                    <a href="#" style="font-size: 11.5px; font-weight: bold; color: #333; text-decoration: none; line-height: 1.3;">Review biệt thự sinh thái Ba Vì ngập tràn cây xanh dành cho kỳ nghỉ gia đình</a>
                                </div>
                            </div>
                            <div style="display: flex; gap: 8px; align-items: center;">
                                <div style="width: 50px; height: 35px; overflow: hidden; border-radius: 2px; flex-shrink: 0;">
                                    <img src="https://images.unsplash.com/photo-1569154941061-e231b4725ef1?auto=format&fit=crop&w=100&q=80" style="width: 100%; height: 100%; object-fit: cover;">
                                </div>
                                <div>
                                    <a href="#" style="font-size: 11.5px; font-weight: bold; color: #333; text-decoration: none; line-height: 1.3;">Top khách sạn boutique mang đậm kiến trúc Pháp cổ ngay cạnh hồ Hoàn Kiếm</a>
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
                <div style="font-size: 13px; font-weight: bold; color: #fff;">Sở hữu xe điện thông minh VinFast hôm nay - Hỗ trợ 100% lệ phí trước bạ & Sạc pin miễn phí 1 năm tại Hà Nội!</div>
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
                Đây là cổng tiếp nhận phản ánh dân sinh và tư vấn pháp luật Lao động tự động của Báo Lao Động Hà Nội.
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
                    <span>💼 Tra cứu Việc làm Hà Nội mới nhất</span> <span>➔</span>
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
                    Tôi muốn tìm kiếm Việc làm Hà Nội
                </div>
                <div style="align-self: flex-start; background-color: #fff; border: 1px solid #e3e3e3; padding: 10px; border-radius: 8px; max-width: 85%; margin-top: 5px;">
                    🔍 Tìm thấy <strong>2 việc làm khẩn cấp</strong> trên địa bàn Hà Nội hôm nay:
                    <ul style="padding-left: 15px; margin: 5px 0;">
                        <li><strong>Canon Việt Nam</strong> (KCN Bắc Thăng Long) - Lắp ráp linh kiện điện tử (8.5 - 11 triệu)</li>
                        <li><strong>Tập đoàn Cơ khí Hà Nội</strong> (CNC Thạch Thất) - Vận hành máy tiện (10 - 13.5 triệu)</li>
                    </ul>
                    Bạn có thể nộp hồ sơ trực tiếp tại bảng "Việc làm tại Hà Nội" nằm ở giữa trang!
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
                Hệ thống đã chuyển thông tin đến <strong>Văn phòng đại diện Báo Lao Động tại Hà Nội</strong> và đồng gửi đến cơ quan quản lý địa bàn. Cảm ơn sự cộng tác dân sinh của bạn.
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
        caugiay: [
            { name: "🥩 Thịt ba rọi heo sạch MEATDeli", normal: "135.000 đ/kg", winmart: "119.000 đ/kg", discount: "12%" },
            { name: "🥬 Rau muống hữu cơ sông Hồng", normal: "15.000 đ/bó", winmart: "12.000 đ/bó", discount: "20%" },
            { name: "🐟 Cá trắm đen tươi sống Ba Vì", normal: "110.000 đ/kg", winmart: "98.000 đ/kg", discount: "11%" },
            { name: "🍚 Gạo tám thơm Điện Biên (Túi 5kg)", normal: "145.000 đ/túi", winmart: "128.000 đ/túi", discount: "12%" }
        ],
        hoankiem: [
            { name: "🥩 Thịt ba rọi heo sạch MEATDeli", normal: "145.000 đ/kg", winmart: "122.000 đ/kg", discount: "15%" },
            { name: "🥬 Rau muống hữu cơ sông Hồng", normal: "18.000 đ/bó", winmart: "13.000 đ/bó", discount: "27%" },
            { name: "🐟 Cá trắm đen tươi sống Ba Vì", normal: "120.000 đ/kg", winmart: "105.000 đ/kg", discount: "12%" },
            { name: "🍚 Gạo tám thơm Điện Biên (Túi 5kg)", normal: "150.000 đ/túi", winmart: "132.000 đ/túi", discount: "12%" }
        ],
        hadong: [
            { name: "🥩 Thịt ba rọi heo sạch MEATDeli", normal: "130.000 đ/kg", winmart: "115.000 đ/kg", discount: "11%" },
            { name: "🥬 Rau muống hữu cơ sông Hồng", normal: "12.000 đ/bó", winmart: "10.000 đ/bó", discount: "16%" },
            { name: "🐟 Cá trắm đen tươi sống Ba Vì", normal: "105.000 đ/kg", winmart: "95.000 đ/kg", discount: "9%" },
            { name: "🍚 Gạo tám thơm Điện Biên (Túi 5kg)", normal: "140.000 đ/túi", winmart: "125.000 đ/túi", discount: "10%" }
        ],
        bavi: [
            { name: "🥩 Thịt ba rọi heo sạch MEATDeli", normal: "120.000 đ/kg", winmart: "108.000 đ/kg", discount: "10%" },
            { name: "🥬 Rau muống hữu cơ sông Hồng", normal: "10.000 đ/bó", winmart: "8.000 đ/bó", discount: "20%" },
            { name: "🐟 Cá trắm đen tươi sống Ba Vì", normal: "90.000 đ/kg", winmart: "82.000 đ/kg", discount: "8%" },
            { name: "🍚 Gạo tám thơm Điện Biên (Túi 5kg)", normal: "135.000 đ/túi", winmart: "120.000 đ/túi", discount: "11%" }
        ]
    };

    function changeDistrictPrices(district) {
        const tbody = document.getElementById('market-prices-tbody');
        if(!tbody) return;
        
        const data = districtPricesData[district] || districtPricesData.caugiay;
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

    // --- LAND PRICE LOOKUP WIDGET DATA & FUNCTIONS ---
    const landPriceDatabase = {
        hanoi: {
            caugiay: {
                name: "Quận Cầu Giấy",
                streets: {
                    "Xuân Thủy": { state: 32000000, market: 180000000, trend: "hot", change: 12 },
                    "Cầu Giấy": { state: 40000000, market: 250000000, trend: "stable", change: 0 },
                    "Duy Tân": { state: 28000000, market: 140000000, trend: "up", change: 5 }
                }
            },
            hoankiem: {
                name: "Quận Hoàn Kiếm",
                streets: {
                    "Đinh Tiên Hoàng": { state: 162000000, market: 1200000000, trend: "hot", change: 15 },
                    "Hàng Ngang": { state: 120000000, market: 950000000, trend: "up", change: 4 },
                    "Tràng Tiền": { state: 162000000, market: 1100000000, trend: "stable", change: 0 }
                }
            },
            haibatrung: {
                name: "Quận Hai Bà Trưng",
                streets: {
                    "Phố Huế": { state: 80000000, market: 450000000, trend: "up", change: 6 },
                    "Bạch Mai": { state: 35000000, market: 190000000, trend: "stable", change: 0 },
                    "Minh Khai": { state: 26000000, market: 120000000, trend: "down", change: -3 }
                }
            },
            dongda: {
                name: "Quận Đống Đa",
                streets: {
                    "Nguyễn Chí Thanh": { state: 50000000, market: 300000000, trend: "up", change: 7 },
                    "Chùa Bộc": { state: 45000000, market: 280000000, trend: "hot", change: 10 },
                    "Xã Đàn": { state: 62000000, market: 380000000, trend: "stable", change: 0 }
                }
            }
        },
        tphcm: {
            quan1: {
                name: "Quận 1",
                streets: {
                    "Đồng Khởi": { state: 162000000, market: 1300000000, trend: "hot", change: 18 },
                    "Nguyễn Huệ": { state: 162000000, market: 1250000000, trend: "stable", change: 0 },
                    "Lê Lợi": { state: 150000000, market: 980000000, trend: "up", change: 6 }
                }
            },
            binhthanh: {
                name: "Quận Bình Thạnh",
                streets: {
                    "Điện Biên Phủ": { state: 40000000, market: 220000000, trend: "up", change: 5 },
                    "Nguyễn Hữu Cảnh": { state: 45000000, market: 240000000, trend: "hot", change: 10 },
                    "Lê Quang Định": { state: 28000000, market: 130000000, trend: "stable", change: 0 }
                }
            },
            thuduc: {
                name: "Thành phố Thủ Đức",
                streets: {
                    "Trần Não": { state: 35000000, market: 210000000, trend: "hot", change: 14 },
                    "Song Hành": { state: 28000000, market: 150000000, trend: "up", change: 8 },
                    "Võ Văn Ngân": { state: 30000000, market: 160000000, trend: "stable", change: 0 }
                }
            }
        }
    };

    let currentRegion = 'hanoi';

    window.initLandPriceWidget = function(region) {
        currentRegion = region;
        const districtSelect = document.getElementById('land-district');
        if (!districtSelect) return;
        
        districtSelect.innerHTML = '';
        const districts = landPriceDatabase[region];
        for (const key in districts) {
            const opt = document.createElement('option');
            opt.value = key;
            opt.innerText = districts[key].name;
            districtSelect.appendChild(opt);
        }
        updateLandStreets();
    }

    window.updateLandStreets = function() {
        const districtSelect = document.getElementById('land-district');
        const streetSelect = document.getElementById('land-street');
        if (!districtSelect || !streetSelect) return;
        
        const districtKey = districtSelect.value;
        const streets = landPriceDatabase[currentRegion][districtKey].streets;
        
        streetSelect.innerHTML = '';
        for (const key in streets) {
            const opt = document.createElement('option');
            opt.value = key;
            opt.innerText = key;
            streetSelect.appendChild(opt);
        }
        showLandPrice();
    }

    const slugify = (text) => text.toString().toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[đĐ]/g, 'd').replace(/[^a-z0-9 -]/g, '').replace(/\s+/g, '-').replace(/-+/g, '-');

    window.showLandPrice = function() {
        const districtSelect = document.getElementById('land-district');
        const streetSelect = document.getElementById('land-street');
        const resultDiv = document.getElementById('land-price-result');
        if (!districtSelect || !streetSelect || !resultDiv) return;
        
        const districtKey = districtSelect.value;
        const streetKey = streetSelect.value;
        const districtName = landPriceDatabase[currentRegion][districtKey].name;
        const streetData = landPriceDatabase[currentRegion][districtKey].streets[streetKey];
        
        if (!streetData) return;
        
        let trendIcon = '➖';
        let trendColor = '#888';
        let trendText = 'Ổn định';
        if (streetData.trend === 'hot') {
            trendIcon = '🔥';
            trendColor = '#d71920';
            trendText = `Tăng nóng (+${streetData.change}%)`;
        } else if (streetData.trend === 'up') {
            trendIcon = '📈';
            trendColor = '#28a745';
            trendText = `Tăng (+${streetData.change}%)`;
        } else if (streetData.trend === 'down') {
            trendIcon = '📉';
            trendColor = '#007bff';
            trendText = `Giảm nhẹ (${streetData.change}%)`;
        }
        
        const bdsLink = `https://batdongsan.com.vn/nha-dat-ban-${slugify(streetKey)}-${slugify(districtName)}`;
        
        resultDiv.style.display = 'block';
        resultDiv.innerHTML = `
            <div style="color: #002d62; font-weight: bold; margin-bottom: 5px; display: flex; justify-content: space-between;">
                <span>✔ Kết quả tra cứu:</span>
                <span style="color: ${trendColor}; font-size: 11px; font-weight: bold;">${trendIcon} ${trendText}</span>
            </div>
            <div style="line-height: 1.6; font-size: 11.5px; color: #333;">
                • Bảng giá Nhà nước: <strong>${(streetData.state).toLocaleString()} đ/m²</strong><br>
                • Giá thực tế batdongsan.com.vn: <strong style="color: #d71920;">${(streetData.market).toLocaleString()} đ/m²</strong><br>
                • Chênh lệch thực tế: <strong>x${(streetData.market / streetData.state).toFixed(1)} lần</strong><br>
                <div style="margin-top: 8px; text-align: center;">
                    <a href="${bdsLink}" target="_blank" style="background-color: #002d62; color: #fff; text-decoration: none; padding: 6px 12px; border-radius: 4px; font-weight: bold; display: inline-block; width: 80%; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">Xem tin rao bán tại tuyến đường này</a>
                </div>
            </div>
        `;
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
                        <td style="border: 1px solid #ddd; padding: 6px;">Miền Bắc</td>
                        <td style="border: 1px solid #ddd; padding: 6px;">Chỉ mục toàn bộ trang</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 6px; font-weight: bold;">Lớp 2: Tỉnh/Thành</td>
                        <td style="border: 1px solid #ddd; padding: 6px;">Hà Nội (Trọng điểm Tầng 1)</td>
                        <td style="border: 1px solid #ddd; padding: 6px;">Canonical cố định tại laodong.vn/vung-mien/ha-noi/</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 6px; font-weight: bold;">Lớp 3: Quận/Huyện</td>
                        <td style="border: 1px solid #ddd; padding: 6px;" id="schema-district">Quận Hoàn Kiếm</td>
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
</div> <!-- Close b-center wrapper -->
</div> <!-- Close body-content wrapper -->

<script>
    const originalHanoiArticles = PLACEHOLDER_RAW_ARTICLES;
    let hanoiArticles = [...originalHanoiArticles];

    // Helper to safely fetch articles from the filtered list (looping if we run out)
    function getSafeArticle(pool, index, globalFallbackIndex) {
        if (pool && pool.length > 0) {
            return pool[index % pool.length];
        }
        return originalHanoiArticles[globalFallbackIndex % originalHanoiArticles.length];
    }

    let featuredArticleId = hanoiArticles[0].id;
    let articlesVolume = 120;
    let isIndexedStatus = true;

    function toggleDevConsole() {
        const drawer = document.getElementById('dev-console-drawer');
        drawer.style.display = drawer.style.display === 'none' || drawer.style.display === '' ? 'flex' : 'none';
    }

    function populateCuratorOptions() {
        const select = document.getElementById('curator-select');
        select.innerHTML = '';
        hanoiArticles.forEach(a => {
            const opt = document.createElement('option');
            opt.value = a.id;
            opt.innerText = a.title.substring(0, 50) + "...";
            select.appendChild(opt);
        });
    }

    function renderMainCover() {
        const centerArt = hanoiArticles.find(a => a.id === featuredArticleId) || getSafeArticle(hanoiArticles, 0, 0);
        const leftSubPool = hanoiArticles.filter(a => a.id !== centerArt.id);
        const sub1 = getSafeArticle(leftSubPool, 0, 1);
        const sub2 = getSafeArticle(leftSubPool, 1, 2);
        const rightPool = hanoiArticles.filter(a => a.id !== centerArt.id && a.id !== sub1.id && a.id !== sub2.id);
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
        const mostReadPool = hanoiArticles.filter(a => !displayedIds.has(a.id)).slice(0, 15);
        const mostReadIds = new Set(mostReadPool.map(a => a.id));

        // Latest News Feed (3 items) - Must not duplicate featured/spotlight AND must not duplicate most read
        const latestNewsPool = hanoiArticles.filter(a => !displayedIds.has(a.id) && !mostReadIds.has(a.id));
        const feed1 = getSafeArticle(latestNewsPool, 0, 10);
        const feed2 = getSafeArticle(latestNewsPool, 1, 11);
        const feed3 = getSafeArticle(latestNewsPool, 2, 12);

        let el_main_cover_container = document.getElementById('main-cover-container');
        if (el_main_cover_container) el_main_cover_container.innerHTML = `
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

        let el_subcover_container = document.getElementById('subcover-container');
        if (el_subcover_container) el_subcover_container.innerHTML = `
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

        let el_subcover_bottom_row = document.getElementById('subcover-bottom-row');
        if (el_subcover_bottom_row) el_subcover_bottom_row.innerHTML = `
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

        let el_spotlight_container = document.getElementById('spotlight-container');
        if (el_spotlight_container) el_spotlight_container.innerHTML = `
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

        const commentPool = hanoiArticles.filter(a => a.category === "Thời sự" && a.id !== centerArt.id);
        const commentArt = getSafeArticle(commentPool, 0, 10);
        const kindnessPool = hanoiArticles.filter(a => a.category === "Xã hội" && a.id !== centerArt.id);
        const kindnessArt = getSafeArticle(kindnessPool, 0, 12);
        
        if (document.getElementById('sidebar-commentary-title')) {
            let el_sidebar_commentary_title = document.getElementById('sidebar-commentary-title');
        if (el_sidebar_commentary_title) el_sidebar_commentary_title.innerText = commentArt.title;
            document.getElementById('sidebar-commentary-title').href = commentArt.url;
        }
        if (document.getElementById('sidebar-kindness-title')) {
            let el_sidebar_kindness_title = document.getElementById('sidebar-kindness-title');
        if (el_sidebar_kindness_title) el_sidebar_kindness_title.innerText = kindnessArt.title;
            document.getElementById('sidebar-kindness-title').href = kindnessArt.url;
        }



        // Render Most Read Carousel
        const mostReadContainer = document.getElementById('most-read-container');
        const mostReadDotsEl = document.getElementById('most-read-dots');
        if (mostReadContainer && mostReadPool.length > 0) {
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
            
            mostReadContainer.innerHTML = containerHtml;
            if (mostReadDotsEl) mostReadDotsEl.innerHTML = dotsHtml;
            
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
    }

    function renderMediaSection() {
        const mediaPool = hanoiArticles.filter(a => a.category === "Xã hội" || a.category === "Thời sự").slice(5, 11);
        if (mediaPool.length < 6) return;

        let el_media_col_1 = document.getElementById('media-col-1');
        if (el_media_col_1) el_media_col_1.innerHTML = `
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
        
        let el_media_col_2 = document.getElementById('media-col-2');
        if (el_media_col_2) el_media_col_2.innerHTML = `
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
            let el_tv_player_img = document.getElementById('tv-player-img');
        if (el_tv_player_img) el_tv_player_img.src = mediaPool[activeIdx].image;
        }, 5000);
    }

    function renderCategoryColumns() {
        const row1Categories = ["Thời sự", "Xã hội", "Giáo dục", "Kinh tế"];
        const row2Categories = ["Công đoàn", "Bất động sản", "Văn hóa - Giải trí", "Thể thao"];

        function makeColumnHtml(categoryName) {
            let catPool = hanoiArticles.filter(a => a.category === categoryName);
            if (catPool.length < 5) {
                // Only fall back to articles within the filtered district to prevent leakage
                const generalCatPool = hanoiArticles;
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
        let el_categories_grid_row1 = document.getElementById('categories-grid-row1');
        if (el_categories_grid_row1) el_categories_grid_row1.innerHTML = row1Html;

        let row2Html = '';
        row2Categories.forEach(cat => { row2Html += makeColumnHtml(cat); });
        let el_categories_grid_row2 = document.getElementById('categories-grid-row2');
        if (el_categories_grid_row2) el_categories_grid_row2.innerHTML = row2Html;
    }

    function renderEnterpriseBlock() {
        let prPool = hanoiArticles.filter(a => a.category === "Kinh tế").slice(0, 5);
        if (prPool.length < 5) {
            const generalPrPool = originalHanoiArticles.filter(a => a.category === "Kinh tế");
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
        let el_enterprise_grid_container = document.getElementById('enterprise-grid-container');
        if (el_enterprise_grid_container) el_enterprise_grid_container.innerHTML = html;
    }

    function pinFeaturedStory(idStr) {
        featuredArticleId = parseInt(idStr);
        renderMainCover();
        updateSchemaMarkup();
    }

    function updateThresholdDemo(val) {
        articlesVolume = parseInt(val);
        let el_threshold_val = document.getElementById('threshold-val');
        if (el_threshold_val) el_threshold_val.innerText = val + " bài/tháng";
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
        const curFeatured = hanoiArticles.find(a => a.id === featuredArticleId) || hanoiArticles[0];
        const schema = {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "name": "Lao Động Hà Nội - Trang tin tức Thủ đô",
            "url": "https://laodong.vn/vung-mien/ha-noi/",
            "description": "Trang tin tức của Báo Lao Động về Hà Nội, cập nhật tin thời sự, xã hội, công đoàn.",
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
                        "name": "Hà Nội",
                        "item": "https://laodong.vn/vung-mien/ha-noi/"
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
        let el_json_schema_output = document.getElementById('json-schema-output');
        if (el_json_schema_output) el_json_schema_output.innerText = JSON.stringify(schema, null, 2);
    }

    function fetchHanoiWeather() {
        const options = { weekday: 'long', year: 'numeric', month: '2-digit', day: '2-digit' };
        const today = new Date();
        let el_current_date_vietnam = document.getElementById('current-date-vietnam');
        if (el_current_date_vietnam) el_current_date_vietnam.innerText = today.toLocaleDateString('vi-VN', options);

        const url = "https://api.open-meteo.com/v1/forecast?latitude=21.0285&longitude=105.8542&current=temperature_2m,relative_humidity_2m,weather_code";
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
                    
                    let el_weather_temp_span = document.getElementById('weather-temp-span');
        if (el_weather_temp_span) el_weather_temp_span.innerHTML = `
                        Hà Nội: ${emoji} <strong>${temp}°C</strong> (${condition}) <span style="font-weight: normal; color: #666; margin-left: 5px;">💧 ${humidity}% ẩm</span>
                    `;
                }
            })
            .catch(err => {
                console.error("Lỗi khi tải thời tiết:", err);
                let el_weather_temp_span = document.getElementById('weather-temp-span');
        if (el_weather_temp_span) el_weather_temp_span.innerHTML = "Hà Nội: ⛅ 28°C";
            });
    }

    const provincialProfiles = {
        all: {
            title: "HÀ NỘI - THỦ ĐÔ VÀ TRUNG TÂM KINH TẾ - CHÍNH TRỊ QUỐC GIA",
            profileHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Diện tích:</strong> 3.359 km² (Lớn nhất cả nước sau sáp nhập với Hà Tây)<br>
                    • <strong>Dân số:</strong> 8.5 triệu người (Đông thứ 2 cả nước)<br>
                    • <strong>Quy mô kinh tế (GRDP):</strong> Đứng thứ 2 cả nước, trung tâm tài chính - ngân hàng, thương mại và dịch vụ.<br>
                    • <strong>Hạ tầng chiến lược:</strong> Vành đai 4 đang thi công, sân bay Nội Bài mở rộng, 8 tuyến đường sắt đô thị quy hoạch.
                </div>
            `,
            indicatorHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Năng lực cạnh tranh (PCI 2025):</strong> Hạng 25/63 tỉnh thành (65.80 điểm) - Nhóm Khá.<br>
                    • <strong>Hiệu quả quản trị hành chính (PAPI 2025):</strong> Nằm trong nhóm Trung bình Cao - cải thiện mạnh về cung ứng dịch vụ công.<br>
                    • <strong>Thế mạnh:</strong> Trung tâm giáo dục, y tế, văn hóa, hành chính quốc gia. Hub kinh tế số và đổi mới sáng tạo.<br>
                    • <strong>Khuyến nghị:</strong> Rút ngắn thời gian cấp phép xây dựng, giảm ùn tắc giao thông, đẩy nhanh chuyển đổi số dịch vụ công.
                </div>
            `
        },
        'noi-thanh': {
            title: "HÀ NỘI NỘI THÀNH - TRUNG TÂM ĐÔ THỊ",
            profileHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Các quận nội thành:</strong> Hoàn Kiếm, Ba Đình, Đống Đa, Hai Bà Trưng, Cầu Giấy, Thanh Xuân, Tây Hồ, Hoàng Mai, Long Biên, Nam Từ Liêm, Bắc Từ Liêm.<br>
                    • <strong>Mật độ dân số:</strong> Cao nhất cả nước, trung bình 20.000-45.000 người/km².<br>
                    • <strong>Thế mạnh kinh tế:</strong> Thương mại, dịch vụ, tài chính - ngân hàng, giáo dục đại học, y tế chuyên sâu.
                </div>
            `,
            indicatorHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Hạ tầng đặc thù:</strong> Trục đường sắt Cát Linh - Hà Đông, Nhổn - Ga Hà Nội đang vận hành & hoàn thiện.<br>
                    • <strong>Bất động sản:</strong> Mặt bằng giá ở mức cao, trung tâm thị trường nhà ở toàn khu vực phía Bắc.<br>
                    • <strong>Áp lực:</strong> Quá tải hạ tầng giao thông giờ cao điểm, tắc nghẽn ngõ phố, môi trường không khí cần cải thiện.
                </div>
            `
        },
        'ha-dong': {
            title: "HÀ ĐÔNG & PHỤ CẬN - ĐÔ THỊ VỆ TINH PHÍA TÂY",
            profileHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Phạm vi:</strong> Quận Hà Đông, Huyện Thanh Oai, Chương Mỹ, Mỹ Đức (sáp nhập vào Hà Nội năm 2008).<br>
                    • <strong>Dân số:</strong> Hơn 1.2 triệu người, tốc độ đô thị hóa nhanh nhất Hà Nội.<br>
                    • <strong>Thế mạnh kinh tế:</strong> Trung tâm thương mại dịch vụ khu vực phía Tây, làng nghề truyền thống, bất động sản vệ tinh.
                </div>
            `,
            indicatorHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Hạ tầng chiến lược:</strong> Đường sắt Cát Linh - Hà Đông (đã vận hành), Vành đai 4 qua khu vực phía Tây.<br>
                    • <strong>Quy hoạch:</strong> Đô thị vệ tinh Hòa Lạc và Xuân Mai quy hoạch trở thành trung tâm đổi mới sáng tạo.<br>
                    • <strong>Làng nghề nổi bật:</strong> Hàng Gai - Hà Đông (lụa), Vạn Phúc (lụa tơ tằm), La Phù (đan len).
                </div>
            `
        },
        'gia-lam': {
            title: "GIA LÂM MỚI & ĐÔNG BẮC HÀ NỘI - CỬA NGÕ PHÍA ĐÔNG",
            profileHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Phạm vi:</strong> Huyện Gia Lâm (đang lên Quận), Quận Long Biên, Huyện Đông Anh, Huyện Sóc Sơn.<br>
                    • <strong>Dân số:</strong> Hơn 1.5 triệu người, tốc độ tăng dân số cơ học cao do nhập cư.<br>
                    • <strong>Thế mạnh kinh tế:</strong> Công nghiệp chế biến, logistics, cảng hàng không Nội Bài (Sóc Sơn), khu công nghiệp Thăng Long.
                </div>
            `,
            indicatorHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Hạ tầng chiến lược:</strong> Cầu Vĩnh Tuy 2, Cầu Đuống mới, Vành đai 3.5, cao tốc Hà Nội - Hải Phòng.<br>
                    • <strong>KCN trọng điểm:</strong> KCN Thăng Long (Đông Anh), KCN Quang Minh (Mê Linh), Khu CNC Hòa Lạc.<br>
                    • <strong>Tiềm năng:</strong> Gia Lâm dự kiến lên quận năm 2026, thúc đẩy bất động sản khu vực phía Đông Hà Nội.
                </div>
            `
        },
        'dong-anh': {
            title: "ĐÔNG ANH & PHÍA BẮC HÀ NỘI - TRUNG TÂM CÔNG NGHIỆP MỚI",
            profileHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Phạm vi:</strong> Huyện Đông Anh (đang lên quận), Huyện Mê Linh, Huyện Sóc Sơn.<br>
                    • <strong>Dân số:</strong> Hơn 900.000 người, tập trung lao động khu công nghiệp.<br>
                    • <strong>Thế mạnh kinh tế:</strong> KCN Thăng Long - Toyota, Honda, Canon; Sân bay Nội Bài (logistics hàng không); Nông nghiệp công nghệ cao.
                </div>
            `,
            indicatorHtml: `
                <div style="font-size: 11.5px; line-height: 1.6; color: #333;">
                    • <strong>Hạ tầng chiến lược:</strong> Vành đai 4 đang thi công đoạn qua Đông Anh - Mê Linh, đường Nhật Tân - Nội Bài.<br>
                    • <strong>KCN nổi bật:</strong> KCN Thăng Long I,II,III (thu hút FDI Nhật Bản lớn nhất phía Bắc), KCN Quang Minh.<br>
                    • <strong>Quy hoạch:</strong> Đông Anh dự kiến lên quận 2026; xây dựng khu đô thị thông minh ven sông Hồng.
                </div>
            `
        }
    };

    function updateProvincialProfileWidget(district) {
        const widget = document.getElementById('provincial-profile-widget');
        if (!widget) return;
        const profile = provincialProfiles[district] || provincialProfiles.all;
        
        widget.innerHTML = `
            <div style="border-right: 1px solid #eee; padding-right: 20px;">
                <h4 style="margin: 0 0 10px 0; font-size: 12px; font-weight: bold; color: #002d62; text-transform: uppercase; letter-spacing: 0.5px; display: flex; align-items: center; gap: 6px;">
                    📌 ${profile.title}
                </h4>
                ${profile.profileHtml}
            </div>
            <div>
                <h4 style="margin: 0 0 10px 0; font-size: 12px; font-weight: bold; color: #c00000; text-transform: uppercase; letter-spacing: 0.5px; display: flex; align-items: center; gap: 6px;">
                    📊 CHỈ SỐ CẢI CÁCH &amp; CẠNH TRANH CHÍNH THỐNG
                </h4>
                ${profile.indicatorHtml}
            </div>
        `;
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

    window.filterSpokeDistrict = function(district) {
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
        if (district === 'all') {
            hanoiArticles = [...originalHanoiArticles];
            if (pageTitle) pageTitle.innerText = "Trang Hà Nội";
        } else if (district === 'noi-thanh') {
            hanoiArticles = originalHanoiArticles.filter(a => a.district && (
                a.district.includes('Hoàn Kiếm') || a.district.includes('Ba Đình') || 
                a.district.includes('Đống Đa') || a.district.includes('Hai Bà Trưng') ||
                a.district.includes('Cầu Giấy') || a.district.includes('Thanh Xuân') ||
                a.district.includes('Tây Hồ') || a.district.includes('Long Biên') ||
                a.district.includes('Nam Từ Liêm') || a.district.includes('Bắc Từ Liêm') ||
                a.district.includes('Hoàng Mai')
            ));
            if (pageTitle) pageTitle.innerText = "Hà Nội Nội thành";
        } else if (district === 'ha-dong') {
            hanoiArticles = originalHanoiArticles.filter(a => a.district && (
                a.district.includes('Hà Đông') || a.district.includes('Thanh Oai') || 
                a.district.includes('Chương Mỹ') || a.district.includes('Mỹ Đức')
            ));
            if (pageTitle) pageTitle.innerText = "Khu vực Hà Đông";
        } else if (district === 'gia-lam') {
            hanoiArticles = originalHanoiArticles.filter(a => a.district && (
                a.district.includes('Gia Lâm') || a.district.includes('Đông Anh') ||
                a.district.includes('Sóc Sơn') || a.district.includes('Mê Linh')
            ));
            if (pageTitle) pageTitle.innerText = "Khu vực Gia Lâm mới";
        } else if (district === 'dong-anh') {
            hanoiArticles = originalHanoiArticles.filter(a => a.district && (
                a.district.includes('Đông Anh') || a.district.includes('Mê Linh') ||
                a.district.includes('Sóc Sơn')
            ));
            if (pageTitle) pageTitle.innerText = "Huyện Đông Anh";
        }

        updateProvincialProfileWidget(district);
        featuredArticleId = getSafeArticle(hanoiArticles, 0, 0).id;
        
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

    function openSchemaModal() {
        document.getElementById('schema-modal').style.display = 'flex';
        updateSchemaMarkup();
    }
    function closeSchemaModal() {
        document.getElementById('schema-modal').style.display = 'none';
    }

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
        { name: "Nha khoa Quốc tế Hà Đông", address: "145 Quang Trung, Hà Đông", phone: "0988.xxx.xxx" },
        { name: "Trung tâm Gia sư Sư phạm thủ khoa", address: "Ngõ 192 Lê Trọng Tấn, Thanh Xuân", phone: "0912.xxx.xxx" },
        { name: "Gốm sứ Bát Tràng chính gốc - Shop Lộc Phát", address: "Chợ cổ Bát Tràng, Gia Lâm", phone: "0945.xxx.xxx" },
        { name: "Cứu hộ Giao thông Hà Nội 24/7 (Đống Đa - Ba Đình)", address: "12 Giảng Võ, Đống Đa", phone: "0904.xxx.xxx" },
        { name: "Trường Dạy nghề ẩm thực Hanoi Cook", address: "89 Trần Phú, Hà Đông", phone: "0916.xxx.xxx" },
        { name: "Viện Thẩm mỹ Công nghệ cao An Beauty", address: "24 Kim Mã, Ba Đình", phone: "0989.xxx.xxx" },
        { name: "Phòng khám Đông y gia truyền Lãn Ông Đường", address: "Phố Lãn Ông, Hoàn Kiếm", phone: "0973.xxx.xxx" },
        { name: "Gói vay ưu đãi hộ kinh doanh - HDBank Cầu Giấy", address: "19 Duy Tân, Cầu Giấy", phone: "0903.xxx.xxx" },
        { name: "Sửa chữa máy tính & Laptop lấy ngay Bách Khoa", address: "56 Tạ Quang Bửu, Hai Bà Trưng", phone: "0985.xxx.xxx" },
        { name: "Thiết kế thi công nội thất xanh An Cường", address: "218 Hoàng Quốc Việt, Cầu Giấy", phone: "0942.xxx.xxx" },
        { name: "Buffet chay Hương Thiền", address: "261 Xã Đàn, Đống Đa", phone: "0967.xxx.xxx" },
        { name: "Cửa hàng hoa tươi Sunny Flower", address: "12 Trần Hưng Đạo, Hoàn Kiếm", phone: "0918.xxx.xxx" },
        { name: "Giặt là công nghiệp siêu tốc Green Laundry", address: "45 Nguyễn Khánh Toàn, Cầu Giấy", phone: "0936.xxx.xxx" },
        { name: "Nha khoa nụ cười Việt (Smile Dental)", address: "88 Xã Đàn, Đống Đa", phone: "0977.xxx.xxx" },
        { name: "Sửa xe máy phân khối lớn & tay ga chuyên nghiệp", address: "102 Đường Láng, Đống Đa", phone: "0909.xxx.xxx" },
        { name: "Vận tải & chuyển nhà trọn gói Thành Hưng", address: "12 Cầu Diễn, Bắc Từ Liêm", phone: "0915.xxx.xxx" },
        { name: "Đại lý vé máy bay & du lịch VietTravel Cầu Giấy", address: "165 Xuân Thủy, Cầu Giấy", phone: "0981.xxx.xxx" },
        { name: "Phòng khám nha khoa quốc tế Paris Cầu Giấy", address: "110 Nguyễn Khánh Toàn, Cầu Giấy", phone: "0982.xxx.xxx" },
        { name: "Cà phê rang xay nguyên chất Tây Nguyên Coffee", address: "88 Nguyễn Chí Thanh, Láng Hạ", phone: "0947.xxx.xxx" },
        { name: "Cửa hàng đặc sản giò chả Ước Lễ chính gốc", address: "15 Ngõ Huyện, Hoàn Kiếm", phone: "0914.xxx.xxx" },
        { name: "Salon tóc & Làm đẹp chuyên nghiệp Minh Huy", address: "78 Chùa Láng, Đống Đa", phone: "0983.xxx.xxx" },
        { name: "Lớp học vẽ & Mỹ thuật thiếu nhi Art Sun", address: "12 ngõ 45 phố Vọng, Hai Bà Trưng", phone: "0941.xxx.xxx" },
        { name: "Đại lý yến sào Khánh Hòa chính hãng", address: "210 Phố Huế, Hai Bà Trưng", phone: "0911.xxx.xxx" },
        { name: "Cửa hàng thực phẩm sạch & rau hữu cơ Organic Mart", address: "44 Phùng Hưng, Hoàn Kiếm", phone: "0984.xxx.xxx" },
        { name: "Sửa điện lạnh & Điều hòa bách khoa 24h", address: "32 Láng Hạ, Đống Đa", phone: "0902.xxx.xxx" },
        { name: "Cho thuê vest cưới & Áo dài cô dâu Bella", address: "15 Mai Hắc Đế, Hai Bà Trưng", phone: "0917.xxx.xxx" },
        { name: "Lớp học tiếng Anh giao tiếp chuẩn Edspace", address: "5 ngõ 106 Hoàng Quốc Việt", phone: "0938.xxx.xxx" },
        { name: "Dịch vụ hút bể phốt & Thông tắc cống đô thị 24h", address: "99 Định Công, Hoàng Mai", phone: "0906.xxx.xxx" },
        { name: "Cơm văn phòng sạch & Giao hàng tận nơi Hanoi Bento", address: "15 ngõ 80 Trần Duy Hưng", phone: "0975.xxx.xxx" },
        { name: "Vàng bạc đá quý Phú Quý Trần Nhân Tông", address: "30 Trần Nhân Tông, Hai Bà Trưng", phone: "0986.xxx.xxx" }
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
        initLandPriceWidget('hanoi');
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

# Save as demo_landing_page_hanoi_ads.html
ads_html_path = 'c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/demo_landing_page_hanoi_ads.html'
with open(ads_html_path, 'w', encoding='utf-8') as f:
    f.write(full_html_content)

# Save as index_ads.html for easy Vercel routing
index_ads_path = 'c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/index_ads.html'
with open(index_ads_path, 'w', encoding='utf-8') as f:
    f.write(full_html_content)

# Overwrite original demo_landing_page_hanoi.html
orig_html_path = 'c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/demo_landing_page_hanoi.html'
with open(orig_html_path, 'w', encoding='utf-8') as f:
    f.write(full_html_content)

# Overwrite index.html for default Vercel routing
index_path = 'c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/index.html'
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(full_html_content)

print("Demo Hanoi Ads page compiled and merged into root templates successfully!")
