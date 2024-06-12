import tkinter as tk
from tkinter.font import BOLD, ITALIC
import telebot, os
import threading
import signal
import sys

# id mio tramite link bot: 5164190782
#API_TOKEN = '6471162107:AAFM7CMTYw7e7DFMVkiOxw90lfuecPC9CeA'
API_TOKEN = '7290062710:AAFSQo_7vZwY2o0krBcbXkBYmcz6jBlIfg8'
bot = telebot.TeleBot(API_TOKEN)

variabile = os.getcwd()


finestra1 = tk.Tk()
finestra1.title('Dialogo')
finestra1.geometry('800x500')
finestra1.resizable(True, True)
finestra1.config(bg='#232323')
finestra1.grid_columnconfigure(0, weight=1)

x=os.path.join(os.getcwd(), 'chats.txt')

def bottone_premuto(event=None):
    bottone.destroy()
    input_testo.grid(row=5, column=0, pady=10)
    bottone2.grid(row=6, column=0, pady=10)
    Benvenuto_label.config(text='Manda un messaggio in chat \ntramite il Link_Bot')
    bottone4.destroy()
    global chat_box, finestra2
    finestra2 = tk.Toplevel()
    finestra2.title('Chat')
    finestra2.geometry('800x500')
    finestra2.resizable(True, True)
    finestra2.config(bg='#232323')
    finestra2.grid_columnconfigure(0, weight=1)

    finestra2.protocol("WM_DELETE_WINDOW", lambda: None)

    chat_box = tk.Text(finestra2, state=tk.DISABLED, bg='#232323', fg='white', font=('Microsoft YaHei', 12))
    chat_box.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    finestra2.grid_rowconfigure(0, weight=1)
    finestra2.grid_columnconfigure(0, weight=1)

def bottone2_premuto(event=None):
    testo = input_testo.get()
    print(f'Hai inviato il messaggio: {testo}')
    #chat_id = 5164190782
    chat_id=1353175499
    bot.send_message(chat_id, testo)
    input_testo.delete(0, tk.END)
    aggiorna_chat(f"Tu: {testo}")

@bot.message_handler(func=lambda message: True)
def messaggio_ricevuto(message):
    user_name = message.from_user.first_name
    chat_id = message.chat.id
    print(f'Chat ID: {chat_id} Nome Utente: {user_name}')
    print(f'Messaggio ricevuto: {message.text}')
    aggiorna_chat(f"{user_name}: {message.text}")

def start_bot():
    bot.polling()

def stop(sig, frame):
    print('Interruzione ricevuta, chiusura del bot e dell\'applicazione...')
    bot.stop_polling()
    finestra1.quit()
    sys.exit(0)

def on_closing():
    print('Chiusura dell\'applicazione...')
    bot.stop_polling()
    if 'finestra2' in globals():
        finestra2.destroy()
    finestra1.destroy()
    sys.exit(0)

def aggiorna_chat(messaggio):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, messaggio + '\n')
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

def bottone4_premuto():
    global chat_id_selezionato
    finestra_scelta = tk.Toplevel()
    finestra_scelta.title('Seleziona chat')
    finestra_scelta.geometry('400x300')
    finestra_scelta.config(bg='#232323')

    label_scelta = tk.Label(finestra_scelta, text="seleziona l'utente con cui chattare:", bg='#232323', fg='white', font=('Microsoft YaHei', 12))
    label_scelta.pack(pady=10)

    #leggi il file chats.txt
    opzioni_chat = []
    try:
        with open(x, 'r') as file:
            for line in file:
                nome, chat_id = line.strip().split(':')
                opzioni_chat.append((nome, chat_id))
    except Exception as e:
        print(f'Errore nella lettura del file {e}')
    
    var_chat = tk.StringVar(finestra_scelta)
    var_chat.set(opzioni_chat[0][0] if opzioni_chat else "Nessuna chat disponibile")

    menu_chat = tk.OptionMenu(finestra_scelta, var_chat, *[nome for nome, _ in opzioni_chat])
    menu_chat.config(bg='#8742f5', fg='black', font=('Times New Roman', 12, BOLD))
    menu_chat.pack(pady=10)


    def seleziona_chat():
        global chat_id_selezionato
        nome_selezionato = var_chat.get()
        for nome, chat_id in opzioni_chat:
            if nome == nome_selezionato:
                chat_id_selezionato = chat_id
                print(f'Selezionato {nome_selezionato} con chat ID: {chat_id}')
                break
        finestra_scelta.destroy()
    
    bottone_seleziona = tk.Button(finestra_scelta, text='Seleziona', command=seleziona_chat, bg='#42f587', fg='black', font=('Times New Roman', 12, BOLD))
    bottone_seleziona.pack(pady=20)


    


# Avvia il bot in un thread separato
bot_thread = threading.Thread(target=start_bot)
bot_thread.start()

signal.signal(signal.SIGINT, stop)
finestra1.protocol("WM_DELETE_WINDOW", on_closing)

Benvenuto_label = tk.Label(finestra1, text="Benvenuto nell'applicazione", font=('Microsoft YaHei', 14, BOLD, ITALIC), bg='#232323', fg='white')
Benvenuto_label.grid(row=1, column=0, pady=20, padx=100, sticky='ew')  # era300

bottone = tk.Button(finestra1, text='Cliccami per chat', font=('Times New Roman', 10, BOLD, ITALIC), bg='#8742f5', fg='black', command=bottone_premuto)
bottone.grid(row=2, column=0, pady=30)
bottone4=tk.Button(text='scegli chat', font=('Times New Roman', 8, BOLD, ITALIC), bg='#8742f5', fg='black', command=bottone4_premuto)
bottone4.grid(row=3, column=0, pady=10)

bottone2 = tk.Button(text='Clicca per inviare il messaggio', font=('Times New Roman', 8, ITALIC), bg='#42f587', fg='black', command=bottone2_premuto)

input_testo = tk.Entry(finestra1, font=('Microsoft YaHei', 12), bd=3, width=50)
input_testo.bind('<Return>', bottone2_premuto)





finestra1.mainloop()