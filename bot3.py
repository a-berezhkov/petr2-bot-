import telebot

bot = telebot.TeleBot("2017460696:AAHAyyMyb3KSVfNyIz8qYi8ZzT09pL1VDyc", parse_mode=None) #

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

bot.polling(none_stop=True)