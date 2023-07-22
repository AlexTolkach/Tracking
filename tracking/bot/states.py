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


class Menu(StatesGroup):
    Main = State()
    Expenses = State()
    WorkTime = State()
    Income = State()
