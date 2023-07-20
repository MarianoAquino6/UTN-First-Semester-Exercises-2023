# Crea un diccionario que represente las edades de varias personas, donde las
# claves son los nombres de las personas y los valores son sus edades.
# Imprime la edad de la persona más joven.

diccionario = {"Omar" : 15, "Enrique" : 8, "Raul" : 35, "Antonio" : 44}

flag_joven = True

for valor in diccionario:
    if (flag_joven == True):
        min_edad = diccionario[valor]
        flag_joven = False
    elif (diccionario[valor] < min_edad):
        min_edad = diccionario[valor]

print(min_edad)