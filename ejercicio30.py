#Escribir un programa que lea un entero porsitivo,  n , introducido por el usuario y después muestre en pantalla la suma de todos los 
#enteros desde 1 hasta  n . La suma de los  n  primeros enteros positivos puede ser calculada de la siguiente forma:


import os
os.system('cls' if os.name == 'nt' else 'clear')



n = int(input("Ingrse el numero entero positivo: "))
suma = n * (n + 1) / 2
print("La suma desde los primeros numeros enteros positivos:  ", n ," es ", suma)