from chalicelib.platforms.base_message import Message
from chalicelib.platforms.telegram.models.webhook.message import TelegramRaw


def parse_telegram_message(payload: dict) -> Message:
    raw = TelegramRaw.model_validate(payload)
    msg = raw.message

    print(f"Parsing Telegram message: {msg}")
    print(f"Message text: {msg.text}")
    command = msg.get_command()
    return Message(
        text=msg.text,
        message_id=str(msg.message_id),
        chat_id=str(msg.chat.id),
        user_id=str(msg.from_user.id),
        command=command,
        raw=payload,
    )
