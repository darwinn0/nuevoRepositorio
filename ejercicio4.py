#Un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre 
#por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
import os
os.system('cls' if os.name == 'nt' else 'clear')

nombre = input("Escriba su primer nombre: ")
print (f"Hola",nombre)