import re

def check_divs(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    idx1 = text.find('<div class="main-content-col">')
    idx2 = text.find('<!-- ===== CỘT PHẢI')
    substr = text[idx1:idx2]
    
    blocks = [
        "<!-- BLOCK 1",
        "<!-- DYNAMIC FULL-WIDTH MOST READ CAROUSEL",
        "<!-- BLOCK 2",
        "<!-- AD SLOT 03",
        "<!-- BLOCK 4:",
        "<!-- BLOCK 4.5",
        "<!-- BLOCK 5:",
        "<!-- BLOCK 5.5",
        "<!-- BLOCK 5.8",
        "<!-- BLOCK 6:",
        "</div>  <!-- /main-content-col"
    ]
    
    print(f"--- {filepath} ---")
    for i in range(len(blocks)-1):
        b_start = substr.find(blocks[i])
        b_end = substr.find(blocks[i+1])
        if b_start != -1 and b_end != -1:
            chunk = substr[b_start:b_end]
            opens = chunk.count('<div')
            closes = chunk.count('</div')
            print(f"{blocks[i]}: opens {opens}, closes {closes}, diff {opens - closes}")

check_divs('Phien_Ban_07_06/apply_ads_layout.py')
check_divs('Phien_Ban_07_06/apply_tphcm_layout.py')
