from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text, Command
from keyboards import keyboard
from main import bot, dp
from config import chat_id


async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='Hello')


@dp.message_handler(Command('shop'))
async def shop_shop(message: Message):
    await message.answer('Shop', reply_markup=keyboard)


@dp.message_handler(Text(equals='Внести данные'))
async def get_goods(message: Message):
    await message.answer(message.text, reply_markup=ReplyKeyboardRemove())
