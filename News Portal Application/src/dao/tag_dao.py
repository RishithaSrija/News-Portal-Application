from config import get_supabase
from models.tag import Tag

supabase = get_supabase()

class TagDAO:
    def create_tag(self, name: str) -> Tag | None:
        resp = supabase.table("tags").insert({"name": name}).execute()
        if resp.data:
            row = resp.data[0]
            return Tag(tag_id=row["tag_id"], name=row["name"])
        return None

    def get_all_tags(self) -> list[Tag]:
        resp = supabase.table("tags").select("*").execute()
        return [Tag(tag_id=row["tag_id"], name=row["name"]) for row in (resp.data or [])]

    def delete_tag(self, tag_id: int) -> bool:
        resp = supabase.table("tags").delete().eq("tag_id", tag_id).execute()
        return bool(resp.data)
    def get_tag_by_id(self, tag_id: int) -> Tag | None:
        resp = supabase.table("tags").select("*").eq("tag_id", tag_id).single().execute()
        if resp.data:
            row = resp.data
            return Tag(tag_id=row["tag_id"], name=row["name"])
        return None

