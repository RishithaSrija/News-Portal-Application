from dao.article_tag_dao import ArticleTagDAO
from models.article_tag import ArticleTag

class ArticleTagService:
    def __init__(self):
        self.dao = ArticleTagDAO()

    def add_tag_to_article(self, article_id: str, tag_id: str) -> ArticleTag | None:
        return self.dao.add_tag_to_article(article_id, tag_id)

    def get_tags_for_article(self, article_id: str) -> list[str]:
        return self.dao.get_tags_for_article(article_id)

    def remove_tag_from_article(self, article_id: str, tag_id: str) -> bool:
        return self.dao.remove_tag_from_article(article_id, tag_id)
