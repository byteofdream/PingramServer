from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
def me() -> dict:
    # In production, user is resolved via bearer auth dependency.
    return {"id": "user-alice", "username": "alice", "phone": "+380501112233"}
