from dao.comment_dao import CommentDAO
from models.comment import Comment

class CommentService:
    def __init__(self):
        self.dao = CommentDAO()

    def create_comment(self, article_id: int, user_id: int, content: str) -> Comment | None:
        return self.dao.create_comment(article_id, user_id, content)

    def get_comments_by_article(self, article_id: int) -> list[Comment]:
        return self.dao.get_comments_by_article(article_id)

    def delete_comment(self, comment_id: int) -> bool:
        return self.dao.delete_comment(comment_id)
