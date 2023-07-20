# Crea un diccionario que contenga las capitales de los países de América del
# Sur. Luego, pide al usuario que ingrese el nombre de un país y muestra su
# capital correspondiente.

diccionario = {"Brasil" : "Brasilia", "Panama" : "Panama", "Ecuador" : "Quito"}

pais_ingresado = input("Ingrese un pais")

for pais in diccionario:
    if (pais_ingresado == pais):
        print(diccionario[pais])