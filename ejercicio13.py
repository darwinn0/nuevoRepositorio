#programa que le pide al usuario que ingrese una frase y una vocal y la vocal introducida la hara mayuscula
import os
os.system('cls' if os.name == 'nt' else 'clear')

# define variables y se pide que el usuario ingrese lo que se le pide
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
#se muestra en pantalla la frase y la vocal en mayuscula
print(frase.replace(vocal, vocal.upper()))