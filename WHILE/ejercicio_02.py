# Dado un número entero n, imprimir todos los números desde 1 hasta n en
# orden ascendente.

numero_txt = input("Ingrese un numero")
numero_int = int(numero_txt)

contador = 1

while (numero_int >= contador):
    print(contador)
    contador = contador + 1