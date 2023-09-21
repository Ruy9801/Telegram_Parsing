import telebot
from telebot import types
import random
from main import main
from main import title_img


TOKEN =  '6498029245:AAEZPBQnxNNJZuRcUwkRY2UNJTzYnKa9joE'


bot = telebot.TeleBot(TOKEN)

keyboard = types.ReplyKeyboardMarkup()

button1 = types.KeyboardButton('/start')
button2 = types.KeyboardButton('Description')
button3 = types.KeyboardButton('Quit')

keyboard.add(button1,button2,button3)


@bot.message_handler(commands=['start'])
def start_message(message):
    msg = bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}, начнем парсинг?', reply_markup=keyboard)
    
    data = main()
    print(message.text)

    bot.register_next_step_handler(msg, check_str)


@bot.message_handler(commands=['Description'])      
def check_str(message):
    
    if  message.text.isalnum():
        res = title_img()
        
        num = 1
        for k,v in res.items():
            media = f'{num}. {k}\n{v}'
            bot.send_message(message.chat.id, media)
            num += 1
    print(message.text)
        
    bot.send_message(message.chat.id, 'some title news you can see Description of this news and Photo')
    msg = bot.send_message(message.chat.id, 'Введите номер стотьи в наличии 20 статей!')







@bot.message_handler(commands=['Quit'])
def quite(message):
    print(message.text)
    bot.send_message(message.chat.id, 'До свидания')
        
def check_digit(message):
    
    if message.text.isdigit():

        data = start_message('/start')
        media = data[int(message)-1]
        bot.send_message(message.chat.id, media)



bot.polling()