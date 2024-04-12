
import os
os.system('cls' if os.name == 'nt' else 'clear')

#este paso es para escribir la contraseña con la que se va entrar al programa
llave = "admin"
#aqui se le pide al usuario que ingrese la contraseña
contraseña = input("Introduce la contraseña: ")
#esta funcion es para que el programa determine si la contraseña ingresada es correcta
if llave == contraseña.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")