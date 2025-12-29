from abc import ABC, abstractmethod


class PlatformClient(ABC):
    @abstractmethod
    def send_message(self, chat_id: str, text: str) -> None: ...

    @abstractmethod
    def set_webhook(self, url: str) -> str: ...

    @abstractmethod
    def set_message_reaction(
        self, chat_id: str, message_id: str, reaction: str
    ) -> None: ...
