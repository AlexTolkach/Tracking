import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.menu_keyboards import projects_keyboard, menu_cd_project, users_keyboard, menu_cd_user, \
    add_work_time_create_keyboard, cancel_button
from states import WorkTime
from loader import dp
from config import auth
from utils.db_api.db_commands import add_user_work_time

work_time = {}


@auth
@dp.message_handler(commands=['add_work_time'])
async def add_work_time(message: types.Message):
    markup = await projects_keyboard()
    await message.answer('Выберите проект или нажмите кнопку "Отмена"', reply_markup=markup)
    await WorkTime.Project.set()


@auth
@dp.callback_query_handler(menu_cd_project.filter(), state=WorkTime.Project)
async def add_work_time_project_id(call: types.CallbackQuery, callback_data: dict):
    project_id = callback_data.get('project_id')
    project_name = callback_data.get('project_name')
    work_time['project_id'] = project_id
    print(work_time)
    markup = await users_keyboard()
    await call.message.answer(f'Проект: {project_name}\n'
                              f'Выберите работника или нажмите кнопку "Отмена"',
                              reply_markup=markup)
    await WorkTime.User.set()


@auth
@dp.callback_query_handler(menu_cd_user.filter(), state=WorkTime.User)
async def add_work_time_user_id(call: types.CallbackQuery, callback_data: dict):
    markup = await cancel_button()
    user_id = callback_data.get('user_id')
    user_name = callback_data.get('user_name')
    work_time['user_id'] = user_id
    print(work_time)
    await call.message.answer(f'Работник: {user_name}\n'
                              f'Введите дату в формате [ГГГГ-ММ-ДД]или нажмите кнопку "Отмена"', reply_markup=markup)
    await WorkTime.Date.set()


@auth
@dp.message_handler(state=WorkTime.Date)
async def add_work_time_date(message: types.Message):
    markup = await cancel_button()
    date = message.text
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        await message.answer('Не верный формат даты. Введите дату в формате [ГГГГ-ММ-ДД] или нажмите "Отмена"',
                             reply_markup=markup)
        return

    work_time['date'] = date
    print(work_time)
    await message.answer(f'Дата: {date}\n'
                         f'Введите количество часов в формате [0-23] или нажмите кнопку "Отмена"', reply_markup=markup)
    await WorkTime.Time.set()


@auth
@dp.message_handler(state=WorkTime.Time)
async def add_work_time_time(message: types.Message):
    markup = await add_work_time_create_keyboard()
    try:
        time = int(message.text)
    except ValueError:
        await message.answer('Введите число от 0 до 23')
        return
    work_time['time_work'] = time
    print(work_time)
    await message.answer(f'Время: {time}ч', reply_markup=markup)
    await WorkTime.Confirm.set()


@auth
@dp.callback_query_handler(text_contains='cancel', state=WorkTime)
async def change_work_time(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.answer('Добавление рабочих часов отменено')
    work_time.clear()
    print(work_time)
    await state.reset_state()


@auth
@dp.callback_query_handler(text_contains='confirm', state=WorkTime.Confirm)
async def confirm_work_time(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    add_user_work_time(work_time)
    work_time.clear()
    await call.message.answer('Часы работы успешно добавлены')
    await state.reset_state()
