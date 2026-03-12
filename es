import telebot

# التوكن الخاص بك من الصورة
TOKEN = '8785273119:AAG02aBV60mk_thGOz2Vb6DSINcSs9sFpos'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "مرحباً! أنا بوت منير الجديد. كيف يمكنني مساعدتك اليوم؟")

@bot.message_handler(func=lambda message: True)
def repeat_all(message):
    # البوت سيقوم برد فعل بسيط على أي رسالة
    bot.reply_to(message, f"وصلت رسالتك: {message.text}")

print("البوت يعمل الآن... اذهب إلى تليجرام وأرسل /start")
bot.infinity_polling()
