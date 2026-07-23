import streamlit as st
from utils.database import save_profile

st.set_page_config(
    page_title="회원정보 입력",
    page_icon="👤",
    layout="centered"
)

st.title("👤 회원정보 입력")
st.write("회원가입을 완료하기 위해 정보를 입력해주세요.")

# -----------------------------
# 로그인한 이메일 가져오기
# -----------------------------
try:
    email = st.session_state["user"].email
except:
    st.warning("로그인 후 이용해주세요.")
    st.stop()

# -----------------------------
# 이메일 표시
# -----------------------------
st.text_input(
    "학교 이메일",
    value=email,
    disabled=True
)

# -----------------------------
# 회원정보 입력
# -----------------------------
name = st.text_input("이름")

student_id = st.text_input("학번")

department = st.selectbox(
    "학과",
    [
        "데이터사이언스전공",
        "컴퓨터과학전공",
        "소프트웨어융합전공",
        "IT공학전공",
        "경영학부",
        "경제학부",
        "기타"
    ]
)

grade = st.selectbox(
    "학년",
    [
        "1학년",
        "2학년",
        "3학년",
        "4학년"
    ]
)

role = st.radio(
    "역할",
    [
        "멘토",
        "멘티"
    ],
    horizontal=True
)

interest = st.text_input("관심 분야")

hope = st.text_input("희망 분야")

intro = st.text_area(
    "자기소개",
    height=150
)

# -----------------------------
# 저장 버튼
# -----------------------------
if st.button("💾 회원정보 저장", use_container_width=True):

    if not all([name, student_id, interest, hope, intro]):
        st.error("모든 정보를 입력해주세요.")

    else:

        data = {
            "email": email,
            "name": name,
            "student_id": student_id,
            "department": department,
            "grade": grade,
            "role": role,
            "interest": interest,
            "hope": hope,
            "intro": intro,
            "image": ""
        }

        try:
            save_profile(data)

            st.success("🎉 회원정보가 저장되었습니다!")

            st.switch_page("pages/4_회원가입완료.py")

        except Exception as e:
            st.error("회원정보 저장에 실패했습니다.")
            st.error(str(e))
