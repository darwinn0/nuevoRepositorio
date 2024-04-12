#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# definimos las variables y pedimos que ingresen lo pedido
n=int (input("Ingrse el numero que desea dividir: "))
d=int (input("Ingrse el numero por el cual va dividirlo: "))

#usamos una condicion para poder ver si se puede dividir 
if n==0:
 print(f"ERROR, no se puede dividir por cero")
else:
 print(n//d)
