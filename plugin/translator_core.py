# -*- coding: utf-8 -*-
"""Google Translate 核心翻译逻辑。"""

import html
import re
import textwrap
import urllib.error
import urllib.parse
import urllib.request

from .config import (
    GOOGLE_TRANSLATE_URL,
    DEFAULT_WRAP_LENGTH,
    USER_AGENT,
    REQUEST_TIMEOUT,
    MAX_QUERY_LENGTH,
)


class TranslationError(Exception):
    """翻译错误基类。"""
    pass


class NetworkError(TranslationError):
    """网络请求错误。"""
    pass


class ParseError(TranslationError):
    """翻译结果解析错误。"""
    pass


class QueryTooLongError(TranslationError):
    """查询文本过长错误。"""
    pass


def translate(text, to_language="auto", from_language="auto", wrap_length=DEFAULT_WRAP_LENGTH):
    """使用 Google Translate 翻译文本。

    Args:
        text: 待翻译文本
        to_language: 目标语言代码（默认 'auto'）
        from_language: 源语言代码（默认 'auto'）
        wrap_length: 文本换行长度

    Returns:
        str: 翻译结果

    Raises:
        QueryTooLongError: 查询文本超过最大长度限制
        NetworkError: 网络请求失败
        ParseError: 无法解析翻译结果

    Note:
        通过抓取 Google Translate 移动版网页获取翻译结果。
        使用正则表达式解析 HTML，可能因网页结构变化而失效。
    """
    # 验证查询长度
    if len(text) > MAX_QUERY_LENGTH:
        raise QueryTooLongError(f"查询文本过长: {len(text)} > {MAX_QUERY_LENGTH}")

    # 构建请求 URL
    params = urllib.parse.urlencode({
        "tl": to_language,
        "sl": from_language,
        "q": text,
    })
    url = f"{GOOGLE_TRANSLATE_URL}?{params}"

    # 发送请求
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT) as response:
            # 检查 HTTP 状态码
            if response.status != 200:
                raise NetworkError(f"HTTP 错误: {response.status}")
            data = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        raise NetworkError(f"网络请求失败: {e}") from e
    except OSError as e:
        raise NetworkError(f"IO 错误: {e}") from e

    # 解析翻译结果
    match = re.search(r'class="result-container">(.*?)<', data)
    if not match:
        raise ParseError("无法解析翻译结果，网页结构可能已变化")

    # 处理 HTML 实体并换行
    result = html.unescape(match.group(1))
    return "\n".join(textwrap.wrap(result, wrap_length))
