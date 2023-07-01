import os
from dotenv import load_dotenv

# Token tg bot
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
chat_id = os.getenv('chat_id')

# bd
NAME = os.getenv('NAME')
PG_USER = os.getenv('PG_USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

POSGRESTURI = f'posgrestsgl://{PG_USER}:{PASSWORD}@{HOST}/{NAME}'
