# from aiogram.types import Message, ReplyKeyboardRemove
# from aiogram.dispatcher.filters import Text, Command
# from loader import bot, dp
# from config import chat_id
# import keyboards as nav
#
#
# async def send_hello(dp):
#     await bot.send_message(chat_id=chat_id, text='Привет, запишем сегодняшние данные')
#
#
# @dp.message_handler(Command('да'))
# async def shop_shop(message: Message):
#     await message.answer('Начали', reply_markup=nav.other_meny)
#
#
# @dp.message_handler(Text(equals='Расходы'))
# async def get_goods(message: Message):
#     await message.answer('Выбери категорию расходов', reply_markup=nav.expenses_meny)
#
#
# @dp.message_handler()
# async def get_other_meny(message: Message):
#     if message.text == 'Главное меню':
#         await message.answer('Выбери какие данные хочешь ввести', reply_markup=nav.other_meny)
#     else:
#         await message.reply('Неизвестная команда')
