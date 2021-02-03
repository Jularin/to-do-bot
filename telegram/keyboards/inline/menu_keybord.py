from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callback_data import make_callback_data

#menu_cd,

async def todo_categories_keybord():
    CURRNET_LEVEL = 0
    markup = InlineKeyboardMarkup()

    personal_callback_data = make_callback_data(level=CURRNET_LEVEL + 1, category='personal')
    personal_category = InlineKeyboardButton(
        text='Personal todo', callback_data=personal_callback_data
    )
    markup.insert(personal_category)

    group_callback_data = make_callback_data(level=CURRNET_LEVEL + 1, category='group')
    group_category = InlineKeyboardButton(
        text='Group todo', callback_data=group_callback_data
    )
    markup.insert(group_category)

    return markup
