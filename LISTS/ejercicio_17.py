# Crea dos listas de números y encuentra los elementos que se encuentran en
# ambas listas

lista_1 = [4, 10, 24, 15]
lista_2 = [8, 100, 24, 4]

contador = 0

for elemento in lista_1:
    while (contador < len(lista_2)):
        if (elemento == lista_2[contador]):
            print(f"El numero {elemento} se repite")
        contador += 1
    contador = 0