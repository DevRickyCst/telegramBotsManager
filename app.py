from importlib import import_module

from chalice import Chalice, Response

from chalicelib.src.telegram.message import Message

app = Chalice(app_name="telegramBots")


def bot_handler(bot_id, message):
    # Check if bot_id exist
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
            bot.handle_message_command_checker(command, message)

    except ModuleNotFoundError:
        print(f"No handler found for {bot_id}")


@app.route("/{bot_id}", methods=["POST"])
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


@app.route("/{bot_id}/send_message", methods=["POST"])
def send_message(bot_id):
    params = app.current_request.json_body
    print(f'Resquest made to {bot_id} to path /send_message')

    text = params['texte']
    chat_id = params['chat_id']

    try:
        # Import Bot
        module_name = import_module(f"chalicelib.bots.{bot_id}")
        # Initialise bot object
        bot = module_name.Bot()
        bot.telegram.sendMessage(text,chat_id)
    except ModuleNotFoundError:
        print(f"{bot_id} isn't configured")



@app.route("/", methods=["GET"])
def index():
    return 'Hello World'
