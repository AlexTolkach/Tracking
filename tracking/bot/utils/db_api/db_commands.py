import datetime
from typing import List
from utils.db_api.database import users_table, session, user_work_time_table, expenses_table, project_table, smeta_table
from sqlalchemy import select, insert


def add_user(*args):
    user = [*args]
    session.execute(insert(users_table), user)
    session.commit()
    return user


def add_project(*args):
    project = [*args]
    session.execute(insert(project_table), project)
    session.commit()
    return project


def add_user_work_time(*args):
    new_user_work_time = [*args]
    session.execute(insert(user_work_time_table), new_user_work_time)
    session.commit()
    return new_user_work_time


def add_expenses(*args):
    new_expenses = [*args]
    session.execute(insert(expenses_table), new_expenses)
    session.commit()
    return new_expenses


def add_income(*args):
    income = [*args]
    session.execute(insert(smeta_table), income)
    session.commit()
    return income


def get_users() -> List[users_table]:
    return session.execute(select(users_table)).all()


def get_projects() -> List[project_table]:
    return session.execute(select(project_table).limit(3)).all()


def get_employee_work_time_data_for_the_last_five_days(*args):
    data = session.execute(select(user_work_time_table, users_table)
                           .join(user_work_time_table)
                           .order_by(users_table.columns.id)
                           .filter(user_work_time_table.columns.date >
                                   datetime.date.today() - datetime.timedelta(days=5))
                           .filter(users_table.columns.name == ' '.join([*args])))

    return data


a = ''
count_time = 0
for row in get_employee_work_time_data_for_the_last_five_days('Константин'):
    count_time += int(row.time_work)
    if f'Работник: {row.name} {row.last_name}\n' in a:
        a += (f'Дата: {row.date}\n'
              f'Время работы: {row.time_work}ч.\n')
    else:
        a += (f'Работник: {row.name} {row.last_name}\n'
              f'Дата: {row.date}\n'
              f'Время работы: {row.time_work}ч.\n')

print(f'{a}\n'
      f'Суммарное кол-во часов: {count_time}ч.\n'
      f'Сумма: {count_time * 6}р.')
