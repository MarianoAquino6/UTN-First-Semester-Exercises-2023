# Crea un diccionario que represente los contactos de un teléfono, donde las
# claves son los nombres de las personas y los valores son los números de
# teléfono correspondientes. Solicitar al usuario el nombre de un contacto:
# agregarlo al diccionario en caso de que no exista. En caso de que exista
# modificar el número de teléfono del contacto.

diccionario = {"Ricardo" : 1135041287, "Raul" : 1158743592, "Pedro" : 1154853526, "Roberto" : 1197643182}

nuevo_contacto = input("Ingrese el nuevo contacto")
telefono_nuevo_contacto_txt = input("Ingrese el nuevo telefono")
telefono_nuevo_contacto_int = int(telefono_nuevo_contacto_txt)

if (nuevo_contacto in diccionario):
    diccionario[nuevo_contacto] = telefono_nuevo_contacto_int
else:
    diccionario[nuevo_contacto] = telefono_nuevo_contacto_int

print(diccionario)