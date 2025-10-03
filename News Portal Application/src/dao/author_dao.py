from config import get_supabase
from models.author import Author

supabase = get_supabase()

class AuthorDAO:
    def create_author(self, name: str, email: str, role: str = "Editor") -> Author | None:
        resp = supabase.table("authors").insert({
            "name": name,
            "email": email,
            "role": role
        }).execute()

        if resp.data:
            row = resp.data[0]
            return Author(
                author_id=row["author_id"],
                name=row["name"],
                email=row["email"],
                role=row["role"],
                created_at=row.get("created_at")
            )
        return None

    def get_all_authors(self) -> list[Author]:
        resp = supabase.table("authors").select("*").execute()
        return [
            Author(
                author_id=row["author_id"],
                name=row["name"],
                email=row["email"],
                role=row["role"],
                created_at=row.get("created_at")
            )
            for row in (resp.data or [])
        ]

    def get_author_by_id(self, author_id: int) -> Author | None:
        resp = supabase.table("authors").select("*").eq("author_id", author_id).single().execute()
        if resp.data:
            row = resp.data
            return Author(
                author_id=row["author_id"],
                name=row["name"],
                email=row["email"],
                role=row["role"],
                created_at=row.get("created_at")
            )
        return None

    def update_author(self, author_id: int, name: str | None = None, email: str | None = None, role: str | None = None) -> Author | None:
        update_fields = {}
        if name is not None:
            update_fields["name"] = name
        if email is not None:
            update_fields["email"] = email
        if role is not None:
            update_fields["role"] = role

        if not update_fields:
            return None

        resp = supabase.table("authors").update(update_fields).eq("author_id", author_id).execute()
        if resp.data:
            row = resp.data[0]
            return Author(
                author_id=row["author_id"],
                name=row["name"],
                email=row["email"],
                role=row["role"],
                created_at=row.get("created_at")
            )
        return None

    def delete_author(self, author_id: int) -> bool:
        resp = supabase.table("authors").delete().eq("author_id", author_id).execute()
        return bool(resp.data)
    
    
