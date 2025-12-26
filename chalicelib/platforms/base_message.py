from pydantic import BaseModel


class Message(BaseModel):
    text: str | None
    message_id: str
    chat_id: str
    user_id: str
    command: str | None = None
    raw: dict | None = None
