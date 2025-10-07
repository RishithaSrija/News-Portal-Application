import streamlit as st
from pathlib import Path
from services.category_service import CategoryService

def categories_page():
    category_service = CategoryService()

    # Load CSS
    css_file = Path(__file__).parent.parent / "styles" / "categories.css"
    if css_file.exists():
        st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

    # Page title
    st.markdown('<h2>📂 Categories</h2>', unsafe_allow_html=True)

    # Fetch and display categories
    categories = category_service.get_all_categories()
    if categories:
        for c in categories:
            st.markdown(
                f'<div class="category-card"><h3>{c.name}</h3><p>{c.description or "No description available."}</p></div>',
                unsafe_allow_html=True
            )
    else:
        st.info("No categories found.")
    selected_tag = st.session_state.get("selected_category")
    if selected_tag:
        st.markdown(f"<h3>Articles in Category: {selected_tag}</h3>", unsafe_allow_html=True)
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.stop()
