#!/usr/bin/env python3
"""hello-git 示例脚本：输出一句问候语。"""

import sys
from datetime import datetime


def greet(name: str = "World") -> str:
    """返回针对 name 的问候语。"""
    return f"Hello, {name}!"


def stamp() -> str:
    """返回当前时间字符串。"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(f"{greet(target)}  [{stamp()}]")
