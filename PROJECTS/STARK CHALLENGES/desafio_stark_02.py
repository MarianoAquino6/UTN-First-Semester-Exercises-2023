from data_stark import lista_personajes
import os

# 0. Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista de héroes. La función deberá:
# Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que representan datos numéricos)
# Validar primero que el tipo de dato no sea del tipo al cual será casteado. 
# Por ejemplo si una key debería ser entero (ejemplo edad) verificar antes que no se encuentre ya en ese tipo de dato.
# Si al menos un dato fue modificado, la función deberá imprimir como mensaje ‘Datos normalizados’, caso contrario 
# no imprimirá nada.
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario imprimirá el mensaje: 
# “Error: Lista de héroes vacía”

def stark_normalizar_datos(superhero_list):
    #Takes superhero list as input
    #Normalizes data
    #Returns a message according to normalization process
    key_list = ["altura", "peso", "fuerza"]
    if not superhero_list:
        show_message = "Error: Lista de héroes vacía"
    else:
        for superhero in superhero_list:
            for key in key_list:
                replaced_value = superhero[key].replace(".", "")
                if replaced_value.isnumeric():
                    if "." in superhero[key] and superhero[key].count(".") == 1:
                        superhero[key] = float(superhero[key])
                        show_message = "Datos normalizados"
                    else:
                        superhero[key] = int(superhero[key])
                        show_message = "Datos normalizados"
    return show_message

# 1.1 Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el cual representara a un 
# héroe y devolverá un string el cual contenga su nombre formateado de la siguiente manera: 
# Nombre: Howard the Duck

def obtener_nombre(superhero_dictionary):
    #Takes a dictionary as input
    #Takes superhero's name
    #Returns a string containing superhero's name
    superhero_name = superhero_dictionary["nombre"]
    return f"Nombre: {superhero_name}"

# 1.2 Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y deberá 
# imprimirlo en la consola. La función no tendrá retorno.

def imprimir_dato(given_string):
    #Takes a string as input
    #Prints the string
    print(given_string)

# 1.3 Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por parámetro la lista de 
# héroes y deberá imprimirla en la consola. Reutilizar las funciones hechas en los puntos 1.1 y 1.2. 
# Validar que la lista no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Con este se resuelve el Ej 1 del desafío #00

def stark_imprimir_nombres_heroes(superhero_list):
    #Takes superheros list as input
    #Prints superhero's name
    if not superhero_list:
        return -1
    else:
        for superhero in superhero_list:
            imprimir_dato(obtener_nombre(superhero)) 

# 2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario 
# el cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener. 
# La función deberá devolver un string el cual contenga el nombre y dato (key) del héroe a imprimir. 
# El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.
# El string resultante debe estar formateado de la siguiente manera: 
# (suponiendo que la key es fuerza)
# Nombre: Venom | fuerza: 500

def obtener_nombre_y_dato (superhero_dictionary, superhero_key):
    #Takes superhero dictionary and key as input
    #Takes superhero's name and characteristic
    #Returns string contaning name and characteristic
    superhero_name = superhero_dictionary["nombre"]
    characteristic = superhero_dictionary[superhero_key]
    return f"Nombre: {superhero_name} | {superhero_key}: {characteristic}"

# 3. Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por parámetro la lista de héroes, 
# la cual deberá iterar e imprimir sus nombres y alturas USANDO la función creada en el punto 2. 
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Con este se resuelve el Ej 2 del desafío #00

def stark_imprimir_nombres_alturas(superhero_list):
    #Takes superhero list as input
    #Prints superhero's name and height
    if not superhero_list:
        return -1
    else:
        for superhero in superhero_list:
            print(obtener_nombre_y_dato(superhero, "altura"))

# 4.1 Crear la función 'calcular_max' la cual recibirá por parámetro la lista de héroes y una key 
# (string) la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el máximo 
# de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar 
# el héroe que tenga el dato más alto.
# Ejemplo de llamada:
# 	calcular_max(lista, 'edad')

def calcular_max(superhero_list, superhero_key):
    #Takes superhero list and key as input
    #Compares superheroes by characteristic and finds max
    #Returns superhero's max name
    flag = True
    for superhero in superhero_list:
        if (flag == True):
            max_characteristic = superhero[superhero_key]
            superhero_max_name = superhero["nombre"]
            flag = False
        elif superhero[superhero_key] > max_characteristic:
            max_characteristic = superhero[superhero_key]
            superhero_max_name = superhero["nombre"]
    return superhero_max_name

# 4.2 Crear la función 'calcular_min' la cual recibirá por parámetro la lista de héroes y una key (string) 
# la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el mínimo de la lista. 
# Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga 
# el dato más bajo. 
# Ejemplo de llamada:
# 	calcular_min(lista, 'edad')

def calcular_min(superhero_list, superhero_key):
    #Takes superhero list and key as input
    #Compares superheroes by characteristic and finds min
    #Returns superhero's min name
    flag = True
    for superhero in superhero_list:
        if (flag == True):
            min_characteristic = superhero[superhero_key]
            superhero_min_name = superhero["nombre"]
            flag = False
        elif superhero[superhero_key] < min_characteristic:
            min_characteristic = superhero[superhero_key]
            superhero_min_name = superhero["nombre"]
    return superhero_min_name

# 4.3 Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:
# -La lista de héroes
# -El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
# -Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
# La función deberá retornar el héroe que cumpla con la condición pedida. Reutilizar las funciones 
# hechas en los puntos 4.1 y 4.2
# Ejemplo de llamada:
# calcular_max_min_dato(lista, "maximo", "edad")

def calcular_max_min_dato(superhero_list, max_min, superhero_key):
    #Takes superhero list, request and key as input
    #Calls functions according to request
    if max_min == "maximo":
        return calcular_max(superhero_list, superhero_key)
    else:
        return calcular_min(superhero_list, superhero_key)

# 4.4 Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres parámetros: 
# -La lista de héroes
# -El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
# -Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
# Con este se resuelve el Ej 3, Ej 4, Ej 6 y Ej 7 del desafío #00
# La función deberá obtener el héroe que cumpla dichas condiciones, imprimir su nombre y el valor calculado. 
# Reutilizar las funciones de los puntos:
# punto 1.2, punto: 2 y punto 4.3 
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Ejemplo de llamada: stark_calcular_imprimir_heroe (lista, "maximo", "edad")
# Ejemplo de salida: Mayor altura: Nombre: Howard the Duck | altura: 79.34                

def stark_calcular_imprimir_heroe(superhero_list, max_min, superhero_key):
    #Takes superhero list, request and key as input
    #Prints superhero's name and characteristic
    if not superhero_list:
        return -1
    else:
        if max_min == "maximo":
            string_in_print = "Mayor"
        else:
            string_in_print = "Menor"
        
        final_string = f"{string_in_print} {superhero_key}: "
        for superhero in superhero_list:
            if superhero["nombre"] == calcular_max_min_dato(superhero_list, max_min, superhero_key):
                superhero_index = superhero_list.index(superhero)
        chosen_superhero_dict = superhero_list[superhero_index]
        print(final_string)
        imprimir_dato(obtener_nombre_y_dato(chosen_superhero_dict, superhero_key))

# 5.1 Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de héroes y un string que 
# representara el dato/key de los héroes que se requiere sumar. Validar que cada héroe sea tipo diccionario y que 
# no sea un diccionario vacío antes de hacer la suma. La función deberá retorna la suma de todos los datos según 
# la key pasada por parámetro

def sumar_dato_heroe(superhero_list, superhero_key):
    #Gets superhero list and key as input
    #Sums the superheroe's characteristic
    #Returns an accumulator containing the sum
    accumulator = 0
    for superhero in superhero_list:
        if type(superhero) == dict and len(superhero) > 0:
            accumulator = accumulator + superhero[superhero_key]
    return accumulator

# 5.2 Crear la función  ‘dividir’ la cual recibirá como parámetro dos números (dividendo y divisor). 
# Se debe verificar si el divisor es 0,  en caso de serlo, retornar 0, caso contrario realizar la división 
# entre los parámetros y retornar el resultado

def dividir(dividend, divider):
    #Gets dividend and divider
    #Divides them
    #Returns the result
    if divider == 0:
        return 0
    else:
        divition_result = dividend / divider
        return divition_result

# 5.3 Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de héroes y 
# un string que representa el dato del héroe que se requiere calcular el promedio. La función debe retornar 
# el promedio del dato pasado por parámetro
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 5.1 y 5.2

def calcular_promedio(superhero_list, superhero_key):
    #Gets superhero list and key
    #Calculates average
    #Returns a function call, containing another function call and counter
    counter = 0
    for superheroe in superhero_list:
        counter = counter + 1
    return dividir(sumar_dato_heroe(superhero_list, superhero_key), counter)

# 5.4 Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá una lista de héroes y 
# utilizando la función del punto 5.3 calcula y mostrará la altura promedio. Validar que la lista de héroes 
# no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y 5.3
# Con este se resuelve el Ej 5 del desafío #00  ???????????????????? PARA QUE 5.1?

def stark_calcular_imprimir_promedio_altura(superhero_list):
    #Takes superhero list as input
    #Calls a function to print average
    if not superhero_list:
        return -1
    else:
        return imprimir_dato(calcular_promedio(superhero_list, "altura"))
    
# 6.1 Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla, el cual permite 
# utilizar toda la funcionalidad ya programada. Se deberá reutilizar la función antes creada encargada de imprimir 
# un string (1.2)              

def imprimir_menu():
    #Prints the menu
    menu =\
    '''
    Bienvenido al desafio STARK 02:
    0. Salir del sistema
    1. Obtener los nombres de todos los superheroes
    2. Obtener los nombres y altura de todos los superheroes
    3. Obtener superheroe mas alto
    4. Obtener superheroe mas bajo
    5. Obtener altura promedio de los superheroes
    6. Obtener los nombres del superheroe mas alto y el mas bajo
    7. Obtener los nombres de los superheroes mas y menos pesados
    '''
    imprimir_dato(menu)

# 6.2 Crear la función “validar_entero” la cual recibirá por parámetro un string de número el cual 
# deberá verificar que sea sea un string conformado únicamente por dígitos. Retornara True en caso de 
# serlo, False caso contrario

def validar_entero(number_string):
    #Validates number in string
    return number_string.isdigit()

# 6.3 Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú de opciones 
# y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. 
# En caso de ser correcto dicho número, lo retornara casteado a entero, caso contrario retorna -1. 
# Reutilizar las funciones del ejercicio 6.1 y 6.2

def stark_menu_principal():
    #Calls a function that prints the menu and offer user a choice
    imprimir_menu()
    user_choice_txt = input("Que opcion desea elegir? ")
    if (validar_entero(user_choice_txt) == True):
        user_choice_int = int(user_choice_txt)
        return user_choice_int
    else:
        return -1

# 7. Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y se 
# encargará de la ejecución principal de nuestro programa. 
# Utilizar if/elif o match según prefiera (match solo para los que cuentan con python 3.10+). 
# Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. 
# Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

def stark_marvel_app(superhero_list):
    #Compares user's choice to cases and executes the program according to it
    while True:
        user_choice_int = stark_menu_principal()
        match user_choice_int:
            case 0:         
                break
            case 1:
                stark_imprimir_nombres_heroes(superhero_list)
            case 2:
                stark_imprimir_nombres_alturas(superhero_list)
            case 3:
                stark_calcular_imprimir_heroe(superhero_list, "maximo", "altura")
            case 4:
                stark_calcular_imprimir_heroe(superhero_list, "minimo", "altura")
            case 5:
                stark_calcular_imprimir_promedio_altura(superhero_list)
            case 6:
                stark_calcular_imprimir_heroe(superhero_list, "maximo", "altura")
                stark_calcular_imprimir_heroe(superhero_list, "minimo", "altura")
            case 7:
                stark_calcular_imprimir_heroe(superhero_list, "maximo", "peso")
                stark_calcular_imprimir_heroe(superhero_list, "minimo", "peso")
            case _:
                print("Ha seleccionado una opcion incorrecta")
        clear_console()
#PROGRAMA:
print(stark_normalizar_datos(lista_personajes))
stark_marvel_app(lista_personajes)