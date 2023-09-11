from aiogram import types
from aiogram.dispatcher import FSMContext
from states import Expenses
from loader import dp
from config import auth
from utils.db_api.db_commands import add_expenses

expenses = {}


@auth
@dp.message_handler(commands=['add_expenses'])
async def add_expense(message: types.Message):
    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Оплата труда', callback_data='w')
            ],
            [
                types.InlineKeyboardButton(text='Покупка и ремонт инструмента', callback_data='b')
            ],
            [
                types.InlineKeyboardButton(text='Транспортные расходы', callback_data='t')
            ],
            [
                types.InlineKeyboardButton(text='Премии', callback_data='p')
            ],
        ]
    )
    await message.answer('Выберите категорию расходов или нажмите /cancel', reply_markup=markup)
    await Expenses.Category.set()


@auth
@dp.callback_query_handler(state=Expenses.Category, text_contains='w')
async def add_expenses_category_w(call: types.CallbackQuery):
    category = 'w'
    expenses['category'] = category
    print(expenses)
    await call.message.answer(f'Категория расходов: Оплата труда\n Введите название расходов или нажмите /cancel')
    await Expenses.Name.set()


@auth
@dp.callback_query_handler(state=Expenses.Category, text_contains='b')
async def add_expenses_category_b(call: types.CallbackQuery):
    category = 'b'
    expenses['category'] = category
    print(expenses)
    await call.message.answer(f'Категория расходов: Покупка и ремонт инструмента\n '
                              f'Введите название расходов или нажмите /cancel')
    await Expenses.Name.set()


@auth
@dp.callback_query_handler(state=Expenses.Category, text_contains='t')
async def add_expenses_category_t(call: types.CallbackQuery):
    category = 't'
    expenses['category'] = category
    print(expenses)
    await call.message.answer(f'Категория расходов: Транспортные расходы\n '
                              f'Введите название расходов или нажмите /cancel')
    await Expenses.Name.set()


@auth
@dp.callback_query_handler(state=Expenses.Category, text_contains='p')
async def add_expenses_category_p(call: types.CallbackQuery):
    category = 'p'
    expenses['category'] = category
    print(expenses)
    await call.message.answer(f'Категория расходов: Премии\n '
                              f'Введите название расходов или нажмите /cancel')
    await Expenses.Name.set()


@auth
@dp.message_handler(state=Expenses.Name)
async def add_expenses_name(message: types.Message):
    name = message.text
    expenses['name'] = name
    print(expenses)
    await message.answer(f'Название расходов: {name}\n Введите описание расходов или нажмите /cancel')
    await Expenses.Description.set()


@auth
@dp.message_handler(state=Expenses.Description)
async def add_expenses_description(message: types.Message):
    description = message.text
    expenses['description'] = description
    print(expenses)
    await message.answer(f'Описание расходов: {description}\n '
                         f'Введите дату расходов в формате [ГГГГ-ММ-ДД]или нажмите /cancel'
                         )
    await Expenses.Date.set()


@auth
@dp.message_handler(state=Expenses.Date)
async def add_expenses_date(message: types.Message):
    date = message.text
    expenses['date'] = date
    print(expenses)
    await message.answer(f'Дата расходов: {date}\n'
                         f'Введите сумму расходов без копеек или нажмите /cancel')
    await Expenses.Summa.set()


@auth
@dp.message_handler(state=Expenses.Summa)
async def add_expenses_summa(message: types.Message):
    try:
        summa = int(message.text)
    except ValueError:
        await message.answer('Неверное значение, ведите целое число')
        return
    expenses['summa'] = summa
    print(expenses)
    markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Добавить расход', callback_data='confirm')
            ],
            [
                types.InlineKeyboardButton(text='Ввести заново', callback_data='change')
            ]
        ]
    )
    await message.answer(
        f'Сумма расходов: {summa} рублей',
        reply_markup=markup
    )
    await Expenses.Confirm.set()


@auth
@dp.callback_query_handler(text_contains='change', state=Expenses.Confirm)
async def change_expenses(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(f'Введите заново сумму расходов')
    await Expenses.Summa.set()


@auth
@dp.callback_query_handler(text_contains='confirm', state=Expenses.Confirm)
async def confirm_expenses(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    add_expenses(expenses)
    expenses.clear()
    await call.message.answer('Расходы успешно сохранены')
    await state.reset_state()


@auth
@dp.message_handler(commands=['cansel'], state=Expenses)
async def cansel(message: types.Message, state: FSMContext):
    await message.answer('Отменено')
    expenses.clear()
    await state.reset_state()