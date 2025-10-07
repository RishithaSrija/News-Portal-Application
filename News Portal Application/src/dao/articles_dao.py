from config import get_supabase
from models.articles import Article

supabase = get_supabase()

class ArticleDAO:
    def create_article(
        self, 
        title: str, 
        content: str, 
        author_id: int, 
        category_id: int | None = None, 
        status: str = "Draft"
    ) -> Article | None:
        resp = supabase.table("articles").insert({
            "title": title,
            "content": content,
            "author_id": author_id,
            "category_id": category_id,
            "status": status
        }).execute()

        if resp.data:
            row = resp.data[0]
            return Article(
                article_id=row["article_id"],
                title=row["title"],
                content=row["content"],
                author_id=row["author_id"],
                category_id=row.get("category_id"),
                status=row["status"],
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
        return None

    def get_all_articles(self) -> list[Article]:
        resp = supabase.table("articles").select("*").execute()
        return [
            Article(
                article_id=row["article_id"],
                title=row["title"],
                content=row["content"],
                author_id=row["author_id"],
                category_id=row.get("category_id"),
                status=row["status"],
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            ) for row in resp.data or []
        ]

    def get_article_by_id(self, article_id: int) -> Article | None:
        resp = supabase.table("articles").select("*").eq("article_id", article_id).single().execute()
        row = resp.data
        if row:
            return Article(
                article_id=row["article_id"],
                title=row["title"],
                content=row["content"],
                author_id=row["author_id"],
                category_id=row.get("category_id"),
                status=row["status"],
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
        return None

    def delete_article(self, article_id: int) -> bool:
        resp = supabase.table("articles").delete().eq("article_id", article_id).execute()
        return bool(resp.data)
