# -*- coding: utf-8 -*-
"""Flow Launcher Google Translate 插件。"""

import urllib.error

from flowlauncher import FlowLauncher, FlowLauncherAPI

from .config import ICON_PATH
from .language import get_system_language, parse_query
from .clipboard import copy_to_clipboard
from .translator_core import (
    translate,
    TranslationError,
    NetworkError,
    ParseError,
    QueryTooLongError,
)


def create_help_result():
    """创建帮助信息结果项。

    Returns:
        dict: Flow Launcher 结果格式
    """
    return {
        "Title": ":es text to translate",
        "SubTitle": "use: 'tr :es your expresion' to translate from auto-detected to Spanish",
        "IcoPath": ICON_PATH,
        "ContextData": "ctxData",
    }


def create_translation_result(translation, source_text, to_language, from_language):
    """创建翻译结果项。

    Args:
        translation: 翻译结果
        source_text: 源文本
        to_language: 目标语言
        from_language: 源语言

    Returns:
        dict: Flow Launcher 结果格式
    """
    return {
        "Title": f"{to_language}: {translation}",
        "SubTitle": f"{from_language}: {source_text}",
        "IcoPath": ICON_PATH,
        "ContextData": "ctxData",
        "JsonRPCAction": {
            "method": "copy",
            "parameters": [translation],
        },
    }


def create_error_result(title, subtitle):
    """创建错误信息结果项。

    Args:
        title: 错误标题
        subtitle: 错误详细信息

    Returns:
        dict: Flow Launcher 结果格式
    """
    return {
        "Title": title,
        "SubTitle": subtitle,
        "IcoPath": ICON_PATH,
        "ContextData": "ctxData",
    }


class GoogTranslate(FlowLauncher):
    """Google Translate 插件主类。"""

    # 默认设置
    settings = {"to_lang": ""}

    def query(self, query):
        """处理翻译查询。

        Args:
            query: 用户输入的查询字符串

        Returns:
            list: Flow Launcher 结果列表
        """
        if not query.strip():
            return [create_help_result()]

        # 获取默认目标语言
        default_lang = self.settings.get("to_lang", "")
        if not default_lang:
            default_lang = get_system_language()

        # 解析查询
        from_language, to_language, text = parse_query(query)

        if not text:
            return [create_help_result()]

        # 使用配置的语言（如果未指定）
        if not to_language:
            to_language = default_lang

        # 执行翻译
        try:
            translation = translate(text, to_language, from_language)
            return [create_translation_result(
                translation, text, to_language, from_language
            )]
        except QueryTooLongError:
            return [create_error_result(
                "查询过长",
                f"文本长度超过限制（最大 5000 字符）"
            )]
        except NetworkError as e:
            return [create_error_result(
                "网络错误",
                f"无法连接到 Google Translate: {e}"
            )]
        except ParseError:
            return [create_error_result(
                "解析错误",
                "无法解析翻译结果，请稍后重试"
            )]
        except TranslationError as e:
            return [create_error_result(
                "翻译错误",
                str(e)
            )]

    def copy(self, ans):
        """复制翻译结果到剪贴板。

        Args:
            ans: 要复制的文本
        """
        if copy_to_clipboard(ans):
            FlowLauncherAPI.show_msg("已复制到剪贴板", "")
        else:
            FlowLauncherAPI.show_msg("复制失败", "")

    def context_menu(self, data):
        """右键菜单。

        Args:
            data: 上下文数据

        Returns:
            list: 菜单项列表
        """
        return [{
            "Title": "设置",
            "SubTitle": "打开插件设置配置默认语言",
            "IcoPath": ICON_PATH,
            "JsonRPCAction": {
                "method": "open_setting_dialog",
                "parameters": [],
            },
        }]

    def open_setting_dialog(self):
        """打开设置对话框。"""
        FlowLauncherAPI.open_setting_dialog()
