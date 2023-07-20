# Dada una lista de números, imprimir la cantidad de números negativos en la
# lista.

lista_numeros = [-8, -4, -2, 2, 4, 5]
cantidad_lista = len(lista_numeros)

contador = 0
contador_negativos = 0

while (cantidad_lista > contador):
    if (lista_numeros[contador] < 0):
        contador_negativos += 1
    contador += 1

print(contador_negativos)