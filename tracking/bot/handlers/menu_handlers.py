# from typing import Union
#
# from aiogram.dispatcher.filters import Command
# from aiogram import types
#
# from config import auth
# from keyboards.inline.menu_keyboards import category_data_keyboard, category_expenses_keyboard, menu_cd
# from loader import dp
#
#
# @dp.message_handler(Command('menu'))
# @auth
# async def show_menu(message: types.Message):
#     await list_categories(message)
#
#
# async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
#     markup = await category_data_keyboard()
#
#     if isinstance(message, types.Message):
#         await message.answer('Главное меню', reply_markup=markup)
#
#     elif isinstance(message, types.CallbackQuery):
#         call = message
#         await call.message.edit_reply_markup(markup)
#
#
# async def list_categories_expenses(callback: types.CallbackQuery, category, **kwargs):
#     markup = await category_expenses_keyboard()
#     await callback.message.edit_reply_markup(markup)
#
#
# @dp.callback_query_handler(menu_cd.filter())
# async def navigate(call: types.CallbackQuery, callback_data: dict):
#     current_level = callback_data.get('level')
#     category = callback_data.get('category')
#
#     levels = {
#         '0': list_categories,
#         '1': list_categories_expenses
#     }
#     current_level_function = levels[current_level]
#
#     await current_level_function(
#         call,
#         category=category
#     )
