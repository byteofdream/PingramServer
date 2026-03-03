from fastapi import APIRouter, Depends, Header, HTTPException, status

from app.core.security import decode_access_token
from app.repositories.message_repository import MessageRepository
from app.schemas.message import MessageResponse, SendMessageRequest
from app.services.message_service import MessageService

router = APIRouter(prefix="/messages", tags=["messages"])


def get_current_user_id(authorization: str | None = Header(default=None)) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token")

    token = authorization.split(" ", 1)[1]
    user_id = decode_access_token(token)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return user_id


@router.post("/send", response_model=MessageResponse)
def send_message(payload: SendMessageRequest, user_id: str = Depends(get_current_user_id)) -> MessageResponse:
    message = MessageService(MessageRepository()).send_message(
        from_user_id=user_id,
        to_user_id=payload.to_user_id,
        text=payload.text,
    )
    return MessageResponse(
        id=message.id,
        from_user_id=message.from_user_id,
        to_user_id=message.to_user_id,
        text=message.text,
        created_at=message.created_at,
    )
