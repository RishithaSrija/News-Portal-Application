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

    # ➕ Add New Category
    with st.expander(" Add New Category", expanded=False):
        new_name = st.text_input("Category Name")
        new_description = st.text_area("Description", height=100)

        if st.button("Add Category"):
            if new_name.strip():
                category_service.create_category(new_name.strip(), new_description.strip())
                st.success(f"Category '{new_name}' added successfully!")
                st.rerun()
            else:
                st.warning("Please enter a category name.")

    # Display existing categories
    categories = category_service.get_all_categories()
    if categories:
        for c in categories:
            st.markdown(
                f'<div class="category-card"><h3>{c.name}</h3><p>{c.description or "No description available."}</p></div>',
                unsafe_allow_html=True
            )
    else:
        st.info("No categories found.")

    # Show filtered articles if tag was selected
    selected_tag = st.session_state.get("selected_category")
    if selected_tag:
        st.markdown(f"<h3>Articles in Category: {selected_tag}</h3>", unsafe_allow_html=True)

    # 🔙 Navigation
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.stop()
