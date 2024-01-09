from chalicelib.src.gpt import Gpt
from chalicelib.src.message import Message
from chalicelib.src.telegram import TelegramInterface

gpt = Gpt(api_key="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")


def handle_message(msg: Message, telegram: TelegramInterface):
    response = gpt.call_image(msg.text)
    telegram.sendImage(response, chat_id=msg.chat["id"])
