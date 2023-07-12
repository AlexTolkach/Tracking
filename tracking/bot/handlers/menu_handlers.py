from typing import Union

from aiogram.dispatcher.filters import Command
from aiogram import types

from config import auth
from loader import dp


@dp.message_hendler(Command('menu'))
@auth
async def show_menu(message: types.Message):
    await list_categories(message)


async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await categories_keyboard()
