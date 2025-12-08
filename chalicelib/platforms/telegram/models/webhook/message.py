from pydantic import BaseModel, Field

from chalicelib.platforms.telegram.models.webhook.common import (
    TelegramChat,
    TelegramImage,
    TelegramUser,
    TelegramVideo,
)


class TelegramMessageCommon(BaseModel):
    """Common fields for all Telegram message types."""

    message_id: int
    from_user: TelegramUser = Field(alias="from")
    chat: TelegramChat
    date: int
    text: str | None = None


class TelegramTextMessage(TelegramMessageCommon):
    """Telegram webhook message model for text messages."""

    def isCommand(self) -> str | None:
        """Return the command name if text starts with '/', otherwise None."""
        if not self.text.startswith("/"):
            return None

        # Remove "/", strip spaces, split words
        parts = self.text[1:].strip().split()
        return parts[0] if parts else None


class TelegramVideoMessage(TelegramMessageCommon):
    """Telegram webhook message model for video messages."""

    video: TelegramVideo
    media_group_id: str | None = None
    caption: str | None = None


class TelegramImageMessage(TelegramMessageCommon):
    """Telegram webhook message model for image messages."""

    photo: list[TelegramImage]
    media_group_id: str | None = None
    caption: str | None = None


class TelegramRaw(BaseModel):
    """Telegram webhook raw update model."""

    update_id: int
    message: TelegramTextMessage | TelegramImageMessage | TelegramVideoMessage
