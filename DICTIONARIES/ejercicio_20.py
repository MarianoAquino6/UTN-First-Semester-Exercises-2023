# Crea un diccionario que represente los asientos de un avión, donde las claves
# son los números de asientos y los valores son "True" si están ocupados y
# "False" si no lo están. Solicita al usuario un número de asiento y modifica su
# valor para marcarlo como ocupado. Luego imprimí la lista de asientos libres

diccionario = {10 : True, 20 : False, 15: True, 32 : False}

lista_asientos_libres = []

asiento_ingresado_txt = input("Ingresa el numero de asiento a modificar")
asiento_ingresado_int = int(asiento_ingresado_txt)

for asiento in diccionario:
    if (asiento_ingresado_int == asiento and diccionario[asiento] == False):
        diccionario[asiento] = True
    if (diccionario[asiento] == False):
        lista_asientos_libres.append(asiento)

print(diccionario)
print(f"Los asientos libres son los asientos con numero: {lista_asientos_libres}")