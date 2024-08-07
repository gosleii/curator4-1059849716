import telebot

bot = telebot.TeleBot("6576047629:AAHuaCk2zmtDEmDN-5efD3HGPnmHxUqGMeM")

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет в мире смешариков!")

@bot.message_handler(commands=["photo"])
def photo_handler(message):
    bot.send_message(message.chat.id, "[Пора знакомиться со всеми](https://www.mstrana.ru/_mod_files/ce_images/eshop/smeshariki-geroi1.jpg)", parse_mode="Markdown")

@bot.message_handler(commands=["map"])
def map_handler(message):
    bot.send_message(message.chat.id, "[Карта мира](https://static.wikia.nocookie.net/smesharikiarhives/images/7/7b/%D0%9A%D0%B0%D1%80%D1%82%D0%B0.jpg/revision/latest/thumbnail/width/360/height/450?cb=20190321060100&path-prefix=ru)", parse_mode="markdown")

bot.infinity_polling()