import asyncio

from aiogram import Bot, Dispatcher, executor, types
import config
from utils.db_api.database import create_pool, engine

loop = asyncio.get_event_loop()

bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


db = loop.run_until_complete(create_pool())
# db = loop.run_until_complete(engine)

chat_id = config.chat_id

