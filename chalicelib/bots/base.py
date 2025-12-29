from abc import ABC
from typing import Callable, List

from chalicelib.bots.runtime import BotRuntime
from chalicelib.bots.settings import BotSettingBase
from chalicelib.platforms.base_message import Message
from chalicelib.platforms.base_platform_client import PlatformClient


class BotBase(ABC):
    def __init__(
        self, settings: BotSettingBase, runtime: BotRuntime, client: PlatformClient
    ) -> None:
        self.settings = settings
        self.runtime = runtime
        self.client = client
        self.pre_hooks: List[Callable[[Message, "BotBase"], None]] = []
        self.post_hooks: List[Callable[[Message, "BotBase"], None]] = []

    @property
    def bot_name(self):
        return self.settings.bot_name

    def handle_message(self, message: Message):
        # Exécuter tous les pre-hooks
        if pre_hooks := self.pre_hooks:
            for hook in pre_hooks:
                hook(message, self)

        # Dispatch de la commande
        if command := message.command:
            if command == "help":
                response = self.send_help(message)
                return response

            print(f"Handling command: {command}")
            handler = self.settings.router.get(command)
            if handler:
                response = handler(message)
                self.send_message(chat_id=message.chat_id, text=response)
            else:
                response = self.on_unknown_command(message)

        # Exécuter tous les post-hooks
        try:
            for hook in self.post_hooks:
                hook(message, self)
        except Exception as e:
            print(f"Error in post_hooks: {e}")
            self.on_error(message, e)

        return None

    def send_message(self, chat_id: str, text: str) -> None:
        """Send a message via the bot's platform."""
        return self.client.send_message(chat_id, text)

    def set_webhook(self, url: str) -> str:
        """Set the webhook URL for the bot's platform."""
        return self.client.set_webhook(url)

    def send_help(self, message: Message):
        self.client.send_message(
            chat_id=message.chat_id,
            text=self.settings.router.describe_commands(),
        )

    def on_unknown_command(self, message: Message):
        self.client.send_message(
            chat_id=message.chat_id,
            text="Commande inconnue. Tape /help",
        )

    def on_error(self, message: Message, error: Exception):
        print(f"Telegram error: {error}")
        self.client.send_message(
            chat_id=message.chat_id,
            text="Une erreur est survenue.",
        )
