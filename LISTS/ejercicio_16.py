# Crea dos listas con la misma cantidad de elementos y luego crea una tercera
# lista que contenga los elementos de ambas listas intercalados. Por ejemplo,
# si las dos listas son [1, 2, 3] y ["a", "b", "c"], la tercera lista debería ser [1, "a", 2,
# "b", 3, "c"].

lista_1 = [4, 10, 24, 15]
lista_2 = [8, 100, 14, 29]
lista_3 = []

contador = 0

for elemento in lista_1:
    lista_3.append(elemento)
    lista_3.append(lista_2[contador])
    contador += 1

print(lista_3, end ="")