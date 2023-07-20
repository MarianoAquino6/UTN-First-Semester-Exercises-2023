# Dado un número entero n, imprimir la secuencia de números primos menores o iguales a n.

numero_txt = input("Ingrese su numero entero")
numero_int = int(numero_txt)

for numero in range(1, numero_int+1, 1):
    contador_divisible = 0
    for numero_ascendente in range(1, numero+1, 1):
        calculo_divisible = numero % numero_ascendente
        if (calculo_divisible == 0):
            contador_divisible += 1
    if (contador_divisible == 2):
        print(numero)