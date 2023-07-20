# Escribir un programa que le pida al usuario que ingrese un número entero, 
# y luego imprima "El número es positivo y par" si el número es positivo y divisible por 2, 
# o "El número no cumple ninguna condición" si el número no cumple ninguna de las dos condiciones anteriores.

numero_txt = input("Ingrese un numero entero")
numero_int = int(numero_txt)
calculo_divisible = numero_int % 2

if (numero_int > 0 and calculo_divisible == 0):
    print("El numero es positivo y par")
elif (numero_int < 0 and calculo_divisible != 0):
    print("El número no cumple ninguna condición")