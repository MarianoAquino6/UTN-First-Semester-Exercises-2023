# Dada una lista de palabras, imprimir todas las palabras que tengan una
# longitud mayor a 5 caracteres.

lista_palabras = ["pedro", "javier", "roman"]
longitud_lista = len(lista_palabras)  #Al separar los strings con comas y ponerlos entre comillas se los considera como elementos individuales

contador = 0

while (longitud_lista > contador):
    if (len(lista_palabras[contador]) > 5):  #Se hace referencia a la longitud de los caracteres de cada elemento de la lista
        print(lista_palabras[contador])
    contador += 1
