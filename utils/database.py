from supabase import create_client
import streamlit as st

# Supabase 연결
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(url, key)


# ==========================
# 회원정보 저장
# ==========================
def save_profile(data):
    response = (
        supabase.table("profiles")
        .insert(data)
        .execute()
    )
    return response


# ==========================
# 이메일로 회원정보 가져오기
# ==========================
def get_profile(email):
    response = (
        supabase.table("profiles")
        .select("*")
        .eq("email", email)
        .execute()
    )

    if len(response.data) > 0:
        return response.data[0]

    return None


# ==========================
# 회원정보 수정
# ==========================
def update_profile(email, data):
    response = (
        supabase.table("profiles")
        .update(data)
        .eq("email", email)
        .execute()
    )

    return response
