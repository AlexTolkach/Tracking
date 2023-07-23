from loader import chat_id
from aiogram import Bot


async def send_message_time(bot: Bot):
    await bot.send_message(chat_id, 'Давай внесем сегодняшние данные\n '
                                    'Нажми /menu чтобы выбрать какие данные хочешь записать')
