from fastapi import FastAPI

from app.api import auth, files, messages, users
from app.core.config import settings

app = FastAPI(title=settings.app_name)

app.include_router(auth.router, prefix=settings.api_prefix)
app.include_router(messages.router, prefix=settings.api_prefix)
app.include_router(users.router, prefix=settings.api_prefix)
app.include_router(files.router, prefix=settings.api_prefix)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
