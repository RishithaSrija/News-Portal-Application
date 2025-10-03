import streamlit as st
from pathlib import Path

css_file = Path(__file__).parent.parent / "styles" / "home.css"
if css_file.exists():
    st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

st.title("👋 Welcome to News Portal")
st.write("""
This is your one-stop platform to:
- ✍️ Publish articles  
- 🔍 Search & edit articles  
- 📂 Manage categories  
""")

col1, col2 = st.columns([1,1])
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

st.markdown('</div>', unsafe_allow_html=True)
