import asyncio
from aiogram import Bot, Dispatcher
import config
from utils.db_api.database import create_pool
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

loop = asyncio.get_event_loop()

bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')

dp = Dispatcher(bot, storage=storage)

db = loop.run_until_complete(create_pool())

chat_id = config.chat_id
