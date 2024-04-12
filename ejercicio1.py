#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
import os
os.system('cls' if os.name == 'nt' else 'clear')
 
#pregunta la edad de la persona 
edad = int(input("Ingrese la edad de la persona: "))
#esta funcion hace que el programa diga si es menor o mayor de edad
if edad <= 18:
    print (f"La persona es menor de edad")
else:
    print (f"La persona es mayor de edad")

