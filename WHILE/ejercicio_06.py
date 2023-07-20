# Dado un número entero n, imprimir la suma de todos los números pares,
# menores o iguales a n.

numero_txt = input("Ingrese un numero")
numero_int = int(numero_txt)

numero_descendente = numero_int
contador = 0
acumulador_pares = 0
acumulador_menores = 0
acumulador_iguales = 0

while (numero_int >= contador):  #Incluimos el 0
    calculo_par = numero_descendente % 2

    if (calculo_par == 0):
        acumulador_pares = acumulador_pares + numero_descendente
    if (numero_descendente < numero_int):
        acumulador_menores = acumulador_menores + numero_descendente
    if (numero_descendente == numero_int):
        acumulador_iguales = acumulador_iguales + numero_descendente
    numero_descendente = numero_descendente - 1

    contador = contador + 1

suma_numeros = acumulador_pares + acumulador_iguales + acumulador_menores

print(suma_numeros)