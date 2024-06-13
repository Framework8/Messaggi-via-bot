import telebot

API_TOKEN = "<api_token>"

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Ciao sono chatbot!
lancia il comando /chat_id e riferisci a chi te lo ha chiesto i numeri che ti darò in risposta. \
""")


@bot.message_handler(commands=['chat_id'])
def chat_id(message):
    chat_id=message.chat.id
    bot.send_message(chat_id, chat_id)
    print(type(chat_id))

#risponde in questo modo a qualisasi messaggio non sia /chat_id; /start; /help
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, 'puoi solo mandare il comando /chat_id')


bot.infinity_polling()
