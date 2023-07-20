# Dada una lista de números, imprimir la suma de los números en la lista que
# son mayores que el promedio de la lista.

lista_numeros = [40, 20, 1, 46, 18]
longitud_lista = len(lista_numeros)

acumulador_promedio = 0
acumulador_numeros_mayores = 0

for numero in lista_numeros:
    acumulador_promedio = acumulador_promedio + numero

promedio_lista = acumulador_promedio / longitud_lista

for numero_2 in lista_numeros:
    if (numero_2 > promedio_lista):
        acumulador_numeros_mayores = acumulador_numeros_mayores + numero_2

print(acumulador_numeros_mayores)