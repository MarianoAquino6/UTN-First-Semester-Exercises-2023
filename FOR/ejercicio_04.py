# Dado un número entero n, imprimir la suma de los números impares menores
# o iguales a n.

numero_txt = input("Ingrese su numero")
numero_int = int(numero_txt)

acumulador = 0

for numero in range(1, numero_int+1, 2):
    acumulador = acumulador + numero
print(acumulador)