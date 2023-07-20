# Crea una lista de números enteros y luego encuentra la suma de los números
# en índices impares.

lista = [4, 2, 3, 1, 10, 11, 12]

acumulador = 0

for numero in range(len(lista)):
    calculo_indice_impar = numero % 2
    if (calculo_indice_impar != 0):
        acumulador = acumulador + lista[numero]

print(acumulador)