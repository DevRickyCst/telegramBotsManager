from chalicelib.platforms.telegram.models.webhook.message import (
    TelegramTextMessage,
)
from chalicelib.src.blockchain import BockchainInterface

# Bot-specific handlers
blockchain = BockchainInterface()


def get_price(message: TelegramTextMessage):
    try:
        symbol = message.text.replace("/getPrice", "").strip()
        symbolprice = blockchain.getPrice(symbol=symbol)
        return f"{symbol.upper()}/USDT : {symbolprice}"
    except BaseException:
        return "Check the symbol you asked for."
