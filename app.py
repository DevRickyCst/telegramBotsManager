from chalice import Chalice, Cron

from chalicelib.bots.telegram import get_bot
from chalicelib.bots.telegram.message import Message
from chalicelib.schedules.task import send_scheduled_message
from chalicelib.utils.webhook_manager import WebhookManager

app = Chalice(app_name="telegramBots")


webhook_manager = WebhookManager(
    "https://6sm86mr5n3.execute-api.eu-central-1.amazonaws.com/api/"
)


@app.route("/{bot_id}", methods=["POST"])
def webhook_index(bot_id):
    """Handle the webhook call from Telegram for a specific bot."""
    # Get params sent by Telegram
    params = app.current_request.json_body
    # Create message object
    message = Message(params)

    # If the user sends a command
    if message.input["isCommand"]:
        print(f"Bot {bot_id} called by {message.user['username']}")
        print(f"with params: {message}")

        bot = get_bot(bot_id=bot_id)

        bot.handle_message(message)
    else:
        print("No command was sent.")
    # Always return ok to Telegram bot
    return {"statusCode": 200}


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


# Define a function for each scheduled task
@app.schedule(
    Cron(1, "10,14", "*", "*", "?", "*")
)  # Every 2 hours between 8 AM and 4 PM
def alertewaterbot_schedule(event):
    send_scheduled_message(
        bot_id="alertewaterbot",
        text="C'est l'heure de boire de l'eau !",
    )
