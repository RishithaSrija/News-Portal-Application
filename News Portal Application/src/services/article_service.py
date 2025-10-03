from dao.articles_dao import ArticleDAO
from models.articles import Article

class ArticleService:
    def __init__(self):
        self.dao = ArticleDAO()

    def create_article(self, title: str, content: str, author_id: int) -> Article | None:
        return self.dao.create_article(title, content, author_id)

    def get_all_articles(self) -> list[Article]:
        return self.dao.get_all_articles()

    def get_article_by_id(self, article_id: int) -> Article | None:
        return self.dao.get_article_by_id(article_id)

    def delete_article(self, article_id: int) -> bool:
        return self.dao.delete_article(article_id)
