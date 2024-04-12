#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese 
#número separados por comas.

#se define la varible y se le pide al usurio que ingrese un numero
numero = int(input("Ingrese un numero entero: "))
#se usa el ciclo for para establecer un rango y diga los numeros impares
for a in range (1, numero +1, 2):
    #muestra a pantalla los numeros impares dentro del rango establecido
    print(a, end=", ")