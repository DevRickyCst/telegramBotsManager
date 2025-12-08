from chalice import Chalice

from chalicelib.platforms.telegram.bot.bots import get_bot
from chalicelib.platforms.telegram.models.webhook.message import (
    TelegramImageMessage,
    TelegramRaw,
    TelegramTextMessage,
    TelegramVideoMessage,
)
from chalicelib.utils.webhook_manager import WebhookManager

app = Chalice(app_name="telegramBots")


webhook_manager = WebhookManager(
    "https://hip-onagraceous-arianna.ngrok-free.dev/"
    # "https://6sm86mr5n3.execute-api.eu-central-1.amazonaws.com/api/"
)


@app.route("/{bot_id}", methods=["POST"])
def webhook_index(bot_id):
    """Handle the webhook call from Telegram for a specific bot."""
    print(f"Request made to {bot_id} to path /{bot_id}")
    params = app.current_request.json_body
    bot = get_bot(bot_id)
    print(params)
    try:
        update = TelegramRaw.model_validate(params)
    except Exception as e:
        app.log.error(f"Invalid Telegram payload: {e}")
        return {"ok": True}
    print(update)
    message = update.message

    if isinstance(message, TelegramTextMessage):
        bot.handle_message(message)
    elif isinstance(message, TelegramImageMessage):
        print("image")
    elif isinstance(message, TelegramVideoMessage):
        print("video")
    return {"ok": True}


@app.route("/{bot_id}/send_message", methods=["POST"])
def send_message(bot_id):
    """Send a message from a bot to a specific chat."""
    params = app.current_request.json_body
    print(f"Request made to {bot_id} to path /send_message")

    text = params["texte"]
    chat_id = params["chat_id"]

    bot = get_bot(bot_id=bot_id)

    bot.telegram.sendMessage(text=text, chat_id=chat_id)


@app.route("/", methods=["GET"])
def index():
    return "Hello World"


@app.route("/set-webhooks", methods=["POST"])
def set_webhooks():
    """Configure webhooks for all bots."""
    results = webhook_manager.set_webhooks_for_all()
    return {"status": "Webhooks configured", "results": results}


# @app.schedule(
#    Cron(1, "10,14", "*", "*", "?", "*")
# )  # Every 2 hours between 8 AM and 4 PM
# def alertewaterbot_schedule(event):
#    send_scheduled_message(
#        bot_id="alertewaterbot",
#        text="ok",
#    )
