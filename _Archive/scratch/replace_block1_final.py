import re

def process_file(filepath, region_text, is_hanoi):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace HTML structure
    html_pattern = re.compile(r'<!-- BLOCK 1: MAIN COVER GRID -->.*?<!-- DYNAMIC FULL-WIDTH MOST READ CAROUSEL', re.DOTALL)
    
    new_html = f'''<!-- BLOCK 1: MAIN COVER GRID - HERO MINIMALIST -->
            <div class="blk-10 main-cover m-top-20" style="display: flex; gap: 25px; align-items: stretch;">
                <!-- Left Hero (65%) -->
                <div class="hero-left" style="flex: 0 0 65%; width: 65%;">
                    <div id="main-cover-container">
                        <!-- JS populated -->
                    </div>
                    <!-- Row of 3 bottom stories -->
                    <div class="subcover-bottom-row" id="subcover-bottom-row" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 20px; padding-top: 20px; border-top: 1px dashed #eee;">
                        <!-- JS populated -->
                    </div>
                </div>
                
                <!-- Right Trending (35%) -->
                <div class="hero-right" style="flex: 0 0 calc(35% - 25px); width: calc(35% - 25px);">
                    <div class="p-tieudiem" style="height: 100%; background: #fcfcfc; border: 1px solid #eef1f5; border-radius: 6px; padding: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
                        <div style="font-size: 14px; font-weight: bold; color: #c00000; text-transform: uppercase; margin-bottom: 15px; border-bottom: 2px solid #c00000; padding-bottom: 6px; letter-spacing: 0.5px;">Tiêu điểm {region_text}</div>
                        <div id="spotlight-container">
                            <!-- JS populated -->
                        </div>
                    </div>
                </div>
            </div>

            <!-- DYNAMIC FULL-WIDTH MOST READ CAROUSEL'''
    
    content = html_pattern.sub(new_html, content)
    
    # 2. Replace JS population logic robustly
    start_str = "document.getElementById('main-cover-container').innerHTML = `"
    end_str = "        let containerHtml = '';"
    
    idx1 = content.find(start_str)
    idx2 = content.find(end_str, idx1)
    
    if idx1 == -1 or idx2 == -1:
        print("COULD NOT FIND JS BLOCK IN", filepath)
        return
        
    new_js = f'''document.getElementById('main-cover-container').innerHTML = `
            <article class="v4 cv-001 hero-main-article" style="display: block;">
                <a class="link-img" href="` + centerArt.url + `" target="_blank">
                    <figure class="_thumb" style="margin-bottom: 12px; width: 100%;">
                        <img src="` + centerArt.image + `" class="img-art" alt="` + centerArt.title + `" style="width: 100%; border-radius: 6px; aspect-ratio: 16/9; object-fit: cover;">
                    </figure>
                </a>
                <a class="link-title" href="` + centerArt.url + `" target="_blank" style="text-decoration: none;">
                    <h2 class="title cover prefix-icon" style="font-size: 26px; line-height: 1.3; margin-bottom: 10px; font-weight: 800; color: #111; letter-spacing: -0.5px;">` + centerArt.title + `</h2>
                </a>
                <div class="chapeau ellipsis fade-out" style="font-size: 14.5px; line-height: 1.5; color: #444; -webkit-line-clamp: 4; display: -webkit-box; -webkit-box-orient: vertical; overflow: hidden;">` + centerArt.excerpt + `</div>
            </article>
        `;

        document.getElementById('subcover-bottom-row').innerHTML = `
            ` + [bottom1, bottom2, bottom3].map(art => `
                <article class="v4 p2c" style="display: flex; flex-direction: column; gap: 8px;">
                    <a class="link-img" href="`+art.url+`" target="_blank">
                        <figure class="_thumb" style="margin: 0; width: 100%;">
                            <img src="`+art.image+`" class="img-art" alt="`+art.title+`" style="width: 100%; aspect-ratio: 16/10; object-fit: cover; border-radius: 4px;">
                        </figure>
                    </a>
                    <a class="link-title" href="`+art.url+`" target="_blank" style="text-decoration: none;">
                        <h2 class="title prefix-icon" style="font-size: 14.5px; line-height: 1.3; font-weight: 700; color: #111; margin: 0; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">`+art.title+`</h2>
                    </a>
                </article>
            `).join('') + `
        `;

        const spotStyles = ['border-bottom: 1px dashed #ddd; padding-bottom: 15px; margin-bottom: 15px;','border-bottom: 1px dashed #ddd; padding-bottom: 15px; margin-bottom: 15px;','border-bottom: 1px dashed #ddd; padding-bottom: 15px; margin-bottom: 15px;',''];
        document.getElementById('spotlight-container').innerHTML = `
            ` + [spot1, spot2, spot3, spot4].map((art, i) => `
                <article class="v4 p2c" style="display: flex; gap: 12px; align-items: flex-start; `+spotStyles[i]+`">
                    <a class="link-img" href="`+art.url+`" target="_blank" style="flex: 0 0 110px;">
                        <img src="`+art.image+`" class="img-art" alt="`+art.title+`" style="width: 110px; height: 82px; object-fit: cover; border-radius: 4px;">
                    </a>
                    <a class="link-title" href="`+art.url+`" target="_blank" style="text-decoration: none; flex: 1;">
                        <h2 class="title prefix-icon" style="font-size: 13.5px; line-height: 1.4; color: #111; font-weight: bold; margin: 0; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden;">`+art.title+`</h2>
                    </a>
                </article>
            `).join('') + `
        `;

'''
    
    content = content[:idx1] + new_js + content[idx2:]
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

import subprocess
# Restore original files
subprocess.run(['git', 'checkout', 'HEAD', '--', 'Phien_Ban_07_06/apply_tphcm_layout.py', 'Phien_Ban_07_06/apply_ads_layout.py'])

process_file('Phien_Ban_07_06/apply_tphcm_layout.py', 'TP.HCM & Đông Nam Bộ', False)
process_file('Phien_Ban_07_06/apply_ads_layout.py', 'Hà Nội & Vùng Thủ đô', True)
print("Updated successfully")
