from chalicelib.src.telegram.message import Message
from chalicelib.src.telegram.telegram import TelegramInterface
import os
from chalicelib.bots._botInterface import BotInterface


class Bot(BotInterface):
    def __init__(self):
        commands = ["test", "test2"]
        bot_id = os.path.splitext(os.path.basename(__file__))[0]

        super().__init__(commands, bot_id)

    def handle_message(self, command: str, message: Message):
        print(command)
        print("ok")
        return 0
