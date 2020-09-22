import config
import telebot
from googletrans import Translator
from telebot import types
# GOOGLE TRANSLATE BOT by BASIL0

bot = telebot.TeleBot(config.token)

# here is a variable with a value of chosen target language
lang = 'en'

@bot.message_handler(commands=["info"])

def info(message):
	bot.send_message(message.chat.id, "/setLanguage <-- Choose language", message.text)


@bot.message_handler(commands=["setLanguage"])

def set_language(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text=lang, callback_data=lang)
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "This option is not avalible at the moment", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])

def trans(message): # translates message to english using Translator() from googletrans module
	t = Translator()
	bot.send_message(message.chat.id, t.translate(message.text, dest=lang).text)

if __name__ == '__main__':
     bot.infinity_polling()