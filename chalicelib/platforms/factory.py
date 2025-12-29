# chalicelib/platforms/factory.py
from chalicelib.bots.settings import Platform
from chalicelib.platforms.discord.adapter import DiscordPlatformAdapter
from chalicelib.platforms.telegram.adapter import TelegramPlatformAdapter


def get_platform_adapter(platform: Platform):
    if platform == Platform.TELEGRAM:
        return TelegramPlatformAdapter()
    if platform == Platform.DISCORD:
        return DiscordPlatformAdapter()
    raise ValueError(f"Unsupported platform: {platform}")
