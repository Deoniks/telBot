import telebot
import sqlite3

token = '********:**************'
bot = telebot.TeleBot(token)

conn = sqlite3.connect('db/telbot.db', check_same_thread=False)
cursor = conn.cursor()

order_menu = ['хлеб', 'булочки', '/пирожные', '/чай', '/молоко', '/кофе']
order_count = ['/1', '/2' '/3'
                     '/4', '/5', '/10']
