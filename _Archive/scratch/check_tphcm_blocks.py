import re
import sys

# Change standard output encoding
sys.stdout.reconfigure(encoding='utf-8')

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
        "<!-- CHUYỂN ĐỘNG",
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
            print(f"Block {i}: opens {opens}, closes {closes}, diff {opens - closes}")
        else:
            print(f"Missing Block {i} or {i+1}")

check_divs('tphcm_index.html')
