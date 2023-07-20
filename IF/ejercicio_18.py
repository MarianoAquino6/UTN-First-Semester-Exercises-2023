# Escribir un programa que le pida al usuario que ingrese un número entero, 
# y luego imprima "El número es par y es múltiplo de 3" si el número es par y es múltiplo de 3, 
# o "El número no cumple ninguna de las dos condiciones" si el número no cumple ninguna de las dos condiciones.

numero_txt = input("Ingrese un numero entero")
numero_int = int(numero_txt)

calculo_par = numero_int % 2
calculo_multiplo_3 = numero_int % 3

if (calculo_par == 0 and calculo_multiplo_3 == 0):
    print("El número es par y es múltiplo de 3")
elif (calculo_par != 0 and calculo_multiplo_3 != 0):
    print("El número no cumple ninguna de las dos condiciones")