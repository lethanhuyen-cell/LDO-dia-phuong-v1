with open('Phien_Ban_07_06/apply_tphcm_layout.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

s = -1
e = -1
for i, line in enumerate(lines):
    if '<div class="main-content-col">' in line:
        s = i
    if '</div>  <!-- /main-content-col -->' in line:
        e = i
        break

total = 0
for i in range(s, e):
    opens = lines[i].count('<div')
    closes = lines[i].count('</div')
    total += opens - closes
    if opens != closes:
        print(f"Line {i+1}: opens={opens}, closes={closes}, running={total}")
        print("  " + lines[i].strip())
