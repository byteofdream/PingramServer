from dataclasses import dataclass


@dataclass
class User:
    id: str
    username: str
    phone: str
    password_hash: str
