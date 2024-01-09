import os
from importlib import import_module

from chalice import Chalice, Response

from chalicelib.bots.botsmanager.blueprint import app_bots_manager
from chalicelib.src.message import Message
from chalicelib.src.telegram import TelegramInterface

app = Chalice(app_name="telegramBots")
app.register_blueprint(app_bots_manager)


def bot_handler(bot_id, request):
    params = request.json_body
    message = Message(params)
    print(f"Bot {bot_id} called by {message.user['username']}")
    print(f"with params : {params}")

    try:
        module_name = import_module(f"chalicelib.bots.{bot_id}")
        bot_key = os.environ[bot_id]
        telegram = TelegramInterface(bot_key)
        module_name.handle_message(message, telegram)

    except FileNotFoundError:
        print(f"No handler found for {bot_id}")


@app.route("/{bot_id}", methods=["POST", "GET"])
def webhook_index(bot_id):
    bot_handler(bot_id, app.current_request)
    return Response({"ok": True})
