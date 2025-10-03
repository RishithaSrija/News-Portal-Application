import streamlit as st
from pathlib import Path
from services.user_service import UserService

# --- Load CSS ---
css_file = Path(__file__).parent.parent / "styles" / "login.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Login Form Wrapper ---
st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="login-card">', unsafe_allow_html=True)
st.markdown('<h2>Welcome back</h2>', unsafe_allow_html=True)
st.markdown('<div class="login-sub">Sign in to access personalized articles and comments</div>', unsafe_allow_html=True)

# --- Inputs using Streamlit widgets (needed for proper input) ---
email = st.text_input("Email", key="email")
password = st.text_input("Password", type="password", key="password")

# --- Login Button ---
if st.button("Login"):
    user_service = UserService()
    user = user_service.login(email, password)
    if user:
        st.session_state.user = user
        st.session_state.page = "Home"
        st.success(f"Welcome {user}!")
        st.stop()
    else:
        st.error("Invalid email or password")

# --- Sign Up / Forgot Password Buttons ---
st.markdown('<div class="form-row" style="margin-top:12px;">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("Sign Up"):
        st.session_state.page = "signup"
        st.stop()
with col2:
    if st.button("Forgot Password?"):
        st.session_state.page = "forgot_password"
        st.stop()

st.markdown('</div>', unsafe_allow_html=True)  # Close form-row
st.markdown('</div></div>', unsafe_allow_html=True)  # Close login-card and login-wrapper
