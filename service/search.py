def find_english_words_with_meta_and_match_status(korean_words, dictionary):

    results = []

    for korean_word in korean_words:

        # 정확히 일치하는 단어 찾기

        exact_match = next((entry for entry in dictionary if entry['korean'] == korean_word), None)

        if exact_match:

            results.append({

                'Korean': exact_match['korean'],

                'English': exact_match['english'], 

                'Meta': exact_match.get('meta', ''),  # meta 정보가 없는 경우 빈 문자열 반환

                'Match Type': 'Exact'

            })

            continue



        # 부분 일치하는 단어들 찾기

        partial_matches = [entry for entry in dictionary if korean_word in entry['korean']]

        if partial_matches:

            for match in partial_matches:

                results.append({

                    'Korean': match['korean'], 

                    'English': match['english'], 

                    'Meta': match.get('meta', ''),  # meta 정보가 없는 경우 빈 문자열 반환

                    'Match Type': 'Partial'

                })

            continue



        # 일치하는 단어가 없을 경우

        results.append({

            'Korean': korean_word, 

            'English': '(Not Found)', 

            'Meta': '',  # 일치하는 단어가 없으므로 meta 정보도 없음

            'Match Type': 'None'

        })



    # Match Type에 따라 결과 정렬

    results = sorted(results, key=lambda x: (x['Match Type'] != 'Exact', x['Korean']))

    return results



def get_search_result(korean_words, dictionary):

    # 결과를 그리드로 출력할 수 있는 형태로 반환

    results = find_english_words_with_meta_and_match_status(korean_words, dictionary)

    return results

