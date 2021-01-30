import sqlite3

con = sqlite3.connect('mydatabase.db')
cur = con.cursor()


# TODO: перенести создание таблицы туда где пользователь нажимет /start в телеге
def creat_table():
    lst = 'l_' + '42'
    cur.execute(f'''
    CREATE TABLE {lst} (
    name_task TEXT NOT NULL,
    description TEXT,
    deadline TEXT);
    ''')

# creat_table()
