# Dado un número entero n, imprimir la secuencia de números pares menores o
# iguales a n.

numero_txt = input("Ingrese su numero")
numero_int = int(numero_txt)

for numero in range(0, numero_int+1, 2):
    print(numero)