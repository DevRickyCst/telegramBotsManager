from chalicelib.src.blockchain import BockchainInterface
from chalicelib.src.message import Message
from chalicelib.src.telegram import TelegramInterface

blockchain = BockchainInterface()


def handle_message(msg: Message, telegram: TelegramInterface):
    try:
        symbolprice = blockchain.getPrice(symbol=msg.text)
        telegram.sendMessage(
            f"{msg.text.upper()}/USDT : {symbolprice}", chat_id=msg.chat["id"]
        )

    except:
        telegram.sendMessage(
            f"Impossible de récupérer la valeure de la device {msg.text}",
            chat_id=msg.chat["id"],
        )
