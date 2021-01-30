from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    """Handle start command"""
    await message.answer(
        f'Hi, {message.from_user.full_name}!'
    )
