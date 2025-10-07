class ArticleTag:
    def __init__(self, article_id: int, tag_id: int):
        self.article_id = article_id
        self.tag_id = tag_id

    def __repr__(self):
        return f"<ArticleTag article_id={self.article_id} tag_id={self.tag_id}>"

    def to_dict(self):
        return {
            "article_id": self.article_id,
            "tag_id": self.tag_id,
        }
