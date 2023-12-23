from typing import Annotated

from nonebot import get_driver, on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="echo",
    description="",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)


echo = on_command("echo", rule=to_me(), block=True)


@echo.handle()
async def _(message: Annotated[Message, CommandArg()]):
    await echo.finish(message.extract_plain_text())
