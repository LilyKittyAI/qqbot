import re

from qqbot.constants import PYPROJECT_FILE


def get_version_info() -> tuple[int, int, int]:
    """获取版本信息

    Returns:
        tuple[int, int, int]: 元组形式的版本信息
    """
    with open(PYPROJECT_FILE, mode="r", encoding="utf-8") as f:
        return tuple(
            map(
                int,
                re.search(r"version = \"(\d\.\d\.\d)\"", f.read())
                .groups()[0]
                .split("."),
            )
        )
