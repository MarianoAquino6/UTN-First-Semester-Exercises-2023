# Dado un número entero n, imprimir la suma de todos los números impares
# menores o iguales a n.

numero_txt = input("Ingrese un numero")
numero_int = int(numero_txt)

numero_descendente = numero_int
contador = 0
acumulador_impares = 0
acumulador_menores = 0
acumulador_iguales = 0

while (numero_int >= contador):  #Incluimos el 0
    calculo_impar = numero_descendente % 2

    if (calculo_impar != 0):
        acumulador_impares = acumulador_impares + numero_descendente
    if (numero_descendente < numero_int):
        acumulador_menores = acumulador_menores + numero_descendente
    if (numero_descendente == numero_int):
        acumulador_iguales = acumulador_iguales + numero_descendente
    numero_descendente = numero_descendente - 1

    contador = contador + 1

suma_numeros = acumulador_impares + acumulador_iguales + acumulador_menores

print(suma_numeros)