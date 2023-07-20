# Escribir un programa que le pida al usuario que ingrese un número entero positivo, 
# y luego imprima "El número es primo" si el número es primo, o "El número no es primo" 
# si el número no es primo.

numero_txt = input("Ingrese un numero entero positivo")
numero_int = int(numero_txt)
contador = 0
contador_divisibles = 0

while (numero_int > contador):
    contador = contador + 1

    if (numero_int % contador == 0):
        contador_divisibles = contador_divisibles + 1

if (contador_divisibles == 2):
    print("El número es primo")
else:
    print("El número no es primo")