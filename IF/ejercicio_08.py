# Escribir un programa que le pida al usuario que ingrese un número entero positivo, 
# y luego imprima "El número es un cuadrado perfecto" si el número es un cuadrado perfecto, 
# o "El número no es un cuadrado perfecto" si el número no es un cuadrado perfecto.

numero_txt = input("Ingrese un numero positivo")
numero_int = int(numero_txt)

raiz_numero = numero_int ** 0.5 # o raiz_numero:float = math.sqrt(numero_int)

raiz_int = int(raiz_numero)

numero_dividido_por_si_mismo = raiz_numero / raiz_int

if (numero_dividido_por_si_mismo == 1):
    print("El numero es cuadrado perfecto")
else:
    print("El numero no es cuadrado perfecto")

# otra manera es con if(raiz_int.is_integer():