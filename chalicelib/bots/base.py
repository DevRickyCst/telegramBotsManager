from abc import ABC, abstractmethod
from typing import Callable, List

from chalicelib.bots.runtime import BotRuntime
from chalicelib.bots.settings import BotSettingBase
from chalicelib.platforms.base_message import Message


class BotBase(ABC):
    def __init__(
        self, settings: BotSettingBase, runtime: BotRuntime, client=None
    ) -> None:
        self.settings = settings
        self.runtime = runtime
        self.pre_hooks: List[Callable[[Message, "BotBase"], None]] = []
        self.post_hooks: List[Callable[[Message, "BotBase"], None]] = []
        self.client = client

    @property
    def platform(self):
        return self.settings.platform

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
            print(f"Handling command: {command}")
            handler = self.settings.router.get(command)
            if handler:
                response = handler(message)
            else:
                response = self.default_handler(message)
        else:
            response = self.default_handler(message)
        # Exécuter tous les post-hooks
        try:
            for hook in self.post_hooks:
                hook(message, self)
        except Exception as e:
            print(f"Error in post_hooks: {e}")

        return response

    @abstractmethod
    def default_handler(self, message: Message) -> None:
        """
        Called when no command matches.
        Platform-specific behavior.
        """
        raise NotImplementedError
