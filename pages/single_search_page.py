import streamlit as st
import pandas as pd
import json
from service.single_search import get_search_result

def load_dictionary(filter_option):
    """Loads data from specified JSON file or combines all if 'All'."""
    if filter_option == "All":
        all_dictionaries = ["ui", "com", "ift", "hof", "ent", "cms", "etc"]
        combined_dict = []
        for dictionary in all_dictionaries:
            with open(f'./static/{dictionary}.json', 'r', encoding='utf-8') as file:
                combined_dict.extend(json.load(file))
        return combined_dict
    else:
        with open(f'./static/{filter_option}.json', 'r', encoding='utf-8') as file:
            return json.load(file)

def single_search_page():
    st.title('KFTC Meta Dictionary')

    # Select box for choosing the filter
    filter_option = st.selectbox("조건을 선택해주세요", ("All", "ui", "com", "ift", "hof", "ent", "cms", "etc"))

    # Load the appropriate dictionary based on the selected filter
    kftc_dictionary = load_dictionary(filter_option)

    # User input for search terms
    keyword_input = st.text_input("검색할 용어를 입력해주세요.")
    if keyword_input:
        keywords = [keyword.strip() for keyword in keyword_input.split(',')]
        
        # Call the function and use results
        results = get_search_result(keywords, kftc_dictionary)

        # Convert results to DataFrame
        df = pd.DataFrame(results)
        if not df.empty:
            # Apply styling for match types
            def style_specific_rows(row):
                if row['Match Type'] == 'Exact':
                    return pd.Series('color: red; font-weight: bold;', index=row.index)
                else:
                    return pd.Series('', index=row.index)

            styled_df = df.style.apply(style_specific_rows, axis=1)
            st.subheader(f'{keyword_input}에 대한 검색 결과')
            grid_height = min(60 * len(df), 600)  # Adjust the height based on the number of results
            st.dataframe(styled_df, height=grid_height)
        else:
            st.write("검색 결과가 없습니다.")

if __name__ == "__main__":
    st.sidebar.title('Navigation')
    st.sidebar.page_link("pages/single_search_page.py", label="단어 조회하기", icon="🔍")
    st.sidebar.page_link("pages/multi_search_page.py", label="다건 조회하기", icon="📚")
    single_search_page()
