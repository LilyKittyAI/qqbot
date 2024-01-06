from typing import Annotated

from nonebot import get_driver, on_regex
from nonebot.adapters.qq.exception import ActionFailed
from nonebot.params import RegexStr
from nonebot.plugin import PluginMetadata

from .config import Config
from .data_sources import fetch_video_info

__plugin_meta__ = PluginMetadata(
    name="url_seeker.bilibili",
    description="哔哩哔哩相关的链接解析",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)

VideoSeeker = on_regex(r"(BV\w{10})\\?")


@VideoSeeker.handle()
async def _(bvid: Annotated[str, RegexStr()]):
    if data := await fetch_video_info(bvid):
        message_template = (
            "{title}\n"
            "{author}\n"
            "{category}\n"
            "{desc}\n"
            f"https://bilibili.com/video/{bvid}"
        )
        try:
            await VideoSeeker.finish(
                message_template.format(
                    title=data["title"],
                    author=data["owner"]["name"],
                    category=data["tname"],
                    desc=data["desc"],
                )
            )
        except ActionFailed:
            ...
