# Crea un diccionario que contenga el nombre y el nivel de dificultad de varios
# juegos de mesa. Luego, pedirle al usuario un nivel de dificultad, buscar los que
# coinciden e imprimir sus nombres

diccionario = {"Ludo" : "Facil", "Monopoly" : "Dificil", "TEC" : "Intermedio"}

nivel_dificultad_ingresado = input("Ingrese el nombre del producto")

for juego in diccionario:
    if (diccionario[juego] == nivel_dificultad_ingresado):
        print(juego)