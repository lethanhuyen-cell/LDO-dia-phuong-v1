"""
scrape_supplement.py
====================
Bổ sung bài cho Đồng Nai và Tây Ninh bằng cách scan sâu hơn
Không scan lại TPHCM (đã đủ 31 bài)
Append vào file JSON hiện có
"""

import urllib.request, re, http.cookiejar, json, time, sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

MAX_PER_CATEGORY = 8   # Nới lỏng thêm cho tỉnh nhỏ
MAX_PAGES = 30         # Scan sâu hơn

# Keywords mở rộng tối đa
PROVINCE_KEYWORDS = {
    "dongnai": [
        # Tên tỉnh và thành phố
        "đồng nai", "dong nai", "biên hòa", "bien hoa",
        "long khánh", "long khanh",
        # Huyện/thị xã
        "nhơn trạch", "nhon trach", "trảng bom", "trang bom",
        "long thành", "long thanh", "vĩnh cửu", "vinh cuu",
        "định quán", "dinh quan", "tân phú đồng nai",
        "xuân lộc", "xuan loc", "cẩm mỹ", "cam my",
        "thống nhất đồng nai", "thong nhat dong nai",
        # Địa danh đặc trưng
        "sân bay long thành", "san bay long thanh",
        "amata", "hồ trị an", "ho tri an",
        "giang điền", "giang dien",
        "khu công nghiệp biên hòa",
        # Bình Phước (thuộc vùng ĐNB)
        "bình phước", "binh phuoc", "đồng xoài", "dong xoai",
        "chơn thành", "chon thanh", "bình long", "binh long",
        "phước long", "phuoc long", "bù đăng", "bu dang",
        "bù đốp", "bu dop", "lộc ninh", "loc ninh",
        "sóc bom bo", "bà rá",
    ],
    "tayninh": [
        # Tên tỉnh
        "tây ninh", "tay ninh",
        # Huyện/thành phố trực thuộc
        "hòa thành tây ninh", "trảng bàng", "trang bang",
        "bến cầu", "ben cau", "gò dầu", "go dau",
        "dương minh châu", "duong minh chau",
        "tân biên tây ninh", "tân châu tây ninh",
        "châu thành tây ninh",
        # Địa danh đặc trưng
        "núi bà đen", "nui ba den", "tòa thánh tây ninh",
        "gò kén", "go ken", "happy land tây ninh",
        "lò gò xa mát", "vườn quốc gia lò gò",
        # Long An (vùng ĐNB liền kề)
        "long an", "tân an long an", "kiến tường",
        "bến lức", "ben luc", "đức hòa", "duc hoa",
        "cần giuộc", "can giuoc", "cần đước", "can duoc",
        "thủ thừa", "thu thua", "vàm cỏ", "vam co",
        "mỹ an long an", "làng nổi tân lập",
    ]
}

SPOKE_CONFIG = {
    "dongnai": {
        "province": "dongnai", "province_label": "Đồng Nai",
        "tag_label": "Đồng Nai", "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
        "target": 20
    },
    "tayninh": {
        "province": "tayninh", "province_label": "Tây Ninh",
        "tag_label": "Tây Ninh", "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
        "target": 15
    }
}

CATEGORY_URLS = [
    {"name": "Xã hội",              "url": "https://laodong.vn/xa-hoi"},
    {"name": "Thời sự",             "url": "https://laodong.vn/thoi-su"},
    {"name": "Bất động sản",        "url": "https://laodong.vn/bat-dong-san"},
    {"name": "Kinh tế",             "url": "https://laodong.vn/kinh-doanh"},
    {"name": "Công đoàn",           "url": "https://laodong.vn/cong-doan"},
    {"name": "Giáo dục",            "url": "https://laodong.vn/giao-duc"},
    {"name": "Văn hóa - Giải trí",  "url": "https://laodong.vn/van-hoa-giai-tri"},
    {"name": "Bất động sản",        "url": "https://laodong.vn/quy-hoach"},
    {"name": "Xã hội",              "url": "https://laodong.vn/giao-thong"},
    {"name": "Xã hội",              "url": "https://laodong.vn/moi-truong"},
    {"name": "Thời sự",             "url": "https://laodong.vn/su-kien-binh-luan"},
    {"name": "Kinh tế",             "url": "https://laodong.vn/thi-truong"},
    {"name": "Kinh tế",             "url": "https://laodong.vn/doanh-nghiep-doanh-nhan"},
    {"name": "Công đoàn",           "url": "https://laodong.vn/viec-lam"},
]

CATEGORY_URL_MAP = {
    "thoi-su": "Thời sự", "su-kien-binh-luan": "Thời sự", "mat-tran": "Thời sự",
    "xa-hoi": "Xã hội", "giao-thong": "Xã hội", "moi-truong": "Xã hội",
    "kinh-doanh": "Kinh tế", "tien-te": "Kinh tế", "thi-truong": "Kinh tế",
    "doanh-nghiep": "Kinh tế",
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

# HTTP setup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'vi-VN,vi;q=0.9',
    'Referer': 'https://laodong.vn/'
}
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

print("Cookie bypass...")
try:
    with opener.open(urllib.request.Request('https://laodong.vn/', headers=headers)) as r:
        html0 = r.read().decode('utf-8')
    cm = re.search(r'D1N=([0-9a-fA-F]+)', html0)
    if cm:
        ck = http.cookiejar.Cookie(0,'D1N',cm.group(1),None,False,'laodong.vn',True,False,'/',True,False,None,True,None,None,{},False)
        cj.set_cookie(ck)
        print(f"  Cookie loaded.")
except Exception as e:
    print(f"  Warning: {e}")

# Load existing data
with open('tphcm_dongnambo_consolidated.json', encoding='utf-8') as f:
    existing = json.load(f)

seen_urls = set(a['url'] for a in existing)
print(f"Loaded {len(existing)} existing articles. seen_urls: {len(seen_urls)}")

new_articles = []

for province_key, spoke_cfg in SPOKE_CONFIG.items():
    keywords = PROVINCE_KEYWORDS[province_key]
    cat_counter = Counter(a['category'] for a in existing if a.get('province') == province_key)
    existing_count = sum(1 for a in existing if a.get('province') == province_key)
    target = spoke_cfg["target"]
    collected = 0

    print(f"\n{'='*60}")
    print(f"SUPPLEMENT: {spoke_cfg['province_label']} — already {existing_count}, need {target - existing_count} more")
    print(f"{'='*60}")

    if existing_count >= target:
        print(f"  Already enough articles, skipping.")
        continue

    for cat in CATEGORY_URLS:
        if collected + existing_count >= target:
            break
        cat_name = cat["name"]
        if cat_counter[cat_name] >= MAX_PER_CATEGORY:
            continue

        print(f"\n  [{cat_name}] {cat['url']} ...")

        for page in range(1, MAX_PAGES + 1):
            if collected + existing_count >= target or cat_counter[cat_name] >= MAX_PER_CATEGORY:
                break
            page_url = cat['url'] if page == 1 else f"{cat['url']}?page={page}"

            try:
                with opener.open(urllib.request.Request(page_url, headers=headers)) as resp:
                    html = resp.read().decode('utf-8')

                links = list(re.finditer(
                    r'<a[^>]+href="(https://laodong\.vn/[^"]+\.ldo)"[^>]*>(.*?)</a>',
                    html, re.DOTALL
                ))
                if not links:
                    break

                found_match = False
                for m in links:
                    if collected + existing_count >= target or cat_counter[cat_name] >= MAX_PER_CATEGORY:
                        break
                    url = m.group(1)
                    title = re.sub(r'<[^>]+>', '', m.group(2)).strip()
                    if not title or len(title) < 15 or url in seen_urls:
                        continue
                    title_lower = title.lower()
                    url_lower = url.lower()
                    if not any(kw in title_lower or kw in url_lower for kw in keywords):
                        continue

                    seen_urls.add(url)
                    found_match = True
                    time.sleep(0.25)

                    try:
                        with opener.open(urllib.request.Request(url, headers=headers)) as rd:
                            detail = rd.read().decode('utf-8')
                        img_m = re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', detail)
                        image = img_m.group(1) if img_m else ""
                        ch = re.search(r'<[hp][^>]*class="chapeau"[^>]*>(.*?)</[hp]>', detail, re.DOTALL)
                        excerpt = re.sub(r'<[^>]+>', '', ch.group(1)).strip() if ch else title
                        dm = re.search(r'(\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2})', detail)
                        date = dm.group(1) if dm else "02/06/2026 08:00"
                        actual_cat = guess_category(url, cat_name)

                        art = {
                            "id": 0, "title": title,
                            "excerpt": excerpt[:250],
                            "image": image or "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=800&q=80",
                            "url": url, "date": date,
                            "office": spoke_cfg["office"],
                            "province": spoke_cfg["province"],
                            "province_label": spoke_cfg["province_label"],
                            "tags": [spoke_cfg["tag_label"], actual_cat],
                            "category": actual_cat,
                            f"is_{spoke_cfg['province']}": True,
                            "district": spoke_cfg["province_label"]
                        }
                        new_articles.append(art)
                        cat_counter[actual_cat] += 1
                        collected += 1
                        print(f"    ✓ [{actual_cat}] {title[:65]}")
                    except Exception as ex:
                        print(f"    ✗ {ex}")

                if not found_match and page > 5:
                    break
            except Exception as ex:
                print(f"    ✗ Page {page}: {ex}")
                break

    print(f"\n  => Collected {collected} new articles for {spoke_cfg['province_label']}")

# Merge and reassign IDs
all_articles = existing + new_articles
for idx, art in enumerate(all_articles):
    art["id"] = idx

print(f"\n{'='*60}")
print(f"FINAL TOTAL: {len(all_articles)} articles")
dist = Counter(a.get("province","?") for a in all_articles)
for p, c in dist.items():
    print(f"  {p}: {c}")

with open('tphcm_dongnambo_consolidated.json', 'w', encoding='utf-8') as f:
    json.dump(all_articles, f, ensure_ascii=False, indent=4)
print(f"\n✅ Saved {len(all_articles)} articles to tphcm_dongnambo_consolidated.json")
