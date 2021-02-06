from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_menu():
    start_keyboard = InlineKeyboardMarkup(row_width=1)
    create_task_btn = InlineKeyboardButton("Создать задание", callback_data="create_task")
    see_all_task = InlineKeyboardButton("Посмотреть все задания", callback_data="see_all_task")
    see_task_only_category = InlineKeyboardButton("Посмотреть задания из категорий",
                                                  callback_data="see_task_only_category")
    category_menu = InlineKeyboardButton("Создать категорию", callback_data="category_menu")
    # group_menu = InlineKeyboardButton("Меню группы", callback_data="see_task")
    start_keyboard.add(
        create_task_btn,
        see_all_task,
        see_task_only_category,
        category_menu
    )
    return start_keyboard


def task_menu():
    start_keyboard = InlineKeyboardMarkup()
    skip = InlineKeyboardButton("Пропустить", callback_data="skip")
    back = InlineKeyboardButton("Назад", callback_data="back")
    start_keyboard.add(skip,
                       back)
    return start_keyboard


def true_or_false():
    start_keyboard = InlineKeyboardMarkup()
    true = InlineKeyboardButton("Подтвердить", callback_data="true")
    false = InlineKeyboardButton("Назад", callback_data="false")
    start_keyboard.add(true,
                       false)
    return start_keyboard

# TODO: create group button
