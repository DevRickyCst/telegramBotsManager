from enum import Enum

from pydantic import BaseModel

from chalicelib.bots.commands import CommandRouter


class Platform(Enum):
    TELEGRAM = "telegram"


class BotSettingBase(BaseModel):
    platform: Platform
    bot_name: str
    router: CommandRouter

    model_config = {"arbitrary_types_allowed": True}
