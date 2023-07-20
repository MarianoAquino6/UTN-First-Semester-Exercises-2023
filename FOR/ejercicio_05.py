# Dada una lista de números, imprimir el número más pequeño de la lista.

lista_numeros = [10, 2, 40, 10]
min_numero = lista_numeros[0]

for numero in lista_numeros:
    if(numero < min_numero):
        min_numero = numero

print(min_numero)