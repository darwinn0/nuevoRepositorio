#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que 
#introduzca la contraseña correcta.


import os
os.system('cls' if os.name == 'nt' else 'clear')

#se definen variables y en una de ellas pondremos la contraseña y en la otra sera para que ingresen la contraseña
llave = "admin"
contraseña =""

#se usa el ciclo while para que el programa se repita hasta que se ingrese la contraseña correcta
while contraseña != llave:
    contraseña = input("Introduce la contraseña: ")
    # cuando se imprime que la contraseña es correcta el programa se termina
print("Contraseña correcta")