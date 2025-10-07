# import streamlit as st
# from pathlib import Path
# from services.user_service import UserService

# # --- Load CSS ---
# css_file = Path(__file__).parent.parent / "styles" / "login.css"
# if css_file.exists():
#     st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

# # --- Login Layout ---
# st.markdown("<h1 style='text-align:center; color:#e62c2c;'>🔐 Login to News Portal</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center; color:#ccc;'>Access personalized articles and manage your content</p>", unsafe_allow_html=True)

# with st.container():
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         user_service = UserService()
#         user = user_service.login(email, password)
#         if user:
#             st.session_state.user = user
#             st.session_state.page = "Home"
#             st.success(f"Welcome {user.name}!")  # Assuming user object has .name
#             st.stop()
#         else:
#             st.error("Invalid email or password")

#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("Sign Up"):
#             st.session_state.page = "signup"
#             st.stop()
#     with col2:
#         if st.button("Forgot Password?"):
#             st.session_state.page = "forgot_password"
#             st.stop()

import streamlit as st
from pathlib import Path
from services.user_service import UserService

def login_page():
    css_file = Path(__file__).parent.parent / "styles" / "login.css"
    if css_file.exists():
        st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center; color:#e62c2c;'>🔐 Login to News Portal</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ccc;'>Access personalized articles and manage your content</p>", unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not email or not password:
            st.warning("Please enter both email and password.")
        else:
            user_service = UserService()
            user = user_service.login(email, password)
            if user:
                st.session_state.user = user
                st.session_state.page = "home"
                st.success(f"Welcome {user['name']}!")
                st.rerun()
            else:
                st.error("Invalid email or password.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sign Up"):
            st.session_state.page = "signup"
            st.stop()
    with col2:
        if st.button("Forgot Password?"):
            st.session_state.page = "forgot"
            st.stop()
