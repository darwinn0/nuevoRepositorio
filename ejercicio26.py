# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista y la muestre por pantalla.


import os
os.system('cls' if os.name == 'nt' else 'clear')

#se declara una varible y con llaves se le ponen dentro de comillas las asignaturas
asiganaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua", "Español"]
#se imprime la variable asignatura donde estan las materias
print(asiganaturas)