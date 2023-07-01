from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import my_callback

other_meny = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Время работы', callback_data=my_callback.new(
                data_name='Name', quantity='9'
            ))
        ],
        [
            InlineKeyboardButton(text='Расходы', callback_data=my_callback.new(
                data_name='Name', quantity='9'
            ))
        ],
        [
            InlineKeyboardButton(text='Доходы', callback_data=my_callback.new(
                data_name='Name', quantity='9'
            ))
        ]
    ]
)
