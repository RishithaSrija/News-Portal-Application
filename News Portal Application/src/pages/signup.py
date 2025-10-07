# import streamlit as st
# from pathlib import Path
# from services.user_service import UserService

# css_file = Path(__file__).parent.parent / "styles" / "signup.css"
# if css_file.exists():
#     st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

# st.markdown('<div class="signup-wrapper">', unsafe_allow_html=True)
# st.markdown('<div class="signup-card">', unsafe_allow_html=True)
# st.markdown('<h2>Create Account</h2>', unsafe_allow_html=True)
# st.markdown('<div class="signup-sub">Fill in your details to sign up</div>', unsafe_allow_html=True)

# name = st.text_input("Name")
# email = st.text_input("Email")
# password = st.text_input("Password", type="password")

# if st.button("Register"):
#     user_service = UserService()
#     user = user_service.create_user(name, email, [])  # preferences empty for now
#     if user:
#         st.success("Account created! Please login.")
#         st.session_state.page = "login"
#         st.stop()
#     else:
#         st.error("Registration failed. Check details.")

# if st.button("Back to Login"):
#     st.session_state.page = "login"
#     st.stop()

# st.markdown('</div></div>', unsafe_allow_html=True)
import streamlit as st
from pathlib import Path
from services.user_service import UserService

def signup_page():
    # Load CSS
    css_file = Path(__file__).parent.parent / "styles" / "signup.css"
    if css_file.exists():
        st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

    # Signup layout
    st.markdown('<div class="signup-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="signup-card">', unsafe_allow_html=True)
    st.markdown('<h2>Create Account</h2>', unsafe_allow_html=True)
    st.markdown('<div class="signup-sub">Fill in your details to sign up</div>', unsafe_allow_html=True)

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if not name or not email or not password:
            st.warning("Please fill in all fields.")
        else:
            user_service = UserService()
            user = user_service.create_user(name, email, password, [])
            if user:
                st.session_state.user = user
                st.session_state.page = "home"
                st.success(f"Welcome {user['name']}!")
                st.stop()
            else:
                st.error("Registration failed. Email may already be in use.")

    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.stop()

    st.markdown('</div></div>', unsafe_allow_html=True)
