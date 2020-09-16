import config
import telebot
from googletrans import Translator
from telebot import types


bot = telebot.TeleBot(config.token)

lang = 'ru'

@bot.message_handler(commands=["info"])

def info(message):
	bot.send_message(message.chat.id, "/setLanguage < Choose language", message.text)


@bot.message_handler(commands=["setLanguage"])

def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Push me", callback_data="test")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Push", reply_markup=keyboard)

# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Bang")
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")


@bot.message_handler(content_types=["text"])

def trans(message): #translates message to english
	t = Translator()
	bot.send_message(message.chat.id, t.translate(message.text, dest=lang).text)

if __name__ == '__main__':
     bot.infinity_polling()