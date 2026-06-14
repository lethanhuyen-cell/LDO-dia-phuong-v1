with open('scratch/old_tphcm.py', 'r', encoding='utf-16') as f:
    text = f.read()

idx1 = text.find('<div class="main-content-col">')
idx2 = text.find('<!-- ===== CỘT PHẢI')

substr = text[idx1:idx2]
opens = substr.count('<div')
closes = substr.count('</div')
print('Old TPHCM count:', opens - closes)
