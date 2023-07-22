from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from config import auth
from loader import dp


@dp.message_handler(CommandStart())
@auth
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}\n'
                         f'жми /menu')
