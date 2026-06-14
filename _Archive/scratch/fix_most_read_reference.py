import os

files_to_fix = [
    'Phien_Ban_07_06/apply_ads_layout.py',
    'Phien_Ban_07_06/apply_tphcm_layout.py'
]

target_str = """            mostReadContainer.innerHTML = containerHtml;
            if (mostReadDotsEl) mostReadDotsEl.innerHTML = dotsHtml;"""

replace_str = """            let mrc = document.getElementById('most-read-container');
            if (mrc) mrc.innerHTML = containerHtml;
            let mrde = document.getElementById('most-read-dots');
            if (mrde) mrde.innerHTML = dotsHtml;"""

for file_path in files_to_fix:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if target_str in content:
            content = content.replace(target_str, replace_str)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {file_path}")
        else:
            print(f"Target string not found in {file_path}")
    else:
        print(f"File not found: {file_path}")
