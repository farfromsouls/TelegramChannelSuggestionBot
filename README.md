# TelegramChannelSuggestionBot

This bot allows you to conveniently administer user requests for posting in a telegram channel or chat.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install aiogram3.x.

```bash
pip install aiogram
```

## Usage

1. Create "tmp" folder in the bot's directory.
2. Create "secret.py", it should look like this:
```python
token = # telegram bot token
admin_id = # admin id here
CHAT_ID = # channel or chat id (should be 13 digits number)
```
3. Then just start the bot:
```bash
python main.py
```
