# Dada una lista de números, imprimir el número más grande de la lista.

lista_numeros = [1, 20, 40, 10]
max_numero = lista_numeros[0]

for numero in lista_numeros:
    if(numero > max_numero):
        max_numero = numero

print(max_numero)