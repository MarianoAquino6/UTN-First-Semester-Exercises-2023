# Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, agrega
# la palabra a la lista si no se encuentra ya en la lista. Repite este proceso hasta
# que la lista tenga al menos 5 palabras.

lista = []

flag_primera_palabra = True

while (len(lista) < 6):
    nueva_palabra = input("Ingrese una nueva palabra")
    contador_repetidos = 0
    if (flag_primera_palabra == True):
        lista.append(nueva_palabra)
        print("Se agrego nueva palabra")
        print(f"Ahora la lista es {lista} y su longitud es de {len(lista)} elementos")
        flag_primera_palabra = False
    else:
        for elemento in lista:
            if (nueva_palabra == elemento):
                    print(f"{nueva_palabra} ya se encuentra en la lista")
                    contador_repetidos +=1
        if (contador_repetidos == 0):
            lista.append(nueva_palabra)
            print("Se agrego nueva palabra")
            print(f"Ahora la lista es {lista} y su longitud es de {len(lista)} elementos")

print(lista, end="")