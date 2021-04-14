import telebot
import Config

bot = telebot.TeleBot(Config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(msg):
    pic = open('sticker.png', 'rb')
    bot.send_sticker(msg.chat.id, pic)

    bot.send_message(msg.chat.id, "Приветствую, {0.first_name} {1}\nПолюбуйся этим прекрасным стикером".format(msg.from_user, '\U0001F60E'), parse_mode='html')

@bot.message_handler(content_types=['text'])
def test(msg):
    bot.send_message(msg.chat.id, msg.text)

bot.polling(none_stop=True)