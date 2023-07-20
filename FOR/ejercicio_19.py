# Dada una lista de palabras, imprimir las palabras que tienen una letra
# mayúscula.

lista_palabras = ["Hola", "Mundo", "en", "Python"]

for palabra in lista_palabras:
    for letra in palabra:
        if (letra.isupper()):
            print(palabra)