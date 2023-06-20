from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Внести данные')
        ]
    ],
    resize_keyboard=True
)
