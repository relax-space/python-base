import os
import platform
import re
import sys


def get_file_size(file_path: str) -> str:
    """
    计算文件大小
    """
    size = os.path.getsize(file_path)
    m = 1024 * 1024
    g = 1024 * 1024 * 1024
    res = ""
    if size < m:
        res = f"{round(size/1024)}K"
    elif size < g:
        res = f"{round(size/m)}M"
    else:
        res = f"{round(size/g,1)}G"
    return res


def safe_str(raw: str):
    """
    去除windows文件名中不合法的字符
    """
    return re.sub(r'[<>:"/\|?*]', "", raw)


def to_second(raw: str) -> int:
    """
    将时间转换成秒
    """
    r = raw.split(":")
    n = len(r)
    if n == 1:
        return int(r[0])
    elif n == 2:
        return 60 * int(r[0]) + int(r[1])
    elif n == 3:
        return 3600 * int(r[0]) + 60 * int(r[1]) + int(r[2])
    else:
        return 0


def get_dir():
    """
    获取当前路径: 无论安装包, 还是本地测试都能正确获取到相应路径
    """
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.realpath(sys.executable))
    elif __file__:
        return os.path.dirname(__file__)


def get_os() -> str:
    # windows, linux, darwin
    return platform.system().lower()


def get_search_param(url, key):
    ptn = rf"[?&]{key}=([^&]*)"
    match = re.search(ptn, url)
    if match:
        return match.group(1)
    return None


# 示例用法
url1 = "https://example.com/page?param1=value1&param2=value2&param3=value3"
url2 = "https://example.com/page?param2=value2&param1=value1"
url3 = "https://example.com/page?param2=value2"
url4 = "https://example.com/page&param1=value1"

print(get_search_param(url1, "param1"))  # 输出: value1
print(get_search_param(url1, "param2"))  # 输出: value2
print(get_search_param(url1, "param3"))  # 输出: value3
