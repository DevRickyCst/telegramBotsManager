from chalicelib.src.message import Message
from chalicelib.src.meteo import obtenir_meteo_ville
from chalicelib.src.telegram import TelegramInterface


def handle_message(msg: Message, telegram: TelegramInterface):
    result = obtenir_meteo_ville(msg.text)
    telegram.sendMessage(result, msg.chat["id"])
