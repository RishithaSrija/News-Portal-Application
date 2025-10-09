# # import streamlit as st
# # from pathlib import Path
# # from services.article_service import ArticleService
# # from services.author_service import AuthorService
# # from services.article_tag_service import ArticleTagService
# # from services.tag_service import TagService

# # def articles_page():
# #     # Initialize services
# #     article_service = ArticleService()
# #     author_service = AuthorService()
# #     tag_service = TagService()
# #     article_tag_service = ArticleTagService()

# #     # Load CSS
# #     css_file = Path(__file__).parent.parent / "styles" / "article.css"
# #     if css_file.exists():
# #         st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

# #     # Page title
# #     st.markdown('<h2>📰 Articles</h2>', unsafe_allow_html=True)
# #     st.markdown('<div class="articles-grid">', unsafe_allow_html=True)

# #     # Fetch and display articles
# #     articles = article_service.get_all_articles()
# #     if articles:
# #         for article in articles:
# #             author = author_service.get_author_by_id(article.author_id)
# #             author_name = author.name if author else "Unknown"

# #             tag_ids = article_tag_service.get_tags_for_article(article.article_id)
# #             tags = [tag_service.get_tag_by_id(tid).name for tid in tag_ids if tag_service.get_tag_by_id(tid)]
# #             tags_html = "".join([f'<span class="tag">{t}</span>' for t in tags])

# #             with st.expander(f"📰 {article.title} — by {author_name}"):
# #                 st.markdown(f"""
# # <div class="article-card">
# #     <div class="article-meta">📅 {article.created_at or "N/A"}</div>
# #     <p>{article.content}</p>
# #     {tags_html}
# # </div>
# # """, unsafe_allow_html=True)
# #     else:
# #         st.info("No articles found.")

# #     st.markdown('</div>', unsafe_allow_html=True)

# #     # Navigation
# #     if st.button("Back to Home"):
# #         st.session_state.page = "home"
# #         st.stop()

# import streamlit as st
# from pathlib import Path
# from services.article_service import ArticleService
# from services.author_service import AuthorService
# from services.article_tag_service import ArticleTagService
# from services.tag_service import TagService

# def articles_page():
#     # Initialize services
#     article_service = ArticleService()
#     author_service = AuthorService()
#     tag_service = TagService()
#     article_tag_service = ArticleTagService()

#     # Load CSS
#     css_file = Path(__file__).parent.parent / "styles" / "article.css"
#     if css_file.exists():
#         st.markdown(f"<style>{css_file.read_text()}</style>", unsafe_allow_html=True)

#     st.markdown('<h2 style="background-color:#ffffff; color:#e62c2c; padding:10px; border-radius:8px;">📰 Articles</h2>', unsafe_allow_html=True)


#     with st.expander("➕ Add New Article", expanded=True):
#         new_title = st.text_input("Article Title")
#         new_content = st.text_area("Content", height=200)
#         edit_mode = st.checkbox("Edit before publishing")

#     if st.button("Publish Article"):
#         if new_title.strip() and new_content.strip():
#             author_id = st.session_state.user.user_id if st.session_state.get("user") else None
#             if author_id:
#                 article_service.create_article(new_title, new_content, author_id)
#                 st.success("Article published successfully!")
#                 st.experimental_rerun()
#             else:
#                 st.error("User not logged in. Please log in to publish.")
#         else:
#             st.warning("Please fill in both title and content.")


#     # Display existing articles
#     st.markdown('<div class="articles-grid">', unsafe_allow_html=True)
#     articles = article_service.get_all_articles()
#     if articles:
#         for article in articles:
#             author = author_service.get_author_by_id(article.author_id)
#             author_name = author.name if author else "Unknown"

#             tag_ids = article_tag_service.get_tags_for_article(article.article_id)
#             tags = [tag_service.get_tag_by_id(tid).name for tid in tag_ids if tag_service.get_tag_by_id(tid)]
#             tags_html = "".join([f'<span class="tag">{t}</span>' for t in tags])

#             with st.expander(f"📰 {article.title} — by {author_name}"):
#                 st.markdown(f"""
# <div class="article-card-scroll">
#     <div class="article-meta">📅 {article.created_at or "N/A"}</div>
#     <div class="article-content">{article.content}</div>
#     {tags_html}
# </div>
# """, unsafe_allow_html=True)
#     else:
#         st.info("No articles found.")
#     st.markdown('</div>', unsafe_allow_html=True)

#     # Navigation
#     if st.button("Back to Home"):
#         st.session_state.page = "home"
#         st.stop()

# import streamlit as st
# from pathlib import Path
# from services.article_service import ArticleService
# from services.author_service import AuthorService
# from services.article_tag_service import ArticleTagService
# from services.tag_service import TagService

# def articles_page():
#     # Initialize services
#     article_service = ArticleService()
#     author_service = AuthorService()
#     tag_service = TagService()
#     article_tag_service = ArticleTagService()

#     # Load CSS
#     css_file = Path(__file__).parent.parent / "styles" / "article.css"
#     if css_file.exists():
#         try:
#             css_content = css_file.read_text(encoding="utf-8")
#         except UnicodeDecodeError:
#             css_content = css_file.read_text(encoding="utf-8", errors="ignore")
#         st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

#     # Page Title
#     st.markdown('<h2>📰 Articles</h2>', unsafe_allow_html=True)

#     # ➕ Add New Article
#     with st.expander("➕ Add New Article", expanded=False):
#         new_title = st.text_input("Article Title")
#         new_content = st.text_area("Content", height=200)

#         # Dynamic Author Selection
#         author_input_mode = st.radio("Author Input Mode", ["Select Existing", "Enter New"])
#         author_id = None

#         if author_input_mode == "Select Existing":
#             authors = author_service.get_all_authors()
#             author_options = {author.name: author.author_id for author in authors}
#             selected_author_name = st.selectbox("Select Author", list(author_options.keys()))
#             author_id = author_options[selected_author_name]
#         else:
#             new_author_name = st.text_input("Enter Author Name")
#             if new_author_name.strip():
#                 existing = [a for a in author_service.get_all_authors() if a.name.lower() == new_author_name.lower()]
#                 if existing:
#                     author_id = existing[0].author_id
                
#                 if isinstance(current_user, dict) and "email" in current_user:
#                     author_id = author_service.create_author(new_author_name, current_user["email"]).author_id
#                 else:
#                     st.error("User email not found. Please log in again.")
#                     st.stop()
#         if st.button("Publish Article"):
#             if new_title.strip() and new_content.strip() and author_id:
#                 article_service.create_article(new_title, new_content, author_id)
#                 st.success("Article published successfully!")
#                 st.rerun()
#             else:
#                 st.warning("Please fill in all fields.")

#     # 📰 Display Existing Articles
#     st.markdown('<div class="articles-grid">', unsafe_allow_html=True)
#     articles = article_service.get_all_articles()
#     current_user = st.session_state.get("user")

#     if articles:
#         for article in articles:
#             author = author_service.get_author_by_id(article.author_id)
#             author_name = author.name if author else "Unknown"

#             tag_ids = article_tag_service.get_tags_for_article(article.article_id)
#             tags = [tag_service.get_tag_by_id(tid).name for tid in tag_ids if tag_service.get_tag_by_id(tid)]
#             tags_html = "".join([f'<span class="tag">{t}</span>' for t in tags])

#             with st.expander(f"📰 {article.title} — by {author_name}"):
#                 st.markdown(f"""
#                 <div class="article-card-scroll">
#                     <div class="article-meta">📅 {article.created_at or "N/A"}</div>
#                     <div class="article-content">{article.content}</div>
#                     {tags_html}
#                 </div>
#                 """, unsafe_allow_html=True)

#                 # 🔖 Tag filter buttons
#                 for tag_name in tags:
#                     if st.button(f"🔖 {tag_name}", key=f"tag_{tag_name}_{article.article_id}"):
#                         st.session_state.selected_category = tag_name
#                         st.session_state.page = "categories"
#                         st.stop()

#                 # 🗑️ Secure Delete Logic
#                 if current_user and current_user.get("user_id") == article.author_id:
#                     if st.button(f"Delete '{article.title}'", key=f"trigger_delete_{article.article_id}"):
#                         st.session_state.confirm_delete_id = article.article_id

#                     if st.session_state.get("confirm_delete_id") == article.article_id:
#                         st.warning(f"Are you sure you want to delete '{article.title}'?")
#                         col1, col2 = st.columns([1, 1])
#                         with col1:
#                             if st.button("✅ Confirm Delete", key=f"confirm_{article.article_id}"):
#                                 article_service.delete_article(article.article_id)
#                                 st.success(f"Deleted article: {article.title}")
#                                 st.session_state.confirm_delete_id = None
#                                 st.rerun()
#                         with col2:
#                             if st.button("❌ Cancel", key=f"cancel_{article.article_id}"):
#                                 st.session_state.confirm_delete_id = None
#     else:
#         st.info("No articles found.")
#     st.markdown('</div>', unsafe_allow_html=True)

#     # 🔙 Navigation
#     if st.button("Back to Home"):
#         st.session_state.page = "home"
#         st.stop()

import streamlit as st
from pathlib import Path
from services.article_service import ArticleService
from services.author_service import AuthorService
from services.article_tag_service import ArticleTagService
from services.tag_service import TagService

def articles_page():
    # Initialize services
    article_service = ArticleService()
    author_service = AuthorService()
    tag_service = TagService()
    article_tag_service = ArticleTagService()



    current_user = st.session_state.get("user")

    # Load CSS
    css_file = Path(__file__).parent.parent / "styles" / "article.css"
    if css_file.exists():
        try:
            css_content = css_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            css_content = css_file.read_text(encoding="utf-8", errors="ignore")
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

    # Page Title
    st.markdown('<h2>📰 Articles</h2>', unsafe_allow_html=True)

    # ➕ Add New Article
    with st.expander("➕ Add New Article", expanded=False):
        new_title = st.text_input("Article Title")
        new_content = st.text_area("Content", height=200)
        author_id = None

        # Dynamic Author Selection
        author_input_mode = st.radio("Author Input Mode", ["Select Existing", "Enter New"])

        if author_input_mode == "Select Existing":
            authors = author_service.get_all_authors()
            author_options = {author.name: author.author_id for author in authors}
            selected_author_name = st.selectbox("Select Author", list(author_options.keys()))
            author_id = author_options[selected_author_name]
        else:
            new_author_name = st.text_input("Enter Author Name")
            if new_author_name.strip():
                existing = [a for a in author_service.get_all_authors() if a.name.lower() == new_author_name.lower()]
                if existing:
                    author_id = existing[0].author_id
                elif isinstance(current_user, dict) and "email" in current_user:
                    author_id = author_service.create_author(new_author_name, current_user["email"]).author_id
                else:
                    st.error("User email not found. Please log in again.")
                    st.stop()

        if st.button("Publish Article"):
            if new_title.strip() and new_content.strip():
        # 🧩 Find or create the author linked to the current user’s email
                existing_author = next(
                    (a for a in author_service.get_all_authors()
                    if a.email.strip().lower() == current_user["email"].strip().lower()),
                    None
                    )
                if existing_author:
                    author_id = existing_author.author_id
                else:
                    new_author = author_service.create_author(
                    current_user["name"],
                    current_user["email"]
                    )
                    author_id = new_author.author_id

            # ✅ Now create the article with correct author_id
                article_service.create_article(new_title, new_content, author_id)
                st.success("Article published successfully!")
                st.rerun()
            else:
                st.warning("Please fill in all fields.")

    # 📰 Display Existing Articles
    st.markdown('<div class="articles-grid">', unsafe_allow_html=True)
    articles = article_service.get_all_articles()

    if articles:
        for article in articles:
            author = author_service.get_author_by_id(article.author_id)
            author_name = author.name if author else "Unknown"
            
            tag_ids = article_tag_service.get_tags_for_article(article.article_id)
            tags = [tag_service.get_tag_by_id(tid).name for tid in tag_ids if tag_service.get_tag_by_id(tid)]
            tags_html = "".join([f'<span class="tag">{t}</span>' for t in tags])

            with st.expander(f"📰 {article.title} — by {author_name}"):
                st.markdown(f"""
                <div class="article-card-scroll">
                    <div class="article-meta">📅 {article.created_at or "N/A"}</div>
                    <div class="article-content">{article.content}</div>
                    {tags_html}
                </div>
                """, unsafe_allow_html=True)

                # 🔖 Tag filter buttons
                for tag_name in tags:
                    if st.button(f"🔖 {tag_name}", key=f"tag_{tag_name}_{article.article_id}"):
                        st.session_state.selected_category = tag_name
                        st.session_state.page = "categories"
                        st.stop()

                # 🗑️ Secure Delete Logic (Email-based ownership check)
                author = author_service.get_author_by_id(article.author_id)
                if (
                    author
                    and isinstance(current_user, dict)
                    and author.email.strip().lower() == current_user.get("email", "").strip().lower()
                    ):
                    article_title_safe = article.title if article.title else "Untitled Article"
                    article_id_safe = article.article_id
                    delete_key = f"trigger_delete_{article_id_safe}"

                    if st.button(f"🗑️ Delete '{article_title_safe}'", key=delete_key):
                        st.session_state["confirm_delete_id"] = article_id_safe

                    if st.session_state.get("confirm_delete_id") == article_id_safe:
                        st.markdown(f"""
                        <div style="background-color:#330000; color:#ff6666; padding:15px; border-radius:10px; margin-top:10px;">
                        ⚠️ <strong>Are you sure you want to delete '{article_title_safe}'?</strong>
                        </div>
                        """, unsafe_allow_html=True)

                        col1, col2 = st.columns([1, 1])
                        with col1:
                            if st.button("✅ Confirm Delete", key=f"confirm_{article_id_safe}"):
                                article_service.delete_article(article_id_safe)
                                st.success(f"Deleted article: {article_title_safe}")
                                st.session_state["confirm_delete_id"] = None
                                st.rerun()
                        with col2:
                            if st.button("❌ Cancel", key=f"cancel_{article_id_safe}"):
                                st.session_state["confirm_delete_id"] = None


    else:
        st.info("No articles found.")
    st.markdown('</div>', unsafe_allow_html=True)

    # 🔙 Navigation
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.stop()
