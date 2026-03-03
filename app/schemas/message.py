from datetime import datetime

from pydantic import BaseModel, Field


class SendMessageRequest(BaseModel):
    to_user_id: str
    text: str = Field(min_length=1, max_length=4096)


class MessageResponse(BaseModel):
    id: str
    from_user_id: str
    to_user_id: str
    text: str
    created_at: datetime
