import requests
import sys
import os
import time
import zipfile  # <-- You forgot to import this

# Defining Required Functions
def animation_text(text, delay):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)

def clear():
    os.system("cls" if os.name == "nt" else "clear")  # works on Windows & Linux

# Logo Section
logo = """
\033[1;34m================================================


 
.----.    .--.   .---.  .-..-. .----.   .---.   .----.  .----. .-. 
} {-. \  / {} \  } }}_} | ' /  | {_} } / {-. \ { {__-` { {__-` { | 
} '-} / /  /\  \ | } \  | . \  | {_} } \ '-} / .-._} } .-._} } | } 
`----'  `-'  `-' `-'-'  `-'`-` `----'   `---'  `----'  `----'  `-' 

       \033[1;32mAuthor   : darkboss1 Ak47
       Facebook : www.facebook.com/cybercrackervai
       Github   : www.github.com/darkboss1
       Group    : DARKBOSS1 SQUAED

       Use the tool for Educational Purpose No Misuse

\033[1;34m================================================\033[0m
"""

first_line = """\033[1;32m
------------------------------------------------
|                                              |
|Zip File Extract with brute force by darkboss1|
|                                              |
------------------------------------------------\n\n\033[0m"""

# Main Program
clear()
animation_text(logo, 0.01)
animation_text(first_line, 0.01)

option = "\n\n\t\033[1;35m1. Unlock Zip File\n\n\t2. Exit\n\033[0m"
animation_text(option, 0.1)

choice = input("\n\n\tEnter your choice: ").strip()

if choice == "1":
    zip_path = input("\n\n\tEnter ZIP file path: ").strip()
    wordlist_path = input("\n\tEnter password list path: ").strip()

    try:
        zip_file = zipfile.ZipFile(zip_path)
    except FileNotFoundError:
        print(f"❌ \n\t\033[1;33mZIP file not found:\033[0m {zip_path}")
        sys.exit(1)

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
            found = False
            for password in file:
                password = password.strip()
                try:
                    zip_file.extractall(pwd=bytes(password, "utf-8"))
                    print(f"\n\t✅ \033[1;32mPassword found: {password}\n")
                    found = True
                    break
                except:
                    print(f"\n\t❌ Tried: {password}")
            if not found:
                print("\n\t\033[1;31m❌ No password matched.\n")
    except FileNotFoundError:
        print(f"❌ Wordlist file not found: {wordlist_path}")

elif choice == "2":
    print("\n\n\t\t\033[1;31mExiting...\n\n")
else:
    print("❌ Invalid choice.")
