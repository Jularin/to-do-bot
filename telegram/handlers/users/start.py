from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import bot
from keyboards.inline.create_task import start_menu
from loader import dp


@dp.message_handler(CommandStart(), state="*")
async def start(message: types.Message, state: FSMContext):
    """Handle start command"""
    await state.finish()
    await bot.send_message(message.from_user.id, "Выберите действие:", reply_markup=start_menu())


