from chalicelib.bots.commands import CommandRouter
from chalicelib.bots.settings import BotSettingBase, Platform
from chalicelib.platforms.base_message import Message
from chalicelib.platforms.telegram.bot import TelegramBot


def get_price(message: Message) -> None:
    print("BTC : $30,000")


_TELEGRAM_BOTS = {
    "blockchainbot": {
        "type": TelegramBot,
        "default_chat_id": "426680033",
        "router": CommandRouter({"getPrice": get_price}),
    }
}


def load_bot_settings(platform: Platform, bot_name: str) -> BotSettingBase:
    if platform == Platform.TELEGRAM:
        bot_data = _TELEGRAM_BOTS.get(bot_name)
        if not bot_data:
            raise ValueError(f"Unknown Telegram bot: {bot_name}")
        return BotSettingBase(
            platform=platform,
            bot_name=bot_name,
            router=bot_data["router"],  # type: ignore
        )

    raise ValueError(f"Unknown platform: {platform}")
