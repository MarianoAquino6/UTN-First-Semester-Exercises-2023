# Crear un programa que solicite al usuario ingresar: nombre del producto,
# cantidad y precio unitario. Guardar los datos en 3 listas distintas. Solicitar
# productos hasta que el nombre del producto sea ‘xxx’. Luego imprimir la lista
# de artículos con el siguiente formato:
# nombre_articulo cantidad $ precio_unitario $ total
# Ejemplo:
# alfajor capitan del espacio 6 $ 150 $ 900

lista_1 = []
lista_2 = []
lista_3 = []

lista_total = []

flag = True

while (flag == True):
    nombre_producto = input("Ingrese el nombre del producto")

    if (nombre_producto == "xxx"):
        flag = False
    else:
        cantidad_productos_txt = input("Ingrese la cantidad de productos")
        cantidad_productos_int = int(cantidad_productos_txt)
        precio_unitario_txt = input("Ingrese el precio unitario")
        precio_unitario_int = int(precio_unitario_txt)
        lista_1.append(nombre_producto)
        lista_2.append(cantidad_productos_int)
        lista_3.append(precio_unitario_int)
    
    precio_total = cantidad_productos_int * precio_unitario_int
    lista_total.append(precio_total)

contador_print = 0

while (len(lista_1) > contador_print):
    print(f"{lista_1[contador_print]} {lista_2[contador_print]} ${lista_3[contador_print]} ${lista_total[contador_print]}")
    contador_print += 1