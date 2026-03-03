from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    phone: str = Field(min_length=7, max_length=20)
    password: str = Field(min_length=6)


class RegisterRequest(BaseModel):
    phone: str = Field(min_length=7, max_length=20)
    password: str = Field(min_length=6)
    username: str = Field(min_length=3, max_length=32)


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
