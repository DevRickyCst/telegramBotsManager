from chalicelib.platforms.base_message import Message
from chalicelib.platforms.telegram.models.webhook.message import TelegramRaw


def parse_discord_message(payload: dict) -> Message:
    print("Parsing Discord message:")
    print(payload)
    raw = TelegramRaw.model_validate(payload)
    msg = raw.message
    command = msg.get_command()
    return Message(
        text=msg.text,
        message_id=str(msg.message_id),
        chat_id=str(msg.chat.id),
        user_id=str(msg.from_user.id),
        command=command,
        raw=payload,
    )
