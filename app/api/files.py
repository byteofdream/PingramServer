from fastapi import APIRouter

router = APIRouter(prefix="/files", tags=["files"])


@router.get("/{file_id}")
def get_file_meta(file_id: str) -> dict:
    return {"file_id": file_id, "url": f"https://cdn.pingram.local/{file_id}"}
