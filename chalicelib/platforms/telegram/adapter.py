# chalicelib/platforms/telegram/adapter.py
from chalice.app import Request

from chalicelib.bots.runtime import BotRuntime
from chalicelib.platforms.base_message import Message
from chalicelib.platforms.base_platform import PlatformAdapter
from chalicelib.platforms.telegram.client import TelegramClient
from chalicelib.platforms.telegram.parser import parse_telegram_message


class TelegramPlatformAdapter(PlatformAdapter):
    def verify_request(self, request: Request) -> None:
        # Telegram n’a pas de signature obligatoire
        return None

    def early_response(self, request: Request) -> None:
        return None

    def parse_message(self, request: Request) -> Message:
        return parse_telegram_message(request.json_body)

    def create_client(self, runtime: BotRuntime) -> TelegramClient:
        return TelegramClient(runtime.bot_token)
