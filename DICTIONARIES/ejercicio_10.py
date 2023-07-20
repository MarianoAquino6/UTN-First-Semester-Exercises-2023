# Crea un diccionario que represente las notas de un examen de varios
# estudiantes, donde las claves son los nombres de los estudiantes y los
# valores son sus notas. Imprime el promedio de las notas.

diccionario = {"Tamara" : 1, "Esteban" : 7, "Ezequiel" : 10}

acumulador = 0
contador = 0

for alumno in diccionario:
    contador += 1
    acumulador = acumulador + diccionario[alumno]

promedio_notas = acumulador / contador
print(promedio_notas)