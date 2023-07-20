# Crea dos listas de 10 números enteros cada una y realiza una multiplicación
# de los elementos con el mismo índice en ambas listas.

lista_1 = [10, 9, 1, 12, 14, 20 ,41, 81, 92, 54]
lista_2 = [54, 84, 72, 95, 62, 31, 41, 25, 85, 14]

contador = 0

for numero in lista_1:
    multiplicacion = lista_1[contador] * lista_2[contador]
    print(f"El resultado de la multiplicacion de el {contador}° elemento en la primera lista, por el {contador}° elemento en la segunda lista es de: {multiplicacion}")
    contador += 1