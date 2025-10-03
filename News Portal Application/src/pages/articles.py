import streamlit as st
from pathlib import Path
from services.article_service import ArticleService
from services.author_service import AuthorService
from services.article_tag_service import ArticleTagService
from services.tag_service import TagService

# Initialize services
article_service = ArticleService()
author_service = AuthorService()
tag_service = TagService()
article_tag_service = ArticleTagService()

# Load CSS
css_file = Path(__file__).parent.parent / "styles" / "article.css"
if css_file.exists():
    st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

st.markdown('<h2>Articles</h2>', unsafe_allow_html=True)
st.markdown('<div class="articles-grid">', unsafe_allow_html=True)

# Fetch all articles dynamically
articles = article_service.get_all_articles()

if articles:
    for article in articles:
        # Get author name
        author = author_service.get_author_by_id(article.author_id)
        author_name = author.name if author else "Unknown"

        # Get tags for this article
        tag_ids = article_tag_service.get_tags_for_article(article.article_id)
        tags = [tag_service.get_tag_by_id(tid).name for tid in tag_ids if tag_service.get_tag_by_id(tid)]
        tags_html = "".join([f'<span class="tag">{t}</span>' for t in tags])

        # Article description (truncate if too long)
        description = article.content[:200] + "..." if len(article.content) > 200 else article.content

        # Render article card
        st.markdown(f"""
        <div class="article-card">
            <h3>{article.title}</h3>
            <div class="article-meta">By {author_name} • {article.created_at or "N/A"}</div>
            <p>{description}</p>
            {tags_html}
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No articles found.")

# Back to Home button
if st.button("Back to Home"):
    st.session_state.page = "home"
    st.stop()

st.markdown('</div>', unsafe_allow_html=True)
