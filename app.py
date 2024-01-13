import os
from importlib import import_module

from chalice import Chalice, Response

from chalicelib.bots.botsmanager.blueprint import app_bots_manager
from chalicelib.src.message import Message
from chalicelib.src.telegram import TelegramInterface

app = Chalice(app_name="telegramBots")
app.register_blueprint(app_bots_manager)


def bot_handler(bot_id, message):
    # Check if bot_id exist
    try:
        # Import Bot
        module_name = import_module(f"chalicelib.bots.{bot_id}")
        # Initialise telegram bot object
        bot_key = os.environ[bot_id]
        telegram = TelegramInterface(bot_key)
        # Get command
        command = message.input["command"]
        # Check if bot handle this command or not
        if command in module_name.handle_command:
            try:
                module_name.handle_message(command, message, telegram)
            except:
                telegram.sendMessage(
                    f"Fail to execute command {command}", message.chat["id"]
                )
        else:
            telegram.sendMessage(
                f"No handler found for command /{command}\nAvailable commands are {module_name.handle_command}",
                message.chat["id"],
            )

    except FileNotFoundError:
        print(f"No handler found for {bot_id}")


@app.route("/{bot_id}", methods=["POST", "GET"])
def webhook_index(bot_id):
    # Get input params
    params = app.current_request.json_body
    message = Message(params)

    # If user send a command
    if message.input["isCommand"]:
        print(f"Bot {bot_id} called by {message.user['username']}")
        print(f"with params : {message}")

        bot_handler(bot_id, message)

    return Response({"ok": True})
