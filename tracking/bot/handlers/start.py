from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from config import auth
from loader import dp


@auth
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}\n'
                         f'жми /menu')


@auth
@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    await message.answer(f'Меню\n'
                         f'1. Добавить расходы /add_expenses\n'
                         f'2. Добавить доходы /add_income\n'
                         f'3. Добавить время работы /add_work_time\n'
                         f'4. Добавить новый проект /add_project\n'
                         f'5. Добавить работника /add_worker\n'
                         f'6. Рассчитать зарплату за последние 5 дней /calculate_salary'
                         )
