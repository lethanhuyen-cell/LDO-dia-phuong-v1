import os

# Files to process
files = [
    'Phien_Ban_07_06/demo_landing_page_hanoi_clean.html',
    'Phien_Ban_07_06/demo_landing_page_hanoi.html',
    'Phien_Ban_07_06/index.html',
    'Phien_Ban_07_06/index_ads.html',
    'Phien_Ban_07_06/tphcm_index.html',
    'Phien_Ban_07_06/apply_ads_layout.py',
    'Phien_Ban_07_06/apply_tphcm_layout.py',
    'Phien_Ban_07_06/apply_tphcm_layout_opt1.py',
    'Phien_Ban_07_06/apply_tphcm_layout_opt2.py'
]

pattern_to_find = """            setInterval(() => {
                let nextSlide = (window.currentMostReadSlide + 1) % slideCount;
                window.switchMostReadSlide(nextSlide);
            }, 5000);
        }
    }
"""

replacement = """            setInterval(() => {
                let nextSlide = (window.currentMostReadSlide + 1) % slideCount;
                window.switchMostReadSlide(nextSlide);
            }, 5000);
        }
"""

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if pattern_to_find in content:
            new_content = content.replace(pattern_to_find, replacement)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filepath}")
        else:
            print(f"Pattern not found in {filepath}")
