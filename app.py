from typing import Optional

from chalice.app import Chalice

from chalicelib.bots.context import load_bot_context
from chalicelib.bots.registry import list_bot_settings, load_bot_settings
from chalicelib.bots.settings import Platform
from chalicelib.webhook_manager import WebhookManager

app = Chalice(app_name="telegramBots")


@app.route("/webhooks/set/{platform}", methods=["POST"])
@app.route("/webhooks/set/{platform}/{bot_name}", methods=["POST"])
def set_webhook(platform: str, bot_name: Optional[str] = None):
    try:
        platform_enum = Platform(platform)
    except ValueError:
        return {"error": f"Unknown platform: {platform}"}

    manager = WebhookManager(base_url="https://hip-onagraceous-arianna.ngrok-free.dev")
    results = []

    bots_to_configure = (
        [load_bot_settings(platform_enum, bot_name)]
        if bot_name
        else list_bot_settings(platform_enum)
    )

    results = []
    for settings in bots_to_configure:
        try:
            results.append(manager.set_webhook(settings))
        except Exception as e:
            results.append(
                {"bot": getattr(settings, "bot_name", str(settings)), "error": str(e)}
            )

    return {"results": results}


@app.route("/{platform}/{bot_name}", methods=["POST"])
def webhook_handler(platform: str, bot_name: str):
    try:
        ctx = load_bot_context(platform, bot_name)

        # 1️⃣ sécurité / ping
        ctx.adapter.verify_request(app.current_request)  # type: ignore

        if early := ctx.adapter.early_response(app.current_request):  # type: ignore
            return early

        # 2️⃣ message
        message = ctx.adapter.parse_message(app.current_request)  # type: ignore
        print(message)
        # 3️⃣ business
        ctx.bot.handle_message(message)

        return {"ok": True}

    except ValueError as e:
        return {"error": str(e)}


@app.route("/", methods=["GET"])
def index():
    return "Hello World"
