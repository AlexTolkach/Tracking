from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.database import user_work_time_table, expenses_table, smeta_table

CATEGORIES_OF_EXPENSES = [
    ('w', 'Оплата труда'),
    ('b', 'Покупка и ремонт инструмента'),
    ('t', 'Транспортные расходы'),
    ('p', 'Премии')
]

CATEGORIES_OF_DATA = [
    ('Время работы', user_work_time_table),
    ('Расходы', expenses_table),
    ('Доходы', smeta_table)
]

menu_cd = CallbackData('show_menu', 'level', 'category')
output_data = CallbackData('output')


def make_callback_data(level, category='0'):
    return menu_cd.new(level=level, category=category)


async def category_data_keyboard():
    current_level = 0
    markup = InlineKeyboardMarkup()

    for category in CATEGORIES_OF_DATA:
        button_text = f'{category[0]}'
        callback_data = make_callback_data(
            level=current_level + 1,
            category=category[1]
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data),
        )
    return markup


async def category_expenses_keyboard():
    current_level = 1
    markup = InlineKeyboardMarkup()

    categories = CATEGORIES_OF_EXPENSES
    for category in categories:
        button_text = f'{category[1]}'
        callback_data = make_callback_data(
            level=current_level + 1,
            category=category[0]
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data),
        )
    markup.row(
        InlineKeyboardButton(
            text='Назад',
            callback_data=make_callback_data(level=current_level - 1)
        )
    )
    return markup


