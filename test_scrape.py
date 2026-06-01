import urllib.request
import re
import http.cookiejar
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://laodong.vn/thoi-su/cong-an-ha-noi-thang-cap-bac-ham-nang-luong-cho-hon-5000-can-bo-chien-si-1709840.ldo"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

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
    
    # Let's search for some div elements
    print("HTML length:", len(html))
    
    # Check for <article
    for match in re.finditer(r'<article[^>]*>', html):
        print("Found article tag:", match.group(0))
        start_idx = match.start()
        print(html[start_idx:start_idx+1000])
        print("---")
        
except Exception as e:
    print("Error:", e)
