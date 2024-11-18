from chalice import Cron

from chalicelib.bots import get_bot

# Configuration des tâches planifiées
SCHEDULED_TASKS = [
    {
        "bot_id": "alertewaterbot",  # Bot ID
        "chat_id": "646579882",  # Chat ID à envoyer
        "text": "C'est l'heure de boire de l'eau !",  # Message
        "schedule": Cron(
            0, "12,16", "*", "*", "?", "*"
        ),  # Toutes les 2 heures entre 8h et 16h
    },
    # Ajoutez d'autres tâches ici
]


def register_schedules(app):
    """Enregistre toutes les tâches planifiées définies dans SCHEDULED_TASKS."""
    for task in SCHEDULED_TASKS:
        schedule = task["schedule"]
        bot_id = task["bot_id"]
        chat_id = task["chat_id"]
        text = task["text"]

        # Définir une fonction d'envoi spécifique pour chaque tâche
        @app.schedule(schedule)
        def send_scheduled_message(event, bot_id=bot_id, chat_id=chat_id, text=text):
            """Envoi d'un message planifié."""
            try:
                # Récupérer une instance de bot configurée
                bot_instance = get_bot(bot_id=bot_id)
                if not bot_instance:
                    print(f"Bot {bot_id} non trouvé ou non initialisé.")
                    return

                # Envoyer le message via le bot
                bot_instance.telegram.sendMessage(text=text, chat_id=chat_id)
                print(f"Message envoyé par {bot_id} à {chat_id}: {text}")
            except Exception as e:
                print(f"Erreur lors de l'envoi du message planifié pour {bot_id}: {e}")
