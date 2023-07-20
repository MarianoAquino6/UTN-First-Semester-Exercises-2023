import re
import json
import os

json_adress = "data_stark_json_5.json"

def imprimir_dato(given_string):
    #Takes a string as input
    #Prints the string
    print(given_string)

def imprimir_menu_desafio_6():
    # Prints the menu
    menu_desafio_6 =\
    """
    Bienvenido al desafio STARK 06. A continuacion, el menu de opciones:
    A. Obtener lista de superheroes ordenada por altura en orden DESCENDENTE
    B. Obtener lista de superheroes ordenada por peso en orden ASCENDENTE
    C. Obtener lista de superheroes ordenada alfabeticamente por nombre
    D. Obtener lista de superheroes ordenada por largo del nombre en forma DESCENDENTE
    E. Obtener lista de superheroes ordenada segun el key ingresado en la forma ingresada
    _________________________________________________________________________________________________________________
    """
    imprimir_dato(menu_desafio_6)

def stark_menu_principal_desafio_6():
    """
    This function displays a menu and prompts the user to input an option, then checks if the input
    matches a specific pattern and returns it or -1 if it doesn't.
    :return: either the user's input string (if it matches the regular expression pattern) or -1 (if it
    does not match the pattern).
    """
    imprimir_menu_desafio_6()
    user_input_str = input("Ingrese su opcion").lower()
    result = re.match("^[a-o]|z$", user_input_str)
    if result:
        return user_input_str
    else:
        return -1

def leer_archivo(file_adress):
    """
    The function reads a JSON file and returns a list of superheroes.
    
    :param file_adress: The file path or address of the JSON file that contains the data to be read
    :return: a list of superheroes that is extracted from a JSON file located at the file address
    specified in the function argument.
    """
    with open(file_adress,"r") as lovely_file:
        data = json.load(lovely_file)
        superhero_list = data["heroes"]
    return superhero_list

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

# 1. Crear una función llamada ‘ordenar_por_altura’ que reciba como parámetro la lista de héroes y devuelva la lista 
# ordenada por la altura de cada personaje de menor a mayor.

def ordenar_por_altura(superhero_list):
    """
    The function sorts a list of superheroes by their height in ascending order using bubble sort
    algorithm.
    
    :param superhero_list: a list of dictionaries, where each dictionary represents a superhero and
    contains information about their name, height, weight, and other attributes
    :return: The function `ordenar_por_altura` is returning a sorted list of superheroes based on their
    height.
    """
    flag_swap = True
    while(flag_swap):
        flag_swap = False

        for indice_A in range(len(superhero_list) - 1):
            if superhero_list[indice_A]["altura"] > superhero_list[indice_A+1]["altura"]:
                superhero_list[indice_A],superhero_list[indice_A+1] = superhero_list[indice_A+1],superhero_list[indice_A]
                flag_swap = True
    return superhero_list

# 2. Crear una función llamada ‘ordenar_por_peso’ que reciba como parámetro la lista de héroes y devuelva la lista 
# ordenada por el peso de cada personaje mayor a mayor.

def ordenar_por_peso(superhero_list):
    """
    The function sorts a list of superheroes by their weight in descending order.
    
    :param superhero_list: a list of dictionaries, where each dictionary represents a superhero and
    contains information about their name, weight, and other attributes
    :return: The function `ordenar_por_peso` is returning a sorted list of superheroes based on their
    weight in descending order.
    """
    flag_swap = True
    while(flag_swap):
        flag_swap = False

        for indice_A in range(len(superhero_list) - 1):
            if superhero_list[indice_A]["peso"] < superhero_list[indice_A+1]["peso"]:
                superhero_list[indice_A],superhero_list[indice_A+1] = superhero_list[indice_A+1],superhero_list[indice_A]
                flag_swap = True
    return superhero_list

# 3. Crear una función llamada ‘ordenar_por_nombre’ que reciba como parámetro
# la lista de héroes y la devuelva la lista de héroes ordenada por nombres de
# forma alfabética ascendente (de la A a la Z)

def ordenar_por_nombre(superhero_list):
    """
    The function sorts a list of superheroes by their name in alphabetical order.
    
    :param superhero_list: a list of dictionaries, where each dictionary represents a superhero and
    contains the keys "nombre" (name), "poder" (power), and "edad" (age)
    :return: The function `ordenar_por_nombre` returns a sorted list of dictionaries containing
    information about superheroes, sorted by their name in alphabetical order.
    """
    flag_swap = True
    while(flag_swap):
        flag_swap = False

        for indice_A in range(len(superhero_list) - 1):
            if superhero_list[indice_A]["nombre"] > superhero_list[indice_A+1]["nombre"]:
                superhero_list[indice_A],superhero_list[indice_A+1] = superhero_list[indice_A+1],superhero_list[indice_A]
                flag_swap = True
    return superhero_list

# 4. Crear una función llamada ‘ordenar_por_largo_nombre’ que reciba como
# parámetro la lista de héroes y la devuelva la lista de héroes ordenada por el
# largo del nombre de forma descendente

def ordenar_por_largo_nombre(superhero_list):
    """
    This function sorts a list of superheroes by the length of their names in descending order.
    
    :param superhero_list: a list of dictionaries, where each dictionary represents a superhero and
    contains a "nombre" key with the superhero's name as its value
    :return: The function `ordenar_por_largo_nombre` returns a sorted list of superheroes based on the
    length of their names, in descending order.
    """
    flag_swap = True
    while(flag_swap):
        flag_swap = False

        for indice_A in range(len(superhero_list) - 1):
            if len(superhero_list[indice_A]["nombre"]) < len(superhero_list[indice_A+1]["nombre"]):
                superhero_list[indice_A],superhero_list[indice_A+1] = superhero_list[indice_A+1],superhero_list[indice_A]
                flag_swap = True
    return superhero_list

# 5. Crear una función llamada ‘ordenar_por_key’ la misma recibirá tres parámetros:
# a. La lista de héroes
# b. Un string que represente el nombre de una key
# c. Un booleano que represente el sentido de ordenamiento (por defecto
# debe tomar el valor True)
# La función deberá ordenar la lista de personajes según la key especificada. El
# sentido de ordenamiento lo determina el tercer parámetro, en caso de ser
# True el orden va a ser ascendente (de menor a mayor) y en el caso de ser
# False el sentido es descendente (mayor a menor)

def ordenar_por_key(superhero_list, superhero_key, bloolean_value = True):
    """
    The function sorts a list of dictionaries based on a specified key in ascending or descending order.
    
    :param superhero_list: a list of dictionaries, where each dictionary represents a superhero and
    contains information about them such as name, powers, etc
    :param superhero_key: The key by which the superhero_list will be sorted. It is a string
    representing the name of the key in the dictionary of each superhero in the list
    :param bloolean_value: The parameter "bloolean_value" is a boolean value (True or False) that
    determines whether the sorting should be done in ascending or descending order. If it is True, the
    sorting will be done in ascending order, and if it is False, the sorting will be done in descending
    order, defaults to True (optional)
    :return: The function `ordenar_por_key` returns a sorted list of dictionaries based on the value of
    a specified key. The sorting order can be ascending or descending based on the value of the
    `bloolean_value` parameter.
    """
    flag_swap = True
    while(flag_swap):
        flag_swap = False

        for indice_A in range(len(superhero_list) - 1):
            if bloolean_value == True:
                if superhero_list[indice_A][superhero_key] > superhero_list[indice_A+1][superhero_key]:
                    superhero_list[indice_A],superhero_list[indice_A+1] = superhero_list[indice_A+1],superhero_list[indice_A]
                    flag_swap = True
            else:
                if superhero_list[indice_A][superhero_key] < superhero_list[indice_A+1][superhero_key]:
                    superhero_list[indice_A],superhero_list[indice_A+1] = superhero_list[indice_A+1],superhero_list[indice_A]
                    flag_swap = True
    return superhero_list

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

def stark_marvel_app_6(hero_list):
    """
    This is a function that takes a list of heroes and presents a menu of options to the user, with each
    option corresponding to a letter of the alphabet.
    
    :param hero_list: The hero_list parameter is a list of heroes that will be used in the function.
    """
    print(stark_normalizar_datos(hero_list))
    while True:
        user_choice = stark_menu_principal_desafio_6()
        match user_choice:
            case "a":
                print(ordenar_por_altura(hero_list))
            case "b":
                print(ordenar_por_peso(hero_list))
            case "c":
                print(ordenar_por_nombre(hero_list))
            case "d":
                print(ordenar_por_largo_nombre(hero_list))
            case "e":
                user_choice_key = input("Ingrese la key por la cual quiere ordenar: 'altura', 'peso' o 'fuerza'")
                if user_choice_key != "altura" and user_choice_key != "peso" and user_choice_key != "fuerza":
                    print("Ha ingresado mal la opcion de key.")
                    break
                
                user_choice_order = input("Ingrese el orden: 'ascendente' o 'descendente'")
                if user_choice_order == "ascendente":
                    user_choice_order = True
                elif user_choice_order == "descendente":
                    user_choice_order = True
                else:
                    print("Ha ingresado mal la opcion de orden.")
                    break
                print(ordenar_por_key(leer_archivo(json_adress), user_choice_key, user_choice_order))
            case _:
                print("Ha ingresado una letra incorrecta")
        clear_console()

stark_marvel_app_6(leer_archivo(json_adress))