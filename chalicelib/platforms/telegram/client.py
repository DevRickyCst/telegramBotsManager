import requests

from chalicelib.platforms.telegram.models.client.request_adapters import (
    SendMessageRequest,
    SetMessageReactionRequest,
)


class TelegramClient:
    def __init__(self, bot_token: str):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}"

    def send_message(self, chat_id: int, text: str):
        request_params = SendMessageRequest(chat_id=chat_id, text=text)
        url = f"{self.base_url}/sendMessage"
        response = requests.post(url, json=request_params.model_dump())
        return response.json()

    def set_message_reaction(self, message_id: int, chat_id: int, reaction: str):
        url = f"{self.base_url}/setMessageReaction"
        request_params = SetMessageReactionRequest(
            message_id=message_id,
            chat_id=chat_id,
            reaction=[{"type": "emoji", "emoji": reaction}],
        )
        response = requests.post(url, json=request_params.model_dump())
        return response.json()
