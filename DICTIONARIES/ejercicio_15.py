# Crea un diccionario que contenga el nombre y el sueldo de varios empleados.
# Luego, permite al usuario aumentar el sueldo de un empleado y actualizar el
# valor correspondiente en el diccionario.

diccionario = {"Mariano" : 800, "Azul" : 200, "Florencia": 400, "Omar" : 500}

empleado_aumento_sueldo = input("Ingrese el aumento de sueldo de alguno de los trabajadores")
cantidad_aumento_sueldo_txt = input("Ingrese cuanto desea aumentar el sueldo")
cantidad_aumento_sueldo_int = int(cantidad_aumento_sueldo_txt)


for empleado in diccionario:
    if (empleado == empleado_aumento_sueldo):
        nuevo_sueldo = diccionario[empleado] + cantidad_aumento_sueldo_int
        diccionario[empleado] = nuevo_sueldo

print(diccionario)
