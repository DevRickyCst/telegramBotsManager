import glob
import os

import requests


class WebhookManager:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def set_webhook(self, bot_id: str, bot_token: str):
        """Configure le webhook pour un bot spécifique."""
        url = f"https://api.telegram.org/bot{bot_token}/setWebhook"
        webhook_url = f"{self.base_url}/{bot_id}"
        payload = {"url": webhook_url}

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            print(f"Webhook set for bot: {bot_id} at {webhook_url}")
            return {"status": "success", "bot_id": bot_id}
        except requests.RequestException as e:
            print(f"Failed to set webhook for bot: {bot_id}. Error: {e}")
            return {"status": "error", "bot_id": bot_id, "error": str(e)}

    def set_webhooks_for_all(self, bots_folder: str):
        """Configure les webhooks pour tous les bots présents dans le dossier spécifié."""
        bot_files = glob.glob(os.path.join(bots_folder, "*bot.py"))
        bot_names = [os.path.splitext(os.path.basename(file))[0] for file in bot_files]

        results = []
        for bot_name in bot_names:
            bot_token = os.environ.get(bot_name)
            if not bot_token:
                print(f"No token found for bot: {bot_name}. Skipping...")
                results.append(
                    {"status": "error", "bot_id": bot_name, "error": "Token not found"}
                )
                continue
            result = self.set_webhook(bot_name, bot_token)
            results.append(result)

        return results