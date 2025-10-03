from dao.category_dao import CategoryDAO
from models.category import Category

class CategoryService:
    def __init__(self):
        self.dao = CategoryDAO()

    def create_category(self, name: str, description: str = None) -> Category | None:
        return self.dao.create_category(name, description)

    def get_all_categories(self) -> list[Category]:
        return self.dao.get_all_categories()

    def get_category_by_id(self, category_id: int) -> Category | None:
        return self.dao.get_category_by_id(category_id)

    def delete_category(self, category_id: int) -> bool:
        return self.dao.delete_category(category_id)
