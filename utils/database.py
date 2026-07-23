from supabase import create_client
import streamlit as st

# Supabase 연결
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(url, key)


# -----------------------------
# 회원정보 저장 (없으면 INSERT, 있으면 UPDATE)
# -----------------------------
def save_profile(data):

    email = data["email"]

    # 기존 회원 조회
    result = (
        supabase.table("profiles")
        .select("*")
        .eq("email", email)
        .execute()
    )

    # 이미 존재하면 UPDATE
    if result.data:

        response = (
            supabase.table("profiles")
            .update(data)
            .eq("email", email)
            .execute()
        )

    # 없으면 INSERT
    else:

        response = (
            supabase.table("profiles")
            .insert(data)
            .execute()
        )

    return response


# -----------------------------
# 회원정보 조회
# -----------------------------
def get_profile(email):

    response = (
        supabase.table("profiles")
        .select("*")
        .eq("email", email)
        .execute()
    )

    if response.data:
        return response.data[0]

    return None


# -----------------------------
# 회원정보 수정
# -----------------------------
def update_profile(email, data):

    response = (
        supabase.table("profiles")
        .update(data)
        .eq("email", email)
        .execute()
    )

    return response
