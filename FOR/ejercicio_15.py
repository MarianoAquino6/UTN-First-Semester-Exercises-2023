# Dada una lista de números, imprimir la cantidad de números impares en la
# lista.

lista_numeros = [24, 15, 18, 11, 20, 92]

contador_impares = 0

for numero in lista_numeros:
    calculo_impares = numero % 2
    if (calculo_impares != 0):
        contador_impares += 1

print(contador_impares)