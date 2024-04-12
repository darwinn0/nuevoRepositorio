#programa que pide al usuario peso, estatura y calcula su masa coorporal
import os
os.system('cls' if os.name == 'nt' else 'clear')

# se definen las variables y se pide que el usuario ingrese lo pedido 
peso =(input("Introduzca su peso en kg: "))
estatura =(input("cual es su estatura en metros: "))

# calculo para saber el peso de la persona
imc = round(float(peso)/float(estatura)**2.2)

# imprime en pantalla la masa coorporal
print(f"Tu índice de masa corporal es: ",imc) 