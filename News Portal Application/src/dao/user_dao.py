from config import get_supabase
from models.user import User

supabase = get_supabase()

class UserDAO:
    def create_user(self, name: str, email: str, preferences: list[str] = None) -> User | None:
        resp = supabase.table("users").insert({
            "name": name,
            "email": email,
            "preferences": preferences or []
        }).execute()

        if resp.data:
            row = resp.data[0]
            return User(
                user_id=row["user_id"],
                name=row["name"],
                email=row["email"],
                preferences=row.get("preferences", []),
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
        return None

    def get_all_users(self) -> list[User]:
        resp = supabase.table("users").select("*").execute()
        return [
            User(
                user_id=row["user_id"],
                name=row["name"],
                email=row["email"],
                preferences=row.get("preferences", []),
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
            for row in (resp.data or [])
        ]

    def get_user_by_id(self, user_id: int) -> User | None:
        resp = supabase.table("users").select("*").eq("user_id", user_id).single().execute()
        if resp.data:
            row = resp.data
            return User(
                user_id=row["user_id"],
                name=row["name"],
                email=row["email"],
                preferences=row.get("preferences", []),
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
        return None

    def update_user(self, user_id: int, name: str | None = None, email: str | None = None, preferences: list[str] | None = None) -> User | None:
        update_fields = {}
        if name is not None:
            update_fields["name"] = name
        if email is not None:
            update_fields["email"] = email
        if preferences is not None:
            update_fields["preferences"] = preferences

        if not update_fields:
            return None

        resp = supabase.table("users").update(update_fields).eq("user_id", user_id).execute()
        if resp.data:
            row = resp.data[0]
            return User(
                user_id=row["user_id"],
                name=row["name"],
                email=row["email"],
                preferences=row.get("preferences", []),
                created_at=row.get("created_at"),
                updated_at=row.get("updated_at")
            )
        return None

    def delete_user(self, user_id: int) -> bool:
        resp = supabase.table("users").delete().eq("user_id", user_id).execute()
        return bool(resp.data)
