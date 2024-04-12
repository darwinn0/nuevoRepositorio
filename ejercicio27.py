#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
#en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# se declara la variable asignatura y se le ponen las clases 
asignatura = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
# se muestra a pantalla el string que desea, se pone una coma fuera del string y se escribe la palabra donde estan almacenados los valores
print(f"Yo estudio las clases de: ",asignatura)