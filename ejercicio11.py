#programa que pregunte el nombre del usuario en la consola y un número entero e
#imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# define variables y se le pide al usuario que ingrese lo pedido 
nombre = input("Escribe tu nombre ")
n = input("Introduce un número entero: ")
# paso para hacer el procedimiento de escribir en lineas distintos el nombre
nombre = ((nombre + "\n")*int(n))
print(nombre)