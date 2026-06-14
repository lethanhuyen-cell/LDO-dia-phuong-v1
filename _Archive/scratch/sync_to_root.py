import sys
import shutil
import os

sys.stdout.reconfigure(encoding='utf-8')

src = r'c:\Users\Admin\Documents\Work_Folders\4_Hoat_Dong_Ca_Nhan\LANDING PAGE THƯỜNG TRÚ\Phien_Ban_07_06'
dst = r'c:\Users\Admin\Documents\Work_Folders\4_Hoat_Dong_Ca_Nhan\LANDING PAGE THƯỜNG TRÚ'

# Files to copy from test folder to root
html_files = [
    'index.html',
    'index_ads.html',
    'demo_landing_page_hanoi.html',
    'demo_landing_page_hanoi_ads.html',
    'demo_landing_page_tphcm.html',
    'demo_landing_page_tphcm_ads.html',
    'tphcm_index.html',
    'tphcm_index_ads.html',
]

copied = 0
skipped = 0

for fname in html_files:
    src_file = os.path.join(src, fname)
    dst_file = os.path.join(dst, fname)
    if os.path.exists(src_file):
        shutil.copy2(src_file, dst_file)
        print(f'  [OK] Copied: {fname}')
        copied += 1
    else:
        print(f'  [SKIP] Not found in test folder: {fname}')
        skipped += 1

print(f'\nDone! Copied {copied} files, skipped {skipped} files.')
