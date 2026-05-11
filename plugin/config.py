# -*- coding: utf-8 -*-
"""插件配置常量。"""

# Google Translate 网页地址
GOOGLE_TRANSLATE_URL = "https://translate.google.com/m"

# 文本换行长度
DEFAULT_WRAP_LENGTH = 200

# 请求 User-Agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# 请求超时时间（秒）
REQUEST_TIMEOUT = 15

# 默认语言
DEFAULT_LANGUAGE = "en-US"

# 插件图标路径
ICON_PATH = "Images/gt.png"

# 最大查询长度，防止滥用
MAX_QUERY_LENGTH = 5000

# Windows LCID 到语言代码的映射
LANGUAGE_MAP = {
    0x0804: "zh-CN",   # 简体中文
    0x0404: "zh-TW",   # 繁体中文
    0x0409: "en-US",   # 英语（美国）
    0x0809: "en-GB",   # 英语（英国）
    0x0411: "ja",      # 日语
    0x0412: "ko",      # 韩语
    0x040c: "fr",      # 法语
    0x0407: "de",      # 德语
    0x0c0a: "es",      # 西班牙语
    0x0416: "pt-BR",   # 葡萄牙语（巴西）
    0x0816: "pt-PT",   # 葡萄牙语（葡萄牙）
    0x0419: "ru",      # 俄语
    0x0410: "it",      # 意大利语
    0x0413: "nl",      # 荷兰语
    0x0414: "no",      # 挪威语
    0x0415: "pl",      # 波兰语
    0x041d: "sv",      # 瑞典语
    0x0406: "da",      # 丹麦语
    0x040b: "fi",      # 芬兰语
    0x0408: "el",      # 希腊语
    0x0405: "cs",      # 捷克语
    0x040e: "hu",      # 匈牙利语
    0x041f: "tr",      # 土耳其语
    0x0421: "id",      # 印尼语
    0x0420: "ur",      # 乌尔都语
    0x0429: "fa",      # 波斯语
    0x041a: "hr",      # 克罗地亚语
    0x041b: "sk",      # 斯洛伐克语
    0x0424: "sl",      # 斯洛文尼亚语
    0x0813: "nl-BE",   # 荷兰语（比利时）
    0x0814: "nn",      # 挪威语（尼诺斯克语）
}
