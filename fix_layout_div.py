import sys

filepath = 'Phien_Ban_07_06/apply_tphcm_layout.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Add missing divs before BLOCK 5.8
target_str = """                        </div>
                    </div>
                                
            </div>

            

            <!-- BLOCK 5.8"""

replacement_str = """                        </div>
                    </div>
                    </div>
                
            </div>

            

            <!-- BLOCK 5.8"""

content = content.replace(target_str, replacement_str)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fix applied.")
