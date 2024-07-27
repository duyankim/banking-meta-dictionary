import json

# dictionary.txt 파일 읽기
with open('dictionary.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

dictionary = []
for line in lines:
    parts = line.strip().split(',')
    if len(parts) >= 2:
        entry = {
            'korean': parts[0].strip(),
            'english': parts[1].strip(),
            # meta 정보가 없는 경우를 처리
            'meta': ''.join(parts[2:]).strip().lower().replace('_', ' ').title().replace(' ', '') if len(parts) > 2 else ''
        }
        dictionary.append(entry)

# 업데이트된 내용을 kftc_dictionary.json에 쓰기
# JSON 형식으로 쓰기 위해 json.dump 사용
with open('kftc_dictionary.json', 'w', encoding='utf-8') as json_file:
    json.dump(dictionary, json_file, ensure_ascii=False, indent=2)

print('dictionary has been updated.')