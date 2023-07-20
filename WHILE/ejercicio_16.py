# Dada una lista de números, imprimir todos los números que son múltiplos de 3.

lista_numeros = [10,12,24,15]
longitud_lista = len(lista_numeros)

contador = 0

while (longitud_lista > contador):

    calculo_multiplo = lista_numeros[contador] % 3
    if (calculo_multiplo == 0):
        print(lista_numeros[contador])

    contador += 1