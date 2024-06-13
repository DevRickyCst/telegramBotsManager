import requests


class TelegramInterface:
    def __init__(self, bot_id=None):
        self.url = f"https://api.telegram.org/bot{bot_id}"

    def sendMessage(self, text: str, chat_id: str):
        extra_url = "/sendMessage"
        payload = {"chat_id": chat_id, "text": text}
        print(self.url + extra_url)
        return requests.post(self.url + extra_url, data=payload)

    def sendImage(self, text: str, chat_id: str):
        extra_url = "/sendPhoto"
        payload = {
            "chat_id": chat_id,
            "photo": text,
        }
        print(self.url + extra_url)
        return requests.post(self.url + extra_url, data=payload)

    def setWebhook(self, extra_url: str, _bot_id: str):
        # Force url since self.url isnt the one used
        url = f"https://api.telegram.org/bot{_bot_id}/setWebhook"
        webhook_url = "https://ia6orftg8f.execute-api.eu-central-1.amazonaws.com/api/"

        payload = {"url": webhook_url + extra_url}
        print(f"Seting Webhook for {_bot_id} to {url}")

        response = requests.get(url, data=payload)

        print(response)

        return "ok"
