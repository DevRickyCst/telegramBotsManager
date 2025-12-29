from chalicelib.bots.base import BotBase
from chalicelib.bots.runtime import BotRuntime
from chalicelib.bots.settings import BotSettingBase
from chalicelib.platforms.base_platform import PlatformAdapter


class BotFactory:
    @staticmethod
    def create(
        settings: BotSettingBase,
        runtime: BotRuntime,
        adapter: PlatformAdapter,
    ) -> BotBase:
        """
        Create a bot instance for the given settings.
        """
        client = adapter.create_client(runtime)
        return BotBase(
            settings=settings,
            runtime=runtime,
            client=client,
        )
