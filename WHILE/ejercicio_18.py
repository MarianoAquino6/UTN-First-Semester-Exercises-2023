# Dado un número entero n, imprimir la suma de todos los números que son
# múltiplos de 5 menores o iguales a n.

numero_txt = input("Ingrese su numero")
numero_int = int(numero_txt)

contador = 0
numero_descendente = numero_int
acumulador = 0

while (numero_int > contador):
    calculo_multiplo = numero_descendente % 5
    if (calculo_multiplo == 0):
        acumulador = acumulador + numero_descendente
    numero_descendente -= 1
    contador += 1

print(acumulador)