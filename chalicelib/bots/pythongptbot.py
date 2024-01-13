import os

from chalicelib.src.gpt import Gpt
from chalicelib.src.message import Message
from chalicelib.src.telegram import TelegramInterface

gpt = Gpt()

handle_command = ["chatgpt", "dalle"]


def handle_message(command: str, msg: Message, telegram: TelegramInterface):
    if command == handle_command[0]:
        response = gpt.call_chat(msg.input["text"])
        telegram.sendMessage(response, chat_id=msg.chat["id"])
    elif command == handle_command[1]:
        response = gpt.call_image(msg.input["text"])
        telegram.sendImage(response, chat_id=msg.chat["id"])
