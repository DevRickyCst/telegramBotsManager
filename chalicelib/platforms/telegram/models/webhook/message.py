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

    def get_command(self) -> str | None:
        """Get command from the message if available."""
        if self.text is not None and self.text.startswith("/"):
            return self.text.split()[0][1:]  # Remove leading '/' and get command
        return None


class TelegramTextMessage(TelegramMessageCommon):
    """Telegram webhook message model for text messages."""

    pass


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
