import streamlit as st

st.set_page_config(
    page_title="이어질 숙명",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 이어질 숙명")

st.subheader("숙명여자대학교 멘토 · 멘티 매칭 서비스")

st.write("---")

st.write("""
이어질 숙명은

선배와 후배를 연결하여

학교생활과 진로를 함께 고민하는

멘토링 플랫폼입니다.
""")

st.info("왼쪽 메뉴에서 로그인 또는 회원가입을 선택하세요.")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔑 로그인", use_container_width=True):
        st.switch_page("pages/1_로그인.py")

with col2:
    if st.button("📝 회원가입", use_container_width=True):
        st.switch_page("pages/2_회원가입.py")
