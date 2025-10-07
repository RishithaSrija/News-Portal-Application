import streamlit as st
from pathlib import Path
from services.article_service import ArticleService

def profile_page():
# Load CSS
    css_file = Path(__file__).parent.parent / "styles/main.css"
    if css_file.exists():
        st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

    st.title("👤 My Profile")

    if "user" not in st.session_state or st.session_state.user is None:
        st.warning("Please login first.")
    else:
        user = st.session_state.user
        article_service = ArticleService()
        all_articles = article_service.get_all_articles()
    
    # Filter articles by author_id
        user_articles = [article for article in all_articles if article.author_id == user["user_id"]]
        article_count = len(user_articles)

    # Display profile info
        st.markdown(f"""
        <div class='card'>
            <h3>{user['name']}</h3>
            <p>Email: {user['email']}</p>
            <p><strong>Articles Posted:</strong> {article_count}</p>
        </div>
        """, unsafe_allow_html=True)
