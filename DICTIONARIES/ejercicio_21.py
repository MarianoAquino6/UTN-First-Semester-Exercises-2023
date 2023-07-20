# Crea un diccionario que represente los gastos de una persona en diferentes
# categorías, donde las claves son los nombres de las categorías y los valores
# son los gastos correspondientes. Calcula el total de gastos de la persona.

diccionario = {"Sandias" : 10, "Juegos" : 1, "Uber" : 4, "Sal" : 15}

acumulador = 0

for categoria in diccionario:
    acumulador = acumulador + diccionario[categoria]

print(acumulador)