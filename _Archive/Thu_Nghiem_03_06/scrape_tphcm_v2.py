"""
scrape_tphcm_v2.py  (V2.1 - Fixed)
====================================
Cào bài CHÍNH XÁC theo địa phương với:
- Giới hạn MAX_PER_CATEGORY bài/chuyên mục/tỉnh → đảm bảo đa dạng
- Keyword list mở rộng cho Tây Ninh và Đồng Nai
- Scan tối đa 20 trang/category
- KHÔNG backfill bằng bài không liên quan địa phương
"""

import urllib.request
import re
import http.cookiejar
import json
import time
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

MAX_PER_CATEGORY = 5   # Tối đa bài/chuyên mục/tỉnh
MAX_PAGES        = 20  # Scan tối đa bao nhiêu trang/category

# ============================================================
# KEYWORD MAPS — LỌC BÀI THEO TỈNH
# Dùng cả title lẫn URL để khớp
# ============================================================
PROVINCE_KEYWORDS = {
    "tphcm": [
        # Tên chính thức
        "tphcm", "tp.hcm", "tp hcm", "hồ chí minh", "ho chi minh",
        "sài gòn", "sai gon", "saigon",
        # Quận/huyện đặc trưng
        "thủ đức", "thu duc", "bình chánh", "binh chanh",
        "củ chi", "cu chi", "cần giờ", "can gio",
        "hóc môn", "hoc mon", "nhà bè", "nha be",
        "gò vấp", "go vap", "bình thạnh", "binh thanh",
        "phú nhuận", "phu nhuan", "tân bình", "tan binh",
        "tân phú", "tan phu", "bình tân", "binh tan",
        "quận 1", "quan 1", "quận 3", "quận 4", "quận 5",
        "quận 6", "quận 7", "quận 8", "quận 10", "quận 11", "quận 12",
        # Landmark đặc trưng
        "landmark 81", "đồng khởi", "dong khoi",
        "nguyễn huệ", "bến thành", "ben thanh",
        # Tỉnh lân cận thường được tính vào Đông Nam Bộ (khi tag tphcm)
        "bình dương", "binh duong", "thuận an", "thuan an",
        "dĩ an", "di an", "bến cát", "ben cat",
        "vũng tàu", "vung tau", "bà rịa", "ba ria", "brvt",
    ],
    "dongnai": [
        # Tên tỉnh và thành phố
        "đồng nai", "dong nai", "biên hòa", "bien hoa",
        "long khánh", "long khanh",
        # Huyện/thị xã
        "nhơn trạch", "nhon trach", "trảng bom", "trang bom",
        "long thành", "long thanh", "vĩnh cửu", "vinh cuu",
        "định quán", "dinh quan", "tân phú", "tan phu",
        "xuân lộc", "xuan loc", "cẩm mỹ", "cam my",
        "thống nhất", "thong nhat",
        # Địa danh đặc trưng
        "sân bay long thành", "san bay long thanh",
        "amata", "hồ trị an", "ho tri an",
        "giang điền", "giang dien",
        "khu công nghiệp biên hòa", "khu cong nghiep bien hoa",
        # Tỉnh Bình Phước (thuộc ĐNB)
        "bình phước", "binh phuoc", "đồng xoài", "dong xoai",
        "chơn thành", "chon thanh", "bình long", "binh long",
        "phước long", "phuoc long", "bù đăng", "bu dang",
        "bù đốp", "bu dop", "lộc ninh", "loc ninh",
    ],
    "tayninh": [
        # Tên tỉnh
        "tây ninh", "tay ninh",
        # Huyện/thành phố trực thuộc
        "hòa thành", "hoa thanh", "trảng bàng", "trang bang",
        "bến cầu", "ben cau", "gò dầu", "go dau",
        "dương minh châu", "duong minh chau",
        "tân biên", "tan bien", "tân châu", "tan chau",
        "châu thành", "chau thanh",
        # Địa danh đặc trưng
        "núi bà đen", "nui ba den", "tòa thánh", "toa thanh",
        "gò kén", "go ken", "happy land",
        "lò gò", "lo go", "xa mát", "xa mat",
        # Long An (thỉnh thoảng xuất hiện cùng Tây Ninh)
        "long an", "tân an", "tan an",
        "bến lức", "ben luc", "đức hòa", "duc hoa",
        "cần giuộc", "can giuoc", "cần đước", "can duoc",
        "thủ thừa", "thu thua",
    ]
}

# Cấu hình các tỉnh
SPOKE_CONFIG = {
    "tphcm": {
        "province": "tphcm",
        "province_label": "TP.HCM",
        "tag_label": "TP.HCM",
        "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
        "target": 35
    },
    "dongnai": {
        "province": "dongnai",
        "province_label": "Đồng Nai",
        "tag_label": "Đồng Nai",
        "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
        "target": 25
    },
    "tayninh": {
        "province": "tayninh",
        "province_label": "Tây Ninh",
        "tag_label": "Tây Ninh",
        "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
        "target": 20
    }
}

# Category pages to scan
CATEGORY_URLS = [
    {"name": "Thời sự",             "url": "https://laodong.vn/thoi-su"},
    {"name": "Xã hội",              "url": "https://laodong.vn/xa-hoi"},
    {"name": "Kinh tế",             "url": "https://laodong.vn/kinh-doanh"},
    {"name": "Giáo dục",            "url": "https://laodong.vn/giao-duc"},
    {"name": "Bất động sản",        "url": "https://laodong.vn/bat-dong-san"},
    {"name": "Công đoàn",           "url": "https://laodong.vn/cong-doan"},
    {"name": "Văn hóa - Giải trí",  "url": "https://laodong.vn/van-hoa-giai-tri"},
    {"name": "Thể thao",            "url": "https://laodong.vn/the-thao"},
    # Extra sources tăng coverage
    {"name": "Xã hội",              "url": "https://laodong.vn/giao-thong"},
    {"name": "Kinh tế",             "url": "https://laodong.vn/thi-truong"},
    {"name": "Thời sự",             "url": "https://laodong.vn/su-kien-binh-luan"},
    {"name": "Bất động sản",        "url": "https://laodong.vn/quy-hoach"},
]

# Category guess from URL
CATEGORY_URL_MAP = {
    "thoi-su": "Thời sự", "su-kien-binh-luan": "Thời sự", "mat-tran": "Thời sự",
    "xa-hoi": "Xã hội", "giao-thong": "Xã hội", "moi-truong": "Xã hội",
    "kinh-doanh": "Kinh tế", "tien-te": "Kinh tế", "thi-truong": "Kinh tế", "doanh-nghiep": "Kinh tế",
    "bat-dong-san": "Bất động sản", "nha-dep": "Bất động sản", "quy-hoach": "Bất động sản",
    "giao-duc": "Giáo dục", "tuyen-sinh": "Giáo dục",
    "cong-doan": "Công đoàn", "viec-lam": "Công đoàn",
    "van-hoa": "Văn hóa - Giải trí", "giai-tri": "Văn hóa - Giải trí",
    "du-lich": "Văn hóa - Giải trí", "van-hoa-giai-tri": "Văn hóa - Giải trí",
    "the-thao": "Thể thao", "bong-da": "Thể thao",
}

def guess_category(url, fallback="Thời sự"):
    url_lower = url.lower()
    for key, cat in CATEGORY_URL_MAP.items():
        if key in url_lower:
            return cat
    return fallback

# ============================================================
# HTTP Setup
# ============================================================
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8',
    'Referer': 'https://laodong.vn/'
}
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

print("Initializing cookie bypass...")
try:
    req_init = urllib.request.Request('https://laodong.vn/', headers=headers)
    with opener.open(req_init) as resp:
        html_init = resp.read().decode('utf-8')
    cm = re.search(r'D1N=([0-9a-fA-F]+)', html_init)
    if cm:
        cookie = http.cookiejar.Cookie(
            version=0, name='D1N', value=cm.group(1), port=None, port_specified=False,
            domain='laodong.vn', domain_specified=True, domain_initial_dot=False,
            path='/', path_specified=True, secure=False, expires=None, discard=True,
            comment=None, comment_url=None, rest={}, rfc2109=False
        )
        cj.set_cookie(cookie)
        print(f"  Cookie D1N={cm.group(1)[:8]}... loaded.")
except Exception as e:
    print(f"  Cookie warning: {e}")

# ============================================================
# Scrape function
# ============================================================
def scrape_province(province_key, spoke_cfg, seen_urls):
    keywords = PROVINCE_KEYWORDS[province_key]
    cat_counter = Counter()   # track articles per category
    articles = []
    target = spoke_cfg["target"]

    for cat in CATEGORY_URLS:
        if len(articles) >= target:
            break
        cat_name = cat["name"]
        # Check if this category already has enough articles
        if cat_counter[cat_name] >= MAX_PER_CATEGORY:
            continue

        print(f"\n  [{cat_name}] scanning {cat['url']} ...")

        for page in range(1, MAX_PAGES + 1):
            if len(articles) >= target or cat_counter[cat_name] >= MAX_PER_CATEGORY:
                break
            page_url = cat['url'] if page == 1 else f"{cat['url']}?page={page}"

            try:
                req = urllib.request.Request(page_url, headers=headers)
                with opener.open(req) as resp:
                    html = resp.read().decode('utf-8')

                links = list(re.finditer(
                    r'<a[^>]+href="(https://laodong\.vn/[^"]+\.ldo)"[^>]*>(.*?)</a>',
                    html, re.DOTALL
                ))
                if not links:
                    break

                found_match = False
                for m in links:
                    if len(articles) >= target or cat_counter[cat_name] >= MAX_PER_CATEGORY:
                        break

                    url = m.group(1)
                    title = re.sub(r'<[^>]+>', '', m.group(2)).strip()
                    if not title or len(title) < 15 or url in seen_urls:
                        continue

                    title_lower = title.lower()
                    url_lower = url.lower()
                    is_match = any(kw in title_lower or kw in url_lower for kw in keywords)
                    if not is_match:
                        continue

                    seen_urls.add(url)
                    found_match = True

                    # Fetch detail
                    time.sleep(0.25)
                    try:
                        req_d = urllib.request.Request(url, headers=headers)
                        with opener.open(req_d) as resp_d:
                            detail = resp_d.read().decode('utf-8')

                        # OG image
                        img_m = re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', detail)
                        image = img_m.group(1) if img_m else ""
                        if not image:
                            img_m2 = re.search(r'<img[^>]+src="(https://media-cdn[^"]+)"', detail)
                            image = img_m2.group(1) if img_m2 else ""

                        # Chapeau/excerpt
                        ch = re.search(r'<[hp][^>]*class="chapeau"[^>]*>(.*?)</[hp]>', detail, re.DOTALL)
                        excerpt = re.sub(r'<[^>]+>', '', ch.group(1)).strip() if ch else title

                        # Date
                        dm = re.search(r'(\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2})', detail)
                        date = dm.group(1) if dm else "02/06/2026 08:00"

                        actual_cat = guess_category(url, cat_name)

                        article = {
                            "id": 0,
                            "title": title,
                            "excerpt": excerpt[:250],
                            "image": image or "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=800&q=80",
                            "url": url,
                            "date": date,
                            "office": spoke_cfg["office"],
                            "province": spoke_cfg["province"],
                            "province_label": spoke_cfg["province_label"],
                            "tags": [spoke_cfg["tag_label"], actual_cat],
                            "category": actual_cat,
                            f"is_{spoke_cfg['province']}": True,
                            "district": spoke_cfg["province_label"]
                        }
                        articles.append(article)
                        cat_counter[actual_cat] += 1
                        print(f"    ✓ [{actual_cat}] {title[:60]}")

                    except Exception as ex:
                        print(f"    ✗ Detail error: {ex}")

                if not found_match and page > 3:
                    # No matches for 3+ pages → move to next category
                    break

            except Exception as ex:
                print(f"    ✗ Page error: {ex}")
                break

    return articles


# ============================================================
# MAIN
# ============================================================
all_articles = []
seen_urls = set()

for province_key, spoke_cfg in SPOKE_CONFIG.items():
    print(f"\n{'='*60}")
    print(f"SCRAPING: {spoke_cfg['province_label']}  (target: {spoke_cfg['target']})")
    print(f"{'='*60}")
    arts = scrape_province(province_key, spoke_cfg, seen_urls)
    print(f"\n  => {len(arts)} articles for {spoke_cfg['province_label']}")
    all_articles.extend(arts)

# Assign IDs
for idx, art in enumerate(all_articles):
    art["id"] = idx

print(f"\n{'='*60}")
print(f"GRAND TOTAL: {len(all_articles)} articles")
dist = Counter(a.get("province","?") for a in all_articles)
for p, c in dist.items():
    print(f"  {p}: {c}")
cat_dist = Counter(a.get("category","?") for a in all_articles)
print("\nCategory distribution:")
for cat, cnt in cat_dist.most_common():
    print(f"  {cat}: {cnt}")

# Save
with open('tphcm_dongnambo_consolidated.json', 'w', encoding='utf-8') as f:
    json.dump(all_articles, f, ensure_ascii=False, indent=4)
print(f"\n✅ Saved to tphcm_dongnambo_consolidated.json")
