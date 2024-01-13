from chalicelib.src.gmail import Gmail
from chalicelib.src.message import Message
from chalicelib.src.telegram import TelegramInterface

gmail = Gmail()

handle_command = [
    'sendMail'
]

def handle_message(command: str, msg: Message, telegram: TelegramInterface):
    if command == 'sendMail':
        if msg.user["id"] == 426680033:
            gmail.send_email("hello", msg.input['text'], "dev.creusot.aym@gmail.com")
