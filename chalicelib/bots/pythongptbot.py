import os

from chalicelib.bots._botInterface import BotInterface
from chalicelib.src.gpt import Gpt
from chalicelib.src.telegram.message import Message

gpt = Gpt()


class Bot(BotInterface):
    def __init__(self):
        commands = ["chatgpt", "dalle"]
        bot_id = os.path.splitext(os.path.basename(__file__))[0]

        super().__init__(commands, bot_id)

    def handle_message(self, command: str, message: Message):
        if command == self.commands[0]:
            response = gpt.call_chat(message.input["text"])
            self.telegram.sendMessage(response, chat_id=message.chat["id"])
        elif command == self.commands[1]:
            response = gpt.call_image(message.input["text"])
            self.telegram.sendImage(response, chat_id=message.chat["id"])
