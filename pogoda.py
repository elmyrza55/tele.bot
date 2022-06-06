
import telebot
import requests

bot = telebot.TeleBot('5354205774:AAFfo_zYN_5j-H5VPtvRM_ykvUQmq7MUhJM')

weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=fa0c69065a227aae0ae1081d5953bcfa&units=metric'



@bot.message_handler(commands=['start', 'hi'])
def welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name} ')

@bot.message_handler(content_types=['text']) 
def get_text_messages(message):

    if message.text == 'привет':
        bot.send_message(message.chat.id, f'привет {message.from_user.first_name}')
    elif message.text.lower() == '/help':
        bot.send_message(message.chat.id, '/help погода, /help cord, /help hello')
    elif message.text.lower() == '/help погода':
        bot.send_message(message.chat.id,'если хочешь узнать погоду пример: погода ru moscow')
    elif message.text.lower() == '/help cord':
        bot.send_message(message.chat.id,'если хочешь узнать кординаты пример: cord ru moscow')
    elif message.text.lower() == '/help hello':
        bot.send_message(message.chat.id,'напиши привет!')
    elif message.text.split(' ')[0] == 'погода':
        textsplitted = message.text.lower().split(' ')
        city = textsplitted[2]
        country = textsplitted[1]
        w_final_url = weather_url.format(city=city, country=country)
        response = requests.get(w_final_url)
        pog_json  = response.json()
        country = pog_json['sys']['country']
        gor = pog_json['name']
        temp = pog_json['main']['temp']
        feel = pog_json['main']['feels_like']
        wind = pog_json['wind']['speed']
        bot.send_message(message.chat.id,f'код страны { country }')
        bot.send_message(message.chat.id,f'погода в городе { gor }')
        bot.send_message(message.chat.id,f'{ temp } градусов')
        bot.send_message(message.chat.id,f'ошушается как { feel }')
        bot.send_message(message.chat.id,f'скорость ветра { wind } км/ч')
    
    elif message.text.split(' ')[0] == 'cord':
        textsplitted = message.text.lower().split(' ')
        city = textsplitted[2]
        country = textsplitted[1]
        w_final_url = weather_url.format(city=city, country=country)
        response = requests.get(w_final_url)
        cord_json  = response.json()
        lat = cord_json['coord']['lat'] 
        lon = cord_json['coord']['lon'] 
        bot.send_message(message.chat.id,f' широта : { lat }')
        bot.send_message(message.chat.id,f'долгота : { lon }')

    else:
        bot.send_message(message.chat.id, 'я не понимаю что это значит напишите /help')

print('Бот запушенxh .....')
bot.infinity_polling()