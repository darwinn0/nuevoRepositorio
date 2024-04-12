#programa que le pregunta al usuario el nombre y le dice cuantas letras tiene

import os
os.system('cls' if os.name == 'nt' else 'clear')
# define variables y que el usuario ingrese lo pedido
nombre = input("Ingrese el nombre: ")
#procedimiento para que el programa determine cuantas letras tiene el nombre (contando los espacios)
nombre=(nombre.upper()," tiene ",(len(nombre))," letras")
print(nombre)