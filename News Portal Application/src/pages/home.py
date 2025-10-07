import streamlit as st
from pathlib import Path

if "user" not in st.session_state or st.session_state.user is None:
    st.session_state.user = type("User", (), {"name": "Rishitha"})()

def top_navbar():
    if st.session_state.get("user"):
        nav = st.columns([8, 1, 1, 1])
        with nav[0]:
            st.markdown(
                f"<div class='navbar-welcome'>Welcome, <strong>{st.session_state.user['name']}</strong></div>",
                unsafe_allow_html=True
            )
        with nav[1]:
            if st.button("👤", help="Go to Profile"):
                st.session_state.page = "profile"
                st.stop()
        with nav[2]:
            if st.button("⚙️", help="Settings"):
                st.session_state.page = "settings"
                st.stop()
        with nav[3]:
            if st.button("🚪", help="Logout"):
                st.session_state.user = None
                st.session_state.page = "login"
                st.experimental_rerun()

def home_page():
    # Load CSS
    css_file = Path(__file__).parent.parent / "styles" / "home.css"
    if css_file.exists():
        st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

    # Sidebar Navigation
    st.sidebar.title("📚 News Portal")
    st.sidebar.markdown("### Menu")
    st.sidebar.button("Welcome", on_click=lambda: st.session_state.update({"page": "home"}))
    st.sidebar.button("Articles", on_click=lambda: st.session_state.update({"page": "articles"}))
    st.sidebar.button("Categories", on_click=lambda: st.session_state.update({"page": "categories"}))
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"user": None, "page": "login"}))
    st.sidebar.markdown("<p style='color:#e62c2c;'>News will be soon available here.</p>", unsafe_allow_html=True)

    # Top Navigation
    top_navbar()

    # Main Content
    st.title("👋 Welcome to News Portal")
    st.markdown("""
    <p>This is your one-stop platform to:</p>
    <ul>
        <li>✍️ Publish articles</li>
        <li>🔍 Search & edit articles</li>
        <li>📂 Manage categories</li>
    </ul>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Articles"):
            st.session_state.page = "articles"
            st.stop()
    with col2:
        if st.button("Categories"):
            st.session_state.page = "categories"
            st.stop()

    if st.button("Logout"):
        st.session_state.user = None
        st.session_state.page = "login"
        st.stop()
