import random
from hugchat import hugchat
from hugchat.login import Login
from colorama import Fore
import getpass
import os
import time
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


clear_screen()
# Frases de bienvenida
frases_bienvenida = [
    "Ask what you want."
]


tugmail = input("Enter your email: ")
tupass = getpass.getpass("Enter your password: ")
clear_screen()

ascii_art = [
    Fore.LIGHTGREEN_EX+" __    __  __    __   ______    ______   __    __   ______  ________ ",
    Fore.LIGHTGREEN_EX+"|  \  |  \|  \  |  \ /      \  /      \ |  \  |  \ /      \|        \\",
    Fore.LIGHTGREEN_EX+"| $$  | $$| $$  | $$|  $$$$$$\|  $$$$$$\| $$  | $$|  $$$$$$\\$$$$$$$$",
    Fore.LIGHTGREEN_EX+"| $$__| $$| $$  | $$| $$ __\$$| $$   \$$| $$__| $$| $$__| $$  | $$   ",
    Fore.LIGHTGREEN_EX+"| $$    $$| $$  | $$| $$|    \| $$      | $$    $$| $$    $$  | $$   ",
    Fore.LIGHTGREEN_EX+"| $$$$$$$$| $$  | $$| $$ \$$$$| $$   __ | $$$$$$$$| $$$$$$$$  | $$   ",
    Fore.LIGHTGREEN_EX+"| $$  | $$| $$__/ $$| $$__| $$| $$__/  \| $$  | $$| $$  | $$  | $$   ",
    Fore.LIGHTGREEN_EX+"| $$  | $$ \$$    $$ \$$    $$ \$$    $$| $$  | $$| $$  | $$  | $$   ",
    Fore.LIGHTGREEN_EX+" \$$   \$$  \$$$$$$   \$$$$$$   \$$$$$$  \$$   \$$ \$$   \$$   \$$   "
]


for line in ascii_art:
    print(line)
    time.sleep(0.1)

# Muestra una frase de bienvenida aleatoria
mensaje_bienvenida = random.choice(frases_bienvenida)

sign = Login(tugmail, tupass)
cookies = sign.login()
chatbot = hugchat.ChatBot(cookies=cookies)
id = chatbot.new_conversation()
chatbot.change_conversation(id)

chatbot.switch_llm(1)

tamano_cuadro = len(max(mensaje_bienvenida.splitlines(), key=len)) + 2

personaje_ascii = f"""
┏{'━' * tamano_cuadro}┓
┃{mensaje_bienvenida.center(tamano_cuadro - 1)}┃
┗{'━' * tamano_cuadro}┛
     O
    /|\\
    / \\
"""

print(Fore.WHITE + personaje_ascii)
print("")

while True:
    user_input = input(Fore.WHITE + '>')
    clear_screen()
    print(Fore.YELLOW + "Computing: ", end="", flush=True)
    
    # Simulamos una animación de carga mientras esperamos la respuesta
    animation_chars = "|/-\\"
    for _ in range(15):
        for char in animation_chars:
            print(char, end="\b", flush=True)
            time.sleep(0.1)
    
    response = chatbot.chat(user_input)
    mensaje_bienvenida = random.choice(frases_bienvenida)
    tamano_cuadro = len(max(mensaje_bienvenida.splitlines(), key=len)) + 2
    
    personaje_ascii = f"""
┏{'━' * tamano_cuadro}┓
┃{mensaje_bienvenida.center(tamano_cuadro - 3)}┃
┗{'━' * tamano_cuadro}┛
     O
    /|\\
    / \\    
"""
    print(Fore.WHITE + personaje_ascii)
    print("")
    print(Fore.WHITE + response)
