from datetime import datetime

from aiogram import executor
from loader import bot, chat_id
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers import apsched


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    scheduler = AsyncIOScheduler(time_zone='Europe/Minsk')
    scheduler.add_job(apsched.send_message_time, trigger='cron', hour=18,
                      minute=20, start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.start()
    await bot.send_message(chat_id, 'Бот запущен! Нажмите /start')


if __name__ == '__main__':
    from loader import dp
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
