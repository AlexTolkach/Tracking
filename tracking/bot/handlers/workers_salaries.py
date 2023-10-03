from aiogram import types

from keyboards.inline.menu_keyboards import users_keyboard, menu_cd_user
from loader import dp
from config import auth
from aiogram.dispatcher import FSMContext
from states import Salary
from utils.db_api.db_commands import get_employee_work_time_data_for_the_last_five_days


@auth
@dp.message_handler(commands=['calculate_salary'])
async def get_worker_name_step1(message: types.Message):
    markup = await users_keyboard()
    await message.answer('Выберите работника или нажмите кнопку "Отмена"', reply_markup=markup)
    await Salary.Name.set()


@auth
@dp.callback_query_handler(menu_cd_user.filter(), state=Salary.Name)
async def calculate_salary_worker(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    name = callback_data.get('user_name')
    report = ''
    count_time = 0
    for row in get_employee_work_time_data_for_the_last_five_days(name):
        count_time += int(row.time_work)
        if f'Работник: {row.name} {row.last_name}\n' in report:
            report += (f'Дата: {row.date}\n'
                       f'Время работы: {row.time_work}ч.\n')
        else:
            report += (f'Работник: {row.name} {row.last_name}\n'
                       f'Дата: {row.date}\n'
                       f'Время работы: {row.time_work}ч.\n')

    await call.message.answer(f'{report}\n'
                              f'Суммарное кол-во часов: {count_time}ч.\n'
                              f'Сумма: {count_time * 6}р.')
    await state.reset_state()


@auth
@dp.callback_query_handler(text_contains='change', state=Salary)
async def change_worker(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await state.reset_state()
    await call.message.answer('Отменено')
