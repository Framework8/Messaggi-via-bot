# Messaggi via bot

Questo progetto è un'applicazione desktop che permette di chattare su Telegram tramite un bot.

## Funzionalità principali
- Selezione di una chat da una lista predefinita
- Invio di messaggi alla chat selezionata
- Visualizzazione in tempo reale dei messaggi inviati e ricevuti

## Prerequisiti
- Python 3 installato sul sistema
- Accesso a Internet per l'utilizzo dell'API di Telegram
- Token API valido per il bot Telegram

## Installazione e utilizzo
1. Clonare il repository: `git clone https://github.com/Framework8/Messaggi-via-bot_Telegram`
2. Installare le dipendenze: `pip install -r requirements.txt`

## Configurazione del file chats.txt

![image](https://github.com/Framework8/Messaggi-via-bot_Telegram/assets/109827575/d38e08b2-fb35-477c-8e72-c27082b79450)

Inserire manualmente nel file il nome e il chat ID separandoli solo con ":" come mostrato in foto.

## Ottenere il chat ID

![image](https://github.com/Framework8/Messaggi-via-bot_Telegram/assets/109827575/697e2765-4df3-45c3-b594-dc5fbfeb84f1)

Un modo per ottenere il chat ID di un utente con il bot è collegarlo ad uno script come quello indicato sopra in immagine (in allegato come "chat_id_bot.py") e far inviare all'utente con cui si vuole chattare il comando "/chat_id". Una volta che il bot gli avrà risposto con il chat ID, basterà aggiungerlo al file `chats.txt`.
