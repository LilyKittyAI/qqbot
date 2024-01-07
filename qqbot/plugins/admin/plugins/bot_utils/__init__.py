from typing import Annotated

from nonebot import get_driver, on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me

from qqbot.utils import get_version_info

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="bot_utils",
    description="机器人管理有关命令",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)


Echo = on_command("echo", rule=to_me(), block=True)


@Echo.handle()
async def _(message: Annotated[Message, CommandArg()]):
    await Echo.finish(message.extract_plain_text())


Version = on_command("version", rule=to_me(), block=True)


@Version.handle()
async def _():
    await Version.finish("LilyKitty QQbot " ".".join(get_version_info()))
