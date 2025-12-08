from typing import Optional

from chalicelib.platforms.telegram.bot import TelegramBot
from chalicelib.platforms.telegram.bot.commands import get_price

# Bot Configuration
BOT_CONFIG = {
    "blockchainbot": {
        "type": TelegramBot,
        "default_chat_id": "426680033",
        "commands": [
            {"command": "getPrice", "handler": get_price},
        ],
    },
    "gmailbot": {
        "type": TelegramBot,
        "default_chat_id": "426680033",
        "commands": [
            # {"command": "sendMail", "handler": send_mail},
        ],
    },
    "meteobot": {
        "type": TelegramBot,
        "default_chat_id": "426680033",
        "commands": [
            # {"command": "meteo", "handler": get_meteo},
        ],
    },
    "pythongptbot": {
        "type": TelegramBot,
        "default_chat_id": "426680033",
        "commands": [
            # {"command": "chatgpt", "handler": call_gpt},
        ],
    },
    "airflowrickybot": {
        "type": TelegramBot,
        "default_chat_id": "426680033",
    },
    "alertewaterbot": {
        "type": TelegramBot,
        "default_chat_id": "646579882",
    },
}


def get_bot(bot_id: str) -> Optional[TelegramBot]:
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
        commands = bot_config.get("commands", None)
        default_chat_id = bot_config.get("default_chat_id", None)

        # Créer l'instance du bot avec ses commandes
        bot_instance: TelegramBot = bot_type(
            bot_id=bot_id, commands=commands, default_chat_id=default_chat_id
        )
        return bot_instance

    except Exception as e:
        # Journalisation en cas d'erreur (remplacer par un logger en production)
        print(f"Error while initializing bot {bot_id}: {e}")
        return None
