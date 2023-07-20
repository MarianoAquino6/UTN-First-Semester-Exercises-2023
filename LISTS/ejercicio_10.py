# Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.

lista = ["pizza", "ozzy", "dio", "james hetfield", "cerveza", "calculadora"]

contador_letras = 0

for palabra in lista:
    for letra in palabra:
        contador_letras += 1
    if (contador_letras > 5):
        print(palabra)
    contador_letras = 0