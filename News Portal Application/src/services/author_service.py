from dao.author_dao import AuthorDAO
from models.author import Author

class AuthorService:
    def __init__(self):
        self.dao = AuthorDAO()

    def create_author(self, name: str, email: str, role: str = "Editor") -> Author | None:
        return self.dao.create_author(name, email, role)

    def get_all_authors(self) -> list[Author]:
        return self.dao.get_all_authors()

    def get_author_by_id(self, author_id: int) -> Author | None:
        return self.dao.get_author_by_id(author_id)
