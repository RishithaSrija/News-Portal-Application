# src/dao/article_tag_dao.py

from config import get_supabase
from models.article_tag import ArticleTag

supabase = get_supabase()

class ArticleTagDAO:
    def add_tag_to_article(self, article_id: str, tag_id: str) -> ArticleTag | None:
        resp = supabase.table("article_tags").insert({
            "article_id": article_id,
            "tag_id": tag_id
        }).execute()

        if resp.data:
            row = resp.data[0]
            return ArticleTag(article_id=row["article_id"], tag_id=row["tag_id"])
        return None

    def get_tags_for_article(self, article_id: str) -> list[str]:
        """Return list of tag_ids for a given article"""
        resp = supabase.table("article_tags").select("*").eq("article_id", article_id).execute()
        return [row["tag_id"] for row in resp.data]

    def remove_tag_from_article(self, article_id: str, tag_id: str) -> bool:
        resp = supabase.table("article_tags").delete().eq("article_id", article_id).eq("tag_id", tag_id).execute()
        return bool(resp.data)
