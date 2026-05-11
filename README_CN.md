# FlowLauncher.Google.Translator

[English](README.md)

这是一个 [Flow Launcher](https://www.flowlauncher.com/) 插件，使用 [Google Translate](https://translate.google.com/) 进行翻译并支持一键复制。

## 安装

通过 Flow Launcher 安装此插件：
```
pm install Google Translate
```

## 使用方法

### 基本翻译

```
tr es:en es mi traducción    # 从西班牙语翻译到英语
tr es mi traducción          # 自动检测源语言，翻译到西班牙语
tr :es my translation        # 自动检测源语言，翻译到西班牙语
tr hello world               # 翻译到配置的默认语言
```

### 查询格式

```
tr [源语言[:目标语言]] 文本
```

- `源语言`：源语言代码（可选，省略时自动检测）
- `目标语言`：目标语言代码（可选，省略时使用默认语言）
- `文本`：待翻译文本

## 配置

### 默认语言

插件会自动检测 Windows 系统语言作为默认翻译目标。

手动配置方法：

1. 找到插件目录：
   ```
   %APPDATA%\FlowLauncher\Plugins\FlowLauncher.Google.Translator\
   ```

2. 创建或编辑 `settings.json`：
   ```json
   {
     "to_lang": "zh-CN"
   }
   ```

3. 重启 Flow Launcher

### 支持的语言

| 代码 | 语言 |
|------|------|
| zh-CN | 简体中文 |
| zh-TW | 繁体中文 |
| en-US | 英语（美国） |
| en-GB | 英语（英国） |
| ja | 日语 |
| ko | 韩语 |
| fr | 法语 |
| de | 德语 |
| es | 西班牙语 |
| pt-BR | 葡萄牙语（巴西） |
| pt-PT | 葡萄牙语（葡萄牙） |
| ru | 俄语 |
| it | 意大利语 |
| nl | 荷兰语 |
| no | 挪威语 |
| pl | 波兰语 |
| sv | 瑞典语 |
| da | 丹麦语 |
| fi | 芬兰语 |
| el | 希腊语 |
| cs | 捷克语 |
| hu | 匈牙利语 |
| tr | 土耳其语 |
| id | 印尼语 |
| fa | 波斯语 |
| hr | 克罗地亚语 |
| sk | 斯洛伐克语 |
| sl | 斯洛文尼亚语 |

## 功能特性

- 多语言互译
- 自动检测源语言
- 一键复制翻译结果到剪贴板
- 可配置默认目标语言
- 右键菜单快速访问设置
- 输入验证（最大 5000 字符）
- 详细的网络和解析错误提示

## 项目结构

```
FlowLauncher.Google.Translator/
├── main.py                  # 入口点
├── plugin.json              # 插件配置
├── plugin/
│   ├── __init__.py          # 包初始化
│   ├── config.py            # 配置常量
│   ├── language.py          # 语言检测和查询解析
│   ├── clipboard.py         # 剪贴板操作
│   ├── translator_core.py   # 翻译核心逻辑
│   └── plugin.py            # Flow Launcher 插件接口
└── images/
    └── gt.png
```

## 致谢

此插件修改自 [laercioskt](https://github.com/laercioskt) 创建的 [Wox.Plugin.GoogleTranslate](https://github.com/laercioskt/Wox.Plugin.GoogleTranslate)。

## 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。
