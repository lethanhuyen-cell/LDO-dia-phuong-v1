with open('Phien_Ban_07_06/apply_tphcm_layout.py', 'r', encoding='utf-8') as f:
    c = f.read()
s = c.find('<div class="main-content-col">')
e = c.find('</div>  <!-- /main-content-col -->')
print('s:', s, 'e:', e)
sub = c[s:e]
opens = sub.count('<div')
closes = sub.count('</div')
print('Main content col:', opens, 'opens,', closes, 'closes')
print('Diff:', opens - closes)
