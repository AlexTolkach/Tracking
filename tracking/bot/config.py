import os
from dotenv import load_dotenv

# Token tg bot
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
chat_id = os.getenv('chat_id')
