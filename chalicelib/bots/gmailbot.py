import os

from chalicelib.bots._botInterface import BotInterface
from chalicelib.src.gmail import Gmail
from chalicelib.src.telegram.message import Message

gmail = Gmail()

def send_mail(message: Message):
    try:
        if message.user["id"] == 426680033:
            gmail.send_email(
                "hello", message.input["text"], "dev.creusot.aym@gmail.com"
            )
        return ("Mail sent.")
    except:
        return ("Une erreur est apparu. Le mail n'as pas été envoyer.")

class Bot(BotInterface):

    class Commands(BotInterface.Commands):
        SEND_MAIL = ("sendMail", send_mail)

    def __init__(self):
        bot_id = os.path.splitext(os.path.basename(__file__))[0]
        super().__init__(bot_id)

