# Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, muestra
# la primera letra de la palabra. Repite este proceso hasta que el usuario
# ingrese una palabra que comience con la letra "z".

lista = []

flag = True

while (flag == True):
    palabra = input("Ingrese una palabra")
    for letra in palabra[0]:
        if (letra != "z"):
            print(letra)
            lista.append(palabra)
        else:
            flag = False