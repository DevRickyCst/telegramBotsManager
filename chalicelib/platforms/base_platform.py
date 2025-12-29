# chalicelib/platforms/base_platform.py
from abc import ABC, abstractmethod
from typing import Optional

from chalice.app import Request

from chalicelib.bots.runtime import BotRuntime
from chalicelib.platforms.base_message import Message
from chalicelib.platforms.base_platform_client import PlatformClient


class PlatformAdapter(ABC):
    @abstractmethod
    def verify_request(self, request: Request) -> None:
        """
        Lève une exception si la requête n'est pas valide
        """

    @abstractmethod
    def early_response(self, request: Request) -> Optional[dict]:
        """
        Permet de répondre immédiatement (ex: Discord PING)
        Retourne None si on continue le flow normal
        """

    @abstractmethod
    def parse_message(self, request: Request) -> Message:
        """
        Transforme la requête HTTP en Message interne
        """

    @abstractmethod
    def create_client(self, runtime: BotRuntime) -> PlatformClient:
        """
        Crée le client de la plateforme (TelegramClient, DiscordClient, ...)
        """
