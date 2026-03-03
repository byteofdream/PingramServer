from datetime import datetime, timezone
from uuid import uuid4

from app.models.message import Message


class MessageRepository:
    _messages: list[Message] = []

    def create(self, from_user_id: str, to_user_id: str, text: str) -> Message:
        message = Message(
            id=str(uuid4()),
            from_user_id=from_user_id,
            to_user_id=to_user_id,
            text=text,
            created_at=datetime.now(timezone.utc),
        )
        self._messages.append(message)
        return message
