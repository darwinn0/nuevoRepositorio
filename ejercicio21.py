#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, 
#de altura el número introducido.

import os
os.system('cls' if os.name == 'nt' else 'clear')

#se define la varible y se pide la altura del triangulo
numero=int(input("Ingrese la altura del triangulo: "))

#se usa el ciclo for para determinar el rango  de altura de triangulo 
for f in range(numero):
    for j in range(f+1):
        print("*", end="")
        #se deja este print vacio para que se forme el triangulo
    print("")