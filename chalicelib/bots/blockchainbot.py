from chalicelib.src.blockchain import BockchainInterface
from chalicelib.src.message import Message
from chalicelib.src.telegram import TelegramInterface

blockchain = BockchainInterface()

handle_command = ["getPrice"]


def handle_message(command: str, msg: Message, telegram: TelegramInterface):
    if command == handle_command[0]:
        symbolprice = blockchain.getPrice(symbol=msg.input["text"])
        print(symbolprice)
        telegram.sendMessage(
            f"{msg.input['text'].upper()}/USDT : {symbolprice}", chat_id=msg.chat["id"]
        )
