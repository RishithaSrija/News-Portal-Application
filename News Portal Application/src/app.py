import streamlit as st
from pathlib import Path

# Initialize session_state
if "page" not in st.session_state:
    st.session_state.page = "login"
if "user" not in st.session_state:
    st.session_state.user = None

# Page router
page = st.session_state.page

if page == "login":
    from pages import login
elif page == "signup":
    from pages import signup
elif page == "forgot":
    from pages import forgot_pass
elif page == "home":
    from pages import Home
elif page == "articles":
    from pages import articles
elif page == "categories":
    from pages import categories
