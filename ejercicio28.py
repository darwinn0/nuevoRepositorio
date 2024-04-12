# Escribir un programa que almacene en una lista los números del 0 al 10 y los muestre por pantalla en orden inverso separados por comas.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# se declara la variable donde se almacenara las cosas
numeros = [0,1,2,3,4,5,6,7,8,9,10]
# usamos el ciclo for y determinamos el rango que deseamos 
for i in range(1, 12):
    #imprimimos la variable donde se almacenan los numeros y dentro de corchetes pones -i para que se muestren en pantalla al reves
    print(numeros[-i], end=", ")