from fastapi import APIRouter

from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, LoginResponse, RegisterRequest
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest) -> LoginResponse:
    token = AuthService(UserRepository()).login(payload.phone, payload.password)
    return LoginResponse(access_token=token)


@router.post("/register", response_model=LoginResponse)
def register(payload: RegisterRequest) -> LoginResponse:
    token = AuthService(UserRepository()).register(payload.phone, payload.password, payload.username)
    return LoginResponse(access_token=token)
