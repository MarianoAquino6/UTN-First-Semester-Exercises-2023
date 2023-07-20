# Dada una lista de palabras, imprimir las palabras que tienen una letra específica.

lista_palabras = ["tintura", "jason", "becker", "van", "halen"]

for palabra in lista_palabras:
    for letra in palabra:
        if (letra == "a"):
            print(palabra)