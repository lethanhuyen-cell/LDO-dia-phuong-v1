import os
import re

files = [
    'Phien_Ban_07_06/demo_landing_page_hanoi_clean.html',
    'Phien_Ban_07_06/demo_landing_page_hanoi.html',
    'Phien_Ban_07_06/index.html',
    'Phien_Ban_07_06/index_ads.html',
    'Phien_Ban_07_06/apply_ads_layout.py'
]

pattern = re.compile(r"""(                setInterval\(\(\) => \{
                    let nextSlide = \(window\.currentMostReadSlide \+ 1\) % slideCount;
                    window\.switchMostReadSlide\(nextSlide\);
                \}, 5000\);
            \}
        \})(?:\r?\n)(?:    \})""")

replacement = r"\1"

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content, count = pattern.subn(replacement, content)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filepath} ({count} replacements)")
        else:
            print(f"Pattern not found in {filepath}")
