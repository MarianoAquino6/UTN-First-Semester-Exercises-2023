# Escribir un programa que le pida al usuario que ingrese un número entero, 
# y luego imprima "El número es divisible por 3 y por 5" si el número es divisible por 3 y por 5,
# o "El número no es divisible por 3 y por 5" si el número no es divisible por 3 y por 5.

numero_txt = input("Ingrese un numero entero")
numero_int = int(numero_txt)

calculo_divisible_3 = numero_int % 3
calculo_divisible_5 = numero_int % 5

if (calculo_divisible_3 == 0 and calculo_divisible_5 == 0):
    print("El número es divisible por 3 y por 5")
else:
    print("El número no es divisible por 3 y por 5")