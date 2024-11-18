

## Installation
1. Create a virtual venv:

     `python3 -m venv venv` (or with pyenv)

2. Install dependencies :

     `pip install -r requirements.txt`.

3. Configure your AWS crendetials in `~/.aws/credentials`

    https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-configure.html 

4. You can now run your webhook application with: 

    `make local`


## Setting a telegram bot


1. Create your Telegram bot(s) and obtain your API tokens.
    
    https://core.telegram.org/bots#how-do-i-create-a-bot
    

2. Set up your Chalice environment variable such as :

          "environment_variables":{
                "myfirstbot": "bot_api_token_1",
                "mysecondbot": "bot_api_token_2"
             }

    https://aws.github.io/chalice/topics/configfile#environment-variables

3. In the folder `chalicelib/bots`, create a python file named as you telegrambot (Ex : myfirstbot.py)

4. Each bot should be implemented as a separate Python module with a class named Bot.

    Such as : 
    ```python 
    def get_meteo(message: Message):
        return obtenir_meteo_ville(message.input["text"])

    COMMANDS = [Command("meteo", get_meteo)]

    class Bot(BotInterface):

        def __init__(self):
            bot_id = os.path.splitext(os.path.basename(__file__))[0]
            super().__init__(bot_id, COMMANDS)
    ```


## Project Structure

```plaintext
telegramBots/
├── app.py                     # Main application file
├── chalicelib/
│   ├── bots/                  # Folder for bot implementations
│   │   └── myfirstbot.py      # Example bot implementation
│   └── src/
│       ├── bot/
│       │   └── _botInterface.py # Bot interface definition
│       ├── telegram/
│       │   ├── message.py     # Message handling classes
│       │   └── telegram.py    # Telegram interaction classes
│       └── gmail.py           # Example additional service
├── requirements.txt           # Project dependencies
└── .chalice/
    └── config.json            # Chalice configuration
```
## License

This project is licensed under the MIT License.

## License
