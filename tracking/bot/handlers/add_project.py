from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.menu_keyboards import add_project_create_keyboard
from states import Project
from loader import dp
from config import auth
from utils.db_api.db_commands import add_project

project = {}


@auth
@dp.message_handler(commands=['cansel'], state=Project)
async def cansel(message: types.Message, state: FSMContext):
    await message.answer('Отменено')
    project.clear()
    await state.reset_state()


@auth
@dp.message_handler(commands=['add_project'])
async def add_project_handler(message: types.Message):
    await message.answer('Введите название проекта или нажмите /cancel')
    await Project.Name.set()


@auth
@dp.message_handler(state=Project.Name)
async def add_project_name_handler(message: types.Message):
    name = message.text
    project['name'] = name
    print(project)
    await message.answer('Введите адрес проекта или нажмите /cancel')
    await Project.Address.set()


@auth
@dp.message_handler(state=Project.Address)
async def add_project_address_handler(message: types.Message):
    address = message.text
    project['address'] = address
    print(project)
    await message.answer(f'Введите дату начала проекта в формате [ГГГГ-ММ-ДД] или нажмите /cancel')
    await Project.Start_date.set()


@auth
@dp.message_handler(state=Project.Start_date)
async def add_project_start_date_handler(message: types.Message):
    markup = await add_project_create_keyboard()
    start_date = message.text
    project['start_date'] = start_date
    print(project)
    await message.answer(f'Дата начала проекта: {start_date}', reply_markup=markup)
    await Project.Confirm.set()


@auth
@dp.callback_query_handler(text_contains='change', state=Project.Confirm)
async def change_income(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer('Введите дату заново')
    await Project.Start_date.set()


@auth
@dp.callback_query_handler(text_contains='confirm', state=Project.Confirm)
async def confirm_income(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    add_project(project)
    project.clear()
    await call.message.answer('Проект успешно добавлен')
    await state.reset_state()
