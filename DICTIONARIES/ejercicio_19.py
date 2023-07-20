# Crea un diccionario que represente las temperaturas de una ciudad durante
# una semana, donde las claves son los días de la semana y los valores son las
# temperaturas correspondientes. Calcula la temperatura promedio de la
# semana.

diccionario = {"Lunes" : 10, "Martes" : 1, "Miercoles" : 4, "Jueves" : 15, "Viernes" : 11, "Sabado" : 9, "Domingo" : 12}

acumulador = 0
contador = 0

for dia in diccionario:
    acumulador = acumulador + diccionario[dia]
    contador += 1

temperatura_promedio = acumulador / contador
print(temperatura_promedio)