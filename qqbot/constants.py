"""程序运行中会用到的常量信息
"""
from os.path import dirname, join

SOURCE_DIR = dirname(__file__)
PROJECT_DIR = dirname(SOURCE_DIR)

PYPROJECT_FILE = join(PROJECT_DIR, "pyproject.toml")
