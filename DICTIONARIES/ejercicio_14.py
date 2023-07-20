# Crea un diccionario que contenga el nombre como clave y el puntaje como
# valor de varios jugadores en un juego. Luego, pedirle al usuario el nombre del
# jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.

diccionario = {"Mariano" : 8, "Azul" : 2, "Florencia": 4, "Omar" : 5}

nuevo_jugador = input("Ingrese el nombre del nuevo jugador")
nuevo_puntaje_txt = input("Ingrese el puntaje del nuevo jugador")
nuevo_puntaje_int = int(nuevo_puntaje_txt)

diccionario[nuevo_jugador] = nuevo_puntaje_int

print(diccionario)