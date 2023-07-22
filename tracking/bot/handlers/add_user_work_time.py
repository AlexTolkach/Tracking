from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.menu_keyboards import projects_keyboard, menu_cd_project, users_keyboard, menu_cd_user, \
    add_work_time_create_keyboard
from states import WorkTime
from loader import dp
from config import auth
from utils.db_api.db_commands import add_user_work_time

work_time = {}


@auth
@dp.message_handler(commands=['cansel'], state=WorkTime)
async def cansel(message: types.Message, state: FSMContext):
    await message.answer('Отменено')
    work_time.clear()
    await state.reset_state()


@auth
@dp.message_handler(commands=['add_work_time'])
async def add_work_time(message: types.Message):
    markup = await projects_keyboard()
    await message.answer('Выберите проект или нажмите /cancel', reply_markup=markup)
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
                              f'Выберите работника или нажмите /cancel',
                              reply_markup=markup)
    await WorkTime.User.set()


@auth
@dp.callback_query_handler(menu_cd_user.filter(), state=WorkTime.User)
async def add_work_time_user_id(call: types.CallbackQuery, callback_data: dict):
    user_id = callback_data.get('user_id')
    user_name = callback_data.get('user_name')
    work_time['user_id'] = user_id
    print(work_time)
    await call.message.answer(f'Работник: {user_name}\n'
                              f'Введите дату в формате [ГГГГ-ММ-ДД]или нажмите /cancel')
    await WorkTime.Date.set()


@auth
@dp.message_handler(state=WorkTime.Date)
async def add_work_time_date(message: types.Message):
    date = message.text
    work_time['date'] = date
    print(work_time)
    await message.answer(f'Дата: {date}\n'
                         f'Введите количество часов в формате [0-23] или нажмите /cancel')
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
@dp.callback_query_handler(text_contains='change', state=WorkTime.Confirm)
async def change_work_time(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer('Введите количество часов заново')
    await WorkTime.Time.set()


@auth
@dp.callback_query_handler(text_contains='confirm', state=WorkTime.Confirm)
async def confirm_work_time(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    add_user_work_time(work_time)
    work_time.clear()
    await call.message.answer('Часы работы успешно добавлены')
    await state.reset_state()
