class User:
    def __init__(self, user_id: int, name: str, email: str, preferences: list = None, created_at: str = None, updated_at: str = None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.preferences = preferences or []
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<User id={self.user_id} name={self.name}>"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "preferences": self.preferences,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
