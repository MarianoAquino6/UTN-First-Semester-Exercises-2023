# Dado un número entero n, imprimir todos los números desde n hasta 1 en
# orden descendente.

numero_txt = input("Ingrese un numero")
numero_int = int(numero_txt)

while (numero_int >= 1):
    print(numero_int)
    numero_int = numero_int - 1