# Dada una lista de palabras, imprimir la cantidad total de vocales en la lista

lista_palabras = ["oscar", "homero", "ozzy"]

contador_vocales = 0

for palabra in lista_palabras:
    for letras in palabra:
        if (letras == "a" or letras == "e" or letras == "i" or letras == "o" or letras == "u"):
            contador_vocales += 1

print(contador_vocales)