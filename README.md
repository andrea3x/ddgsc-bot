# Duckduckgo Search - Telegram Bot
**Search Duckduckgo with the bot or using inline mode!**

This is the source code for a Telegram bot that lets you search Duckduckgo.

### Features
- Type your search and send it to the bot
- Use inline mode in other chats and search!

This script can work without the need of a public IP.

### Usage
1. Clone the repository.
2. Install the dependencies (uninstall `flask` or `waitress` if using locally¹):
```
pip install -r requirements.txt
```
3. Ask BotFather to create a bot for you, create a `.env` file and paste there the token you've been given:
```
    TELEGRAM_BOT_TOKEN=<paste here the token>
```
4. *[optional] Set up the webhook for the server to work¹.*
5. Start the script:
```
python main.py
```

##### Notes
¹: The script can run both as a *server* accepting hooks from Telegram and as a *client* (= no public IP) that asks Telegram for updates. If either `flask` or `waitress` is not installed, the script falls back to *client mode*.

*This project is not affiliated with Duckduckgo.*