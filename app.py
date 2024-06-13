import glob
import os
from importlib import import_module

import requests
from chalice import Chalice

from chalicelib.src.telegram.message import Message

app = Chalice(app_name="telegramBots")


def bot_handler(bot_id: str, message: Message):
    """Check if bot exist,
    import bot
    Ask the bot to process the message
    """
    try:
        # Import Bot
        module_name = import_module(f"chalicelib.bots.{bot_id}")
        # Initialise bot object
        bot = module_name.Bot()

        # Get command
        command = message.input["command"]
        if command == "help":
            bot.describe_commands(chat_id=message.chat["id"])
        # Check if bot handle this command or not
        else:
            bot.handle_message(command, message)

    except ModuleNotFoundError:
        print(f"No handler found for {bot_id}")


# Webhook endpoint (ex: /myfirstbot, for the bot myfirstbot)
@app.route("/{bot_id}", methods=["POST"])
def webhook_index(bot_id):
    # Get params sent by telegram
    params = app.current_request.json_body
    # Create message object
    message = Message(params)

    # If user send a command
    if message.input["isCommand"]:
        print(f"Bot {bot_id} called by {message.user['username']}")
        print(f"with params : {message}")

        bot_handler(bot_id, message)
    else:
        print("No command was sent.")
    # Anyway return ok to telegram bot
    return {"statusCode": 200}


# Specific endpoint to interact with a bot.


@app.route("/{bot_id}/send_message", methods=["POST"])
def send_message(bot_id):
    """Send a message from a bot"""

    params = app.current_request.json_body
    print(f"Resquest made to {bot_id} to path /send_message")

    text = params["texte"]
    chat_id = params["chat_id"]

    # Try to send the message from the bot
    try:
        # Import Bot
        module_name = import_module(f"chalicelib.bots.{bot_id}")
        # Initialise bot object
        bot = module_name.Bot()
        bot.telegram.sendMessage(text, chat_id)
    except ModuleNotFoundError:
        print(f"{bot_id} isn't configured")


@app.route("/", methods=["GET"])
def index():
    return "Hello World"


# Chemin du dossier à explorer
bots_folder = "chalicelib/bots"

# Get a list of all path
list_path = glob.glob(bots_folder + "/*bot.py")
print(list_path)

# Get only the file name
list_bot = [os.path.splitext(os.path.basename(fichier))[0] for fichier in list_path]
print(list_bot)


def setWebhook(extra_url: str, _bot_id: str):
    # Force url since self.url isn't the one used
    url = f"https://api.telegram.org/bot{_bot_id}/setWebhook"
    webhook_url = "https://ia6orftg8f.execute-api.eu-central-1.amazonaws.com/api/"
    payload = {"url": webhook_url + extra_url}
    print(f"Setting Webhook for {_bot_id} to {url}")

    response = requests.get(url, data=payload)
    print(payload)
    return "ok"


@app.route("/set-webhooks", methods=["POST"])
def set_webhooks():
    for bot_name in list_bot:
        setWebhook(bot_name, os.environ[bot_name])
    return {"status": "webhooks set"}
