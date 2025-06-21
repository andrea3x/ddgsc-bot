
from textwrap import shorten
from duckduckgo_search import DDGS

from app.commands import start
from app.telegram.send import answer_inline_query, send_message


search = DDGS().text


async def new_update(update):
    message = update.get("message", None)
    inline_query = update.get("inline_query", None)

    if message:
        new_message(message)
    elif inline_query:
        new_inline_query(inline_query)



def new_message(message):
    if message.get("via_bot") != None or message.get("text") == None: return

    chat_id = message["chat"]["id"]
    text = message["text"]

    if text == '/start':
        return send_message(chat_id, start())

    results = search(text, max_results=5)
    send_message(chat_id, sumup(results))



def new_inline_query(inline_query):
    if inline_query["query"] == '': return

    results = search(inline_query["query"])
    iq_results = [{
        "type": "article",
        "id": indx,
        "title": result["title"],
        "description": result["href"],
        "input_message_content": {
            "message_text": result["href"]
        }
    } for indx, result in enumerate(results)]

    iq_results.insert(0, {
        "type": "article",
        "id": -1,
        "title": "Send all search results.",
        "input_message_content": {
            "message_text": sumup(results)
        }
    })

    answer_inline_query(inline_query["id"], iq_results)




def sumup(results):
    return "\n\n".join([f"{r["title"]}\n{r["href"]}\n{shorten(r["body"], width=70, placeholder='...')}" for r in results])