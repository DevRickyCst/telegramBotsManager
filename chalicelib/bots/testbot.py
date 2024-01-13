from chalicelib.src.message import Message
from chalicelib.src.telegram import TelegramInterface

handle_command = [
    'test',
    'test2'
]

def handle_message(msg: Message, telegram: TelegramInterface):
    #telegram.sendMessage(msg.text, msg.chat["id"])
    print('ok')
    return 0
