from fastapi import HTTPException, status
from uuid import uuid4

from app.core.security import create_access_token
from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def login(self, phone: str, password: str) -> str:
        user = self.user_repo.get_by_phone(phone)
        if not user or user.password_hash != password:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return create_access_token(user.id)

    def register(self, phone: str, password: str, username: str) -> str:
        if self.user_repo.get_by_phone(phone):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Phone already registered")
        if self.user_repo.get_by_username(username):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already taken")

        user = User(
            id=f"user-{uuid4().hex[:12]}",
            username=username,
            phone=phone,
            password_hash=password,
        )
        self.user_repo.create(user)
        return create_access_token(user.id)
