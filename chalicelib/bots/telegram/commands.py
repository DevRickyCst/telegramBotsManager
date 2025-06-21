from chalicelib.bots.telegram.message import Message
from chalicelib.src.blockchain import BockchainInterface


# Bot-specific handlers
blockchain = BockchainInterface()


def get_price(message: Message):
    try:
        symbolprice = blockchain.getPrice(symbol=message.input["text"])
        return f"{message.input['text'].upper()}/USDT : {symbolprice}"
    except BaseException:
        return "Check the symbol you asked for."
