import streamlit as st
from utils.auth import sign_in

st.set_page_config(
    page_title="로그인",
    page_icon="🔑"
)

st.title("🔑 로그인")
st.write("숙명여자대학교 계정으로 로그인하세요.")

email = st.text_input("학교 이메일")
password = st.text_input("비밀번호", type="password")

if st.button("로그인", use_container_width=True):

    if email == "" or password == "":
        st.error("이메일과 비밀번호를 입력해주세요.")

    elif not email.endswith("@sookmyung.ac.kr"):
        st.error("숙명대학교 이메일만 로그인할 수 있습니다.")

    else:
        try:
            response = sign_in(email, password)

            if response.user is not None:

                st.session_state["user"] = response.user

                st.success("로그인 성공!")

                st.switch_page("pages/4_회원정보입력.py")

        except Exception as e:
            st.error("로그인에 실패했습니다.")
            st.error(str(e))

st.write("---")

if st.button("회원가입"):
    st.switch_page("pages/2_회원가입.py")
