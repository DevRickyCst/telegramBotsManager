# chalicelib/platforms/discord/adapter.py
from chalice.app import Request
from nacl.exceptions import BadSignatureError
from nacl.signing import VerifyKey

from chalicelib.bots.runtime import BotRuntime
from chalicelib.platforms.base_platform import PlatformAdapter
from chalicelib.platforms.discord.client import DiscordClient
from chalicelib.platforms.discord.parser import parse_discord_message


class DiscordPlatformAdapter(PlatformAdapter):
    def verify_request(self, request: Request) -> None:
        print("Verifying Discord request signature")
        signature = request.headers.get("X-Signature-Ed25519")
        timestamp = request.headers.get("X-Signature-Timestamp")
        body = request.raw_body

        if not signature or not timestamp:
            raise PermissionError("Missing Discord signature headers")

        verify_key = VerifyKey(bytes.fromhex("okok"))
        try:
            verify_key.verify(timestamp.encode() + body, bytes.fromhex(signature))
        except BadSignatureError:
            raise PermissionError("Invalid Discord signature")

    def early_response(self, request: Request):
        print("Checking for early Discord response")
        payload = request.json_body
        print(payload)
        if payload.get("type") == 1:  # PING
            return {"type": 1}

    def parse_message(self, request: Request):
        return parse_discord_message(request.json_body)

    def create_client(self, runtime: BotRuntime) -> DiscordClient:
        return DiscordClient(runtime.bot_token)
