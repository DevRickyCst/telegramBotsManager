from chalicelib.bots.settings import Platform
from chalicelib.platforms.base_message import Message


def parse_message(platform: str, payload: dict) -> Message:
    if platform == Platform.TELEGRAM:
        from chalicelib.platforms.telegram.parser import parse_telegram_message

        return parse_telegram_message(payload)

    raise ValueError(f"Unsupported platform: {platform}")
