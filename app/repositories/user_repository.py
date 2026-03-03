from app.models.user import User


class UserRepository:
    # Demo in-memory users. Replace with PostgreSQL in production.
    _users = {
        "alice": User(id="user-alice", username="alice", phone="+380501112233", password_hash="password123"),
        "bob": User(id="user-bob", username="bob", phone="+380671234567", password_hash="password123"),
    }

    @staticmethod
    def _normalize_phone(phone: str) -> str:
        # Keep only digits so +380..., 380..., and spaced formats match.
        return "".join(ch for ch in phone if ch.isdigit())

    def get_by_username(self, username: str) -> User | None:
        return self._users.get(username)

    def get_by_phone(self, phone: str) -> User | None:
        normalized = self._normalize_phone(phone)
        return next(
            (
                u
                for u in self._users.values()
                if self._normalize_phone(u.phone) == normalized
            ),
            None,
        )

    def get_by_id(self, user_id: str) -> User | None:
        return next((u for u in self._users.values() if u.id == user_id), None)

    def create(self, user: User) -> User:
        self._users[user.username] = user
        return user
