class Comment:
    def __init__(self, comment_id: int, article_id: int, user_id: int,
                 content: str, created_at: str = None, updated_at: str = None):
        self.comment_id = comment_id
        self.article_id = article_id
        self.user_id = user_id
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Comment id={self.comment_id} article_id={self.article_id} user_id={self.user_id}>"

    def to_dict(self):
        return {
            "comment_id": self.comment_id,
            "article_id": self.article_id,
            "user_id": self.user_id,
            "content": self.content,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
