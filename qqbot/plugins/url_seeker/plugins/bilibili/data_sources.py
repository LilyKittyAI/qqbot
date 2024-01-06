from bilibili_api.errors import ResponseCodeException
from bilibili_api.video import Video


async def fetch_video_info(bvid: str) -> dict | None:
    """获取视频信息

    Args:
        bvid (str): 视频 BVID

    Returns:
        dict|None: 官方API返回的数据
    """
    v = Video(bvid=bvid)
    try:
        return await v.get_info()
    except ResponseCodeException:
        return None
