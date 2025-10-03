import streamlit as st
from pathlib import Path

# Load CSS
css_file = Path(__file__).parent.parent / "styles" / "forgot.css"
if css_file.exists():
    st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

st.markdown('<div class="forgot-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="forgot-card">', unsafe_allow_html=True)
st.markdown('<h2>Forgot Password</h2>', unsafe_allow_html=True)
st.markdown('<div class="forgot-sub">Enter your email to reset password</div>', unsafe_allow_html=True)

email = st.text_input("Email")

if st.button("Send Reset Link"):
    st.success(f"Password reset link sent to {email}!")

if st.button("Back to Login"):
    st.session_state.page = "login"
    st.stop()

st.markdown('</div></div>', unsafe_allow_html=True)
