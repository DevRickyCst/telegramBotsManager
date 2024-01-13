import os

from chalicelib.bots._botInterface import BotInterface
from chalicelib.src.blockchain import BockchainInterface
from chalicelib.src.telegram.message import Message
from chalicelib.src.telegram.telegram import TelegramInterface

blockchain = BockchainInterface()


class Bot(BotInterface):
    def __init__(self):
        commands = ["getPrice"]
        bot_id = os.path.splitext(os.path.basename(__file__))[0]

        super().__init__(commands, bot_id)

    def handle_message(self, command: str, message: Message):
        if command == self.commands[0]:
            symbolprice = blockchain.getPrice(symbol=message.input["text"])
            self.telegram.sendMessage(
                f"{message.input['text'].upper()}/USDT : {symbolprice}",
                chat_id=msg.chat["id"],
            )
