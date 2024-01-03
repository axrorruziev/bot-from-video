import telebot
from telebot import types

bot = telebot.TeleBot('6759569134:AAFmfoIwqbEryXwY_kZatU54YPSoAxv8aOQ')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'<b>привет</b> {message.from_user.first_name} введите site чтобы выбрать сайт',
                     parse_mode='html')


@bot.message_handler(commands='site')
def site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('YOUTUBE', url='https//youtube.com'))
    markup.add(types.InlineKeyboardButton('GOOGLE', url='https//google.com'))
    bot.send_message(message, 'какой сайт хотите открыть ?', reply_markup=markup)


bot.infinity_polling()
