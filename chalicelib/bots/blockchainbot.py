import os

from chalicelib.bots._botInterface import BotInterface
from chalicelib.src.blockchain import BockchainInterface
from chalicelib.src.telegram.message import Message
blockchain = BockchainInterface()


def get_price(message: Message):
    try:
        symbolprice = blockchain.getPrice(symbol=message.input["text"])
        return (f"{message.input['text'].upper()}/USDT : {symbolprice}")
    except BaseException as e:
        return(f"Check the symbol you asked for.")
    
class Bot(BotInterface):

    class Commands(BotInterface.Commands):
        GET_TOKEN_PRICE = ("getPrice", get_price)
        GET_TOKEN_PRICE2 = ("getPrice2", get_price)

    def __init__(self):
        bot_id = os.path.splitext(os.path.basename(__file__))[0]
        super().__init__(bot_id)

