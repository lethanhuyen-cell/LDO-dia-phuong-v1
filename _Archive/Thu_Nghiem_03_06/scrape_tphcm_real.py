import urllib.request
import re
import http.cookiejar
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

# List of categories to scrape and map for the landing page
CATEGORIES = [
    {"name": "Thời sự", "url": "https://laodong.vn/thoi-su"},
    {"name": "Xã hội", "url": "https://laodong.vn/xa-hoi"},
    {"name": "Kinh tế", "url": "https://laodong.vn/kinh-doanh"}, # We will map "Kinh doanh" to "Kinh tế"
    {"name": "Giáo dục", "url": "https://laodong.vn/giao-duc"},
    {"name": "Bất động sản", "url": "https://laodong.vn/bat-dong-san"},
    {"name": "Công đoàn", "url": "https://laodong.vn/cong-doan"},
    {"name": "Văn hóa - Giải trí", "url": "https://laodong.vn/van-hoa-giai-tri"},
    {"name": "Thể thao", "url": "https://laodong.vn/the-thao"}
]

# Keywords config for 3 Southeast region new provinces (ông/cha/con/cháu hierarchy)
REGION_CFG = {
    "tphcm": {
        "tag": "TPHCM",
        "keywords": ["tphcm", "tp.hcm", "hồ chí minh", "sài gòn", "bình dương", "vũng tàu", "bà rịa", "brvt", "thủ đức", "thuận an", "dĩ an", "bến cát", "củ chi", "cần giờ", "nhà bè", "hóc môn", "bình chánh", "long hải", "hồ tràm", "hòn bà", "đại nam", "thủy châu", "suối tiên", "đầm sen", "tao đàn", "landmark 81", "lê thị riêng", "chùa bà"],
        "disambiguation": ["bình dương", "vũng tàu", "bà rịa"]
    },
    "dongnai": {
        "tag": "Đồng Nai",
        "keywords": ["đồng nai", "biên hòa", "long khánh", "nhơn trạch", "trảng bom", "long thành", "vĩnh cửu", "định quán", "bình phước", "đồng xoài", "chơn thành", "bình long", "phước long", "bù đăng", "bù đốp", "lộc ninh", "sóc bom bo", "bà rá", "thác mơ", "nam cát tiên", "bửu long", "suối mơ", "hồ trị an", "giang điền"],
        "disambiguation": ["bình phước"]
    },
    "tayninh": {
        "tag": "Tây Ninh",
        "keywords": ["tây ninh", "hòa thành", "trảng bàng", "bến cầu", "gò dầu", "dương minh châu", "tân biên", "tân châu", "núi bà đen", "gò kén", "tòa thánh tây ninh", "lò gò", "long an", "tân an", "kiến tường", "bến lức", "đức hòa", "cần giuộc", "cần đước", "thủ thừa", "làng nổi tân lập", "láng sen", "cánh đồng bất tận", "happy land", "mỹ quỳnh"],
        "disambiguation": ["long an", "châu thành"]
    }
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Setup cookie jar
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

# Bypass cookie gate
print("Initializing cookie gate bypass...")
req_init = urllib.request.Request('https://laodong.vn/', headers=headers)
try:
    with opener.open(req_init) as resp:
        html_init = resp.read().decode('utf-8')
    cookie_match = re.search(r'D1N=([0-9a-fA-F]+)', html_init)
    if cookie_match:
        cookie_val = cookie_match.group(1)
        cookie = http.cookiejar.Cookie(
            version=0, name='D1N', value=cookie_val, port=None, port_specified=False,
            domain='laodong.vn', domain_specified=True, domain_initial_dot=False,
            path='/', path_specified=True, secure=False, expires=None, discard=True,
            comment=None, comment_url=None, rest={}, rfc2109=False
        )
        cj.set_cookie(cookie)
        print(f"Cookie D1N={cookie_val} successfully loaded into jar.")
except Exception as e:
    print("Warning: Cookie bypass failed, proceeding with default requests.", e)

scraped_articles = []
seen_urls = set()

MAX_PAGES_PER_CATEGORY = 12
TARGET_ARTICLES_PER_CATEGORY = 8

for cat in CATEGORIES:
    cat_name = cat["name"]
    target_category_name = "Kinh tế" if cat_name == "Kinh doanh" else cat_name
    print(f"\nScanning category: {cat_name} (mapped to {target_category_name})...")
    
    regional_candidates = []
    general_candidates = []
    
    # Phase 1: Collect candidates list without fetching details yet
    for page in range(1, MAX_PAGES_PER_CATEGORY + 1):
        page_url = cat['url'] if page == 1 else f"{cat['url']}?page={page}"
        print(f"  Scanning page {page} index...")
        
        try:
            req = urllib.request.Request(page_url, headers=headers)
            with opener.open(req) as resp:
                html = resp.read().decode('utf-8')
            
            links = re.finditer(r'<a[^>]+href="(https://laodong\.vn/[^"]+\.ldo)"[^>]*>(.*?)</a>', html, re.DOTALL)
            found_any = False
            for m in links:
                url = m.group(1)
                title = re.sub(r'<[^>]+>', '', m.group(2)).strip()
                if not title or len(title) < 15 or url in seen_urls:
                    continue
                seen_urls.add(url)
                found_any = True
                
                title_lower = title.lower()
                is_match = False
                target_region = None
                for reg, cfg in REGION_CFG.items():
                    if any(kw in title_lower or kw in url.lower() for kw in cfg["keywords"]):
                        is_match = True
                        target_region = reg
                        break
                
                candidate = {"url": url, "title": title, "target_region": target_region}
                if is_match:
                    regional_candidates.append(candidate)
                else:
                    general_candidates.append(candidate)
                    
            if not found_any:
                break
                
            # If we have gathered enough regional candidates, we can stop scanning pages to save time
            if len(regional_candidates) >= TARGET_ARTICLES_PER_CATEGORY:
                break
                
        except Exception as ex:
            print(f"    Error scanning page {page}: {ex}")
            break
            
    print(f"  Scan done. Found {len(regional_candidates)} regional, {len(general_candidates)} general candidates.")
    
    # Phase 2: Fetch details for regional candidates
    category_articles = []
    for cand in regional_candidates[:TARGET_ARTICLES_PER_CATEGORY]:
        print(f"    Fetching regional: '{cand['title']}'...")
        time.sleep(0.2)
        try:
            req_detail = urllib.request.Request(cand["url"], headers=headers)
            with opener.open(req_detail) as resp:
                detail_html = resp.read().decode('utf-8')
            
            chapeau_match = re.search(r'<h2[^>]+class="chapeau"[^>]*>(.*?)</h2>', detail_html, re.DOTALL) or re.search(r'<p[^>]+class="chapeau"[^>]*>(.*?)</p>', detail_html, re.DOTALL)
            excerpt = re.sub(r'<[^>]+>', '', chapeau_match.group(1)).strip() if chapeau_match else ""
            img_match = re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', detail_html) or re.search(r'<img[^>]+src="([^"]+)"', detail_html)
            image = img_match.group(1) if img_match else ""
            if image.startswith('/'): image = 'https://laodong.vn' + image
            date_match = re.search(r'(\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2})', detail_html)
            date = date_match.group(1) if date_match else "01/06/2026 12:00"
            
            article_data = {
                "id": 0,
                "title": cand["title"],
                "excerpt": excerpt or cand["title"],
                "image": image or "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=800&q=80",
                "url": cand["url"],
                "date": date,
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "tags": [REGION_CFG[cand["target_region"]]["tag"], target_category_name],
                "category": target_category_name
            }
            if cand["target_region"] == "tphcm":
                article_data["is_tphcm"] = True
                article_data["district"] = "TP.HCM"
            elif cand["target_region"] == "dongnai":
                article_data["is_dongnai"] = True
                article_data["district"] = "Đồng Nai"
            elif cand["target_region"] == "tayninh":
                article_data["is_tayninh"] = True
                article_data["district"] = "Tây Ninh"
            category_articles.append(article_data)
        except Exception as ex:
            print(f"      Error fetching detail: {ex}")
            
    # Phase 3: Fetch details for general candidates (if we need to backfill)
    needed = TARGET_ARTICLES_PER_CATEGORY - len(category_articles)
    if needed > 0 and general_candidates:
        print(f"    Backfilling {needed} general articles...")
        for cand in general_candidates[:needed]:
            print(f"      Fetching general: '{cand['title']}'...")
            time.sleep(0.2)
            try:
                req_detail = urllib.request.Request(cand["url"], headers=headers)
                with opener.open(req_detail) as resp:
                    detail_html = resp.read().decode('utf-8')
                
                chapeau_match = re.search(r'<h2[^>]+class="chapeau"[^>]*>(.*?)</h2>', detail_html, re.DOTALL) or re.search(r'<p[^>]+class="chapeau"[^>]*>(.*?)</p>', detail_html, re.DOTALL)
                excerpt = re.sub(r'<[^>]+>', '', chapeau_match.group(1)).strip() if chapeau_match else ""
                img_match = re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', detail_html) or re.search(r'<img[^>]+src="([^"]+)"', detail_html)
                image = img_match.group(1) if img_match else ""
                if image.startswith('/'): image = 'https://laodong.vn' + image
                date_match = re.search(r'(\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2})', detail_html)
                date = date_match.group(1) if date_match else "01/06/2026 12:00"
                
                article_data = {
                    "id": 0,
                    "title": cand["title"],
                    "excerpt": excerpt or cand["title"],
                    "image": image or "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=800&q=80",
                    "url": cand["url"],
                    "date": date,
                    "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                    "tags": ["TPHCM", target_category_name],
                    "category": target_category_name,
                    "is_tphcm": True,
                    "district": "TP.HCM"
                }
                category_articles.append(article_data)
            except Exception as ex:
                print(f"        Error fetching detail: {ex}")
                
    scraped_articles.extend(category_articles)

# Assign sequential IDs
for idx, art in enumerate(scraped_articles):
    art["id"] = idx

print(f"\nFinished paginated scraping! Total of {len(scraped_articles)} articles consolidated successfully.")

# Write to database JSON
with open('tphcm_dongnambo_consolidated.json', 'w', encoding='utf-8') as f:
    json.dump(scraped_articles, f, ensure_ascii=False, indent=8)

print("tphcm_dongnambo_consolidated.json successfully updated.")
