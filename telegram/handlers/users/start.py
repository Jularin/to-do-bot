from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.callback_data import menu_cd
from keyboards.inline.menu_keybord import todo_categories_keybord
from keyboards.inline.personal_action_keyboard import personal_action_keybord
from loader import dp


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    """Handle start command"""

    await todo_categories(message)


async def todo_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await todo_categories_keybord()

    if isinstance(message, types.Message):
        await message.answer(text=f'Hi, {message.from_user.full_name}!', reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        await message.message.edit_reply_markup(markup)


async def personal_action(callback: types.CallbackQuery):
    markup = await personal_action_keybord()
    await callback.message.edit_reply_markup(markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):

    '''Navigate through levels'''

    current_level = callback_data.get('level')

    levels = {
        '0': todo_categories,
        '1': personal_action
    }

    current_level_function = levels[current_level]

    await current_level_function(call)
