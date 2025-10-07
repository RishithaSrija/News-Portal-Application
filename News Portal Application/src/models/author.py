class Author:
    def __init__(self, author_id: int, name: str, email: str, role: str = "Editor", created_at: str = None):
        self.author_id = author_id
        self.name = name
        self.email = email
        self.role = role
        self.created_at = created_at

    def __repr__(self):
        return f"<Author id={self.author_id} name={self.name}>"

    def to_dict(self):
        return {
            "author_id": self.author_id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "created_at": self.created_at,
        }
