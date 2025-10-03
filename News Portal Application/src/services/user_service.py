from typing import Optional
from dao.user_dao import UserDAO
from models.user import User

class UserService:
    def __init__(self):
        self.dao = UserDAO()

    def create_user(self, name: str, email: str, preferences: list = None) -> User | None:
        return self.dao.create_user(name, email, preferences)

    def get_all_users(self) -> list[User]:
        return self.dao.get_all_users()

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.dao.get_user_by_id(user_id)

    def delete_user(self, user_id: int) -> bool:
        return self.dao.delete_user(user_id)
    def login(self, email: str, password: str) -> Optional[User]:
        """
        Dummy login: checks if email exists.
        If you want proper authentication, you need to store passwords in your DB.
        """
        users = self.get_all_users()
        for u in users:
            if u.email == email:
                return u
        return None
