# Crea un diccionario que represente los juegos de una consola, donde las
# claves son los nombres de los juegos y los valores son las puntuaciones
# correspondientes. Solicita al usuario el nombre de un juego y luego su
# puntuación, si el juego no existe agregarlo y si existe actualizar su puntuación

diccionario = {"Mario Bros" : 10, "Battlefield" : 8, "Valorant" : 15}

nombre_ingresado = input("Ingrese el nombre del juego")
puntuacion_ingresada_txt = input("Ingrese la puntuacion del juego")
puntuacion_ingresada_int = int(puntuacion_ingresada_txt)


# Se tuvo que hacer con if in, ya que cada vez que se agrega un elemento al diccionario usando for tira error
if (nombre_ingresado in diccionario): 
        diccionario[nombre_ingresado] = puntuacion_ingresada_int
else:
        diccionario[nombre_ingresado] = puntuacion_ingresada_int

print(diccionario)