from chalicelib.bots.telegram.message import Message
from chalicelib.src.blockchain import BockchainInterface
from chalicelib.src.gmail import Gmail
from chalicelib.src.gpt import Gpt
from chalicelib.src.meteo import obtenir_meteo_ville

# Bot-specific handlers
blockchain = BockchainInterface()
gmail = Gmail()
gpt = Gpt()


def get_price(message: Message):
    try:
        symbolprice = blockchain.getPrice(symbol=message.input["text"])
        return f"{message.input['text'].upper()}/USDT : {symbolprice}"
    except BaseException:
        return "Check the symbol you asked for."


def send_mail(message: Message):
    try:
        if message.user["id"] == 426680033:
            gmail.send_email(
                "hello", message.input["text"], "dev.creusot.aym@gmail.com"
            )
        return "Mail sent."
    except BaseException:
        return "Une erreur est apparu. Le mail n'as pas été envoyé."


def get_meteo(message: Message):
    return obtenir_meteo_ville(message.input["text"])


def call_gpt(message: Message):
    return gpt.call_chat(message.input["text"])
