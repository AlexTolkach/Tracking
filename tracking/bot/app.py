from aiogram import executor
from loader import dp
from loader import bot, chat_id


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    await bot.send_message(chat_id, 'Бот запущен!')

if __name__ == '__main__':
    from loader import dp
    from handlers import dp
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
