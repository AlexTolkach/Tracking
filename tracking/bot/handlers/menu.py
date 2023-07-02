# from aiogram.dispatcher.filters import Command
# from aiogram.types import Message
# from keyboards.inline.choice_buttons import other_meny
# from typing import Union

from aiogram import types
from loader import dp, bot, db, chat_id
from utils.db_api.db_commands import database


# @dp.message_handler(Command('menu'))
# async def show_menu(message: types.Message):
#     await list_categories(message)


# async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
#     markup = await categories_ceyboard()


# @dp.message_handler(Command("да"))
# async def show_yes(message: Message):
#     await message.answer(text='Давай внесем данные', reply_markup=other_meny)


@dp.message_handler(commands=["count_workers"])
async def output_count_users(message: types.Message):
    count_users = await database.count_user()
    text = f'Сейчас в базе {count_users} работников'
    await bot.send_message(chat_id, text)
