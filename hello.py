#!/usr/bin/env python3
"""hello-git 示例脚本：输出一句问候语。"""


def greet(name: str = "World") -> str:
    """返回针对 name 的问候语。"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
