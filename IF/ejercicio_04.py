# Escribir un programa que le pida al usuario que ingrese dos números enteros, 
# y luego imprima "El primer número es mayor" si el primer número es mayor que el segundo, 
# "El segundo número es mayor" si el segundo número es mayor que el primero, 
# o "Los dos números son iguales" si los dos números son iguales.

numero_txt_1 = input("Ingrese el primer numero")
numero_txt_2 = input("Ingrese el segundo numero")

numero_int_1 = int(numero_txt_1)
numero_int_2 = int(numero_txt_2)

if (numero_int_1 > numero_int_2):
    print("El primer número es mayor")
elif (numero_int_2 > numero_int_1):
    print("El segundo número es mayor")
else:
    print("Los dos números son iguales")
