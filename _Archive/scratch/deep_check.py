with open('tphcm_index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('<div class="main-content-col">')
idx2 = text.find('<!-- ===== CỘT PHẢI')
substr = text[idx1:idx2]

opens = 0
closes = 0
for i in range(len(substr)):
    if substr[i:i+4] == '<div':
        opens += 1
    elif substr[i:i+5] == '</div':
        closes += 1

print('opens:', opens, 'closes:', closes, 'diff:', opens - closes)

# Print out the blocks again
import re
blocks = [
    "<!-- BLOCK 1",
    "<!-- DYNAMIC FULL-WIDTH MOST READ CAROUSEL",
    "<!-- BLOCK 2",
    "<!-- CHUYỂN ĐỘNG HẠ TẦNG",
    "<!-- AD SLOT 03",
    "<!-- BLOCK 4:",
    "<!-- BLOCK 4.5",
    "<!-- BLOCK 5:",
    "<!-- BLOCK 5.5",
    "<!-- BLOCK 5.8",
    "<!-- BLOCK 6:",
    "</div>  <!-- /main-content-col"
]

for i in range(len(blocks)-1):
    b_start = substr.find(blocks[i])
    b_end = substr.find(blocks[i+1])
    if b_start != -1 and b_end != -1:
        chunk = substr[b_start:b_end]
        o = chunk.count('<div')
        c = chunk.count('</div')
        print(f"Block {i}: opens {o}, closes {c}, diff {o - c}")
