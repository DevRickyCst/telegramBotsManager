from chalicelib.bots.base import BotBase
from chalicelib.bots.runtime import BotRuntime
from chalicelib.bots.settings import BotSettingBase
from chalicelib.platforms.base_message import Message
from chalicelib.platforms.discord.client import DiscordClient


def print_message(message: Message, bot: BotBase):
    print(f"Received message on Discord: {message.text}")


class DiscordBot(BotBase):
    def __init__(self, settings: BotSettingBase, runtime: BotRuntime):
        client = DiscordClient(runtime.bot_token)
        super().__init__(settings, runtime, client)
        self.pre_hooks.extend([print_message])
