import telebot
import const

token = const.token
bot = telebot.TeleBot(token)
connect = const.conn
cursor = const.cursor
or_name = const.order_menu
or_cou = const.order_count


@bot.message_handler(commands=['start'])
def handler_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('/dev_ops', '/ввод', '/вывод')
    user_markup.row('/проверить регу', '/зарегистрировать', '/покинуть')
    bot.send_message(message.from_user.id, 'Добро пожаловать...', reply_markup=user_markup)


@bot.message_handler(commands=['ввод'])
def handler_input(message):
    if message.chat.type == 'private':
        if message.text == '/ввод':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('/наименование', '/кол-во')
            bot.send_message(message.from_user.id, 'Добавить товар ', reply_markup=user_markup)


@bot.message_handler(commands=['наименование', 'колич',
                               'хлеб', 'булочки', 'пирожные',
                               'чай', 'молоко', 'кофе',
                               '1', '2', '3',
                               '4', '5', '10'])
def handler_inp_name(message):
    if message.text == '/наименование':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row(or_name[0], or_name[1], or_name[2])
        user_markup.row(or_name[3], or_name[4], or_name[5])
        bot.send_message(message.from_user.id, 'Наименование', reply_markup=user_markup)
    elif message.text == '/хлеб':
        mess_br = '/колич'
        if mess_br == '/колич':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('/1', '/2', '/3')
            user_markup.row('/4', '/5', '/10')
            bot.send_message(message.from_user.id, 'количество', reply_markup=user_markup)
            if message.text == '/1':
                counn = 1
                name = 'хлеб'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен хлеб в количестве 1-й штуки')
            elif message.text == '/2':
                counn = 2
                name = 'хлеб'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен хлеб в количестве 2-х штук')
            elif message.text == '/3':
                counn = 3
                name = 'хлеб'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен хлеб в количестве 3-х штук')
            elif message.text == '/4':
                counn = 4
                name = 'хлеб'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен хлеб в количестве 4-х штук')
            elif message.text == '/5':
                counn = 5
                name = 'хлеб'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен хлеб в количестве 5-и штук')
            elif message.text == '/10':
                counn = 10
                name = 'хлеб'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен хлеб в количестве 10-и штук')
        else:
            bot.send_message(message.from_user.id, 'Ошибка! Введите число с клавиатуры!')
    elif message.text == '/булочки':
        mess_br = '/колич'
        if mess_br == '/колич':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('/1', '/2', '/3')
            user_markup.row('/4', '/5', '/10')
            bot.send_message(message.from_user.id, 'количество', reply_markup=user_markup)
            if message.text == '/1':
                counn = 1
                name = 'булочки'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлены булочки в количестве 1-й штуки')
            elif message.text == '/2':
                counn = 1
                name = 'булочки'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлены булочки в количестве 2-х штук')
            elif message.text == '/3':
                counn = 3
                name = 'булочки'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлены булочки в количестве 3-х штук')
            elif message.text == '/4':
                counn = 4
                name = 'булочки'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлены булочки в количестве 4-х штук')
            elif message.text == '/5':
                counn = 5
                name = 'булочки'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлены булочки в количестве 5-и штук')
            elif message.text == '/10':
                counn = 10
                name = 'булочки'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлены булочки в количестве 10-и штук')
        else:
            bot.send_message(message.from_user.id, 'Ошибка! Введите число с клавиатуры!')
    elif message.text == '/пирожные':
        mess_br = '/колич'
        if mess_br == '/колич':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('/1', '/2', '/3')
            user_markup.row('/4', '/5', '/10')
            bot.send_message(message.from_user.id, 'количество', reply_markup=user_markup)
            if message.text == '/1':
                counn = 1
                name = 'пирожные'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлены пирожные в количестве 1-й штуки')
            elif message.text == '/2':
                counn = 1
                name = 'пирожные'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлены пирожные в количестве 2-х штук')
            elif message.text == '/3':
                counn = 3
                name = 'пирожные'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлены пирожные в количестве 3-х штук')
            elif message.text == '/4':
                counn = 4
                name = 'пирожные'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлены пирожные в количестве 4-х штук')
            elif message.text == '/5':
                counn = 5
                name = 'пирожные'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлены пирожные в количестве 5-и штук')
            elif message.text == '/10':
                counn = 10
                name = 'пирожные'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлены пирожные в количестве 10-и штук')
        else:
            bot.send_message(message.from_user.id, 'Ошибка! Введите число с клавиатуры!')
    elif message.text == '/чай':
        mess_br = '/колич'
        if mess_br == '/колич':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('/1', '/2', '/3')
            user_markup.row('/4', '/5', '/10')
            bot.send_message(message.from_user.id, 'количество', reply_markup=user_markup)
            if message.text == '/1':
                counn = 1
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 1-й штуки')
            elif message.text == '/2':
                counn = 1
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 2-х штук')
            elif message.text == '/3':
                counn = 3
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 3-х штук')
            elif message.text == '/4':
                counn = 4
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 4-х штук')
            elif message.text == '/5':
                counn = 5
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 5-и штук')
            elif message.text == '/10':
                counn = 10
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 10-и штук')
        else:
            bot.send_message(message.from_user.id, 'Ошибка! Введите число с клавиатуры!')
    elif message.text == '/молоко':
        mess_br = '/колич'
        if mess_br == '/колич':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('/1', '/2', '/3')
            user_markup.row('/4', '/5', '/10')
            bot.send_message(message.from_user.id, 'количество', reply_markup=user_markup)
            if message.text == '/1':
                counn = 1
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 1-й штуки')
            elif message.text == '/2':
                counn = 1
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 2-х штук')
            elif message.text == '/3':
                counn = 3
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 3-х штук')
            elif message.text == '/4':
                counn = 4
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 4-х штук')
            elif message.text == '/5':
                counn = 5
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 5-и штук')
            elif message.text == '/10':
                counn = 10
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 10-и штук')
        else:
            bot.send_message(message.from_user.id, 'Ошибка! Введите число с клавиатуры!')
    elif message.text == '/кофе':
        mess_br = '/колич'
        if mess_br == '/колич':
            user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            user_markup.row('/1', '/2', '/3')
            user_markup.row('/4', '/5', '/10')
            bot.send_message(message.from_user.id, 'количество', reply_markup=user_markup)
            if message.text == '/1':
                counn = 1
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 1-й штуки')
            elif message.text == '/2':
                counn = 1
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 2-х штук')
            elif message.text == '/3':
                counn = 3
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 3-х штук')
            elif message.text == '/4':
                counn = 4
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 4-х штук')
            elif message.text == '/5':
                counn = 5
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 5-и штук')
            elif message.text == '/10':
                counn = 10
                name = 'чай'
                cursor.execute('INSERT INTO orders(name, count) VALUES (?,?)', (name, counn))
                connect.commit()
                bot.send_message(message.from_user.id, 'Добавлен чай в количестве 10-и штук')
        else:
            bot.send_message(message.from_user.id, 'Ошибка! Введите число с клавиатуры телеграма!')


"""@bot.message_handler(commands=['количество'])
def handler_inp_count(message):
    if message.text == '/количество':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('1', '2', '3')
        user_markup.row('4', '5', '10')
        bot.send_message(message.from_user.id, 'количество')"""


@bot.message_handler(commands=['вывод'])
def handler_output(message):
    if message.text == '/вывод':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('/товар', '/кол-во')
        bot.send_message(message.from_user.id, 'Вывести данные о товарах', reply_markup=user_markup)


@bot.message_handler(commands=['товар'])
def handler_out_name(message):
    if message.text == '/товар':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('хлеб', 'булочки', 'пирожные')
        user_markup.row('вода', 'молоко', 'кофе')
        bot.send_message(message.from_user.id, 'Наименование', reply_markup=user_markup)


@bot.message_handler(commands=['кол-во'])
def handler_out_count(message):
    if message.text == '/кол-во':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('1', '5', '10')
        user_markup.row('25', '50', '100')
        bot.send_message(message.from_user.id, 'кол-во', reply_markup=user_markup)


@bot.message_handler(commands=['зарегистрировать'])
def handler_reg(message):
    people_id = message.chat.id
    cursor.execute(f"SELECT user_id FROM urs WHERE user_id = {people_id}")
    data = cursor.fetchone()
    print(data)
    if data is None:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        nickname = message.from_user.username
        cursor.execute('INSERT INTO urs (user_id, user_name, nickname) VALUES(?,?,?)', (user_id, user_name, nickname))
        connect.commit()
        bot.send_message(message.from_user.id, 'Зарегистрирован')
    else:
        bot.send_message(message.from_user.id, 'Ты уже зарегистрирован!')


@bot.message_handler(commands=['покинуть'])
def handler_del(message):
    people_id = message.chat.id
    cursor.execute(f"DELETE FROM urs WHERE user_id = {people_id}")
    connect.commit()
    data = cursor.fetchone()
    print(data)
    if data is None:
        bot.send_message(message.from_user.id, 'Вы не состоите в нашей базе данных!')
    else:
        bot.send_message(message.from_user.id, 'Удален!')


@bot.message_handler(commands=['stop'])
def handler_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Скрыл', reply_markup=hide_markup)


bot.polling(non_stop=True, interval=0)
