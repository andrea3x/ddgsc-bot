import json
import os
import requests


TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}'

def send_message(chat_id, text: str):
    res = requests.get(f'{URL}/sendMessage', params={
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
    })

def answer_inline_query(inline_query_id, results):
    res = requests.get(f'{URL}/answerInlineQuery', params={
        "inline_query_id": inline_query_id,
        "results": json.dumps(results),
        "cache_time": 0,
    })