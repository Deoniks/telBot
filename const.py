import telebot
import sqlite3

token = '********:**************'
bot = telebot.TeleBot(token)

conn = sqlite3.connect('db/telbot.db', check_same_thread=False)
cursor = conn.cursor()

order_menu = ['хлеб', 'булочки', '/пирожные', '/чай', '/молоко', '/кофе']
order_count = ['/1', '/2' '/3'
                     '/4', '/5', '/10']


@bot.message_handler(commands=order_menu)
def mess(message):
    n = message.text
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('хлеб', 'булочки', 'пирожные')
    bot.send_message(message.from_user.id, 'вводим', reply_markup=user_markup)
    print(n)

bot.polling(non_stop=True, interval=0)

"""if bread in order_menu:
    print('ok')
else:
    print('dont no')"""
