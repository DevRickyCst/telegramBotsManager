import os

from chalicelib.bots._botInterface import BotInterface
from chalicelib.src.meteo import obtenir_meteo_ville
from chalicelib.src.telegram.message import Message


def get_meteo(message: Message):
    return obtenir_meteo_ville(message.input["text"])


class Bot(BotInterface):

    class Commands(BotInterface.Commands):
        SEND_MAIL = ("meteo", get_meteo)

    def __init__(self):
        print(os.path.splitext(os.path.basename(__file__))[0])
        bot_id = os.path.splitext(os.path.basename(__file__))[0]
        super().__init__(bot_id)
