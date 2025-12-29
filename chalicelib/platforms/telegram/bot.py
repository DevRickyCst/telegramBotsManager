from chalicelib.bots.base import BotBase
from chalicelib.bots.runtime import BotRuntime
from chalicelib.bots.settings import BotSettingBase
from chalicelib.platforms.base_message import Message
from chalicelib.platforms.telegram.client import TelegramClient


def reaction_hook(message: Message, bot: BotBase):
    if client := bot.client:
        client.set_message_reaction(
            chat_id=message.chat_id, message_id=message.message_id, reaction="👀"
        )


def print_message(message: Message, bot: BotBase):
    print(f"Received message on Telegram: {message.text}")


class TelegramBot(BotBase):
    def __init__(self, settings: BotSettingBase, runtime: BotRuntime):
        client = TelegramClient(runtime.bot_token)
        super().__init__(settings, runtime, client)
        self.pre_hooks.extend([reaction_hook, print_message])
