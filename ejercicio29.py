# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se
#cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de
#dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad 
#de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# se definen las variables y se pide que se ingrse la invercion inicial
inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04

#se hacen los procedimientos para sacar lo que se pide en el ejercicio y se imprime a pantalla cada cosa pedida
bal1 = inversion * (1 + interes)
#se imprime por pantalla 
print("Balance tras el primer año:" ,(round(bal1, 2)))
bal2 = bal1 * (1 + interes)
print("Balance tras el segundo año:" ,(round(bal2, 2)))
bal3 = bal2 * (1 + interes)
print("Balance tras el tercer año:" ,(round(bal3, 2)))