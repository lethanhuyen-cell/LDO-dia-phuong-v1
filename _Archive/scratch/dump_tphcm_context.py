with open('Phien_Ban_07_06/apply_tphcm_layout.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('<!-- ===== CỘT PHẢI: SIDEBAR TIỆN ÍCH (STICKY) ===== -->')
with open('scratch/dump_tphcm_context.txt', 'w', encoding='utf-8') as fw:
    fw.write(text[idx1-200:idx1+100])
