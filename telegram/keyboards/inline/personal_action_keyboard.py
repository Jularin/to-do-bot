from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callback_data import make_callback_data


async def personal_action_keybord():

    '''Creating make and list task buttons'''

    CURRNET_LEVEL = 1  # To know where we are
    markup = InlineKeyboardMarkup()

    task_make_callback_data = make_callback_data(
        level=CURRNET_LEVEL + 1, category='personal', action='taskmake')
    task_make = InlineKeyboardButton(
        text='Make task', callback_data=task_make_callback_data
    )
    markup.insert(task_make)

    task_list_callback_data = make_callback_data(
        level=CURRNET_LEVEL + 1, category='personal', action='tasklist'
    )
    task_list = InlineKeyboardButton(
        text='List task', callback_data=task_list_callback_data
    )
    markup.insert(task_list)

    markup.row(
        InlineKeyboardButton(
            text='Back',
            callback_data=make_callback_data(level=CURRNET_LEVEL - 1)
        )
    )

    return markup
