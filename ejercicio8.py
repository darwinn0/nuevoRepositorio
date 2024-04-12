
import os
os.system('cls' if os.name == 'nt' else 'clear')
#definir variables y pedir al usuario que ingrse lo pedido 
peso_payaso = 112
peso_muñeca = 75

#pedi al usuario que ingrese la cantidad de payasos que se desea enviar
payasos = int(input("Ingrse la cantidad de payasos a enviar: "))
muñecas = int(input("Ingrece la cantidad de muñecas a enviar: "))

#calculo para sacar el peso total
peso_total = peso_payaso * payasos + peso_muñeca * muñecas

#mostrar a pantalla el peso total de los juguetes
print("El peso total del paquete es ",peso_total)