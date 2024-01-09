from chalicelib.src.gmail import Gmail
from chalicelib.src.message import Message
from chalicelib.src.telegram import TelegramInterface

gmail = Gmail()


def handle_message(msg: Message, telegram: TelegramInterface):
    if msg.user["id"] == 426680033:
        gmail.send_email("hello", msg.text, "dev.creusot.aym@gmail.com")
