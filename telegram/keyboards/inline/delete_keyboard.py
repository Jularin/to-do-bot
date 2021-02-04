from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callback_data import make_callback_data


async def delete_keybord():

    '''create delete'''

    CURRNET_LEVEL = 2  # To know where we are
    markup = InlineKeyboardMarkup()

    delete_callback_data = make_callback_data(
        level=CURRNET_LEVEL + 1, action='list', delete='del')
    delete = InlineKeyboardButton(
        text='Delete', callback_data=delete_callback_data
    )
    markup.insert(delete)

    markup.row(
        InlineKeyboardButton(
            text='Back',
            callback_data=make_callback_data(level=CURRNET_LEVEL - 1)
        )
    )

    return markup
