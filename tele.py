from email import message
import telebot

token = '5109270751:AAEwyN0voWiLAhC_vk375_0QW_cVnRKf0tI'

bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start', 'hi'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')
# print('Бот запущен...')
# bot.infinity_polling()

@bot.message_handler(content_types= 'text')
def sendMessage(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'привет, как ты?')
        
    elif  message.text.lower() == 'нормально как сам?':
        bot.send_message(message.chat.id, 'отлично')
        
    elif message.text.lower() == 'что делаеш?':
        bot.send_message(message.chat.id, 'уроки делаю')
        
    elif message.text[0] == '-' and isinstance(int(message.text[1]), int):
        bot.send_message(message.chat.id, 'Отрицательный число !')
   
    elif isinstance(int(message.text[0]), int):
        bot.send_message(message.chat.id, 'Положительный !')
         
    elif message.text[3] == '':
        bot.send_message(message.chat.id, '')  
        
    else:
        bot.send_message(message.chat.id,message.text)
        
print('Бот запущен...')
bot.infinity_polling()