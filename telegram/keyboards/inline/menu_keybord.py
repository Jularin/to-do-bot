from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callback_data import make_callback_data


async def todo_action_keybord():

    '''Creating make and list task buttons'''

    CURRNET_LEVEL = 0  # To know where we are
    markup = InlineKeyboardMarkup()

    task_make_callback_data = make_callback_data(
        level=CURRNET_LEVEL + 1, action='taskmake')
    task_make = InlineKeyboardButton(
        text='Make task', callback_data=task_make_callback_data
    )
    markup.insert(task_make)

    task_list_callback_data = make_callback_data(
        level=CURRNET_LEVEL + 1, action='tasklist'
    )
    task_list = InlineKeyboardButton(
        text='List task', callback_data=task_list_callback_data
    )
    markup.insert(task_list)

    return markup
