#programa que pregunta el precio del producto con decimales
import os
os.system('cls' if os.name == 'nt' else 'clear')

#define la variable y se pide que el usuario ingrese lo pedido
precio = input("Introduce el precio del producto con dos decimales:  ")

#imprime en pantalla el calculo para saber el calculo del precio de los productos
print(precio[:precio.find('.')], 'lempiras y', precio[precio.find('.')+1:], 'centabos.') 
