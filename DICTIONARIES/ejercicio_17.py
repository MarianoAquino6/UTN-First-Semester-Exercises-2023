# Crea un diccionario que represente las películas de un cine, donde las claves
# son los nombres de las películas y los valores son los horarios
# correspondientes. Modifica el horario de la película "Avengers: Endgame" a las
# 19:30.

diccionario = {"Avengers: Endgame" : 20.30, "Jurassic Park" : 17.50}

diccionario["Avengers: Endgame"] = 19.30

for key in diccionario:  #Para configurar que muestre los numeros con 2 decimales en vez de solo uno
    diccionario[key] = "{:.2f}".format(diccionario[key])

print(diccionario)