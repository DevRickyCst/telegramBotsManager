import os

from chalicelib.src.telegram.message import Message
from chalicelib.src.telegram.telegram import TelegramInterface


class BotInterface:
    def __init__(self, commands: list, bot_id: str):
        bot_key = os.getenv(bot_id)
        self.bot_name = bot_id
        self.commands = commands
        self.telegram = TelegramInterface(bot_key)

    def handle_message(self, command: str, message: Message):
        pass

    def describe_commands(self, chat_id: str):
        desciption = (
            f"Welcome to {self.bot_name} !\n" + "List of Available commands :\n"
        )
        for command in self.commands:
            desciption += f"- /{command}\n"
        self.telegram.sendMessage(desciption, chat_id=chat_id)
