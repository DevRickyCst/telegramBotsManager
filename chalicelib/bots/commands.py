from typing import Callable

from chalicelib.platforms.base_message import Message

Handler = Callable[[Message], None]


class CommandRouter:
    def __init__(self, handlers: dict[str, Handler]):
        self._handlers = handlers

    def get(self, command: str) -> Handler | None:
        return self._handlers.get(command)

    def list_commands(self) -> list[str]:
        return list(self._handlers.keys())

    def describe_commands(self) -> str:
        """Describe available commands for the bot."""
        if self._handlers:
            description = "List of Available commands:\n"
            for cmd in self._handlers.keys():
                description += f"- /{cmd}\n"
        else:
            description = "No commands available."

        return description
