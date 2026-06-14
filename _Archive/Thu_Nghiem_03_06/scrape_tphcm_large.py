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
    {"name": "Kinh tế", "url": "https://laodong.vn/kinh-doanh"},
    {"name": "Giáo dục", "url": "https://laodong.vn/giao-duc"},
    {"name": "Bất động sản", "url": "https://laodong.vn/bat-dong-san"},
    {"name": "Công đoàn", "url": "https://laodong.vn/cong-doan"},
    {"name": "Văn hóa - Giải trí", "url": "https://laodong.vn/van-hoa-giai-tri"},
    {"name": "Thể thao", "url": "https://laodong.vn/the-thao"}
]

# Keywords config for 3 Southeast region provinces
REGION_CFG = {
    "tphcm": {
        "tag": "TPHCM",
        "keywords": ["tphcm", "tp.hcm", "hồ chí minh", "sài gòn", "bình dương", "vũng tàu", "bà rịa", "brvt", "thủ đức", "thuận an", "dĩ an", "bến cát", "củ chi", "cần giờ", "nhà bè", "hóc môn", "bình chánh", "long hải", "hồ tràm", "hòn bà", "đại nam", "thủy châu", "suối tiên", "đầm sen", "tao đàn", "landmark 81", "lê thị riêng", "chùa bà"],
    },
    "dongnai": {
        "tag": "Đồng Nai",
        "keywords": ["đồng nai", "biên hòa", "long khánh", "nhơn trạch", "trảng bom", "long thành", "vĩnh cửu", "định quán", "bình phước", "đồng xoài", "chơn thành", "bình long", "phước long", "bù đăng", "bù đốp", "lộc ninh", "sóc bom bo", "bà rá", "thác mơ", "nam cát tiên", "bửu long", "suối mơ", "hồ trị an", "giang điền"],
    },
    "tayninh": {
        "tag": "Tây Ninh",
        "keywords": ["tây ninh", "hòa thành", "trảng bàng", "bến cầu", "gò dầu", "dương minh châu", "tân biên", "tân châu", "núi bà đen", "gò kén", "tòa thánh tây ninh", "lò gò", "long an", "tân an", "kiến tường", "bến lức", "đức hòa", "cần giuộc", "cần đước", "thủ thừa", "làng nổi tân lập", "láng sen", "cánh đồng bất tận", "happy land", "mỹ quỳnh"],
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

# We scan up to 40 pages per category to find a high volume of articles
MAX_PAGES_PER_CATEGORY = 45

for cat in CATEGORIES:
    cat_name = cat["name"]
    target_category_name = "Kinh tế" if cat_name == "Kinh doanh" else cat_name
    print(f"\nScanning category: {cat_name} (mapped to {target_category_name})...")
    
    candidates = []
    
    # Phase 1: Collect all candidates from indices
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
                
                candidates.append({"url": url, "title": title})
                    
            if not found_any:
                break
                
        except Exception as ex:
            print(f"    Error scanning page {page}: {ex}")
            break
            
    print(f"  Scan done. Found {len(candidates)} total candidates for category {target_category_name}.")
    
    # Phase 2: Fetch details and perform deep content-based classification
    category_articles = []
    
    for cand in candidates:
        # We need a decent number of articles for the category, say, 25 articles overall
        if len(category_articles) >= 28:
            break
            
        print(f"    Fetching and classifying: '{cand['title']}'...")
        time.sleep(0.15)  # Safe rate limit
        try:
            req_detail = urllib.request.Request(cand["url"], headers=headers)
            with opener.open(req_detail) as resp:
                detail_html = resp.read().decode('utf-8')
            
            # Content checks
            title_lower = cand["title"].lower()
            url_lower = cand["url"].lower()
            body_text = detail_html.lower()
            
            # Map Spoke regions
            is_tphcm = False
            is_dongnai = False
            is_tayninh = False
            
            # Look in title, url, and full HTML body for regional cues
            # Check Tây Ninh first, then Đồng Nai, then TP.HCM to allow specific localization first
            if any(kw in title_lower or kw in url_lower or kw in body_text for kw in REGION_CFG["tayninh"]["keywords"]):
                is_tayninh = True
            elif any(kw in title_lower or kw in url_lower or kw in body_text for kw in REGION_CFG["dongnai"]["keywords"]):
                is_dongnai = True
            elif any(kw in title_lower or kw in url_lower or kw in body_text for kw in REGION_CFG["tphcm"]["keywords"]):
                is_tphcm = True
            else:
                # If no matching regional keywords are found, it is general. 
                # According to the user request: "nếu vẫn không đủ thì bạn lấy tin ở trang hub đẩy vào".
                # Hub articles will have both is_tphcm=True, is_dongnai=True, is_tayninh=True so they display in all Spokes or Hub default.
                # Let's mark it as a Hub article: available for all 3 Spokes to backfill.
                is_tphcm = True
                is_dongnai = True
                is_tayninh = True
            
            # Extract image, date, excerpt
            chapeau_match = re.search(r'<h2[^>]+class="chapeau"[^>]*>(.*?)</h2>', detail_html, re.DOTALL) or re.search(r'<p[^>]+class="chapeau"[^>]*>(.*?)</p>', detail_html, re.DOTALL)
            excerpt = re.sub(r'<[^>]+>', '', chapeau_match.group(1)).strip() if chapeau_match else ""
            img_match = re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', detail_html) or re.search(r'<meta[^>]+content="([^"]+)"[^>]+property="og:image"', detail_html) or re.search(r'<img[^>]+src="([^"]+)"', detail_html)
            
            image = ""
            if img_match:
                image = img_match.group(1)
            else:
                # fallback to parsing the page with simpler regex
                img_find = re.findall(r'https://[^\s"\'>]+\.(?:jpg|png|jpeg)', detail_html)
                if img_find:
                    image = img_find[0]
            
            if image and image.startswith('/'): 
                image = 'https://laodong.vn' + image
            if not image:
                image = "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=800&q=80"
                
            date_match = re.search(r'(\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2})', detail_html)
            date = date_match.group(1) if date_match else "01/06/2026 12:00"
            
            # Generate local tag based on mapping
            tags = [target_category_name]
            district = "Hub"
            if is_tayninh and not (is_tphcm and is_dongnai):
                tags.append("Tây Ninh")
                district = "Tây Ninh"
            elif is_dongnai and not (is_tphcm and is_tayninh):
                tags.append("Đồng Nai")
                district = "Đồng Nai"
            elif is_tphcm and not (is_dongnai and is_tayninh):
                tags.append("TP.HCM")
                district = "TP.HCM"
            
            article_data = {
                "id": 0,
                "title": cand["title"],
                "excerpt": excerpt or cand["title"],
                "image": image,
                "url": cand["url"],
                "date": date,
                "office": "VPTT TPHCM VÀ ĐÔNG NAM BỘ",
                "tags": tags,
                "category": target_category_name,
                "is_tphcm": is_tphcm,
                "is_dongnai": is_dongnai,
                "is_tayninh": is_tayninh,
                "district": district
            }
            category_articles.append(article_data)
            print(f"      Mapped to: TPHCM={is_tphcm}, DongNai={is_dongnai}, TayNinh={is_tayninh} | Image: {image[:60]}...")
        except Exception as ex:
            print(f"        Error fetching detail: {ex}")
            
    scraped_articles.extend(category_articles)

# Assign sequential IDs
for idx, art in enumerate(scraped_articles):
    art["id"] = idx

print(f"\nScraping complete! Got {len(scraped_articles)} articles.")

# Write to consolidated JSON
with open('tphcm_dongnambo_consolidated.json', 'w', encoding='utf-8') as f:
    json.dump(scraped_articles, f, ensure_ascii=False, indent=8)

print("Saved database to tphcm_dongnambo_consolidated.json successfully.")
