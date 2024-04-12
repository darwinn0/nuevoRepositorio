#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
import os
os.system('cls' if os.name == 'nt' else 'clear')
 
#se le pide al usuario ingrese un numero entero 
n = int(input("ingrese un numero entero: "))
#se usa una funcion para determinar si es par o impar ocompañado de modulo
if n % 2 == 0:
    print ("El numero es par")
else:
    print("El numero es impar")