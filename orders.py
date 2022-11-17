import sqlite3
import const

conn = const.conn
curs = const.cursor
or_name = const.order_menu


def db_order_inp(name: str, count: int):
    curs.execute('INSERT INTO orders (name, count) VALUES (?, ?)', (name, count))
    conn.commit()


