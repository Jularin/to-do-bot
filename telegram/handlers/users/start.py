from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.callback_data import menu_cd
from keyboards.inline.menu_keybord import todo_action_keybord
from keyboards.inline.action_keyboard import taskmake_subaction_keybord, tasklist_subaction_keybord
from keyboards.inline.delete_keyboard import delete_keybord
from loader import dp


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    """Handle start command"""

    await todo_categories(message)


async def todo_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await todo_action_keybord()

    if isinstance(message, types.Message):
        await message.answer(text=f'Hi, {message.from_user.full_name}!', reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        await message.message.edit_reply_markup(markup)


async def taskmake_subaction(callback: types.CallbackQuery, **kwargs):
    markup = await taskmake_subaction_keybord()
    await callback.message.edit_reply_markup(markup)


async def tasklist_subaction(callback: types.CallbackQuery, **kwargs):
    markup = await tasklist_subaction_keybord()
    await callback.message.edit_reply_markup(markup)


async def delete_key(callback: types.CallbackQuery, **kwargs):
    markup = await delete_keybord()
    await callback.message.edit_reply_markup(markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):

    '''Navigate through levels'''

    current_level = callback_data.get('level')
    action = callback_data.get('action')

    #category = callback_data.get('category')
    #subaction = callback_data.get('subaction')
    #delete = callback_data.get('delete')

    first_level = taskmake_subaction if action == 'make' else tasklist_subaction

    levels = {
        '0': todo_categories,
        '1': first_level,
        '2': delete_key
    }

    current_level_function = levels[current_level]

    print(call['data'])
    await current_level_function(call)
