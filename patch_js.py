import os
import re

def patch_file(filepath):
    if not os.path.exists(filepath):
        print(f"Not found: {filepath}")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def repl(m):
        element_id = m.group(1)
        prop = m.group(2)
        var_name = element_id.replace('-', '_')
        return f"let el_{var_name} = document.getElementById('{element_id}');\n        if (el_{var_name}) el_{var_name}.{prop} ="

    pattern = re.compile(r"document\.getElementById\('([^']+)'\)\.(innerHTML|innerText|src)\s*=")
    
    new_content = pattern.sub(repl, content)

    # We also need to fix direct assignments like "document.getElementById('catfish-ad-container').style.display='none'"
    # but those might be inline in onclick="...". The regex above is safe because it only targets innerHTML, innerText, src.

    # Wait, what if we already patched it?
    if "if (el_" in content:
        print(f"Already patched: {filepath}")
        return

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Patched: {filepath}")
    else:
        print(f"No changes for: {filepath}")

patch_file('Phien_Ban_07_06/apply_tphcm_layout.py')
patch_file('Phien_Ban_07_06/apply_ads_layout.py')
patch_file('apply_tphcm_layout.py')
patch_file('apply_ads_layout.py')
