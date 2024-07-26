import streamlit as st
import pandas as pd
import json
from service.search import get_search_result

# JSON 파일을 읽어서 파이썬 딕셔너리로 변환하는 함수
def load_kftc_dictionary():
    with open('static/kftc_dictionary.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def main():
    st.title('KFTC Meta Dictionary')

    # JSON 파일 로드
    kftc_dictionary = load_kftc_dictionary()

    # 사용자 입력을 받음
    keyword_input = st.text_input("검색할 용어를 입력해주세요.")
    if keyword_input:
        # 입력된 키워드를 쉼표로 분리하여 리스트로 만듦
        keywords = [keyword.strip() for keyword in keyword_input.split(',')]
        
        # 함수 호출 및 결과 사용
        results = get_search_result(keywords, kftc_dictionary)

        # 결과 데이터를 DataFrame으로 변환
        df = pd.DataFrame(results)

        if not df.empty:  # 데이터프레임이 비어 있지 않은 경우에만 그리드 표시
            # Match Type에 따라 스타일 지정
            def style_specific_rows(row):
                if row['Match Type'] == 'Exact':
                    return pd.Series('color: red; font-weight: bold;', index=row.index)
                else:
                    return pd.Series('', index=row.index)

            # DataFrame 스타일 적용
            styled_df = df.style.apply(style_specific_rows, axis=1)
            st.subheader(f'{keyword_input}에 대한 검색 결과')
            
            # 결과 행의 수에 따라 높이 조정
            grid_height = min(60 * len(df), 600)  # 최대 높이를 600px로 제한
            st.dataframe(styled_df, height=grid_height)  # 동적으로 그리드 높이 조절
        else:
            st.write("검색 결과가 없습니다.")

if __name__ == "__main__":
    main()
