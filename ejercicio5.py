#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

import os
os.system('cls' if os.name == 'nt' else 'clear')

#declarando variables y pregunta al usuario las horas trabajadas
ht = int  (input("Ingrese la cantidad de horas trabajadas: "))
costo = int (input("Ingrese el costo de hora trabajada: "))
#calculo de la multiplicacion de las horas trabajadas y el costo por hora
resultado = (ht * costo)
#muestra a pantalla lo que se le va a pagar 
print (f"El total que debe pagarse a la persona es de L: ",resultado ) 