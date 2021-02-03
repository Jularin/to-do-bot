from aiogram.utils.callback_data import CallbackData

menu_cd = CallbackData('show_menu', 'level', 'category', 'action', 'subaction', 'delete')


def make_callback_data(level, category='0', action='0', subaction='0', delete='0'):
    return menu_cd.new(
        level=level,
        category=category,
        action=action, 
        subaction=subaction, 
        delete=delete
    )
