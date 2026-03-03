from app.models.message import Message
from app.repositories.message_repository import MessageRepository


class MessageService:
    def __init__(self, message_repo: MessageRepository):
        self.message_repo = message_repo

    def send_message(self, from_user_id: str, to_user_id: str, text: str) -> Message:
        return self.message_repo.create(from_user_id=from_user_id, to_user_id=to_user_id, text=text)
