import re
with open('Phien_Ban_07_06/apply_tphcm_layout.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Original JS had this structure:
# document.getElementById('main-cover-container').innerHTML = `...`;
# document.getElementById('subcover-container').innerHTML = `...`;
# document.getElementById('spotlight-container').innerHTML = `...`;

pattern_str = r"document\.getElementById\('main-cover-container'\)\.innerHTML = `.*?document\.getElementById\('spotlight-container'\)\.innerHTML = `[^`]*`;"
js_pattern = re.compile(pattern_str, re.DOTALL)
match = js_pattern.search(text)

if match:
    print('Match found! Length:', len(match.group(0)))
else:
    print('Match NOT found!')
