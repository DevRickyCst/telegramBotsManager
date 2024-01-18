import os

from chalicelib.src.telegram.message import Message
from chalicelib.src.telegram.telegram import TelegramInterface


class BotInterface:
    def __init__(self, commands: list, bot_id: str):
        bot_key = os.getenv(bot_id)
        self.bot_name = bot_id
        self.commands = commands
        self.telegram = TelegramInterface(bot_key)

    def __str__(self) -> str:
        print(f"Bot : {self.bot_name}")

    def handle_message_command_checker(self, command: str, message: Message):
        if command not in self.commands:
            not_in_commands_str = "Cette comande n'est pas gérer. Tapez /help pour plus d'information."
            self.telegram.sendMessage(not_in_commands_str, chat_id=message.chat["id"])
        else:
            try:
                self.handle_message(command, message)
            except Exception as e:
                self.telegram.sendMessage(e, chat_id=message.chat["id"])


    def handle_message(self, command: str, message: Message):
        pass

    def welcome(self, chat_id: str):
        welcom_message = (f"Welcome to {self.bot_name} !\n"
                          + self._describe_commands(chat_id, False))
        self.telegram.sendMessage(welcom_message, chat_id=chat_id)

    def describe_commands(self, chat_id: str, send: bool = True):
        desciption = "List of Available commands :\n"
        for command in self.commands:
            desciption += f"- /{command}\n"
        if send:
            self.telegram.sendMessage(desciption, chat_id=chat_id)
        else: 
            return desciption
