# Escribir un programa que le pida al usuario que ingrese un número entero, 
# y luego imprima "El número es múltiplo de 4 y de 6" si el número es múltiplo de 4 y de 6, 
# o "El número no es múltiplo de 4 y de 6" si el número no es múltiplo de 4 y de 6.

numero_txt = input("Ingrese un numero entero")
numero_int = int(numero_txt)

calculo_multiplo_4 = numero_int % 4
calculo_multiplo_6 = numero_int % 6

if (calculo_multiplo_4 == 0 and calculo_multiplo_6 == 0):
    print("El número es múltiplo de 4 y de 6")
else:
    print("El número no es múltiplo de 4 y de 6")