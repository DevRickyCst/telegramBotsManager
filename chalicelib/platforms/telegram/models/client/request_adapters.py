from pydantic import BaseModel


class SendMessageRequest(BaseModel):
    chat_id: int
    text: str


class SetMessageReactionRequest(BaseModel):
    message_id: int
    chat_id: int
    reaction: list
