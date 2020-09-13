import config
import telebot
from googletrans import Translator

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])

def trans(message): #translates message to english
	t = Translator()
	bot.send_message(message.chat.id, t.translate(message.text).text)

if __name__ == '__main__':
     bot.infinity_polling()