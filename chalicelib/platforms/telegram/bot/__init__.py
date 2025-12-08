from typing import Callable, Dict, List, Optional

from chalicelib.platforms.telegram.client import TelegramClient
from chalicelib.platforms.telegram.models.webhook.message import TelegramTextMessage
from chalicelib.utils.secret import get_secret


class TelegramBot:
    """Base class for all bots, with support for commands and handling messages."""

    def __init__(
        self,
        bot_id: str,
        default_chat_id: str,
        commands: Optional[List[Dict[str, Callable]]] = None,
    ):
        """
        Initialize the bot.

        Args:
            bot_id (str): The ID of the bot.
            commands (Optional[List[Dict[str, Callable]]]): A list of commands with their handlers (optional).
        """
        bot_key = get_secret("telegrams_bots", bot_id)
        self.default_chat_id = default_chat_id
        self.bot_name = bot_id
        self.client = TelegramClient(bot_token=bot_key)

        # If commands are provided, initialize the command dictionary
        if commands:
            self.commands = {cmd["command"]: cmd["handler"] for cmd in commands}
        else:
            self.commands = {}

    def describe_commands(self):
        """Describe available commands for the bot."""
        if self.commands:
            description = "List of Available commands:\n"
            for command in self.commands.keys():
                description += f"- /{command}\n"
        else:
            description = f"Bot {self.bot_name} has no commands available."

        return description

    def handle_message(self, message: TelegramTextMessage):
        """Handle the message based on the command."""
        try:
            command = message.isCommand()
            if command == "help":
                self.client.sendMessage(
                    chat_id=message.chat.id, text=self.describe_commands()
                )
            elif command in self.commands:
                print(
                    self.client.set_message_reaction(
                        message_id=message.message_id,
                        chat_id=message.chat.id,
                        reaction="👀",
                    )
                )
                handler_function = self.commands[command]
                response = handler_function(message)
                self.client.send_message(chat_id=message.chat.id, text=response)
            else:
                raise ValueError("Command not recognized")
        except Exception as e:
            # Handle errors gracefully
            error_message = (
                "Cette commande n'est pas gérée. Tapez /help pour plus d'informations."
                if isinstance(e, ValueError)
                else str(e)
            )
            print(f"Error handling message: {e}")
            self.client.send_message(chat_id=message.chat.id, text=error_message)
