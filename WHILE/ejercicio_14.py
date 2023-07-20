# Dada una cadena de texto, imprimir la cantidad de veces que aparece una
# letra específica en la cadena.

string = input("Ingrese una cadena de texto")
longitud_string = len(string)

contador = 0
contador_a = 0

while (longitud_string > contador):
    if (string[contador] == "a"):
        contador_a += 1
    contador += 1

print(contador_a)