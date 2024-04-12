#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
import os
os.system('cls' if os.name == 'nt' else 'clear')


#se define variable y se pide al usuario que ingrese un numero
n = int(input("Introduzca un numero entero: "))
#se utiliza el ciclo for para hacer con un rango para el tamaño del triangulo
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
        #se deja el espacio en el print para que se haga el triangulo
    print("")