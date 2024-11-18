from typing import Optional

from chalicelib.bots.bot import AdvancedBot, BaseBot
from chalicelib.src.blockchain import BockchainInterface
from chalicelib.src.gmail import Gmail
from chalicelib.src.gpt import Gpt
from chalicelib.src.meteo import obtenir_meteo_ville
from chalicelib.src.telegram.message import Message

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
    except:
        return "Une erreur est apparu. Le mail n'as pas été envoyé."


def get_meteo(message: Message):
    return obtenir_meteo_ville(message.input["text"])


def call_gpt(message: Message):
    return gpt.call_chat(message.input["text"])


# Bot Configuration
BOT_CONFIG = {
    "blockchainbot": {
        "type": AdvancedBot,
        "commands": [
            {"command": "getPrice", "handler": get_price},
        ],
    },
    "gmailbot": {
        "type": AdvancedBot,
        "commands": [
            {"command": "sendMail", "handler": send_mail},
        ],
    },
    "meteobot": {
        "type": AdvancedBot,
        "commands": [
            {"command": "meteo", "handler": get_meteo},
        ],
    },
    "pythongptbot": {
        "type": AdvancedBot,
        "commands": [
            {"command": "chatgpt", "handler": call_gpt},
        ],
    },
    "airflowrickybot": {
        "type": BaseBot,
        "commands": [],
    },
    "alertewaterbot": {
        "type": BaseBot,
        "commands": [],
    },
}


def get_bot(bot_id: str) -> Optional[BaseBot]:
    """
    Retourne une instance de bot configurée en fonction de l'identifiant fourni.

    :param bot_id: L'identifiant du bot à initialiser.
    :return: Une instance de BaseBot ou None si une erreur se produit.
    """
    try:
        bot_config = BOT_CONFIG.get(bot_id)
        if not bot_config:
            raise ValueError(f"No configuration found for bot_id: {bot_id}")

        bot_type = bot_config["type"]
        commands = bot_config.get("commands", [])

        # Créer l'instance du bot avec ses commandes
        bot_instance: BaseBot = bot_type(bot_id=bot_id, commands=commands)
        return bot_instance

    except Exception as e:
        # Journalisation en cas d'erreur (remplacer par un logger en production)
        print(f"Error while initializing bot {bot_id}: {e}")
        return None
