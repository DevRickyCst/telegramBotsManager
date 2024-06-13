import os

from enum import Enum

from chalicelib.src.telegram.message import Message
from chalicelib.src.telegram.telegram import TelegramInterface


class BotInterface:

    class Commands(Enum):
        '''Available commands for the bot ex: 
        GET_TOKEN_PRICE = ("getPrice", get_price): commands string and function handling'''

        @classmethod
        def get_command_from_value(cls, command: str) -> 'BotInterface.Commands':
            for _command in cls:
                if command == _command.value[0]:
                    return _command
            raise ValueError("Command not found")

        @classmethod
        def get_commands(cls):
            return [cmd.value[0] for cmd in cls]
        
        
    def __init__(self, bot_id: str):
        """Initialize the BotInterface.

        Args:
            bot_id (str): The ID of the bot.
        """
        bot_key = os.getenv(bot_id)
        self.commands = self.Commands.get_commands()
        self.bot_name = bot_id
        self.telegram = TelegramInterface(bot_key)

    def __str__(self) -> str:
        return(f"Bot : {self.bot_name}")

    def command_checker(fonction):
        def command_handler(self, command, message):
            try: 
                # Get bot command object from user input command
                command_object = self.Commands.get_command_from_value(command)
                # Aply handler to the command
                fonction(self, command_object, message)
            except ValueError as e:
                # 
                not_in_commands_str = "Cette comande n'est pas gérer. Tapez /help pour plus d'information."
                self.telegram.sendMessage(not_in_commands_str, chat_id=message.chat["id"])
            except BaseException as e:
                self.telegram.sendMessage(str(e), chat_id=message.chat["id"])
        return command_handler

    @command_checker
    def handle_message(self, command: Commands, message: Message):
        """Handle the message based on the command.

        Args:
            command (Commands): The command received.
            message (Message): The message object.
        """
        handler_function = command.value[1]
        value = handler_function(message)
        self.telegram.sendMessage(
                value,
                chat_id=message.chat["id"],
            )


    def welcome(self, chat_id: str):
        welcome_message = (f"Welcome to {self.bot_name} !\n"
                          + self.describe_commands(chat_id, False))
        self.telegram.sendMessage(welcome_message, chat_id=chat_id)

    def describe_commands(self, chat_id: str, send: bool = True):
        """Describe the available commands.

        Args:
            chat_id (str): The ID of the chat.
            send (bool, optional): Whether to send the description. Defaults to True.

        Returns:
            str: The description of available commands.
        """
        desciption = "List of Available commands :\n"
        for command in self.commands:
            desciption += f"- /{command}\n"
        if send:
            self.telegram.sendMessage(desciption, chat_id=chat_id)
        else: 
            return desciption
