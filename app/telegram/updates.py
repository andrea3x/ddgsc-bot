import asyncio
import logging
import os
import requests


TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}'

def get_updates(update_handler):
    offset = 668427368

    while True:
        res = requests.get(f'{URL}/getUpdates', params={
            "offset": offset,
            "timeout": 30,
        })
        data = res.json()
        for update in data["result"]:
            if offset <= update["update_id"]:
                offset = update["update_id"] + 1
            logging.info(update)
            asyncio.run(update_handler(update))