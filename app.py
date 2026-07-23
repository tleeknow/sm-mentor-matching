import streamlit as st
from utils.database import supabase

st.set_page_config(
    page_title="이어질 숙명",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 이어질 숙명")

st.write("숙명여자대학교 선후배 매칭 서비스")

try:
    supabase.table("users").select("*").limit(1).execute()
    st.success("✅ Supabase 연결 성공!")
except Exception as e:
    st.error("❌ 연결 실패")
    st.write(e)
