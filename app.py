from chalice import Chalice

from chalicelib.bots.factory import BotFactory
from chalicelib.bots.registry import load_bot_settings
from chalicelib.bots.settings import Platform
from chalicelib.platforms.base_parser import parse_message

# from chalicelib.utils.webhook_manager import WebhookManager

app = Chalice(app_name="telegramBots")


# webhook_manager = WebhookManager(
#    "https://hip-onagraceous-arianna.ngrok-free.dev"
# "https://6sm86mr5n3.execute-api.eu-central-1.amazonaws.com/api/"
# )


@app.route("/{platform}/{bot_name}", methods=["POST"])
def webhook_index(platform: str, bot_name: str):
    print(f"Received webhook for platform: {platform}, bot_name: {bot_name}")

    """Handle the webhook call from Telegram for a specific bot."""

    try:
        # 1️⃣ platform string → enum
        platform_enum = Platform(platform)

        # 2️⃣ Charger la config du bot
        settings = load_bot_settings(platform_enum, bot_name)

        # 3️⃣ Créer le bot (runtime + client)
        bot = BotFactory.create(settings)

        # 4️⃣ Parser le message (platform-specific)
        message = parse_message(
            platform=platform_enum,
            payload=app.current_request.json_body,
        )

        # 5️⃣ Déléguer au bot
        bot.handle_message(message)

        return {"ok": "True"}

    except ValueError as e:
        print(str(e))
        return {"ok": "True"}


@app.route("/", methods=["GET"])
def index():
    return "Hello World"


# @app.route("/set-webhooks", methods=["POST"])
# def set_webhooks():
#   """Configure webhooks for all bots."""
# results = webhook_manager.set_webhooks_for_all()
# return {"status": "Webhooks configured", "results": results}


# @app.schedule(
#    Cron(1, "10,14", "*", "*", "?", "*")
# )  # Every 2 hours between 8 AM and 4 PM
# def alertewaterbot_schedule(event):
#    send_scheduled_message(
#        bot_id="alertewaterbot",
#        text="ok",
#    )
