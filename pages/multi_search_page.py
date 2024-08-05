import streamlit as st
import pandas as pd
import json
from collections import Counter
import re

def load_kftc_dictionary():
    all_dictionaries = ["ui", "com", "ift", "hof", "ent", "cms", "etc"]
    combined_dict = []
    for dictionary in all_dictionaries:
        with open(f'./static/{dictionary}.json', 'r', encoding='utf-8') as file:
            combined_dict.extend(json.load(file))
    return combined_dict
    

def get_search_result(keywords, dictionary):
    results = []
    for keyword in keywords:
        matches = [entry for entry in dictionary if keyword in entry['korean']]
        match_strings = [entry['english'] for entry in matches]
        # Join all matches and split by commas to analyze word frequency
        all_matches = ", ".join(match_strings)
        words = re.split(r'\W+', all_matches)  # Split by non-word characters
        most_common_word = Counter(words).most_common(1)[0][0] if words else '(Not matched)'

        results.append({
            'Korean': keyword,
            'Matched Most': most_common_word,
            'English': ", ".join(match_strings)
        })
    return results

def multi_search_page():
    st.title('KFTC Meta Dictionary')

    # Load the dictionary JSON file
    kftc_dictionary = load_kftc_dictionary()

    # Create a text area for user input
    keyword_input = st.text_area("단어를 줄바꿈으로 구분하여 검색합니다.", height=300)

    if st.button('Search'):
        if keyword_input:
            # Split input by newlines and trim whitespace
            keywords = [keyword.strip() for keyword in keyword_input.split('\n') if keyword.strip()]
            
            # Call the function and get results
            results = get_search_result(keywords, kftc_dictionary)
            
            # Convert results to DataFrame
            df = pd.DataFrame(results)
            df = df[['Korean', 'Matched Most', 'English']]  # Reorder columns as needed
            
            # Optionally, you can hide the index to make the DataFrame look cleaner
            st.dataframe(df, height=grid_height, use_container_width=True)
        else:
            st.write("단어를 입력해주세요.")