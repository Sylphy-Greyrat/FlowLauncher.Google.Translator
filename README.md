# FlowLauncher.Google.Translator

[中文](README_CN.md)

This plugin lets you make translations using [Google Translate](https://translate.google.com/) and copy it from [Flow Launcher](https://www.flowlauncher.com/).

## Installation

Install this plugin via Flow Launcher:
```
pm install Google Translate
```

## Usage

### Basic Translation

```
tr es:en es mi traducción    # Translate from Spanish to English
tr es mi traducción          # Auto-detect source, translate to Spanish
tr :es my translation        # Auto-detect source, translate to Spanish
tr hello world               # Translate to configured default language
```

### Query Format

```
tr [from_lang[:to_lang]] text
```

- `from_lang`: Source language (optional, auto-detected if omitted)
- `to_lang`: Target language (optional, uses default if omitted)
- `text`: Text to translate

## Configuration

### Default Language

The plugin automatically detects your Windows system language as the default translation target.

To manually configure:

1. Find the plugin directory:
   ```
   %APPDATA%\FlowLauncher\Plugins\FlowLauncher.Google.Translator\
   ```

2. Create or edit `settings.json`:
   ```json
   {
     "to_lang": "zh-CN"
   }
   ```

3. Restart Flow Launcher

### Supported Languages

| Code | Language |
|------|----------|
| zh-CN | Chinese (Simplified) |
| zh-TW | Chinese (Traditional) |
| en-US | English (US) |
| en-GB | English (UK) |
| ja | Japanese |
| ko | Korean |
| fr | French |
| de | German |
| es | Spanish |
| pt-BR | Portuguese (Brazil) |
| pt-PT | Portuguese (Portugal) |
| ru | Russian |
| it | Italian |
| nl | Dutch |
| no | Norwegian |
| pl | Polish |
| sv | Swedish |
| da | Danish |
| fi | Finnish |
| el | Greek |
| cs | Czech |
| hu | Hungarian |
| tr | Turkish |
| id | Indonesian |
| fa | Persian |
| hr | Croatian |
| sk | Slovak |
| sl | Slovenian |

## Features

- Translate text between multiple languages
- Auto-detect source language
- Copy translation to clipboard with one click
- Configurable default target language
- Context menu for quick settings access
- Input validation (max 5000 characters)
- Detailed error messages for network and parsing failures

## Project Structure

```
FlowLauncher.Google.Translator/
├── main.py                  # Entry point
├── plugin.json              # Plugin configuration
├── plugin/
│   ├── __init__.py          # Package initialization
│   ├── config.py            # Configuration constants
│   ├── language.py          # Language detection and query parsing
│   ├── clipboard.py         # Clipboard operations
│   ├── translator_core.py   # Core translation logic
│   └── plugin.py            # Flow Launcher plugin interface
└── images/
    └── gt.png
```

## Credits

This plugin is a modified port of [Wox.Plugin.GoogleTranslate](https://github.com/laercioskt/Wox.Plugin.GoogleTranslate) created by [laercioskt](https://github.com/laercioskt).

## License

MIT License - see [LICENSE](LICENSE) file.
