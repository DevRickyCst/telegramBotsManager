from chalicelib.bots.settings import BotSettingBase, Platform


class TelegramBotSettings(BotSettingBase):
    platform: Platform = Platform.TELEGRAM
    default_chat_id: str
