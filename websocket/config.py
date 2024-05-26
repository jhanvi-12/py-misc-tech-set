import os
from dotenv import load_dotenv

load_dotenv()

WEBSOCKET_URL = os.environ.get('WEBSOCKET_URL')
SERVER_PORT = os.environ.get('SERVER_PORT')
SERVER_HOST = os.environ.get('SERVER_HOST')