from chalicelib.bots.settings import Platform
from chalicelib.platforms.base_message import Message


def parse_message(platform: Platform, payload: dict) -> Message:
    if platform == Platform.TELEGRAM:
        from chalicelib.platforms.telegram.parser import parse_telegram_message

        return parse_telegram_message(payload)
    elif platform == Platform.DISCORD:
        from chalicelib.platforms.discord.parser import parse_discord_message

        return parse_discord_message(payload)

    raise ValueError(f"Unsupported platform: {platform}")
