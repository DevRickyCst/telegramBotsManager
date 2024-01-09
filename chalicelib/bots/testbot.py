from chalicelib.src.message import Message
from chalicelib.src.telegram import TelegramInterface


def handle_message(msg: Message, telegram: TelegramInterface):
    telegram.sendMessage(msg.text, msg.chat["id"])
