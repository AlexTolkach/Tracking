from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.menu_keyboards import projects_keyboard, menu_cd_project, add_income_create_keyboard
from loader import dp
from config import auth
from utils.db_api.db_commands import add_income
from states import Income

income = {}


@auth
@dp.message_handler(commands=['cansel'], state=Income)
async def cansel(message: types.Message, state: FSMContext):
    await message.answer('Отменено')
    await state.reset_state()


@auth
@dp.message_handler(commands=['add_income'])
async def add_income_project_keyboard(message: types.Message):
    markup = await projects_keyboard()
    await message.answer('Выберите проект или нажмите /cancel', reply_markup=markup)
    await Income.Project.set()


@auth
@dp.callback_query_handler(menu_cd_project.filter(), state=Income.Project)
async def add_income_project_id(call: types.CallbackQuery, callback_data: dict):
    project_id = callback_data.get('project_id')
    project_name = callback_data.get('project_name')
    income['project_id'] = project_id
    print(income)
    await call.message.answer(f'Проект: {project_name}\n'
                              f'Введите дату в формате [ГГГГ-ММ-ДД] или нажмите /cancel')
    await Income.Date.set()


@auth
@dp.message_handler(state=Income.Date)
async def add_income_date(message: types.Message):
    date = message.text
    income['date'] = date
    print(income)
    await message.answer(f'Введите сумму в рублях или нажмите /cancel')
    await Income.Summa.set()


@auth
@dp.message_handler(state=Income.Summa)
async def add_income_summa(message: types.Message):
    markup = await add_income_create_keyboard()
    try:
        summa = int(message.text)
    except ValueError:
        await message.answer('Неверное значение, ведите целое число')
        return
    income['summa'] = summa
    print(income)
    await message.answer(f'Сумма {summa} руб.', reply_markup=markup)
    await Income.Confirm.set()


@auth
@dp.callback_query_handler(text_contains='change', state=Income.Confirm)
async def change_income(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer('Введите количество часов заново')
    await Income.Confirm.set()


@auth
@dp.callback_query_handler(text_contains='confirm', state=Income.Confirm)
async def confirm_income(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    add_income(income)
    income.clear()
    await call.message.answer('Сумма успешно добавлена')
    await state.reset_state()
