import urllib.request
import re
import http.cookiejar
import json
import time
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def extract_article_content(html):
    match = re.search(r'<div[^>]+(?:id="gallery-ctt"|class="art-body")[^>]*>', html)
    if not match:
        match = re.search(r'<article[^>]+class="article-detail"[^>]*>', html)
        if not match:
            # Fallback to general content container
            match = re.search(r'<div[^>]+class="content"[^>]*>', html)
            if not match:
                return ""
    
    start_pos = match.end()
    open_tag = "div" if "div" in match.group(0) else "article"
    
    pos = start_pos
    depth = 1
    while depth > 0 and pos < len(html):
        next_open = html.find(f"<{open_tag}", pos)
        next_close = html.find(f"</{open_tag}>", pos)
        
        if next_close == -1:
            break
            
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + len(open_tag) + 1
        else:
            depth -= 1
            pos = next_close + len(open_tag) + 3
            if depth == 0:
                end_pos = next_close
                return html[start_pos:end_pos].strip()
    
    return html[start_pos:start_pos+3000]

def clean_extracted_html(content_html):
    if not content_html:
        return ""
    # Remove unwanted scripts and styling if any
    content_html = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', content_html, flags=re.IGNORECASE)
    # Remove related box divs or shares if any
    content_html = re.sub(r'<div[^>]+class="[^"]*(?:related|sharing|share)[^"]*"[^>]*>.*?</div>', '', content_html, flags=re.DOTALL)
    # Rewrite relative image paths to absolute
    content_html = re.sub(r'src="/', 'src="https://laodong.vn/', content_html)
    # Handle lazy-loaded images: replace src with data-src if src is tiny/empty and data-src is present
    # Usually, we can just replace src with data-src if it exists
    def replace_lazy_img(match):
        img_tag = match.group(0)
        data_src = re.search(r'data-src="([^"]+)"', img_tag)
        if data_src:
            real_url = data_src.group(1)
            # Replace src attribute with the real URL
            if 'src="' in img_tag:
                img_tag = re.sub(r'src="[^"]*"', f'src="{real_url}"', img_tag)
            else:
                img_tag = img_tag[:-1] + f' src="{real_url}">'
        return img_tag
    
    content_html = re.sub(r'<img[^>]+>', replace_lazy_img, content_html)
    return content_html.strip()

def process_file(json_path):
    if not os.path.exists(json_path):
        print(f"File {json_path} does not exist.")
        return
        
    print(f"\nProcessing {json_path}...")
    with open(json_path, 'r', encoding='utf-8') as f:
        articles = json.load(f)
        
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)
    
    # Bypass cookie gate
    print("Bypassing cookie gate...")
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
            print("Cookie bypass active.")
    except Exception as e:
        print("Warning: Cookie bypass failed", e)
        
    updated_count = 0
    for idx, art in enumerate(articles):
        url = art.get('url', '')
        if not url or not url.startswith('https://laodong.vn/'):
            continue
            
        # If it already has content, we can skip or reload (skip to be faster/safer unless empty)
        if art.get('content') and len(art['content']) > 100:
            continue
            
        print(f"[{idx+1}/{len(articles)}] Fetching: {art['title']} ({url})")
        try:
            req = urllib.request.Request(url, headers=headers)
            with opener.open(req) as resp:
                html = resp.read().decode('utf-8')
            
            raw_content = extract_article_content(html)
            clean_content = clean_extracted_html(raw_content)
            
            if clean_content:
                art['content'] = clean_content
                updated_count += 1
                print(f"  Successfully fetched ({len(clean_content)} chars)")
            else:
                # Use excerpt as fallback content
                art['content'] = f"<p>{art['excerpt']}</p><p><i>(Nội dung đầy đủ của bài viết đang được cập nhật...)</i></p>"
                print("  Warning: Empty content extracted, using excerpt fallback.")
                
            time.sleep(0.15) # respect rate limits
        except Exception as ex:
            print(f"  Error fetching {url}: {ex}")
            art['content'] = f"<p>{art['excerpt']}</p><p><i>(Không thể tải nội dung chi tiết bài viết lúc này...)</i></p>"
            
    if updated_count > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(articles, f, ensure_ascii=False, indent=4)
        print(f"Saved {updated_count} updated articles to {json_path}")
    else:
        print(f"No new articles needed updates in {json_path}")

# Run for both Hanoi and TPHCM json files
process_file('hanoi_final_consolidated.json')
process_file('tphcm_dongnambo_consolidated.json')
print("\nDone processing all databases!")
