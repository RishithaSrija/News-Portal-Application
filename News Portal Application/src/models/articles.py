class Article:
    def __init__(self, article_id: int, title: str, content: str, author_id: int,
                 category_id: int = None, status: str = "Draft", created_at: str = None, updated_at: str = None):
        self.article_id = article_id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.category_id = category_id
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Article id={self.article_id} title={self.title}>"

    def to_dict(self):
        return {
            "article_id": self.article_id,
            "title": self.title,
            "content": self.content,
            "author_id": self.author_id,
            "category_id": self.category_id,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
