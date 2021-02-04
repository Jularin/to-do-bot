from aiogram.utils.callback_data import CallbackData

menu_cd = CallbackData('show_menu', 'level', 'action', 'subaction', 'delete')


def make_callback_data(level, action='0', subaction='0', delete='0'):
    '''Creating valid callbak data'''

    return menu_cd.new(
        level=level,
        action=action,
        subaction=subaction,
        delete=delete
    )
