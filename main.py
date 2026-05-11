# -*- coding: utf-8 -*-
"""Flow Launcher Google Translate 插件入口。"""

import os
import sys

# 将插件目录添加到 Python 路径
PLUGIN_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, PLUGIN_DIR)
sys.path.insert(0, os.path.join(PLUGIN_DIR, "lib"))

from plugin.plugin import GoogTranslate

if __name__ == "__main__":
    GoogTranslate()
