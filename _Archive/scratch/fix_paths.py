with open('Phien_Ban_07_06/apply_tphcm_layout.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Phien_Ban_07_06/tphcm_index_ads.html with tphcm_index_ads.html in paths
text = text.replace('Phien_Ban_07_06/tphcm_index_ads.html', 'tphcm_index_ads.html')
text = text.replace('Phien_Ban_07_06/tphcm_index.html', 'tphcm_index.html')
# We can also fix the unicode path issue by using relative paths
text = text.replace("c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/tphcm_index.html", "tphcm_index.html")
text = text.replace("c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/tphcm_index_ads.html", "tphcm_index_ads.html")
text = text.replace("c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/Phien_Ban_07_06/tphcm_index.html", "tphcm_index.html")
text = text.replace("c:/Users/Admin/Documents/Work_Folders/4_Hoat_Dong_Ca_Nhan/LANDING PAGE THƯỜNG TRÚ/Phien_Ban_07_06/tphcm_index_ads.html", "tphcm_index_ads.html")

# Some literal string match fixes for weird unicode output in the powershell command
text = text.replace("LANDING PAGE TH_oNG TRAs", "LANDING PAGE THƯỜNG TRÚ")

with open('Phien_Ban_07_06/apply_tphcm_layout.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Paths fixed in apply_tphcm_layout.py")
