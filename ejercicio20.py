#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero 
#separados por comas.
import os
os.system('cls' if os.name == 'nt' else 'clear')

#se define la varible y se le pide al usuario que ingrese un numero
numero = int(input("Ingrese un numero positivo: "))

#con el ciclo for usamos una variable y determinamos el rango y ponemos -1 para que quire numeros hasra llegar a 0
for j in range(numero, -1, -1):
    #imprime los numeros al inversa
    print(j, end=", ")