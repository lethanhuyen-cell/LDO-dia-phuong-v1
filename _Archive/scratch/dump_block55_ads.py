with open('Phien_Ban_07_06/apply_ads_layout.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('<!-- BLOCK 5.5')
idx2 = text.find('<!-- BLOCK 5.8')
with open('scratch/dump_block55_ads.txt', 'w', encoding='utf-8') as fw:
    fw.write(text[idx1:idx2])
