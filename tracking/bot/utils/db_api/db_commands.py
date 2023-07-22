from typing import List
from utils.db_api.database import users_table, session, user_work_time_table, expenses_table, project_table, smeta_table
from sqlalchemy import select, insert


def add_user(*args):
    user = [*args]
    session.execute(insert(users_table), user)
    session.commit()
    return user


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
