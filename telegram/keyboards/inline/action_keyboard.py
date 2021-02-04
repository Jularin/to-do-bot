from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callback_data import make_callback_data


async def taskmake_subaction_keybord():

    '''create skip and back buttons'''

    CURRNET_LEVEL = 1  # To know where we are
    markup = InlineKeyboardMarkup()

    skip_callback_data = make_callback_data(
        level=CURRNET_LEVEL + 1, action='taskmake', subaction='skip')
    skip = InlineKeyboardButton(
        text='Skip', callback_data=skip_callback_data
    )
    markup.insert(skip)

    markup.row(
        InlineKeyboardButton(
            text='Back',
            callback_data=make_callback_data(level=CURRNET_LEVEL - 1)
        )
    )

    return markup


async def tasklist_subaction_keybord():
    CURRNET_LEVEL = 1  # To know where we are
    markup = InlineKeyboardMarkup()

    alltask_callback_data = make_callback_data(
        level=CURRNET_LEVEL + 1, action='tasklist', subaction='all')
    alltask = InlineKeyboardButton(
        text='All task', callback_data=alltask_callback_data
    )
    markup.insert(alltask)

    category_callback_data = make_callback_data(
        level=CURRNET_LEVEL + 1, action='tasklist', subaction='category')
    category = InlineKeyboardButton(
        text='All task', callback_data=category_callback_data
    )
    markup.insert(category)

    markup.row(
        InlineKeyboardButton(
            text='Back',
            callback_data=make_callback_data(level=CURRNET_LEVEL - 1)
        )
    )

    return markup
