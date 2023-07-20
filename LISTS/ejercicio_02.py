# Crea una lista con 5 números enteros. Luego solicita un nuevo número y
# reemplaza el tercer elemento de la lista por el número ingresado. Finalmente
# imprime todos los números

lista = [4, 2, 10, 47, 6]

nuevo_numero = input("Ingrese su nuevo numero")

lista[2] = nuevo_numero

for numero in lista:
    print(numero)