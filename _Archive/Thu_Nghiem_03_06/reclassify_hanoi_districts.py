import json
import re

# Load Hanoi articles
with open('hanoi_final_consolidated.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Define matching rules (mapping keyword list to the standard district name)
district_mapping = [
    # Ha Dong & southwest
    ('Hà Đông', ['Hà Đông', 'Ha Dong', 'Ba La', 'Vạn Phúc', 'Yên Nghĩa', 'Mộ Lao', 'La Khê', 'Phú La', 'Văn Quán', 'Hà Cầu']),
    ('Thanh Oai', ['Thanh Oai']),
    ('Chương Mỹ', ['Chương Mỹ', 'Chuong My']),
    ('Mỹ Đức', ['Mỹ Đức', 'My Duc']),
    
    # Gia Lam & Northeast
    ('Gia Lâm', ['Gia Lâm', 'Gia Lam', 'Trâu Quỳ', 'Cổ Bi', 'Yên Viên', 'Bát Tràng']),
    
    # Dong Anh & North
    ('Đông Anh', ['Đông Anh', 'Dong Anh', 'Cổ Loa', 'Đông Ngàn']),
    ('Sóc Sơn', ['Sóc Sơn', 'Soc Son', 'Nội Bài', 'Noi Bai']),
    ('Mê Linh', ['Mê Linh', 'Me Linh', 'Quang Minh']),
    
    # Noi thanh (Inner City)
    ('Hoàn Kiếm', ['Hoàn Kiếm', 'Hoan Kiem', 'Hồ Gươm', 'Tràng Tiền', 'Đinh Tiên Hoàng', 'Phố Cổ']),
    ('Ba Đình', ['Ba Đình', 'Ba Dinh', 'Giảng Võ', 'Kim Mã', 'Liễu Giai']),
    ('Đống Đa', ['Đống Đa', 'Dong Da', 'Láng Hạ', 'Văn Miếu', 'Quốc Tử Giám', 'Xã Đàn']),
    ('Hai Bà Trưng', ['Hai Bà Trưng', 'Hai Ba Trung', 'Bạch Mai', 'Trần Khát Chân', 'Minh Khai']),
    ('Cầu Giấy', ['Cầu Giấy', 'Cau Giay', 'Xuân Thủy', 'Dịch Vọng', 'Trung Hòa', 'Trần Thái Tông']),
    ('Thanh Xuân', ['Thanh Xuân', 'Thanh Xuan', 'Khương Trung', 'Nguyễn Trãi', 'Khuất Duy Tiến']),
    ('Tây Hồ', ['Tây Hồ', 'Tay Hồ', 'Tây hồ', 'Tay Ho', 'Hồ Tây']),
    ('Long Biên', ['Long Biên', 'Long biên', 'Long Bien']),
    ('Nam Từ Liêm', ['Nam Từ Liêm', 'Nam Tu Liem', 'Mỹ Đình', 'My Dinh']),
    ('Bắc Từ Liêm', ['Bắc Từ Liêm', 'Bac Tu Liem', 'Nhổn', 'Cổ Nhuế']),
    ('Hoàng Mai', ['Hoàng Mai', 'Hoang Mai', 'Giáp Bát', 'Linh Đàm']),
    ('Sơn Tây', ['Sơn Tây', 'Sơn tây'])
]

changed = 0
for a in articles:
    # Deduplicate tags
    if 'tags' in a and isinstance(a['tags'], list):
        seen = set()
        new_tags = []
        for t in a['tags']:
            if t not in seen:
                seen.add(t)
                new_tags.append(t)
        a['tags'] = new_tags
    
    # Build text to match
    text = ' '.join([
        a.get('title', ''),
        a.get('excerpt', ''),
        a.get('content', '')
    ])
    
    # Try matching
    matched_district = None
    for district_name, keywords in district_mapping:
        pattern = r'\b(' + '|'.join(map(re.escape, keywords)) + r')\b'
        if re.search(pattern, text, re.IGNORECASE):
            matched_district = district_name
            break
            
    if matched_district and a.get('district') != matched_district:
        a['district'] = matched_district
        changed += 1

print(f"Updated district tags for {changed} articles.")

# Save back
with open('hanoi_final_consolidated.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print("Saved back to hanoi_final_consolidated.json")
