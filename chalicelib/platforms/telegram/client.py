import requests

from chalicelib.platforms.telegram.models.client.request_adapters import (
    ReactionItem,
    SendMessageRequest,
    SetMessageReactionRequest,
)


class TelegramClient:
    def __init__(self, bot_token: str):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}"

    def send_message(self, chat_id: str, text: str):
        request_params = SendMessageRequest(chat_id=chat_id, text=text)
        url = f"{self.base_url}/sendMessage"
        response = requests.post(url, json=request_params.model_dump())
        return response.json()

    def set_message_reaction(self, message_id: str, chat_id: str, reaction: str):
        url = f"{self.base_url}/setMessageReaction"

        reaction_item = ReactionItem(type="emoji", emoji=reaction)

        request_params = SetMessageReactionRequest(
            message_id=message_id,
            chat_id=chat_id,
            reaction=[reaction_item],
        )
        response = requests.post(url, json=request_params.model_dump())
        print(f"Set reaction response: {response.text}")
        return response.json()
