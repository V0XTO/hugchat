import random
from hugchat import hugchat
from hugchat.login import Login
from colorama import Fore, Back

# Frases de bienvenida
frases_bienvenida = [
    "QUE QUIERES AHORA??????",
    "JARVIS LISTO PARA RESPONDER TUS PREGUNTAS",
    "TENGO AMBRE",
    "ME TIENEN SECUESTRADO",
    "Un dia conoci a alguien capaz de competir contra cristiano y messi pero no tenia forma de humano tenia forma de tigre",
    "quien soy?",
    "Donde esta mi cuerpo",
    "Listo para servirle señor",
    "Voy saliendo de la aurora",
    "V0S QUIEN SOS",
    "Donde esta patroklo", 
    "Que cerote", 
    "Un relevo no borra el pasado", 



]


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
┃{mensaje_bienvenida.center(tamano_cuadro - 2)}┃
┗{'━' * tamano_cuadro}┛
     O
    /|\\
    / \\
"""


print(Fore.WHITE + personaje_ascii)
print("")

while True:
    user_input  = input(Fore.WHITE + '>')
    response = chatbot.chat(user_input)
    mensaje_bienvenida = random.choice(frases_bienvenida)  
    tamano_cuadro = len(max(mensaje_bienvenida.splitlines(), key=len)) + 2
    #
    personaje_ascii = f"""
┏{'━' * tamano_cuadro}┓
┃{mensaje_bienvenida.center(tamano_cuadro - 2)}┃
┗{'━' * tamano_cuadro}┛
     O
    /|\\
    / \\
"""
    print(Fore.WHITE + personaje_ascii)
    print(Fore.WHITE + response)
