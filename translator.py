from cgitb import text
from email.mime import audio
import telebot
from googletrans import Translator
from gtts import gTTS
import datetime
from telebot import types


token = '5554011699:AAFzA33dd_MDa9EE3YNZUXU2gCfUU-eobu0'

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def message_send(message):
    
    bot.send_message(message.chat.id, f'привет  {message.chat.first_name}.Я переводчик-бот')
    
@bot.message_handler(commands=['alphabet'])
def alphabet(message):
    markup = types.ReplyKeyboardMarkup()
    buttonA = types.KeyboardButton('A')
    buttonB = types.KeyboardButton('B')
    buttonC = types.KeyboardButton('C')
    buttonD = types.KeyboardButton('D')
    buttonE = types.KeyboardButton('E')
    markup.row(buttonA,buttonB)
    markup.row(buttonC,buttonD)
    markup.row(buttonE)
    bot.send_message(message.chat.id, 'working',reply_markup=markup)
    
@bot.message_handler(commands=['translator'])
def message_send2(message):
    markup = types.ReplyKeyboardMarkup()
    ru = types.KeyboardButton('ru')
    en = types.KeyboardButton('en')
    ky = types.KeyboardButton('ky')
    markup.row(ru,en,ky)
    bot.send_message(message.chat.id, 'Выберите, на какой язык нужно перевести',reply_markup=markup)
@bot.message_handler(content_types='text')
def sendMessage(message):
    translator = Translator()
    translate_to = translator.translate(message.text,dest='ru').text
    voise_message = gTTS(translate_to, lang='en',slow=False)
    
    # if message.text == en.text:
    #   translate_to = translator.translate(message.text,dest='en').text
    #   voise_message = gTTS(translate_to, lang='en',slow=False)
    # elif message.text == ru.text:
    #      translate_to = translator.translate(message.text,dest='ru').text
    #      voise_message = gTTS(translate_to, lang='ru',slow=False)
    # elif message.text == ky.text:
    #     translate_to = translator.translate(message.text,dest='ky').text
    #     voise_message = gTTS(translate_to, lang='ky',slow=False)
    file_name = datetime.datetime.now()
    voise_message.save(f'voices/{file_name}.mp3')
    voise_mess = open(f'voices/{file_name}.mp3','rb')
    bot.send_audio(message.chat.id, audio = voise_mess)
    bot.send_message(message.chat.id, translate_to)
    
print('Бот запущен...')
bot.infinity_polling()


# import telebot
# import requests

# bot = telebot.TeleBot('5277237770:AAEfUMIw4QV15daseekd_TNpLiijMQ_8-yY')

# weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=fa0c69065a227aae0ae1081d5953bcfa&units=metric'



# @bot.message_handler(commands=['start', 'hi'])
# def welcome(message):
#     bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name} ')

# @bot.message_handler(content_types=['text']) 
# def get_text_messages(message):

#     if message.text == 'привет':
#         bot.send_message(message.chat.id, f'привет {message.from_user.first_name}')
#     elif message.text.lower() == '/help':
#         bot.send_message(message.chat.id, '/help погода, /help cord, /help hello')
#     elif message.text.lower() == '/help погода':
#         bot.send_message(message.chat.id,'если хочешь узнать погоду пример: погода ru moscow')
#     elif message.text.lower() == '/help cord':
#         bot.send_message(message.chat.id,'если хочешь узнать кординаты пример: cord ru moscow')
#     elif message.text.lower() == '/help hello':
#         bot.send_message(message.chat.id,'напиши привет!')
#     elif message.text.split(' ')[0] == 'погода':
#         textsplitted = message.text.lower().split(' ')
#         city = textsplitted[2]
#         country = textsplitted[1]
#         w_final_url = weather_url.format(city=city, country=country)
#         response = requests.get(w_final_url)
#         pog_json  = response.json()
#         country = pog_json['sys']['country']
#         gor = pog_json['name']
#         temp = pog_json['main']['temp']
#         feel = pog_json['main']['feels_like']
#         wind = pog_json['wind']['speed']
#         bot.send_message(message.chat.id,f'код страны { country }')
#         bot.send_message(message.chat.id,f'погода в городе { gor }')
#         bot.send_message(message.chat.id,f'{ temp } градусов')
#         bot.send_message(message.chat.id,f'ошушается как { feel }')
#         bot.send_message(message.chat.id,f'скорость ветра { wind } км/ч')
    
#     elif message.text.split(' ')[0] == 'cord':
#         textsplitted = message.text.lower().split(' ')
#         city = textsplitted[2]
#         country = textsplitted[1]
#         w_final_url = weather_url.format(city=city, country=country)
#         response = requests.get(w_final_url)
#         cord_json  = response.json()
#         lat = cord_json['coord']['lat'] 
#         lon = cord_json['coord']['lon'] 
#         bot.send_message(message.chat.id,f' широта : { lat }')
#         bot.send_message(message.chat.id,f'долгота : { lon }')

#     else:
#         bot.send_message(message.chat.id, 'я не понимаю что это значит напишите /help')

# print('Бот работает.....')
# bot.infinity_polling()