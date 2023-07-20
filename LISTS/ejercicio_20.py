# A partir de la lista: [1,80,5,0,15,-5,1,79] determinar, el mayor, el menor, el
# promedio y la suma total de todos los elementos

lista = [1, 80, 5 ,0, 15, -5, 1, 79]

contador_indice = 0
flag_mayor = True
flag_menor = True
acumulador = 0
contador = 0

for numero in lista:
    if (flag_mayor == True):
        numero_mayor = numero
        numero_menor = numero
        flag_mayor = False
    elif (numero > numero_mayor):
        numero_mayor = numero
    elif (numero < numero_menor):
        numero_menor = numero
    acumulador = acumulador + numero
    contador += 1

promedio = acumulador / contador
print(f"El mayor es: {numero_mayor}, el menor es: {numero_menor}, el promedio es: {promedio}, y la suma es: {acumulador}")
    