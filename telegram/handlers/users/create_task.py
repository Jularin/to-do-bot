from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import bot
from loader import dp
from states.states import CreateTask
from keyboards.inline.create_task import true_or_false, task_menu


@dp.callback_query_handler(lambda c: c.data == "create_task", state="*")
async def create_task(callback_query: types.CallbackQuery):
    """User pressed create task button"""
    await bot.edit_message_text(chat_id=callback_query.from_user.id, text="Введите название ",
                                message_id=callback_query.message.message_id)
    await CreateTask.name.set()


@dp.message_handler(state=CreateTask.name)
async def process_task_name(message: types.Message, state: FSMContext):
    """Process task name"""
    async with state.proxy() as data:
        data['task_name'] = message.text
    await bot.send_message(message.from_user.id, "Введите описание задания")
    await CreateTask.next()


@dp.message_handler(state=CreateTask.description)
async def process_task_description(message: types.Message, state: FSMContext):
    """Process task description"""
    async with state.proxy() as data:
        data['task_description'] = message.text
    await bot.send_message(message.from_user.id, "Введите категорию")
    await CreateTask.next()


@dp.message_handler(state=CreateTask.category)
async def process_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await bot.send_message(message.from_user.id, "Введите дедлайн")
    await CreateTask.next()


@dp.message_handler(state=CreateTask.deadline)
async def process_deadline(message: types.Message, state: FSMContext):
    """Process task deadline"""
    async with state.proxy() as data:
        data['task_deadline'] = message.text
    await CreateTask.next()
    await bot.send_message(message.from_user.id, "Подтвердите создание 'Тут будет описание задания'",
                           reply_markup=true_or_false())


@dp.callback_query_handler(lambda c: c.data == "true", state=CreateTask.check)
async def process_true(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, text="Задание добавлено!",
                                message_id=callback_query.message.message_id)


@dp.callback_query_handler(lambda c: c.data =='back', state='*')
async def back(callback_query: types.CallbackQuery, state: FSMContext):
    await CreateTask.previous()


@dp.callback_query_handler(lambda c: c.data =='back', state='*')
async def back(callback_query: types.CallbackQuery, state: FSMContext):
    await CreateTask.previous()


@dp.callback_query_handler(lambda c: c.data == "see_task")
async def create_task(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id, text="вы нажали другую кнопку",
                                message_id=callback_query.message.message_id)

