import asyncio

from telegram import Bot as TelegramSDKBot

from chalicelib.platforms.base_platform_client import PlatformClient


class TelegramClient(PlatformClient):
    def __init__(self, bot_token: str):
        print(bot_token)
        self._bot = TelegramSDKBot(token=bot_token)

    def send_message(self, chat_id: str, text: str):
        asyncio.run(self._bot.send_message(chat_id=chat_id, text=text))

    def set_message_reaction(self, chat_id: str, message_id: str, reaction: str):
        asyncio.run(self._bot.set_message_reaction(chat_id, int(message_id), reaction))

    def set_webhook(self, url: str) -> str:
        asyncio.run(self._bot.set_webhook(url))
        return "ok"
