from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    id: str
    from_user_id: str
    to_user_id: str
    text: str
    created_at: datetime
