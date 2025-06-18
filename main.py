import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
)

from app.telegram.updates import get_updates
from app.update_handler import new_update




print('Starting ddgsc-bot v0.1')

if os.environ.get("TELEGRAM_BOT_TOKEN") == None:
    raise Exception("No TELEGRAM_BOT_TOKEN env. variable found.")


try:

    try:
        __import__("flask")
        __import__("waitress")
        from server import start_server
        start_server()

    except ImportError:
        print('Flask or Waitress not installed. Launching get_updates()')
        get_updates(new_update)

except KeyboardInterrupt:
    pass
except Exception as e:
    raise e