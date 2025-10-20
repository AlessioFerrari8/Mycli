# 🖥️ Personal CLI Launcher

Una **CLI (Command Line Interface) personale** scritta in **Python 3**, progettata per aprire rapidamente siti web di notizie, musica o tecnologia, oppure per avviare applicazioni come **Minecraft**, **Steam** e **Spotify** direttamente dal terminale.  
Include **autocompletamento dei comandi**, messaggi di aiuto e gestione multipiattaforma (Windows, macOS, Linux).

---

## 🚀 Funzionalità principali

- 🌐 **Accesso rapido** a siti di notizie, sport, tecnologia, attualità e musica.  
- 🎮 **Avvio di applicazioni** installate localmente (Minecraft, Steam, Spotify).  
- ⌨️ **Autocompletamento dei comandi** tramite `readline` (premi `TAB` per suggerimenti).  
- 🧠 **Compatibilità multipiattaforma**: Windows, macOS e Linux.  
- 🧩 **Facilmente estendibile** — puoi aggiungere nuovi comandi, URL o applicazioni.

---

## 📦 Requisiti

- Python 3.6 o superiore  
- Browser predefinito configurato (per l’apertura degli URL)  
- Le applicazioni opzionali installate:
  - [Minecraft Launcher](https://www.minecraft.net/)
  - [Steam](https://store.steampowered.com/)
  - [Spotify](https://www.spotify.com/)

---

## ⚙️ Installazione

1. Clona o scarica il repository:
   ```bash
   git clone https://github.com/tuo-username/personal-cli-launcher.git
   cd personal-cli-launcher
   ```

2. Rendi eseguibile lo script (solo su Linux/macOS):
   ```bash
   chmod +x cli_launcher.py
   ```

3. Esegui lo script:
   ```bash
   ./cli_launcher.py
   ```
   Oppure:
   ```bash
   python3 cli_launcher.py
   ```

---

## 💡 Comandi disponibili

| Comando | Descrizione |
|----------|-------------|
| `!h` | Mostra l’elenco dei comandi disponibili |
| `!sport` | Apre i siti di notizie sportive |
| `!tech` | Apre i siti di notizie tecnologiche/scientifiche |
| `!news` | Apre i principali siti di attualità |
| `!music` | Apre i siti musicali |
| `!Minecraft` | Avvia Minecraft (se installato) |
| `!Steam` | Avvia Steam |
| `!Spotify` | Avvia Spotify |
| `exit` | Esce dalla CLI |

> 💬 Suggerimento: puoi digitare `!` e poi premere `TAB` per vedere i comandi disponibili.

---

## 🧠 Come funziona

- Lo script mostra un **banner ASCII** all’avvio.  
- Utilizza `readline` per fornire **autocompletamento dei comandi**.  
- Ogni comando:
  - o apre una lista di URL nel browser predefinito (`open_url()`),
  - o cerca il percorso locale dell’applicazione da eseguire (`get_app_path()`),
  - oppure stampa un messaggio di aiuto.  
- I percorsi delle app sono adattati automaticamente al sistema operativo.

---

## 🧩 Personalizzazione

Puoi modificare le **liste di URL** o aggiungere nuovi comandi nel corpo principale dello script:
```python
sport_news_urls = ["https://sport.sky.it/", "https://www.transfermarkt.it/"]
```

Oppure aggiungere nuove applicazioni nel dizionario della funzione `get_app_path()`:
```python
elif app_name == "vlc":
    paths = ["/usr/bin/vlc", "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"]
```

---

## 🛠️ Compatibilità

| Sistema operativo | Stato supporto |
|--------------------|----------------|
| 🪟 Windows | ✅ Completamente supportato |
| 🍎 macOS | ✅ Completamente supportato |
| 🐧 Linux | ✅ Completamente supportato |

---

## 📸 Esempio d’uso

```bash
$ python3 cli_launcher.py

  ______                   ____ ___  
 |  ____|                 |___ \__ \ 
 | |__ ___ _ __ _ __ ___    __) | ) |
 |  __/ _ \ '__| '__/ _ \  |__ < / / 
 | | |  __/ |  | | | (_) | ___) / /_ 
 |_|  \___|_|  |_|_|  \___/ |____/____|
                      ______         
                     |______|        

Benvenuto nella tua CLI personale!

> !h
Comandi disponibili:
  !sport    - Vedi notizie sport
  !tech     - Vedi notizie tecnologia/scienza
  !news     - Vedi notizie attualità
  !music    - Vedi siti di musica
  !Minecraft - Apri Minecraft locale
  !Steam    - Apri Steam
  !Spotify  - Apri Spotify
  !h        - Mostra questo messaggio di aiuto
  exit      - Esci dalla CLI
```

---

## 🧑‍💻 Autore

**Nome:** Alessio Ferrari  
**GitHub:** [@AlessioFerrari8](https://github.com/AlessioFerrari8)
