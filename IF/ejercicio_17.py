# Escribir un programa que le pida al usuario que ingrese un número entero, 
# y luego imprima "El número es negativo" si el número es menor que cero, 
# "El número es cero" si el número es igual a cero, o "El número es positivo" si el número es mayor que cero.

numero_txt = input("Ingrese un numero entero")
numero_int = int(numero_txt)

if (numero_int < 0):
    print("El número es negativo")
elif (numero_int == 0):
    print("El número es cero")
else:
    print("El número es positivo")