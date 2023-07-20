# Dada una lista de palabras, imprimir las palabras que tienen una longitud impar.

lista_palabras = ["rolo", "tinto", "chaleco", "meta"]

for palabra in lista_palabras:
    longitud_palabras = len(palabra)
    calculo_par = longitud_palabras % 2
    if (calculo_par != 0):
        print(palabra)

