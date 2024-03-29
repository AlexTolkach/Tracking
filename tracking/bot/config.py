import os
from dotenv import load_dotenv

# Token tg bot
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
chat_id = os.getenv('chat_id')


# bd
DB_NAME = os.getenv('DB_NAME')
PG_USER = os.getenv('PG_USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

ip = os.getenv('ip')


def auth(func):
    async def wrapper(message):
        if message['from']['id'] != int(chat_id):
            return await message.reply('access denied', reply=False)
        return await func(message)

    return wrapper
