import re

with open('apply_tphcm_layout.py', 'r', encoding='utf-8') as f:
    code = f.read()

# OPTION 1: Left column with Header
# Modify HTML structure to include the Header for Tin Mới Cập Nhật
opt1_html_find = '<div id="left-column-feed-container" style="margin-top: 15px; border-top: 1px solid #eee; padding-top: 15px; display: flex; flex-direction: column; gap: 15px;">\n                        <!-- JS populated -->\n                    </div>'
opt1_html_replace = '<div style="margin-top: 15px; border-top: 1px solid #eee; padding-top: 15px;">\n                        <div style="font-size: 13.5px; font-weight: bold; color: #c00000; text-transform: uppercase; margin-bottom: 12px; border-bottom: 2px solid #c00000; padding-bottom: 5px;">Tin mới cập nhật</div>\n                        <div id="left-column-feed-container" style="display: flex; flex-direction: column; gap: 12px;">\n                            <!-- JS populated -->\n                        </div>\n                    </div>'

code_opt1 = code.replace(opt1_html_find, opt1_html_replace)

# Save code_opt1 to apply_tphcm_layout_opt1.py
with open('apply_tphcm_layout_opt1.py', 'w', encoding='utf-8') as f:
    f.write(code_opt1)


# OPTION 2: Sidebar Latest News under Ad
# In HTML: Remove left column news container (keep empty or hidden), add it to right column sidebar
opt2_html_find_left = '<div id="left-column-feed-container" style="margin-top: 15px; border-top: 1px solid #eee; padding-top: 15px; display: flex; flex-direction: column; gap: 15px;">\n                        <!-- JS populated -->\n                    </div>'
opt2_html_find_right = '<!-- DYNAMIC FULL-WIDTH MOST READ CAROUSEL'

opt2_html_replace_left = '' # empty left container
opt2_html_replace_right_sidebar_ad = """                                    <div style="background-color: #d4af37; color: #113824; font-size: 11px; font-weight: bold; padding: 8px 15px; border-radius: 2px; align-self: center; cursor: pointer; text-transform: uppercase; width: fit-content; margin-top: 15px;">Tìm hiểu ngay</div>
                                </div>
                            </a>
                        </div>
                        
                        <!-- Option 2 Sidebar Tin Mới -->
                        <div style="margin-top: 15px; border-top: 1px solid #eee; padding-top: 15px;">
                            <div style="font-size: 13px; font-weight: bold; color: #002d62; text-transform: uppercase; margin-bottom: 12px; border-bottom: 2px solid #002d62; padding-bottom: 5px;">Tin mới</div>
                            <div id="sidebar-latest-news-container" style="display: flex; flex-direction: column; gap: 10px;">
                                <!-- JS populated -->
                            </div>
                        </div>"""

code_opt2 = code.replace(opt2_html_find_left, opt2_html_replace_left)
code_opt2 = code_opt2.replace('                                    <div style="background-color: #d4af37; color: #113824; font-size: 11px; font-weight: bold; padding: 8px 15px; border-radius: 2px; align-self: center; cursor: pointer; text-transform: uppercase; width: fit-content; margin-top: 15px;">Tìm hiểu ngay</div>\n                                </div>\n                            </a>\n                        </div>', opt2_html_replace_right_sidebar_ad)

# In JS: Populat sidebar latest news, clear left column feed container
js_find_feed = """        document.getElementById('left-column-feed-container').innerHTML = `"""
js_replace_feed = """        // Option 2 JavaScript population
        if (document.getElementById('left-column-feed-container')) {
            document.getElementById('left-column-feed-container').innerHTML = '';
        }
        document.getElementById('sidebar-latest-news-container').innerHTML = `
            <div style="padding-bottom: 8px; border-bottom: 1px dashed #eee;">
                <a href="` + feed1.url + `" target="_blank" style="font-size: 12px; color: #333; text-decoration: none; font-weight: bold; line-height: 1.35; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;" onmouseover="this.style.color='#c00000'" onmouseout="this.style.color='#333'">` + feed1.title + `</a>
                <div style="font-size: 9.5px; color: #999; margin-top: 3px;">📅 ` + (feed1.date || '01/06/2026') + `</div>
            </div>
            <div style="padding-bottom: 8px; border-bottom: 1px dashed #eee;">
                <a href="` + feed2.url + `" target="_blank" style="font-size: 12px; color: #333; text-decoration: none; font-weight: bold; line-height: 1.35; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;" onmouseover="this.style.color='#c00000'" onmouseout="this.style.color='#333'">` + feed2.title + `</a>
                <div style="font-size: 9.5px; color: #999; margin-top: 3px;">📅 ` + (feed2.date || '01/06/2026') + `</div>
            </div>
            <div style="padding-bottom: 4px;">
                <a href="` + feed3.url + `" target="_blank" style="font-size: 12px; color: #333; text-decoration: none; font-weight: bold; line-height: 1.35; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;" onmouseover="this.style.color='#c00000'" onmouseout="this.style.color='#333'">` + feed3.title + `</a>
                <div style="font-size: 9.5px; color: #999; margin-top: 3px;">📅 ` + (feed3.date || '01/06/2026') + `</div>
            </div>
        `;
        
        // Block original left column feed container innerHTML assign
        const dummy_var = `"""

code_opt2 = code_opt2.replace(js_find_feed, js_replace_feed)
# Close the block
code_opt2 = code_opt2.replace('        `;\n\n        document.getElementById(\'spotlight-container\').innerHTML = `', '        `;\n\n        document.getElementById(\'spotlight-container\').innerHTML = `')

# Replace output file names in code_opt2 so they write to _opt2 files
code_opt2 = code_opt2.replace("demo_landing_page_tphcm_ads.html", "tphcm_index_opt2.html")
code_opt2 = code_opt2.replace("tphcm_index_ads.html", "tphcm_index_opt2_ads.html")
code_opt2 = code_opt2.replace("demo_landing_page_tphcm.html", "tphcm_index_opt2_demo.html")
code_opt2 = code_opt2.replace("tphcm_index.html", "tphcm_index_opt2.html")

with open('apply_tphcm_layout_opt2.py', 'w', encoding='utf-8') as f:
    f.write(code_opt2)

print("Demo generator scripts created.")
