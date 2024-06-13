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
    user_name = message.from_user.first_name
    contenuto = f'{user_name}:{chat_id}'
    
    # Legge il file e controlla se il chat_id è già presente
    opzioni_chat = []
    chat_id_presente = False
    try:
        with open(x, 'r') as file:
            for line in file:
                nome, id_chat = line.strip().split(':')
                opzioni_chat.append((nome, id_chat))
                if str(chat_id) == id_chat:
                    chat_id_presente = True
                    break
    except Exception as e:
        print(f'Errore nella lettura del file: {e}')

    # Se il chat_id non è presente, aggiungi l'utente al file
    if not chat_id_presente:
        try:
            with open(x, 'a') as file:
                file.write('\n' + contenuto)
        except Exception as e:
            print(f'Errore nella scrittura del file: {e}')

#risponde in questo modo a qualisasi messaggio non sia /chat_id; /start; /help
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, 'puoi solo mandare il comando /chat_id')


bot.infinity_polling()
