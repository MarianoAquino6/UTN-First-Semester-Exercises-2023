# Dada una cadena de texto, imprimir cada uno de los caracteres en la cadena.

string = input("Ingrese su cadena de texto")
cantidad_caracteres_string = len(string)
contador = 0

while (cantidad_caracteres_string > contador):
    print(string[contador])
    contador = contador + 1