from utils.auth import sign_up
import streamlit as st

st.title("📝 회원가입")

name = st.text_input("이름")

student_id = st.text_input("학번")

email = st.text_input("숙명대학교 이메일")

password = st.text_input(
    "비밀번호",
    type="password"
)

password2 = st.text_input(
    "비밀번호 확인",
    type="password"
)

if st.button("다음"):

    if (
        name == "" or
        student_id == "" or
        email == "" or
        password == "" or
        password2 == ""
    ):
        st.error("모든 정보를 입력해주세요.")

    elif password != password2:
        st.error("비밀번호가 일치하지 않습니다.")

    elif not email.endswith("@sookmyung.ac.kr"):
        st.error("숙명대학교 이메일만 가입 가능합니다.")

    else:
try:
    sign_up(email, password)

    st.success("회원가입이 완료되었습니다.")
    st.success("학교 이메일로 인증 메일을 보냈습니다.")

    st.switch_page("pages/3_이메일인증.py")

except Exception as e:
    st.error(f"회원가입 실패 : {e}")
