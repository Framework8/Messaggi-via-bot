
import telebot
import os

def ricerca():
    cartella_corrente = os.getcwd()
    try:
        lista_file = os.listdir(cartella_corrente)
        if 'main.py' not in lista_file:
            try:
                cartelle = []
                for elemento in os.listdir(cartella_corrente):
                    percorso_completo = os.path.join(cartella_corrente, elemento)
                    if os.path.isdir(percorso_completo):
                        cartelle.append(percorso_completo)
                trovato = False
                for cartella in cartelle:
                    os.chdir(cartella)
                    if 'main.py' in os.listdir():
                        trovato = True
                        print(f'File main.py trovato nella sottodirectory: {cartella}')
                        break
                    else:
                        os.chdir(cartella_corrente)
                if not trovato:
                    os.chdir(cartella_corrente)
                    print('File main.py non trovato neanche nelle sottodirectory')
            except Exception as e:
                print(f'Errore riscontrato: {e}')
                os.chdir(cartella_corrente)
        else:
            print(f'File main.py trovato nella corrente cartella: {cartella_corrente}')
    except Exception as e:
        os.chdir(cartella_corrente)
        print(f'Riscontrato un errore: {e}')
    if 'main.py' not in os.listdir():
        os.chdir(cartella_corrente)
    else:
        print(f'Ambiente cambiato a {os.getcwd()}')

def scan():
    lista_file = os.listdir()
    try:
        if 'chats.txt' not in lista_file:
            with open('chats.txt', 'w') as file:
                file.write('')
            print('File chats.txt creato')
        else:
            print('File chats.txt già esistente')
    except Exception as e:
        print(f'Errore durante la creazione di chats.txt: {e}')

ricerca()
scan()

API_TOKEN = "<api_token>" #Inserire il proprio api_token

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
