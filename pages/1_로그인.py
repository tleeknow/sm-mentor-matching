import streamlit as st

st.title("🔑 로그인")

email = st.text_input("학교 이메일")

password = st.text_input(
    "비밀번호",
    type="password"
)

if st.button("로그인"):

    st.info("다음 시간에 로그인 기능을 연결합니다.")

st.write("---")

if st.button("회원가입 하러가기"):

    st.switch_page("pages/2_회원가입.py")
