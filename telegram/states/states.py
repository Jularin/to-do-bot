from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateTask(StatesGroup):
    name = State()
    description = State()
    category = State()
    deadline = State()
    check = State()

