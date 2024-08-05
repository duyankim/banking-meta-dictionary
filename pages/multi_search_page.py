import streamlit as st
import pandas as pd
import json

def load_kftc_dictionary():
    with open('./static/ent_dictionary.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def get_search_result(keywords, dictionary):
    results = []
    for keyword in keywords:
        # Gather all partial matches for each keyword
        matches = [entry['english'] for entry in dictionary if keyword in entry['korean']]
        if matches:
            results.append({
                'Korean': keyword,
                'English': ", ".join(matches)  # Join all matches into one string
            })
        else:
            results.append({
                'Korean': keyword,
                'English': '(Not matched)'
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

            # Optionally, you can hide the index to make the DataFrame look cleaner
            st.dataframe(df, width=700, height=800, use_container_width=True)
        else:
            st.write("Please enter some keywords to search.")

if __name__ == "__main__":
    st.sidebar.title('Navigation')
    st.sidebar.page_link("pages/single_search_page.py", label="단어 조회하기", icon="🔍")
    st.sidebar.page_link("pages/multi_search_page.py", label="다건 조회하기", icon="📚")
    multi_search_page()