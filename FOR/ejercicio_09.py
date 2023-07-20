# Dada una lista de números, imprimir la cantidad de números negativos en la
# lista.

lista_numeros = [-5, -8, 5, 24, 9, -12]

contador_negativos = 0

for numeros in lista_numeros:
    if (numeros < 0):
        contador_negativos += 1

print(contador_negativos)