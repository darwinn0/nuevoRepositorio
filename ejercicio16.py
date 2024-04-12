#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
#El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y
#el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
#que le corresponde.
import os
os.system('cls' if os.name == 'nt' else 'clear')

nombre = input("Ingrese el nombre de la persona: ")
genero = input("Ingrse el genero de la persona: ")
if genero == "M":
    if nombre < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre > "honbres":
        grupo = "B"
    else:
        grupo = "A"
print("El grupo al que debes ir es",grupo)