import os

from chalicelib.bots._botInterface import BotInterface
from chalicelib.src.meteo import obtenir_meteo_ville
from chalicelib.src.telegram.message import Message

handle_command = ["meteo"]


class Bot(BotInterface):
    def __init__(self):
        commands = ["meteo"]
        bot_id = os.path.splitext(os.path.basename(__file__))[0]

        super().__init__(commands, bot_id)

    def handle_message(self, command: str, message: Message):
        if command == self.commands[0]:
            result = obtenir_meteo_ville(message.input["text"])
            self.telegram.sendMessage(result, message.chat["id"])
