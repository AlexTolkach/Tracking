from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from utils.db_api.database import user_work_time_table, expenses_table, smeta_table
from utils.db_api.db_commands import get_projects, get_users

# кнопки для add_expenses
menu_cd_project = CallbackData('show_project', 'project_name', 'project_id')


def cb_project(project_name='0', project_id='0'):
    return menu_cd_project.new(project_name=project_name, project_id=project_id)


async def projects_keyboard():
    markup = InlineKeyboardMarkup()
    projects = get_projects()

    for project in projects:
        button_text = f'{project.name}'
        callback_data = cb_project(
            project_name=project.name,
            project_id=project.id,
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data),
        )
    markup.insert(
        InlineKeyboardButton(text='Отмена', callback_data='change'),
    )
    return markup


# кнопки для add_user_work_time
menu_cd_user = CallbackData('show_user', 'user_name', 'user_id')


def cb_user(user_name='0', user_id='0'):
    return menu_cd_user.new(user_name=user_name, user_id=user_id)


async def users_keyboard():
    markup = InlineKeyboardMarkup()
    users = get_users()

    for user in users:
        button_text = f'{user.name}'
        callback_data = cb_user(
            user_name=user.name,
            user_id=user.id,
        )
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data),
        )
    markup.insert(
        InlineKeyboardButton(text='Отмена', callback_data='change')
    )
    return markup


async def add_work_time_create_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Сохранить время', callback_data='confirm')
            ],
            [
                InlineKeyboardButton(text='Отмена', callback_data='change')
            ]
        ]
    )
    return markup


async def add_income_create_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Сохранить сумму', callback_data='confirm')
            ],
            [
                InlineKeyboardButton(text='Ввести заново', callback_data='change')
            ]
        ]
    )
    return markup


async def add_project_create_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Сохранить проект', callback_data='confirm')
            ],
            [
                InlineKeyboardButton(text='Ввести заново', callback_data='change')
            ]
        ]
    )
    return markup


# Кнопки для add_worker
async def add_worker_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Добавить работника', callback_data='confirm')
            ],
            [
                InlineKeyboardButton(text='Отмена', callback_data='change')
            ]
        ]
    )
    return markup


# Кнопка отмены
async def cancel_button():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Отмена', callback_data='change')
            ],
        ]
    )
    return markup
