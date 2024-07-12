import os

from chalicelib.bots._botInterface import BotInterface
from chalicelib.src.telegram.message import Message



class Bot(BotInterface):

    class Commands(BotInterface.Commands):
        pass

    def __init__(self):
        bot_id = os.path.splitext(os.path.basename(__file__))[0]
        super().__init__(bot_id)
