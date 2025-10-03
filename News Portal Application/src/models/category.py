class Category:
    def __init__(self, category_id: int, name: str, description: str = None, created_at: str = None, updated_at: str = None):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Category id={self.category_id} name={self.name}>"

    def to_dict(self):
        return {
            "category_id": self.category_id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
