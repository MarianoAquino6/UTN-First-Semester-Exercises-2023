# Crear un programa que solicite al usuario ingresar precio unitario y cantidad
# de 5 productos. Almacenar cada valor en dos listas distintas. Luego imprimir
# el precio total de cada artículo.

lista_1 = []
lista_2 = []

lista_precios_totales = []
contador_productos = 0

while (contador_productos < 6):
    precio_unitario_txt = input("Ingrese el precio unitario")
    precio_unitario_int = int(precio_unitario_txt)
    lista_1.append(precio_unitario_int)

    cantidad_productos_txt = input("Ingrese la cantidad de productos")
    cantidad_productos_int = int(cantidad_productos_txt)
    lista_2.append(cantidad_productos_int)

    precio_total = precio_unitario_int * cantidad_productos_int
    lista_precios_totales.append(precio_total)

    contador_productos += 1

print(f"La primera lista es: {lista_1}")
print(f"La segunda lista es: {lista_2}")

contador_print = 0

while (contador_print < 6):
    posicion_articulo = contador_print + 1
    print(f"El precio total del {posicion_articulo}° articulo es de: {lista_precios_totales[contador_print]}")
    contador_print += 1