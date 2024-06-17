# Messaggi via bot

Questo progetto è un'applicazione desktop che permette di chattare su Telegram tramite un bot.

## Funzionalità principali
- Selezione di una chat da una lista predefinita
- Invio di messaggi alla chat selezionata
- Visualizzazione in tempo reale dei messaggi inviati e ricevuti
- Archiviazione della chat in un file log
- Creazione automatica del file `chats.txt`

## Prerequisiti
- Python 3 installato sul sistema
- Accesso a Internet per l'utilizzo dell'API di Telegram
- Token API valido per il bot Telegram

## Installazione e utilizzo
1. Clonare il repository: `git clone https://github.com/Framework8/Messaggi-via-bot_Telegram`
2. Installare le dipendenze: `pip install -r requirements.txt`

## Configurazione del file chats.txt

![image](https://github.com/Framework8/Messaggi-via-bot_Telegram/assets/109827575/0b240d4b-9db1-442a-83bd-2ae7d1d4e76a)

Come mostrato nell'immagine, che ritrae la parte dello script responsabile della configurazione del file `chats.txt`, basterà far inviare a chi vuole contattare il comando `/chat_id` al bot (file `bot.py`) ed esso salverà automaticamente le informazioni necessarie nel file `chats.txt`.
