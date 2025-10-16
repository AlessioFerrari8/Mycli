#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

BANNER = r"""
  ______                   ____ ___  
 |  ____|                 |___ \__ \ 
 | |__ ___ _ __ _ __ ___    __) | ) |
 |  __/ _ \ '__| '__/ _ \  |__ < / / 
 | | |  __/ |  | | | (_) | ___) / /_ 
 |_|  \___|_|  |_|  \___/ |____/____|
                      ______         
                     |______|        
"""

def main():
    print(BANNER)
    print("Benvenuto nella tua CLI personale!\n")
    print("Comandi disponibili:")
    print("  1. Apri progetto")
    print("  2. Esegui script")
    print("  3. Mostra path corrente")
    print("  4. Esci")

    while True:
        scelta = input("\n> ").strip()

        if scelta == "1":
            path = input("Inserisci il path del progetto: ").strip()
            if os.path.exists(path):
                os.chdir(path)
                print(f"Aperto progetto in {path}")
            else:
                print("Path non valido.")
        elif scelta == "2":
            script = input("Nome script da eseguire: ").strip()
            subprocess.run(script, shell=True)
        elif scelta == "3":
            print("Path corrente:", Path.cwd())
        elif scelta == "4":
            print("Uscita dalla CLI. 👋")
            break
        else:
            print("Comando non valido.")

if __name__ == "__main__":
    main()
