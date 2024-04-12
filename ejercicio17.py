#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma
#automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del 
#cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, 
#si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
import os
os.system('cls' if os.name == 'nt' else 'clear')


edad=int(input("Ingrese la edad de la persona: "))

# esta funcion va a decir lo que debe pagar la persona segun la edad
if edad < 4:
    precio = 0

elif edad <= 18:
    precio = 4

else:
    precio = 10
# Imprime el precio que la persana debe pagar
print(f"El precio que la persona debe pagar es L: ",precio)