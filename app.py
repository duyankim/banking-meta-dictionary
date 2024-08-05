import streamlit as st
from pages.single_search_page import single_search_page
from pages.multi_search_page import multi_search_page

def main():
    st.sidebar.title('Navigation')

    # 세션 상태 초기화
    if 'page' not in st.session_state:
        st.session_state.page = 'single_search'

    # 메뉴 버튼 스타일
    menu_style = """
    <style>
    .stButton>button {
        width: 100%;
        background-color: #f0f2f6;
        color: #000000;
        border: none;
        padding: 10px;
        text-align: left;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #e0e2e6;
    }
    div[data-testid="stSidebarNav"] {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    </style>
    """
    st.markdown(menu_style, unsafe_allow_html=True)

    # 메뉴 버튼
    if st.sidebar.button("🔍 단어 조회하기"):
        st.session_state.page = 'single_search'
    if st.sidebar.button("📚 다건 조회하기"):
        st.session_state.page = 'multi_search'

    # 선택된 페이지 표시
    if st.session_state.page == 'single_search':
        single_search_page()
    elif st.session_state.page == 'multi_search':
        multi_search_page()

if __name__ == "__main__":
    main()