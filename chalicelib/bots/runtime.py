from pydantic import BaseModel


class BotRuntime(BaseModel):
    bot_token: str
