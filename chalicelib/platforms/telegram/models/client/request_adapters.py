from pydantic import BaseModel


class ReactionItem(BaseModel):
    type: str
    emoji: str


class SendMessageRequest(BaseModel):
    chat_id: int
    text: str


class SetMessageReactionRequest(BaseModel):
    message_id: int
    chat_id: int
    reaction: list[ReactionItem]
