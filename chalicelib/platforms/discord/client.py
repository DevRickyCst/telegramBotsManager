from chalicelib.platforms.base_platform_client import PlatformClient


class DiscordClient(PlatformClient):
    def __init__(self, bot_token: str):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}"

    def send_message(self, chat_id: str, text: str):
        # Implementation for sending a message via Discord API
        pass

    def set_webhook(self, url: str) -> str:
        # Implementation for setting a webhook via Discord API
        return "ok"

    def set_message_reaction(self, chat_id: str, message_id: str, reaction: str):
        # Implementation for setting a message reaction via Discord API
        pass
