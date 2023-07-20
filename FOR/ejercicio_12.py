# Dada una lista de números, imprimir la cantidad de números pares en la lista

lista_numeros = [24, 15, 18, 11, 20, 92]

contador_pares = 0

for numero in lista_numeros:
    calculo_pares = numero % 2
    if (calculo_pares == 0):
        contador_pares += 1

print(contador_pares)