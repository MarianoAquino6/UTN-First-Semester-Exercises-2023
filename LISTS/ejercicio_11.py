# Crea una lista de palabras y pide al usuario que ingrese una palabra. Luego,
# muestra todas las palabras de la lista que tienen la misma longitud que la
# palabra ingresada.

lista = ["pizza", "ozzy", "dio", "james hetfield", "cerveza", "calculadora"]

nueva_palabra = input("Ingrese una nueva palabra")
longitud_nueva_palabra = len(nueva_palabra)

contador_letras = 0

for palabra in lista:
    for letra in palabra:
        contador_letras += 1
    if (contador_letras == longitud_nueva_palabra):
        print(palabra)
    contador_letras = 0