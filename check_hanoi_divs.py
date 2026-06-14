with open('Phien_Ban_07_06/apply_ads_layout.py', 'r', encoding='utf-8') as f:
    c = f.read()
s = c.find('<div class="main-content-col">')
e = c.find('</div>  <!-- /main-content-col -->')
sub = c[s:e]
opens = sub.count('<div')
closes = sub.count('</div')
print('Hanoi diff:', opens - closes)
