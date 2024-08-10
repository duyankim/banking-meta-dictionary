import streamlit as st
import pandas as pd
import json
from service.single_search import find_english_words_with_meta_and_match_status

def load_dictionary(filter_option):
    """Loads data from specified JSON file or combines all if 'All'."""
    combined_dict = []
    dictionaries = ["ui", "com", "ift", "hof", "ent", "cms"] if filter_option == "All" else [filter_option]

    for dictionary in dictionaries:
        try:
            with open(f'./static/{dictionary}.json', 'r', encoding='utf-8') as file:
                entries = json.load(file)
                for entry in entries:
                    entry['Biz Filter'] = dictionary
                combined_dict.extend(entries)
        except Exception as e:
            st.error(f"Failed to load {dictionary}.json: {e}")

    return combined_dict

def single_search_page():
    st.title('KFTC Meta Dictionary')
    st.write("✅ 완벽하게 매칭되는 단어는 빨간색으로 표시됩니다.")
    filter_option = st.selectbox("조건을 선택해주세요", ("All", "ui", "com", "ift", "hof", "ent", "cms"))
    kftc_dictionary = load_dictionary(filter_option)
    keyword_input = st.text_input("검색할 용어를 입력해주세요.")
    if keyword_input:
        keywords = [keyword.replace(" ", "") for keyword in keyword_input.split(',')]
        results = find_english_words_with_meta_and_match_status(keywords, kftc_dictionary)
        df = pd.DataFrame(results)

        if not df.empty:
            # Additional instruction for adjusting the DataFrame style if necessary
            st.markdown("""
            <style>
                .dataframe th {
                    font-size: 110%;
                }
                .dataframe td {
                    max-width: 300px;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    white-space: nowrap;
                }
            </style>
            """, unsafe_allow_html=True)
        
            # Apply styling and hide the 'Exact Match' column
            styled_df = df.style.apply(style_specific_rows, axis=1)
            st.subheader(f'{keyword_input}에 대한 검색 결과')
            grid_height = min(60 * len(df), 600)
            st.dataframe(styled_df, height=grid_height, use_container_width=True)
        else:
            st.write("검색 결과가 없습니다.")

def style_specific_rows(row):
    if row['Exact Match']:  # Assuming 'Exact Match' is a boolean field indicating exact matches
        return pd.Series('color: red; font-weight: bold;', index=row.index)
    return pd.Series('', index=row.index)
