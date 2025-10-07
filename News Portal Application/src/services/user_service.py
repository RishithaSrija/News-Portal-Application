import os
from dotenv import load_dotenv
from supabase import create_client, Client
from typing import Optional
from dao.user_dao import UserDAO
from models.user import User
import bcrypt

class UserService:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        self.client: Client = create_client(url, key)
        self.dao = UserDAO()

    def create_user(self, name: str, email: str, password: str, preferences: list = None) -> dict | None:
    # 🔐 Hash the password before storing
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # Prepare the user data
        data = {
        "name": name,
        "email": email,
        "password": hashed_pw,
        "preferences": preferences or []
        }

    # Insert into Supabase
        try:
            response = self.client.table("users").insert(data).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print("Signup error:", e)
            return None
    def get_all_users(self) -> list[User]:
        return self.dao.get_all_users()

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.dao.get_user_by_id(user_id)

    def delete_user(self, user_id: int) -> bool:
        return self.dao.delete_user(user_id)



    def login(self, email: str, password: str) -> dict | None:
     try:
        response = self.client.table("users").select("*").eq("email", email).limit(1).execute()
        user_list = response.data
        if not user_list:
            return None  # No user found

        user = user_list[0]
        if bcrypt.checkpw(password.encode(), user["password"].encode()):
            return user
        else:
            return None  # Password mismatch
     except Exception as e:
        print("Login error:", e)
        return None

    
