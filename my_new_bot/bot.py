import telebot

TOKEN = '8785273119:AAG02aBV60mk_thGOz2Vb6DSINcSs9sFpos'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "مرحباً! هذا هو البوت الجديد يعمل بنجاح على Termux.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"أنت قلت: {message.text}")

print("جاري تشغيل البوت...")
bot.infinity_polling()
