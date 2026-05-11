# -*- coding: utf-8 -*-
"""剪贴板操作工具。"""

import subprocess
import sys


def copy_to_clipboard(text):
    """安全地将文本复制到剪贴板。

    Args:
        text: 要复制的文本内容

    Returns:
        bool: 复制成功返回 True，失败返回 False

    Note:
        仅支持 Windows 平台（使用 clip 命令）。
        其他平台始终返回 False。
    """
    if sys.platform != "win32":
        return False

    # 验证输入
    if not isinstance(text, str):
        return False

    try:
        # 使用 clip 命令复制到剪贴板
        process = subprocess.Popen(
            ["clip"],
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        # 使用 UTF-16-LE 编码（Windows 剪贴板格式）
        process.communicate(input=text.encode("utf-16-le"))
        return process.returncode == 0
    except (subprocess.SubprocessError, OSError):
        return False
