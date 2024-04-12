#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual 
#y el número de años, y muestre por pantalla el capital obtenido en la inversión.
import os
os.system('cls' if os.name == 'nt' else 'clear')

#definir variables y pide al usuario que ingrse lo que se le pide
cantidad = float(input("Cantidad a invertir: "))
interes = float(input("Interés porcentual anual: "))
años = int(input("Años: "))
#muestra en pantalla el calculo
print("Capital final: ", (round(cantidad * (interes / 100 + 1) ** años, 2)))