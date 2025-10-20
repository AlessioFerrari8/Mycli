
#!/usr/bin/env python3
import os
import sys
import subprocess
import platform

try:
    import readline
except ImportError:
    readline = None

BANNER = r"""
  ______                   ____ ___  
 |  ____|                 |___ \__ \ 
 | |__ ___ _ __ _ __ ___    __) | ) |
 |  __/ _ \ '__| '__/ _ \  |__ < / / 
 | | |  __/ |  | | | (_) | ___) / /_ 
 |_|  \___|_|  |_|_|  \___/ |____/____|
                      ______         
                     |______|        
"""

def open_url(url):
    """Opens a URL in the default web browser."""
    try:
        subprocess.run(['xdg-open', url], check=True) # Linux
    except FileNotFoundError:
        try:
            subprocess.run(['open', url], check=True) # macOS
        except FileNotFoundError:
            try:
                subprocess.run(['start', url], check=True, shell=True) # Windows
            except FileNotFoundError:
                print("Errore: Impossibile aprire il browser. Assicurati di avere un browser installato e configurato.")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'apertura del browser: {e}")

def get_app_path(app_name):
    """Returns the path to an executable based on the OS and app name."""
    system = platform.system()
    home = os.path.expanduser("~")
    
    if system == "Windows":
        if app_name == "minecraft":
            # Common paths for Minecraft launchers on Windows
            paths = [
                os.path.join(home, r"AppData\Local\Programs\TLauncher\TLauncher.exe"),
                os.path.join(home, r"AppData\Local\Minecraft\MinecraftLauncher.exe"),
                r"C:\Program Files\Minecraft Launcher\MinecraftLauncher.exe",
            ]
        elif app_name == "spotify":
            paths = [
                os.path.join(home, r"AppData\Roaming\Spotify\Spotify.exe"),
                r"C:\Users\Public\Desktop\Spotify.lnk",
            ]
        elif app_name == "steam":
            paths = [
                r"C:\Program Files (x86)\Steam\steam.exe",
                r"C:\Program Files\Steam\steam.exe",
            ]
    elif system == "Darwin":  # macOS
        if app_name == "minecraft":
            paths = ["/Applications/MultiMC/MultiMC.app/Contents/MacOS/MultiMC"]
        elif app_name == "spotify":
            paths = ["/Applications/Spotify.app/Contents/MacOS/Spotify"]
        elif app_name == "steam":
            paths = ["/Applications/Steam.app/Contents/MacOS/Steam"]
    else:  # Linux
        if app_name == "minecraft":
            paths = ["minecraft-launcher"]
        elif app_name == "spotify":
            paths = ["spotify"]
        elif app_name == "steam":
            paths = ["steam"]
    
    # Return the first existing path, otherwise return the first in the list
    for path in paths:
        if os.path.exists(path):
            return path
    return paths[0] if paths else None

def autocomplete_commands(text, state):
    """Autocomplete function for readline."""
    commands = ['!h', '!sport', '!tech', '!news', '!music', '!Minecraft', '!Steam', '!Spotify', 'exit']
    matches = [cmd for cmd in commands if cmd.startswith(text)]
    return matches[state] if state < len(matches) else None

def setup_readline():
    """Setup readline for autocomplete."""
    if readline:
        readline.set_completer(autocomplete_commands)
        readline.parse_and_bind('tab: complete')

def main():
    print(BANNER)
    print("Benvenuto nella tua CLI personale!\n")
    
    # Setup autocomplete
    setup_readline()
    
    # Cambiare in base a necessità, aggiungere volendo nuove liste
    sport_news_urls = [
        "https://sport.sky.it/", 
        "https://www.federtamburellolivescore.it/it/1/?desk=1",
        "http://www.tambass.org/",
        "https://www.transfermarkt.it/",
        "https://trentino.medialibrary.it/media/scheda.aspx?id=550276277&source=periodici_mlol_carousel"
    ]
    tech_science_news_urls = [
        "https://www.wired.it/",
        "https://www.geopop.it/",
        "https://www.focus.it/",
        "https://www.tomshw.it/",
        "https://www.developer-tech.com/"
    ]
    current_events_news_urls = [
        "https://www.adnkronos.com/",
        "https://www.repubblica.it/cronaca/",
        "https://www.corriere.it/cronache/",
        "https://www.ilsole24ore.com/",
        "https://www.ansa.it/"
    ]
    music_news_urls = [
        "https://www.last.fm/user/Ferro_32",
        "https://www.rollingstone.it/"
    ]

    while True:
        scelta = input("\n> ").strip()

        if scelta == "!h":
            print("\nComandi disponibili:")
            print("  !sport    - Vedi notizie sport")
            print("  !tech     - Vedi notizie tecnologia/scienza")
            print("  !news     - Vedi notizie attualità")
            print("  !music    - Vedi siti di musica")
            print("  !Minecraft - Apri Minecraft locale")
            print("  !Steam    - Apri Steam")
            print("  !Spotify  - Apri Spotify")
            print("  !h        - Mostra questo messaggio di aiuto")
            print("  exit      - Esci dalla CLI")
        elif scelta == "!sport":
            print("Apertura notizie sport...")
            for url in sport_news_urls:
                open_url(url)
        elif scelta == "!tech":
            print("Apertura notizie tecnologia/scienza...")
            for url in tech_science_news_urls:
                open_url(url)
        elif scelta == "!news":
            print("Apertura notizie attualità...")
            for url in current_events_news_urls:
                open_url(url)
        elif scelta == "!music":
            print("Apertura siti di musica...")
            for url in music_news_urls:
                open_url(url)
        elif scelta == "!Minecraft":
            print("Tentativo di aprire Minecraft...")
            try:
                minecraft_path = get_app_path("minecraft")
                if minecraft_path:
                    subprocess.Popen([minecraft_path])
                    print("Minecraft avviato.")
                else:
                    print("Errore: Impossibile trovare Minecraft. Assicurati che sia installato.")
            except FileNotFoundError:
                print("Errore: Minecraft launcher command not found. Assicurati che Minecraft sia installato.")
            except subprocess.CalledProcessError as e:
                print(f"Errore durante l'avvio di Minecraft: {e}")
        elif scelta == "!Steam":
            print("Tentativo di aprire Steam...")
            try:
                steam_path = get_app_path("steam")
                if steam_path:
                    subprocess.Popen([steam_path])
                    print("Steam avviato.")
                else:
                    print("Errore: Impossibile trovare Steam. Assicurati che sia installato.")
            except FileNotFoundError:
                print("Errore: Steam command not found. Assicurati che Steam sia installato.")
            except subprocess.CalledProcessError as e:
                print(f"Errore durante l'avvio di Steam: {e}")
        elif scelta == "!Spotify":
            print("Tentativo di aprire Spotify...")
            try:
                spotify_path = get_app_path("spotify")
                if spotify_path:
                    subprocess.Popen([spotify_path])
                    print("Spotify avviato.")
                else:
                    print("Errore: Impossibile trovare Spotify. Assicurati che sia installato.")
            except FileNotFoundError:
                print("Errore: Spotify command not found. Assicurati che Spotify sia installato.")
            except subprocess.CalledProcessError as e:
                print(f"Errore durante l'avvio di Spotify: {e}")
        elif scelta == "exit":
            print("Uscita dalla CLI. 👋")
            break
        else:
            print("Comando non valido.")

if __name__ == "__main__":
    main()
