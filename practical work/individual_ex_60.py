#Индивидуальное задание 60 
#Чат-бот поиска статей по ключевой фразе. Программа осуществляет поиск статьи по ключевой фраз, формирует файл из определенного количества ссылок
#и отправляет их пользователю с помощью чат-бота.

import telebot
from telebot import types

#bot initialization
bot = telebot.TeleBot('5952398693:AAF7xvTeDuZnSJc9w32dL8pe0wcoxCVloN0')

#starting command
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)\

#This function creates a new Thread that calls an internal __retrieve_updates function. 
#This allows the bot to retrieve Updates automatically and notify listeners and message handlers accordingly.
#This part required for the bot to work.
bot.polling(none_stop=True, interval=0) 