from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.menu_keyboards import add_worker_keyboard
from states import Worker
from loader import dp
from config import auth
from utils.db_api.db_commands import add_user

worker = {}


@auth
@dp.message_handler(commands=['cansel'], state=Worker)
async def cansel(message: types.Message, state: FSMContext):
    await message.answer('Отменено')
    worker.clear()
    await state.reset_state()


@auth
@dp.message_handler(commands=['add_worker'])
async def add_worker_handler(message: types.Message):
    await message.answer('Введите имя работника или нажмите /cancel')
    await Worker.Name.set()


@auth
@dp.message_handler(state=Worker.Name)
async def add_worker_name_handler(message: types.Message):
    name = message.text
    worker['name'] = name
    print(worker)
    await message.answer(f'Имя работника: {name}\n'
                         f'Введите фамилию работника или нажмите /cancel')
    await Worker.Last_name.set()


@auth
@dp.message_handler(state=Worker.Last_name)
async def add_worker_last_name_handler(message: types.Message):
    markup = await add_worker_keyboard()
    last_name = message.text
    worker['last_name'] = last_name
    print(worker)
    await message.answer(f'Фамилия работника: {last_name}', reply_markup=markup)
    await Worker.Confirm.set()


@auth
@dp.callback_query_handler(text_contains='change', state=Worker.Confirm)
async def change_worker(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    worker.clear()
    await state.reset_state()
    await call.message.answer('Добавление работника отменено')


@auth
@dp.callback_query_handler(text_contains='confirm', state=Worker.Confirm)
async def confirm_worker(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    add_user(worker)
    worker.clear()
    await call.message.answer('Работник успешно добавлен')
    await state.reset_state()
