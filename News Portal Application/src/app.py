import streamlit as st

# Initialize session_state
if "page" not in st.session_state:
    st.session_state.page = "login"
if "user" not in st.session_state:
    st.session_state.user = None

# Page router
page = st.session_state.page

if page == "login":
    from pages.login import login_page
    login_page()
elif page == "signup":
    from pages.signup import signup_page
    signup_page()
elif page == "forgot":
    from pages.forgot import forgot_password_page
    forgot_password_page()
elif page == "home":
    from pages.home import home_page
    home_page()
elif page == "articles":
    from pages.articles import articles_page
    articles_page()
elif page == "categories":
    from pages.categories import categories_page
    categories_page()
