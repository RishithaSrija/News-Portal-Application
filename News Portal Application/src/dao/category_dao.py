from config import get_supabase
from models.category import Category

supabase = get_supabase()

class CategoryDAO:
    def create_category(self, name: str, description: str = None) -> Category | None:
        resp = supabase.table("categories").insert({
            "name": name,
            "description": description
        }).execute()

        if resp.data:
            row = resp.data[0]
            return Category(
                category_id=row["category_id"],
                name=row["name"],
                description=row.get("description"),
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
        return None

    def get_all_categories(self) -> list[Category]:
        resp = supabase.table("categories").select("*").execute()
        return [
            Category(
                category_id=row["category_id"],
                name=row["name"],
                description=row.get("description"),
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
            for row in (resp.data or [])
        ]

    def get_category_by_id(self, category_id: int) -> Category | None:
        resp = supabase.table("categories").select("*").eq("category_id", category_id).single().execute()
        if resp.data:
            row = resp.data
            return Category(
                category_id=row["category_id"],
                name=row["name"],
                description=row.get("description"),
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
        return None

    def update_category(self, category_id: int, name: str | None = None, description: str | None = None) -> Category | None:
        update_fields = {}
        if name is not None:
            update_fields["name"] = name
        if description is not None:
            update_fields["description"] = description

        if not update_fields:
            return None

        resp = supabase.table("categories").update(update_fields).eq("category_id", category_id).execute()
        if resp.data:
            row = resp.data[0]
            return Category(
                category_id=row["category_id"],
                name=row["name"],
                description=row.get("description"),
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
        return None

    def delete_category(self, category_id: int) -> bool:
        resp = supabase.table("categories").delete().eq("category_id", category_id).execute()
        return bool(resp.data)
    
    
