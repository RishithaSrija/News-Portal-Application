# # src/routes/article_routes.py
# from flask import Blueprint, render_template, request, redirect
# from services.article_service import ArticleService

# article_bp = Blueprint("articles", __name__)
# service = ArticleService()

# @article_bp.route("/articles")
# def list_articles():
#     articles = service.get_all_articles()
#     return render_template("articles.html", articles=articles)

# @article_bp.route("/articles/<int:article_id>")
# def view_article(article_id):
#     article = service.get_article(article_id)
#     comments = service.get_comments(article_id)
#     return render_template("article_detail.html", article=article, comments=comments)

# @article_bp.route("/articles/create", methods=["GET", "POST"])
# def create_article():
#     if request.method == "POST":
#         title = request.form["title"]
#         content = request.form["content"]
#         author_id = request.form["author_id"]
#         service.create_article(title, content, author_id)
#         return redirect("/articles")
#     return render_template("article_form.html")

# @article_bp.route("/articles/<int:article_id>/delete")
# def delete_article(article_id):
#     service.delete_article(article_id)
#     return redirect("/articles")
