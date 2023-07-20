# Dada una lista de números, imprimir la suma de todos los elementos de la
# lista.

lista_numeros = [1,4,15,20]
cantidad_lista = len(lista_numeros)
contador = 0
acumulador = 0

while (cantidad_lista > contador):
    acumulador = acumulador + lista_numeros[contador]
    contador = contador + 1

print(acumulador)