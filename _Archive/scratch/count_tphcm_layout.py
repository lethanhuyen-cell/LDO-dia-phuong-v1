with open('Phien_Ban_07_06/apply_tphcm_layout.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('<div class="main-content-col">')
idx2 = text.find('<!-- ===== CỘT PHẢI')

substr = text[idx1:idx2]
opens = substr.count('<div')
closes = substr.count('</div')
print('apply_tphcm_layout count:', opens - closes)
