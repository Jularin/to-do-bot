from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callback_data import make_callback_data


async def group_action_keybord():

    '''Creating make, menege and connect group buttons'''

    CURRNET_LEVEL = 1  # To know where we are
    markup = InlineKeyboardMarkup()

    group_make_callback_data = make_callback_data(
        level=CURRNET_LEVEL + 1, category='group', action='groupmake')
    group_make = InlineKeyboardButton(
        text='Make group', callback_data=group_make_callback_data
    )
    markup.insert(group_make)

    group_manage_callback_data = make_callback_data(
        level=CURRNET_LEVEL + 1, category='group', action='groupmanage'
    )
    group_manage = InlineKeyboardButton(
        text='Manage group', callback_data=group_manage_callback_data
    )
    markup.insert(group_manage)

    group_connect_callback_data = make_callback_data(
        level=CURRNET_LEVEL + 1, category='group', action='groupconnect')
    group_connect = InlineKeyboardButton(
        text='Connect group', callback_data=group_connect_callback_data
    )
    markup.insert(group_connect)

    markup.row(
        InlineKeyboardButton(
            text='Back',
            callback_data=make_callback_data(level=CURRNET_LEVEL - 1)
        )
    )

    return markup
