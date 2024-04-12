# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

import os
os.system('cls' if os.name == 'nt' else 'clear')


#usamos el ciclo white para que el programa se repita hasta que escribamos la palabra salir
while True:
    frase = input("Escribe una palabra: ")
    # dentro del ciclo white usamos la funcion de if
    if frase == "salir":
        break
    #mostramos en pantalla las palabras que escribamos
    print(frase)