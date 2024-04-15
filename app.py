from importlib import import_module

from chalice import Chalice

from chalicelib.src.telegram.message import Message

app = Chalice(app_name="telegramBots")


def bot_handler(bot_id: str, message: Message):
    ''' Check if bot exist, 
        import bot
        Ask the bot to process the message    
    '''
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
    return {'statusCode': 200}



# Specific endpoint to interact with a bot.

@app.route("/{bot_id}/send_message", methods=["POST"])
def send_message(bot_id):
    '''Send a message from a bot'''

    params = app.current_request.json_body
    print(f'Resquest made to {bot_id} to path /send_message')

    text = params['texte']
    chat_id = params['chat_id']

    # Try to send the message from the bot
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
