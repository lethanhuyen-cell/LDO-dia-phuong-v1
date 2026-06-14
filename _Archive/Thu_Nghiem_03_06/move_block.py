import sys
import re

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the right block
    start_str = '<!-- Right: Local Business Directory -->'
    start_idx = content.find(start_str)
    
    # We need to find the </div> that closes this right block.
    # The block ends right before BLOCK 5.8: CẨM NANG HÀ NỘI
    next_block_str = '<!-- BLOCK 5.8: CẨM NANG HÀ NỘI'
    # Wait, TPHCM has a different next block maybe?
    # Let's look for the closing div of the premium-card.
    
    # Actually, a regex that matches from start_str to the end of the block.
    # The end of the block is:
    #                     <!-- Loaded dynamically via JS -->
    #                     </div>
    #                 </div>
    end_marker = '<!-- Loaded dynamically via JS -->\n                    </div>\n                </div>'
    if end_marker not in content:
        print("End marker not found in", file_path)
        return
    end_idx = content.find(end_marker, start_idx) + len(end_marker)
    
    block_to_move = content[start_idx:end_idx]
    
    # Remove block_to_move from the left section
    content = content.replace(block_to_move, '')
    
    # Change the grid layout of BLOCK 5.5 to remove grid columns
    grid_str = '<div class="m-top-20 columns-layout" style="display: grid; grid-template-columns: 2fr 1fr; gap: 20px; font-family: Arial, sans-serif;">'
    new_grid_str = '<div class="m-top-20 columns-layout" style="display: flex; flex-direction: column; gap: 20px; font-family: Arial, sans-serif;">'
    content = content.replace(grid_str, new_grid_str)
    
    # Insert block_to_move into the Right Sidebar
    sidebar_str = '<!-- ===== CỘT PHẢI: SIDEBAR TIỆN ÍCH (STICKY) ===== -->\n                <div class="sidebar-col" style="align-self: start; display: flex; flex-direction: column; gap: 20px;">'
    sidebar_idx = content.find(sidebar_str)
    if sidebar_idx == -1:
        print("Sidebar not found in", file_path)
        return
    
    new_sidebar = sidebar_str + '\n\n                ' + block_to_move
    content = content.replace(sidebar_str, new_sidebar)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Processed {file_path}')

process_file('apply_ads_layout.py')
process_file('apply_tphcm_layout.py')
