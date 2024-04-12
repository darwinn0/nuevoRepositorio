#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
import os
os.system('cls' if os.name == 'nt' else 'clear')

edad = int(input("Ingrese la edad de la persona: "))
#con el ciclo for se repetira hasta que llegue a los años que la persona tiene
for a in range(edad):
    #imprime los años de la persona 
    print(f"Has cumplido: ", (a+1),"años")