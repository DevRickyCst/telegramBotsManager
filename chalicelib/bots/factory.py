from chalicelib.bots.runtime import BotRuntime
from chalicelib.bots.settings import BotSettingBase, Platform
from chalicelib.platforms.telegram.bot import TelegramBot
from chalicelib.utils.secret import get_secret


class BotFactory:
    @staticmethod
    def create(settings: BotSettingBase):
        """
        Create a bot instance for the given settings.
        """
        bot_token = get_secret()

        runtime = BotRuntime(bot_token=bot_token)

        if settings.platform == Platform.TELEGRAM:
            return TelegramBot(settings=settings, runtime=runtime)

        raise ValueError(f"Unsupported platform: {settings.platform}")
