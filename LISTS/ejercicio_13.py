# Crea una lista de números y encuentra el promedio de todos los números en
# la lista.

lista = [12, 14, 10, 15, 9]

acumulador = 0
contador = 0

for numero in lista:
    acumulador = acumulador + numero
    contador += 1

promedio = acumulador / contador
print(promedio)