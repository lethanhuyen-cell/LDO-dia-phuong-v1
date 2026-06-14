import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

def refactor_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find two-col-layout start
    two_col_start_regex = r'(\s*<!-- ========== BẮT ĐẦU LAYOUT 2 CỘT \(VNEXPRESS-STYLE\) ========== -->\s*<div class="m-top-20 two-col-layout"[^\n]*\n\s*<!-- ===== CỘT TRÁI: NỘI DUNG CHÍNH ===== -->\s*<div class="main-content-col">\s*)'
    match = re.search(two_col_start_regex, content)
    if not match:
        print(f'Error finding two-col-layout start in {filepath}')
        two_col_start_regex = r'(\s*<!-- ========== BẮT ĐẦU LAYOUT 2 CỘT ========== -->\s*<div class="m-top-20 two-col-layout"[^\n]*\n\s*<!-- ===== CỘT TRÁI: NỘI DUNG CHÍNH ===== -->\s*<div class="main-content-col">\s*)'
        match = re.search(two_col_start_regex, content)
        if not match:
            print('Still not found. Aborting.')
            return
            
    two_col_str = match.group(1)
    content = content.replace(two_col_str, '\n')
    
    # Insert before BLOCK 1
    block1_idx = content.find('<!-- BLOCK 1: MAIN COVER GRID -->')
    if block1_idx == -1:
        print(f'Error finding BLOCK 1 in {filepath}')
        return
        
    line_start_idx = content.rfind('\n', 0, block1_idx)
    content = content[:line_start_idx+1] + two_col_str.lstrip('\n') + content[line_start_idx+1:]
    
    # Extract TOC + Poll
    toc_start_str = '<!-- KHỐI MỤC LỤC TIỆN ÍCH (Thay thế QC Vietcombank) -->'
    toc_start_idx = content.find(toc_start_str)
    if toc_start_idx != -1:
        poll_end_regex = r'(</div>\s*</div>\s*<!-- Row of 3 bottom stories -->)'
        poll_match = re.search(poll_end_regex, content[toc_start_idx:])
        if poll_match:
            toc_end_idx = toc_start_idx + poll_match.start()
            toc_content = content[toc_start_idx:toc_end_idx]
            content = content[:toc_start_idx] + content[toc_end_idx:]
            
            sidebar_idx = content.find('<div class="sidebar-col"')
            if sidebar_idx != -1:
                sidebar_open_end = content.find('>', sidebar_idx) + 1
                content = content[:sidebar_open_end] + '\n\n' + toc_content + '\n' + content[sidebar_open_end:]
            else:
                print(f'Error finding sidebar-col in {filepath}')
        else:
            print(f'Error finding Poll end in {filepath}')
    else:
        print(f'Error finding TOC in {filepath}')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully refactored {filepath}')

refactor_file('Thu_Nghiem_03_06/apply_ads_layout.py')
refactor_file('Thu_Nghiem_03_06/apply_tphcm_layout.py')
