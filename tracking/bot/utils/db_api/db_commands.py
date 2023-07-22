from typing import List

from utils.db_api.database import users_table, session, user_work_time_table, expenses_table, project_table, smeta_table
from sqlalchemy import select, insert


async def add_user(**kwargs):
    new_user = users_table(**kwargs)
    session.add(new_user)
    session.commit()
    return new_user


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


async def add_smeta(**kwargs):
    new_smeta = smeta_table(**kwargs)
    session.add(new_smeta)
    session.commit()
    return new_smeta


def get_users() -> List[users_table]:
    return session.execute(select(users_table)).all()


def get_projects() -> List[project_table]:
    return session.execute(select(project_table).limit(3)).all()
