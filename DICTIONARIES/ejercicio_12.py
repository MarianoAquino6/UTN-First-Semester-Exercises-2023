# Crea un diccionario que represente una lista de las compras. Cada clave del
# diccionario debe ser el nombre de un producto y cada valor debe ser su
# cantidad. Pedir al usuario que ingrese el nombre del producto e imprimir la
# cantidad

diccionario = {"Manzanas" : 20, "Zanahorias" : 10, "Sandias" : 4}

nombre_producto_ingresado = input("Ingrese el nombre del producto")

for producto in diccionario:
    if (nombre_producto_ingresado == producto):
        print(diccionario[producto])