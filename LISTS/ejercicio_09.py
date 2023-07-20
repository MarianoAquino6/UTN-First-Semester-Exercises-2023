# Crea una lista de números enteros y pide al usuario que ingrese otro número
# entero. Luego, busca el número ingresado en la lista y muestra la posición en
# la que se encuentra. Si el número no se encuentra en la lista, muestra un
# mensaje indicando que no se encontró

lista = [12, 14, 10, 15, 9]

numero_ingresado_txt = input("Ingrese un nuevo numero")
numero_ingresado_int = int(numero_ingresado_txt)
contador = 0

for numero in lista:
    contador += 1
    if (numero == numero_ingresado_int):
        print(f"El numero ingresado se encuentra en la posicion {lista.index(numero_ingresado_int)}")
    elif (contador == len(lista)):
        print("No se encontro el numero ingresado en la lista")
