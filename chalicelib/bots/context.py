# chalicelib/bots/context.py
from dataclasses import dataclass

from chalicelib.bots.base import BotBase
from chalicelib.bots.factory import BotFactory
from chalicelib.bots.registry import load_bot_settings
from chalicelib.bots.runtime import BotRuntime
from chalicelib.bots.settings import BotSettingBase, Platform
from chalicelib.platforms.base_platform import PlatformAdapter
from chalicelib.platforms.factory import get_platform_adapter
from chalicelib.utils.secret import get_secret


@dataclass(frozen=True)
class BotContext:
    platform: Platform
    settings: BotSettingBase
    adapter: PlatformAdapter
    bot: BotBase


# chalicelib/bots/context.py
def load_bot_context(platform: str, bot_name: str) -> BotContext:
    platform_enum = Platform(platform)

    settings = load_bot_settings(platform_enum, bot_name)
    adapter = get_platform_adapter(platform_enum)
    runtime = BotRuntime(bot_token=get_secret())

    bot = BotFactory.create(
        settings=settings,
        runtime=runtime,
        adapter=adapter,
    )

    return BotContext(
        platform=platform_enum,
        settings=settings,
        adapter=adapter,
        bot=bot,
    )
