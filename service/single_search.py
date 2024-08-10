def find_english_words_with_meta_and_match_status(korean_words, dictionary):
    results = []
    for korean_word in korean_words:
        korean_word_cleaned = korean_word.replace(" ", "")
        found_exact = False

        for entry in dictionary:
            dict_korean_cleaned = entry['korean'].replace(" ", "")
            if dict_korean_cleaned == korean_word_cleaned:
                found_exact = True
                results.append({
                    'Korean': entry['korean'],
                    'English': entry['english'],
                    'Meta': entry.get('meta', ''),
                    'Biz Filter': entry['Biz Filter'],
                    'Exact Match': True  # Mark this entry as an exact match
                })
        
        # 정확한 일치가 발견되지 않은 경우 부분 일치를 찾는다.
        if not found_exact:
            for entry in dictionary:
                dict_korean_cleaned = entry['korean'].replace(" ", "")
                if korean_word_cleaned in dict_korean_cleaned:
                    results.append({
                        'Korean': entry['korean'],
                        'English': entry['english'],
                        'Meta': entry.get('meta', ''),
                        'Biz Filter': entry['Biz Filter'],
                        'Exact Match': False
                    })

            # 부분 일치도 없는 경우
            if not any(res['Korean'].replace(" ", "") == korean_word_cleaned for res in results):
                results.append({
                    'Korean': korean_word,
                    'English': '(Not Found)',
                    'Meta': '',
                    'Biz Filter': 'None',
                    'Exact Match': False
                })

    return results
