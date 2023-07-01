from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


other_meny = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Время работы'),
            KeyboardButton(text='Расходы'),
            KeyboardButton(text='Доходы')
        ]
    ],
    resize_keyboard=True
)

expenses_meny = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Выплаты работникам'),
            KeyboardButton(text='Покупка и ремонт инструмента'),
            KeyboardButton(text='Транспортные расходы'),
        ],
        [
            KeyboardButton(text='Главное меню')
        ]
    ],
    resize_keyboard=True
)
# btn_main = KeyboardButton(text='Главное меню')
#
# btn_time_work = KeyboardButton(text='Время работы')
# btn_expenses = KeyboardButton(text='Расходы')
# btn_income = KeyboardButton(text='Доходы')

