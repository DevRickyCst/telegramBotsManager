from pydantic import BaseModel


class SendMessageRequest(BaseModel):
    chat_id: str
    text: str


class ReactionItem(BaseModel):
    type: str
    emoji: str


class SetMessageReactionRequest(BaseModel):
    message_id: str
    chat_id: str
    reaction: list[ReactionItem]
