from qqbot.utils import get_version_info


def test_get_version_info():
    version_info = get_version_info()
    assert isinstance(version_info, tuple)
    assert len(version_info) == 3
    assert all(map(lambda x: isinstance(x, int), version_info))
