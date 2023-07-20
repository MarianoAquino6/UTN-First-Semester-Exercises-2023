# Crea un diccionario que represente una lista de tareas pendientes, donde las
# claves son las tareas y los valores son "True" si están completadas y "False" si
# no lo están. Solicita al usuario el nombre de una tarea y modifica el valor para
# marcarla como completada. Imprimir el listado de tareas pendientes

diccionario = {"Limpiar casa" : False, "Estudiar" : True, "Morir" : False, "Jugar Valorant" : False}

lista_pendientes = []

tarea_ingresada = input("Ingrese el nombre de la tarea")

for tarea in diccionario:
    if (tarea == tarea_ingresada):
        diccionario[tarea] = True
    elif (diccionario[tarea] == False):
        lista_pendientes.append(tarea)

print(lista_pendientes)