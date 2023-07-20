# Escribir un programa que le pida al usuario que ingrese dos números enteros, 
# y luego imprima "El primer número es positivo" si el primer número es mayor que cero, 
# "El segundo número es positivo" si el segundo número es mayor que cero, o "Ambos números son negativos" 
# si los dos números son negativos.

numero_01_txt = input("Ingrese su perimer numero entero")
numero_02_txt = input("Ingrese su segundo numero entero")
numero_01_int = int(numero_01_txt)
numero_02_int = int(numero_02_txt)

if (numero_01_int > 0):
    print("El primer número es positivo")
if (numero_02_int > 0):
    print("El segundo número es positivo")
if (numero_01_int < 0 and numero_01_int < 0):
    print("Ambos números son negativos")