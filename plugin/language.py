# -*- coding: utf-8 -*-
"""语言检测和映射工具。"""

import ctypes
import locale
import sys

from .config import LANGUAGE_MAP, DEFAULT_LANGUAGE


def get_system_language():
    """获取系统语言代码。

    Returns:
        str: 语言代码（如 'en-US'、'zh-CN'）

    Note:
        Windows 平台使用 GetUserDefaultUILanguage() 获取 LCID。
        其他平台使用 locale.getlocale()。
        检测失败时回退到 DEFAULT_LANGUAGE。
    """
    # Windows: 使用 LCID
    if sys.platform == "win32":
        try:
            lang_id = ctypes.windll.kernel32.GetUserDefaultUILanguage()
            return LANGUAGE_MAP.get(lang_id, DEFAULT_LANGUAGE)
        except (AttributeError, OSError):
            pass

    # 其他平台: 使用 locale
    try:
        lang = locale.getlocale()[0]
        if lang:
            # 将 locale 格式（如 'en_US'）转换为语言代码（如 'en-US'）
            return lang.replace("_", "-")
    except (AttributeError, ValueError):
        pass

    return DEFAULT_LANGUAGE


def parse_query(query):
    """解析翻译查询字符串。

    Args:
        query: 查询字符串，格式为 '[from_lang[:to_lang]] text'

    Returns:
        tuple: (from_language, to_language, text)
            - from_language: 源语言代码或 'auto'
            - to_language: 目标语言代码或空字符串
            - text: 待翻译文本

    Examples:
        >>> parse_query('en:zh hello')
        ('en', 'zh', 'hello')
        >>> parse_query(':zh hello')
        ('auto', 'zh', 'hello')
        >>> parse_query('hello')
        ('auto', '', 'hello')
    """
    from_language = "auto"
    to_language = ""
    text = query.strip()

    # 分割语言部分和文本
    parts = query.split(" ", 1)
    if len(parts) <= 1:
        return from_language, to_language, text

    lang_part, text = parts

    # 解析语言规格
    lang_parts = lang_part.split(":")

    if len(lang_parts) == 2:
        # 格式: from:to
        from_lang, to_lang = lang_parts
        from_language = from_lang.strip() or "auto"
        to_language = to_lang.strip()
    elif len(lang_parts) == 1 and lang_part:
        # 格式: to（自动检测源语言）
        to_language = lang_parts[0].strip()

    return from_language, to_language, text.strip()
