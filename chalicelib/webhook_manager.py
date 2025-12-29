from chalicelib.bots.factory import BotFactory
from chalicelib.bots.runtime import BotRuntime
from chalicelib.bots.settings import BotSettingBase
from chalicelib.platforms.factory import get_platform_adapter


class WebhookManager:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def set_webhook(self, settings: BotSettingBase) -> dict:
        try:
            # Création du runtime pour le bot
            runtime = BotRuntime.from_env()

            # Récupération de l'adapter correct pour la plateforme
            adapter = get_platform_adapter(settings.platform)

            # Création du bot via la factory
            bot = BotFactory.create(settings=settings, runtime=runtime, adapter=adapter)

            # Construction de l'URL de webhook
            webhook_url = (
                f"{self.base_url}/{settings.platform.value}/{settings.bot_name}"
            )

            # Définition du webhook
            bot.set_webhook(webhook_url)

            return {
                "bot": settings.bot_name,
                "platform": settings.platform.value,
                "url": webhook_url,
                "status": "success",
            }
        except Exception as e:
            return {"bot": settings.bot_name, "status": "error", "error": str(e)}

    def set_webhooks_for_all(self) -> list[dict]:
        results = []
        from chalicelib.bots.registry import list_bot_settings

        for settings in list_bot_settings():
            try:
                results.append(self.set_webhook(settings))
            except Exception as e:
                results.append({"bot": settings.bot_name, "error": str(e)})
        return results
