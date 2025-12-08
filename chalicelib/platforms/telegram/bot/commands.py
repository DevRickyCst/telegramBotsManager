from chalicelib.platforms.telegram.models.webhook.message import (
    TelegramTextMessage,
)
from chalicelib.src.blockchain import BlockchainInterface

# Bot-specific handlers
blockchain = BlockchainInterface()


def get_price(message: TelegramTextMessage):
    try:
        symbol = message.text.replace("/getPrice", "").strip()
        symbolprice = blockchain.getPrice(symbol=symbol)
        return f"{symbol.upper()}/USDT : {symbolprice}"
    except Exception:
        return "Check the symbol you asked for."
