import streamlit as st
from pathlib import Path

css_file = Path(__file__).parent.parent / "styles/main.css"
if css_file.exists():
    st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

st.title("👤 My Profile")

if "user" not in st.session_state:
    st.warning("Please login first.")
else:
    user = st.session_state["user"]
    st.markdown(f"<div class='card'><h3>{user['name']}</h3><p>Email: {user['email']}</p></div>", unsafe_allow_html=True)
