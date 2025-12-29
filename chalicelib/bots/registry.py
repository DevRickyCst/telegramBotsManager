from typing import Iterable

from chalicelib.bots.commands import CommandRouter
from chalicelib.bots.settings import BotSettingBase, Platform
from chalicelib.platforms.base_message import Message


def get_price(message: Message) -> str:
    return "BTC : $30,000"


_TELEGRAM_BOTS = {
    "blockchainbot": BotSettingBase(
        platform=Platform.TELEGRAM,
        bot_name="blockchainbot",
        router=CommandRouter({"getPrice": get_price}),
    ),
    "jarvis": BotSettingBase(
        platform=Platform.DISCORD,
        bot_name="jarvis",
        router=CommandRouter({}),
    ),
}


def load_bot_settings(platform: Platform, bot_name: str) -> BotSettingBase:
    if platform == Platform.TELEGRAM:
        bot = _TELEGRAM_BOTS.get(bot_name)
        if not bot:
            raise ValueError(f"Unknown Telegram bot: {bot_name}")
        return bot
    elif platform == Platform.DISCORD:
        bot = _TELEGRAM_BOTS.get(bot_name)
        if not bot:
            raise ValueError(f"Unknown Discord bot: {bot_name}")
        return bot
    raise ValueError(f"Unknown platform: {platform}")


def list_bot_settings(platform: Platform | None = None) -> Iterable[BotSettingBase]:
    if platform in (None, Platform.TELEGRAM):
        return _TELEGRAM_BOTS.values()
    return []
