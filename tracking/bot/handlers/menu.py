from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from keyboards.inline.choice_buttons import other_meny

from aiogram import types
from asyncpg import Connection, Record

from loader import dp, bot, db


@dp.message_handler(Command("да"))
async def show_yes(message: Message):
    await message.answer(text='Давай внесем данные', reply_markup=other_meny)


class DBCommands:
    pool: Connection = db
    ADD_TIME_WORK = 'Введите время работы'
