from supabase import create_client
import streamlit as st

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(url, key)

def sign_up(email, password):
    return supabase.auth.sign_up(
        {
            "email": email,
            "password": password,
        }
    )

def sign_in(email, password):
    return supabase.auth.sign_in_with_password(
        {
            "email": email,
            "password": password,
        }
    )
