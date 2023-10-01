from aiogram.dispatcher.filters.state import StatesGroup, State


class Expenses(StatesGroup):
    Category = State()
    Name = State()
    Description = State()
    Date = State()
    Summa = State()
    Confirm = State()


class WorkTime(StatesGroup):
    Project = State()
    User = State()
    Date = State()
    Time = State()
    Confirm = State()


class Income(StatesGroup):
    Project = State()
    Date = State()
    Summa = State()
    Confirm = State()


class Project(StatesGroup):
    Name = State()
    Address = State()
    Start_date = State()
    End_date = State()
    Confirm = State()


class Worker(StatesGroup):
    Name = State()
    Last_name = State()
    Confirm = State()


class Salary(StatesGroup):
    Name = State()
    Confirm = State()
