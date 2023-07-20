# Dada una lista de números, imprimir todos los números que son mayores que
# el promedio de la lista.

lista_numeros = [1,2,3,4,5]
cantidad_lista = len(lista_numeros)

contador = 0
contador_2 = 0
acumulador_lista = 0

while (cantidad_lista > contador):
    acumulador_lista = acumulador_lista + lista_numeros[contador]
    contador = contador + 1

promedio = acumulador_lista / cantidad_lista
print(promedio)

while (cantidad_lista > contador_2):
    if (lista_numeros[contador_2] > promedio):  #Si el elemento de la lista es mayor al promedio
        print(lista_numeros[contador_2]) #Imprimir ese elemento
    contador_2 = contador_2 + 1