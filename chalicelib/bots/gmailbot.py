import os

from chalicelib.bots._botInterface import BotInterface
from chalicelib.src.gmail import Gmail
from chalicelib.src.telegram.message import Message

gmail = Gmail()


class Bot(BotInterface):
    def __init__(self):
        commands = ["sendMail"]
        bot_id = os.path.splitext(os.path.basename(__file__))[0]

        super().__init__(commands, bot_id)

    def handle_message(self, command: str, message: Message):
        if command == self.commands[0]:
            if message.user["id"] == 426680033:
                gmail.send_email(
                    "hello", message.input["text"], "dev.creusot.aym@gmail.com"
                )
