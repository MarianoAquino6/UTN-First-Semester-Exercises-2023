# Dado un número entero n, imprimir la secuencia de números de Harshad
# menores o iguales a n.

numero_txt = input("Ingrese el numero")
numero_int = int(numero_txt)

for numero in range(1, numero_int+1, 1):
    numero_string = str(numero)
    acumulador = 0
    for digitos in numero_string:
        digitos_int = int(digitos)
        acumulador = acumulador + digitos_int
    calculo_harshad = numero % acumulador
    if (calculo_harshad == 0):
        print(numero)