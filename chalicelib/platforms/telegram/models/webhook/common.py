from pydantic import BaseModel


class TelegramUser(BaseModel):
    """Telegram user model."""

    id: int
    is_bot: bool
    first_name: str
    username: str | None = None
    language_code: str | None = None


class TelegramChat(BaseModel):
    """Telegram chat model."""

    id: int
    type: str
    title: str | None = None
    username: str | None = None


class TelegramImage(BaseModel):
    """Telegram image model."""

    file_id: str
    file_unique_id: str
    file_size: int
    width: int
    height: int


class TelegramVideo(BaseModel):
    """Telegram video model."""

    duration: int
    width: int
    height: int
    file_name: str
    mime_type: str
    file_id: str
    file_unique_id: str
    file_size: int
    thumbnail: dict | None = None
    thumb: dict | None = None
