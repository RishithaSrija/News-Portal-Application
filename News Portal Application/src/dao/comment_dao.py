from config import get_supabase
from models.comment import Comment

supabase = get_supabase()

class CommentDAO:
    def create_comment(self, article_id: int, user_id: int, content: str) -> Comment | None:
        resp = supabase.table("comments").insert({
            "article_id": article_id,
            "user_id": user_id,
            "content": content
        }).execute()

        if resp.data:
            row = resp.data[0]
            return Comment(
                comment_id=row["comment_id"],
                article_id=row["article_id"],
                user_id=row["user_id"],
                content=row["content"],
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
        return None

    def get_comments_by_article(self, article_id: int) -> list[Comment]:
        resp = supabase.table("comments").select("*").eq("article_id", article_id).execute()
        return [
            Comment(
                comment_id=row["comment_id"],
                article_id=row["article_id"],
                user_id=row["user_id"],
                content=row["content"],
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
            for row in (resp.data or [])
        ]

    def get_comment_by_id(self, comment_id: int) -> Comment | None:
        resp = supabase.table("comments").select("*").eq("comment_id", comment_id).single().execute()
        if resp.data:
            row = resp.data
            return Comment(
                comment_id=row["comment_id"],
                article_id=row["article_id"],
                user_id=row["user_id"],
                content=row["content"],
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
        return None

    def update_comment(self, comment_id: int, content: str) -> Comment | None:
        resp = supabase.table("comments").update({
            "content": content,
            "updated_at": "now()"
        }).eq("comment_id", comment_id).execute()

        if resp.data:
            row = resp.data[0]
            return Comment(
                comment_id=row["comment_id"],
                article_id=row["article_id"],
                user_id=row["user_id"],
                content=row["content"],
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
        return None

    def delete_comment(self, comment_id: int) -> bool:
        resp = supabase.table("comments").delete().eq("comment_id", comment_id).execute()
        return bool(resp.data)
    
    
