# Dada una lista de números, imprimir la cantidad de números pares en la lista.

numero_txt = input("Ingrese un numero")
numero_int = int(numero_txt)

numero_descendente = numero_int
contador = 0

while (numero_int >= contador):    #Si quiero incluir el 0 es >=
    calculo_par = numero_descendente % 2

    if (calculo_par == 0):
        print(numero_descendente)
    numero_descendente = numero_descendente - 1
    contador = contador + 1