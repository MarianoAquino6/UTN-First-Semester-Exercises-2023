# Dada una cadena de texto, imprimir la cantidad de vocales en la cadena.

string = input("Ingrese su cadena de texto")
cantidad_string = len(string)

contador = 0
contador_vocales = 0

while (cantidad_string > contador):
    if (string[contador] == "a" or string[contador] == "e" or string[contador] == "i" or string[contador] == "o" or string[contador] == "u"):
        contador_vocales += 1
    contador += 1

print(contador_vocales)