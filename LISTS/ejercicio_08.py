# Crea una lista con los nombres de tus 5 libros favoritos y luego imprime solo
# los primeros 3 libros de la lista.

lista = ["Ninguno_1", "Ninguno_2", "Ninguno_3", "Ninguno_4", "Ninguno_5"]

contador_indice = 0

for indice in range(len(lista)):
    if (indice < 3):
        print(lista[indice])
    else:
        break