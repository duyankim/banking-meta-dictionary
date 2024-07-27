import streamlit as st

def main():
    # st.sidebar.title('Navigation')
    st.page_link("pages/single_search_page.py", label="단어 조회하기", icon="🔍")
    st.page_link("pages/multi_search_page.py", label="다건 조회하기", icon="📚")


if __name__ == "__main__":
    main()