from chalicelib.src.message import Message
from chalicelib.src.meteo import obtenir_meteo_ville
from chalicelib.src.telegram import TelegramInterface

handle_command = [
    'meteo'
]

def handle_message(command: str, msg: Message, telegram: TelegramInterface):
    if command == 'meteo':
        result = obtenir_meteo_ville(msg.input['text'])
        telegram.sendMessage(result, msg.chat["id"])
