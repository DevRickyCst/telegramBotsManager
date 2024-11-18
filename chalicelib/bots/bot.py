import os
from typing import Callable, Dict, List

from chalicelib.src.telegram.message import Message
from chalicelib.src.telegram.telegram import TelegramInterface


class BaseBot:
    """Base class for all bots."""

    def __init__(self, bot_id: str):
        bot_key = os.getenv(bot_id)
        self.bot_name = bot_id
        self.telegram = TelegramInterface(bot_key)

    def welcome(self, chat_id: str):
        """Send a welcome message."""
        welcome_message = f"Welcome to {self.bot_name}!"
        self.telegram.sendMessage(welcome_message, chat_id=chat_id)

    def describe_commands(self, chat_id: str):
        """Describe available commands for the bot."""
        desc = f"Bot {self.bot_name} has no commands available."
        self.telegram.sendMessage(desc, chat_id=chat_id)


class AdvancedBot(BaseBot):
    """Advanced bot supporting commands."""

    def __init__(self, bot_id: str, commands: List[Dict[str, Callable]]):
        """
        Initialize the bot with commands.

        Args:
            bot_id (str): The ID of the bot.
            commands (List[Dict[str, Callable]]): List of commands with their handlers.
        """
        super().__init__(bot_id)
        self.commands = {cmd["command"]: cmd["handler"] for cmd in commands}

    def describe_commands(self, chat_id: str, send: bool = True):
        """Describe the available commands."""
        description = "List of Available commands:\n"
        for command in self.commands.keys():
            description += f"- /{command}\n"
        if send:
            self.telegram.sendMessage(description, chat_id=chat_id)
        else:
            return description

    def handle_message(self, message: Message):
        """Handle the message based on the command."""
        try:
            # Find and execute the corresponding command handler
            print(message.input["command"])
            command = message.input["command"]
            if command in list(self.commands.keys()):
                print("ok")
                handler_function = self.commands[command]
                response = handler_function(message)
                self.telegram.sendMessage(response, chat_id=message.chat["id"])
            else:
                raise ValueError("Command not recognized")
        except Exception as e:
            # Handle errors gracefully
            error_message = (
                "Cette commande n'est pas gérée. Tapez /help pour plus d'informations."
                if isinstance(e, ValueError)
                else str(e)
            )
            self.telegram.sendMessage(error_message, chat_id=message.chat["id"])
