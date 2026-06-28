# -*- coding: utf-8 -*-
import re

files = [
    'apply_ads_layout.py',
    'apply_tphcm_layout.py',
    'apply_tphcm_layout_opt1.py',
    'apply_tphcm_layout_opt2.py'
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace grid-template-columns
    content = re.sub(
        r'grid-template-columns: repeat\(auto-fit, minmax\(\d+px, 1fr\)\)',
        r'grid-template-columns: repeat(3, 1fr)',
        content
    )
    
    # Add a third row to HTML if not present
    if 'id="categories-grid-row3"' not in content:
        row2_div = r'<div class="m-top-20" style="display: grid; grid-template-columns: repeat\(3, 1fr\); gap: 15px;" id="categories-grid-row2">\s*<!-- JS populated Row 2 .*? -->\s*</div>'
        row3_div = r'\g<0>\n            <div class="m-top-20" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px;" id="categories-grid-row3">\n                <!-- JS populated Row 3 (3 columns) -->\n            </div>'
        content = re.sub(row2_div, row3_div, content)

    # Replace JS arrays
    content = re.sub(
        r"let row1_cats = \['Thời sự', 'Xã hội', 'Giáo dục', 'Kinh tế'\];",
        "let row1_cats = ['Thời sự', 'Xã hội', 'Giáo dục'];\n        let row2_cats = ['Kinh tế', 'Công đoàn', 'Bất động sản'];\n        let row3_cats = ['Văn hóa - Giải trí', 'Thể thao'];",
        content
    )
    content = re.sub(
        r"let row2_cats = \['Công đoàn', 'Bất động sản', 'Văn hóa - Giải trí', 'Thể thao'\];\s*",
        "",
        content
    )
    
    content = re.sub(
        r'const row1Categories = \["Thời sự", "Xã hội", "Giáo dục", "Kinh tế"\];',
        'const row1Categories = ["Thời sự", "Xã hội", "Giáo dục"];\n        const row2Categories = ["Kinh tế", "Công đoàn", "Bất động sản"];\n        const row3Categories = ["Văn hóa - Giải trí", "Thể thao"];',
        content
    )
    content = re.sub(
        r'const row2Categories = \["Công đoàn", "Bất động sản", "Văn hóa - Giải trí", "Thể thao"\];\s*',
        '',
        content
    )
    
    # Add JS logic for row3
    if 'row3Html +=' not in content and 'row3_html +=' not in content:
        if 'row2_cats.forEach' in content:
            js2 = r"let row2_html = '';\s*row2_cats\.forEach\(cat => { row2_html \+= make_col_html\(cat\); }\);\s*document\.getElementById\('categories-grid-row2'\)\.innerHTML = row2_html;"
            js3 = r"\g<0>\n\n            let el_categories_grid_row3 = document.getElementById('categories-grid-row3');\n            if (el_categories_grid_row3) {\n                let row3_html = '';\n                row3_cats.forEach(cat => { row3_html += make_col_html(cat); });\n                el_categories_grid_row3.innerHTML = row3_html;\n            }"
            content = re.sub(js2, js3, content)
        elif 'row2Categories.forEach' in content:
            js2 = r"let row2Html = '';\s*row2Categories\.forEach\(cat => { row2Html \+= makeColumnHtml\(cat\); }\);\s*document\.getElementById\('categories-grid-row2'\)\.innerHTML = row2Html;"
            js3 = r"\g<0>\n\n        let row3Html = '';\n        row3Categories.forEach(cat => { row3Html += makeColumnHtml(cat); });\n        let row3El = document.getElementById('categories-grid-row3');\n        if(row3El) row3El.innerHTML = row3Html;"
            content = re.sub(js2, js3, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated " + file)
