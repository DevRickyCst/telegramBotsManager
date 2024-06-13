import os

from chalicelib.bots._botInterface import BotInterface
from chalicelib.src.gpt import Gpt
from chalicelib.src.telegram.message import Message

gpt = Gpt()


def call_gpt(message: Message):
    return gpt.call_chat(message.input["text"])


# def call_dalee(message: Message):
#    response = gpt.call_image(message.input["text"])
#    self.telegram.sendImage(response, chat_id=message.chat["id"])


class Bot(BotInterface):

    class Commands(BotInterface.Commands):
        CALL_GPT = ("chatgpt", call_gpt)
        # CALL_DALEE = ("chatgpt", call_dalee)

    def __init__(self):
        bot_id = os.path.splitext(os.path.basename(__file__))[0]
        super().__init__(bot_id)
