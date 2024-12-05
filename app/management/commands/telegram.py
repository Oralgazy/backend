from django.contrib.auth import authenticate
from django.core.management.base import BaseCommand, CommandError
from app.models import Item, UserTelegram
import telebot

bot = telebot.TeleBot("8085096179:AAF0w_46cX9M1Wfw16vh1iRVPd6AFUkPAg4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Добро пожаловать")


@bot.message_handler(func=lambda message: True)
def all_msgs(message: telebot.types.Message):
    user_id = message.from_user.id
    user_telegram = UserTelegram.objects.filter(chat_id=user_id).first()
    if not user_telegram:
        user_telegram = UserTelegram.objects.create(
            chat_id=user_id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
            language_code=message.from_user.language_code
        )

    if message.text.startswith("login"):
        login, username, password = message.text.split()
        user = authenticate(username=username, password = password)
        if user:
            user_telegram.user = user
            user_telegram.save()
            bot.send_message(user_id, "You are logged in")
        else:
            bot.send_message(user_id, "Invalid login or password")
    if not user_telegram.user:
        bot.send_message(user_id, "Please, login: 'login your_login your_password'")
        return

    if message.text == "logour":
        user_telegram.user = None
        user_telegram.save()
        bot.send_message(user_id, "You are logged out")
        return

    if message.text == "items":
        items = Item.objects.all()
        for item in items:
            bot.send_message(user_id, f"{item.name} - KZT {item.price}")

    if message.text.startswith("buy"):
        _, item_name = message.text.split()
        item = Item.objects.filter(name=item_name).first()
        if item:
            bot.send_message(user_id, f"You bought {item.name}")
        else:
            bot.send_message(user_id, "Item not found")
        return




class Command(BaseCommand):
    def handle(self, *args, **options):
        print('start')
        bot.infinity_polling()
        print('stop')