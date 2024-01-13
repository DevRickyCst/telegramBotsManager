import os

from chalice import Blueprint

from chalicelib.src.telegram.telegram import TelegramInterface

bot_name = "botsmanager"

app_bots_manager = Blueprint(__name__)


@app_bots_manager.route("/botsmanager/setWebhook", methods=["POST", "GET"])
def set_webhook():
    params = app_bots_manager.current_request.json_body
    extra_url = params["extra_url"]
    bot_id = params["bot_id"]
    bot_key = os.environ[bot_name]
    telegram = TelegramInterface(bot_key)
    telegram.setWebhook(extra_url=extra_url, _bot_id=bot_id)
