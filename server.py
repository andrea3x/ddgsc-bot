import asyncio
from flask import Flask, request
from waitress import serve

from app.update_handler import new_update

app = Flask(__name__)

@app.post('/')
def handle_post():
    update = request.json
    asyncio.run(new_update(update))
    return 'OK', 200

@app.errorhandler(404)
def err(e):
    return "Error", 400


def start_server():
    serve(app, listen='*:5000')


if __name__ == '__main__':
    print("Please start me from main.py")