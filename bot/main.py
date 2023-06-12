import telebot
import webbrowser

API_TOKEN = '6208348875:AAEFxqAwZlC5hq3LozUo_soBGmbQ2XaZGh4'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('http://127.0.0.1:8000/admin')


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(func=lambda message: True)
def send_message(message):
    bot.send_message(message.chat.id, message)


# bot.polling(none_stop=True)
bot.infinity_polling()
