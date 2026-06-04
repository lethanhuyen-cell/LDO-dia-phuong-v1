import urllib.request
import re
import http.cookiejar
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://laodong.vn/thoi-su/cong-an-ha-noi-thang-cap-bac-ham-nang-luong-cho-hon-5000-can-bo-chien-si-1709840.ldo"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def extract_article_content(html):
    match = re.search(r'<div[^>]+(?:id="gallery-ctt"|class="art-body")[^>]*>', html)
    if not match:
        match = re.search(r'<article[^>]+class="article-detail"[^>]*>', html)
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
    print("Warning: Cookie bypass failed", e)

print(f"Fetching details from {url}...")
try:
    req = urllib.request.Request(url, headers=headers)
    with opener.open(req) as resp:
        html = resp.read().decode('utf-8')
    
    content = extract_article_content(html)
    print("EXTRACTED CONTENT LENGTH:", len(content))
    print("PREVIEW:")
    print(content[:1500])
    print("...")
    print("END PREVIEW")
except Exception as e:
    print("Error:", e)
