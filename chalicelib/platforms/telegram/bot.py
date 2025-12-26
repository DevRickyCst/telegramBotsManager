from chalicelib.bots.base import BotBase
from chalicelib.bots.runtime import BotRuntime
from chalicelib.bots.settings import BotSettingBase
from chalicelib.platforms.base_message import Message
from chalicelib.platforms.telegram.client import TelegramClient


def reaction_hook(message: Message, bot: "BotBase"):
    if client := bot.client:
        client.set_message_reaction(
            chat_id=message.chat_id, message_id=message.message_id, reaction="👀"
        )


def print_message(message: Message, bot: "BotBase"):
    print(f"Received message on Telegram: {message.text}")


class TelegramBot(BotBase):
    def __init__(self, settings: BotSettingBase, runtime: BotRuntime):
        super().__init__(settings, runtime)
        self.client = TelegramClient(runtime.bot_token)
        self.pre_hooks.extend([reaction_hook, print_message])

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

    def default_handler(self, message: Message) -> None:
        self.client.send_message(
            chat_id=message.chat_id,
            text="Cette commande n'est pas reconnue. Tapez /help pour la liste des commandes.",
        )
