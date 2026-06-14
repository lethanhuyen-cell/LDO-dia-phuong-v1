import re

with open('apply_ads_layout.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace file dependencies and outputs
code = code.replace("hanoi_final_consolidated.json", "tphcm_dongnambo_consolidated.json")
code = code.replace("demo_landing_page_hanoi_clean.html", "demo_landing_page_hanoi_clean.html") # We can reuse the clean HTML or adjust it

# Adjust paths in code
code = code.replace("demo_landing_page_hanoi_ads.html", "demo_landing_page_tphcm_ads.html")
code = code.replace("index_ads.html", "tphcm_index_ads.html")
code = code.replace("demo_landing_page_hanoi.html", "demo_landing_page_tphcm.html")
code = code.replace("index.html", "tphcm_index.html")

# Replacing text for Hanoi to TPHCM & Dong Nam Bo in the UI parts
code = code.replace("Hà Nội", "TP.HCM & Đông Nam Bộ")
code = code.replace("HÀ NỘI", "TP.HCM & ĐÔNG NAM BỘ")
code = code.replace("hanoi", "tphcm")
code = code.replace("hanoiArticles", "tphcmArticles")

# Adjust Weather API Latitude/Longitude to HCMC (10.8231, 106.6297)
code = code.replace("lat=21.0285&lon=105.8542", "lat=10.8231&lon=106.6297")
code = code.replace("Hà Nội: Đang tải...", "TP.HCM: Đang tải...")

# Local District Prices to TPHCM districts
code = code.replace("Cầu Giấy", "Quận 1")
code = code.replace("caugiay", "quan1")
code = code.replace("Đống Đa", "Thủ Đức")
code = code.replace("dongda", "thuduc")
code = code.replace("Ba Đình", "Biên Hòa")
code = code.replace("badinh", "bienhoa")
code = code.replace("Thanh Xuân", "Thuận An")
code = code.replace("thanhxuan", "thuanan")
code = code.replace("Long Biên", "Vũng Tàu")
code = code.replace("longbien", "vungtau")

# Save the new compiler script
with open('apply_tphcm_layout.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("apply_tphcm_layout.py created successfully!")
