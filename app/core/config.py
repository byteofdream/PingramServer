from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Pingram API"
    api_prefix: str = "/api/v1"
    secret_key: str = "change-me"
    access_token_expire_minutes: int = 60


settings = Settings()
