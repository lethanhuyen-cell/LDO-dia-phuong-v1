with open('Phien_Ban_07_06/apply_tphcm_layout.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """                            </h4>
                        </div>
                    </div>
                                
            </div>"""

replacement = """                            </h4>
                        </div>
                    </div>
                    </div>
                                
            </div>"""

if target in text:
    text = text.replace(target, replacement)
    with open('Phien_Ban_07_06/apply_tphcm_layout.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Replaced successfully")
else:
    print("Target not found")
