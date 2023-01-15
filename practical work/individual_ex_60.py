#*Индивидуальное задание 60 
#*Чат-бот поиска статей по ключевой фразе. Программа осуществляет поиск статьи по ключевой фраз, формирует файл из определенного количества ссылок
#*и отправляет их пользователю с помощью чат-бота.

import telebot
import wikipedia
from random import random
from telebot import types

#bot initialization
API_TOKEN = '5952398693:AAF7xvTeDuZnSJc9w32dL8pe0wcoxCVloN0'
bot = telebot.TeleBot(API_TOKEN)

#starting command
@bot.message_handler(commands=['start'])
def start(message):
   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   item1 = types.KeyboardButton('🎫Хочу получить список статей!')
   item2 = types.KeyboardButton('🖥Автор')
   
   
   markup.add(item1,item2)

   bot.send_message(message.chat.id, "👋 Привет, {0.first_name}! Я Ваш бот-помощник! Я осуществляю поиск статьи по ключевой фразе, получаю URL-ссылки статей и формирую из них файл, который отправляю Вам!".format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message): 
    if message.chat.type == 'private':
        if message.text == '🖥Автор':
            bot.send_message(message.chat.id, 'Студент группы У-223' + '\n' +'Александр Деденев'  + '\n' +'GitHub: https://github.com/DedenevAI/DedenevAI')
        
        elif message.text == '🎫Хочу получить список статей!':
            sent = bot.send_message(message.chat.id, 'Введите ключевое слово, по которому будет осуществлен поиск')
            bot.register_next_step_handler(sent, searcher)
        else:
            bot.send_message(message.chat.id, 'Пожалуйста, воспользуйтесь пунктами меню')

@bot.message_handler(func=lambda message: True)
def searcher(message):
    key = message.text
    bot.send_message(message.chat.id, "Выполняю поиск статей по ключевому слову " + key + "......")
    
    wikipedia.set_lang("en")
    wikipedia.random(pages=1)
    links = wikipedia.search(key,results = 5)
    test=[]
    for link in links:
        try:
            #try to load the wikipedia page
            page=wikipedia.page(link, auto_suggest=False, redirect=True, preload=False)
            test.append(page.url)
        except wikipedia.exceptions.PageError:
            #if a "PageError" was raised, ignore it and continue to next link
            continue
        except wikipedia.exceptions.DisambiguationError as e:
            #if a "DisambiguationError" was raised, make random choice from list of options
            s = random.choice(e.options)
            page1 = wikipedia.page(s)
            test.append(page1.url)
    with open("references.txt", "w") as file:
        for row in test:
            f = file.write(row + "\n")
    
    bot.send_message(message.chat.id, "Готово!")
    bot.send_document(message.chat.id, open(r'C:\\Users\\Alex\\DedenevAI\\references.txt', 'rb') )

                
            


            

            
                        






#This function creates a new Thread that calls an internal __retrieve_updates function. 
#This allows the bot to retrieve Updates automatically and notify listeners and message handlers accordingly.
#This part required for the bot to work.
bot.polling(none_stop=True) 