from utils.auth import sign_up
import streamlit as st

st.set_page_config(
    page_title="회원가입",
    page_icon="📝"
)

st.title("📝 회원가입")
st.write("숙명여자대학교 이메일로 회원가입을 진행해주세요.")

name = st.text_input("이름")
student_id = st.text_input("학번")
email = st.text_input("숙명대학교 이메일")
password = st.text_input("비밀번호", type="password")
password2 = st.text_input("비밀번호 확인", type="password")

if st.button("회원가입", use_container_width=True):

    # 빈칸 검사
    if not all([name, student_id, email, password, password2]):
        st.error("모든 정보를 입력해주세요.")

    # 숙명대학교 이메일 검사
    elif not email.endswith("@sookmyung.ac.kr"):
        st.error("숙명대학교 이메일(@sookmyung.ac.kr)만 가입할 수 있습니다.")

    # 비밀번호 확인
    elif password != password2:
        st.error("비밀번호가 일치하지 않습니다.")

    # 비밀번호 길이
    elif len(password) < 8:
        st.error("비밀번호는 8자 이상 입력해주세요.")

    else:
        try:
            # Supabase Auth 회원가입
            response = sign_up(email, password)

            # 성공 메시지
            st.success("🎉 회원가입이 완료되었습니다!")
            st.info("📧 숙명대학교 이메일로 인증 메일을 보냈습니다.")
            st.info("이메일 인증을 완료한 후 다시 로그인해주세요.")

            # 이메일 인증 페이지 이동
            st.switch_page("pages/3_이메일인증.py")

        except Exception as e:
            st.error("회원가입에 실패했습니다.")
            st.error(str(e))

st.write("---")

if st.button("← 로그인으로 돌아가기"):
    st.switch_page("pages/1_로그인.py")
