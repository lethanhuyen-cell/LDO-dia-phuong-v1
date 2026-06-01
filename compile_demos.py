import sys

# Modify apply_tphcm_layout_opt1.py to output to tphcm_index_opt1.html
with open('apply_tphcm_layout_opt1.py', 'r', encoding='utf-8') as f:
    opt1_content = f.read()

opt1_content = opt1_content.replace("demo_landing_page_tphcm_ads.html", "tphcm_index_opt1_ads.html")
opt1_content = opt1_content.replace("tphcm_index_ads.html", "tphcm_index_opt1_ads2.html")
opt1_content = opt1_content.replace("demo_landing_page_tphcm.html", "tphcm_index_opt1_demo.html")
opt1_content = opt1_content.replace("tphcm_index.html", "tphcm_index_opt1.html")

with open('apply_tphcm_layout_opt1.py', 'w', encoding='utf-8') as f:
    f.write(opt1_content)

# Let's check apply_tphcm_layout_opt2.py as well
with open('apply_tphcm_layout_opt2.py', 'r', encoding='utf-8') as f:
    opt2_content = f.read()

# Fix the trailing block formatting if dummy_var is not closed properly
# We added dummy_var = ` but didn't close the backtick before the next block!
# Let's search where dummy_var is and close the backtick correctly
if "const dummy_var = `" in opt2_content:
    # Let's find spotlight innerHTML population
    opt2_content = opt2_content.replace(
        "        document.getElementById('spotlight-container').innerHTML = `",
        "        `; // Close dummy_var\n        document.getElementById('spotlight-container').innerHTML = `"
    )

with open('apply_tphcm_layout_opt2.py', 'w', encoding='utf-8') as f:
    f.write(opt2_content)

print("Demo script updates completed.")
