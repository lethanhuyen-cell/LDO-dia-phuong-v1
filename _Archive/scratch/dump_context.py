with open('scratch/old_tphcm.py', 'r', encoding='utf-16') as f:
    text = f.read()

idx1 = text.find('<!-- ===== CỘT PHẢI')
with open('scratch/old_tphcm_context.txt', 'w', encoding='utf-8') as fw:
    fw.write(text[idx1-500:idx1+100])
