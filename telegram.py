import telebot
from app.models import Item


Item.objects.all() 

bot = telebot.TeleBot("8085096179:AAF0w_46cX9M1Wfw16vh1iRVPd6AFUkPAg4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

print('start')
bot.infinity_polling()
print('stop')