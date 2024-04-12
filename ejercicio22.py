#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
import os
os.system('cls' if os.name == 'nt' else 'clear')

#se usa el ciclo for para determinar un rango y se cuenta uno mas para que llega hasta el 10
for a in range(1, 11):
    for f in range(1, 11):
        #se imprime el calculo de las variables donde se almaceno las tablas
        print(a*f, end="\t")
    print("")