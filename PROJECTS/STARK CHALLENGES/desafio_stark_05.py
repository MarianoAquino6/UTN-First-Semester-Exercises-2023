import re
import json
import os

def imprimir_dato(given_string):
    #Takes a string as input
    #Prints the string
    print(given_string)

# 1.1 Crear la función "imprimir_menu_desafio_5" que imprima el menú de
# opciones por pantalla (las opciones son las que se van a utilizar para
# acceder a la funcionalidad de los puntos A hasta el O y Z para salir).
# Reutilizar la función 'imprimir_dato' realizada en una práctica anterior.

def imprimir_menu_desafio_5():
    # Prints the menu
    menu_desafio_5 =\
    """
    Bienvenido al desafio STARK 05. A continuacion, el menu de opciones:
    A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
    B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe degénero F
    C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
    F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
    G. Recorrer la lista y determinar la altura promedio de los superhéroes degénero M
    H. Recorrer la lista y determinar la altura promedio de los superhéroes degénero F
    I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
    J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con "No Tiene").
    M. Listar todos los superhéroes agrupados por color de ojos.
    N. Listar todos los superhéroes agrupados por color de pelo.
    O. Listar todos los superhéroes agrupados por tipo de inteligencia
    Z. Salir
    _________________________________________________________________________________________________________________
    """
    imprimir_dato(menu_desafio_5)

# 1.2 Crear la funcion 'stark_menu_principal_desafio_5' la cual se encargará
# de imprimir el menú de opciones y le pedirá al usuario que ingrese la
# letra de una de las opciones elegidas, deberá validar la letra usando
# RegEx y en caso de ser correcta tendrá que retornarla, Caso contrario
# retornará -1. El usuario puede ingresar tanto letras minúsculas como
# mayúsculas y ambas se deben tomar como válidas
# Reutilizar la función 'imprimir_menu_Desafio_5'

def stark_menu_principal_desafio_5():
    """
    This function displays a menu and prompts the user to input an option, then checks if the input
    matches a specific pattern and returns it or -1 if it doesn't.
    :return: either the user's input string (if it matches the regular expression pattern) or -1 (if it
    does not match the pattern).
    """
    imprimir_menu_desafio_5()
    user_input_str = input("Ingrese su opcion").lower()
    result = re.match("^[a-o]|z$", user_input_str)
    if result:
        return user_input_str
    else:
        return -1
    
# 1.4 Crear la función 'leer_archivo' la cual recibirá por parámetro un string
# que indicará el nombre y extensión del archivo a leer (Ejemplo:
# archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
# retornará la lista de héroes como una lista de diccionarios.

json_adress = "data_stark_json_5.json"

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

# 1.5 Crear la función 'guardar_archivo' la cual recibirá por parámetro un
# string que indicará el nombre con el cual se guardará el archivo junto
# con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
# tendrá un string el cual será el contenido a guardar en dicho archivo.
# Debe abrirse el archivo en modo escritura+, ya que en caso de no
# existir, lo creara y en caso de existir, lo va a sobreescribir La función
# debera retornar True si no hubo errores, caso contrario False, además
# en caso de éxito, deberá imprimir un mensaje respetando el formato:
# .Se creó el archivo: nombre_archivo.csv
# En caso de retornar False, el mensaje deberá decir: ‘Error al crear el
# archivo: nombre_archivo’
# Donde nombre_archivo será el nombre que recibirá el archivo a ser
# creado, conjuntamente con su extensión.

def guardar_archivo(file_adress, to_save_string):
    """
    The function "guardar_archivo" saves a string to a file at a specified address and returns True if
    the file was successfully created, and False otherwise.
    
    :param file_adress: The file path and name where the file will be saved
    :param to_save_string: The string that will be written to the file
    :return: a boolean value, either True or False, depending on whether the file was successfully
    created or not.
    """
    with open(file_adress, "w") as new_file_save:
        new_file_save.write(f"{to_save_string}")
    if os.path.isfile(file_adress):
        imprimir_dato(f"Se creó el archivo {file_adress}")
        return True
    else:
        imprimir_dato(f"Error al crear el archivo {file_adress}")
        return False

# 1.6 Crear la función 'capitalizar_palabras' la cual recibirá por parámetro un
# string que puede contener una o muchas palabras. La función deberá
# retornar dicho string en el cual todas y cada una de las palabras que
# contenga, deberán estar capitalizadas (Primera letra en mayúscula).

def capitalizar_palabras(given_string):
    """
    The function capitalizes the first letter of each word in a given string.
    
    :param given_string: The input string that needs to be capitalized
    :return: a string where the first letter of each word in the input string is capitalized.
    """
    list_of_words = given_string.split(" ")
    capitalized_words_list = []
    for word in list_of_words: 
        capitalized_word = word.capitalize()
        capitalized_words_list.append(capitalized_word)
    capitalized_string = " ".join(capitalized_words_list)
    return capitalized_string

# 1.7 Crear la función 'obtener_nombre_capitalizado' la cual recibirá por
# parámetro un diccionario el cual representará a un héroe y devolverá
# un string el cual contenga su nombre formateado de la siguiente manera:
# Nombre: Venom
# Reutilizar 'capitalizar_palabras'

def obtener_nombre_capitalizado(hero_dict):
    """
    This function capitalizes the name of a hero in a dictionary and returns it with a string prefix.
    
    :param hero_dict: A dictionary containing information about a hero, including their name
    :return: a string that includes the capitalized name of a hero from a dictionary. The string starts
    with "Nombre: " and is followed by the capitalized name of the hero.
    """
    capitalized_hero_name = capitalizar_palabras(hero_dict["nombre"])
    return f"Nombre: {capitalized_hero_name}"

# 1.8 Crear la función 'obtener_nombre_y_dato' la cual recibirá por
# parámetro un diccionario el cual representará a un héroe y una key
# (string) la cual representará la key del héroe a imprimir. La función
# devolverá un string el cual contenga el nombre y dato (key) del héroe a imprimir.
# El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.
# El string resultante debe estar formateado al estilo: (suponiendo que la key es fuerza)
# Nombre: Venom | Fuerza: 500
# Reutilizar 'obtener_nombre_capitalizado'

def obtener_nombre_y_dato(hero_dict, hero_key):
    """
    This function takes a dictionary of hero information and a specific key, and returns a string with
    the hero's name and the value associated with the given key.
    
    :param hero_dict: a dictionary containing information about a hero, including their name and various
    attributes
    :param hero_key: The key of the specific data feature that we want to obtain from the hero_dict
    :return: a string that includes the capitalized name of a hero and a specific feature of that hero,
    based on a given key. The format of the string is "{hero_name} | {feature_key}:{feature_value}".
    """
    heros_name = obtener_nombre_capitalizado(hero_dict)
    for key in hero_dict.keys():
        if key != "nombre" and key == hero_key:
            capitalized_key = key.capitalize()
            string_feature = f"{capitalized_key}:{hero_dict[key]}" 
    return f"{heros_name} | {string_feature}"

# 2.1 Crear la función 'es_genero' la cual recibirá por parámetro un
# diccionario que representará un héroe y un string el cual será usado
# para evaluar si el héroe coincide con el género buscado (El string
# puede ser M, F o NB). retornará True en caso de que cumpla, False
# caso contrario.

def es_genero(hero_dict, gender_string):
    """
    The function checks if a given gender string matches the gender of a hero in a dictionary.
    
    :param hero_dict: a dictionary containing information about a hero, including their gender
    :param gender_string: A string representing the gender of a hero. It can be "M" for male, "F" for
    female, or "NB" for non-binary
    :return: a boolean value (True or False) depending on whether the "genero" key in the hero_dict
    dictionary matches the gender_string input and whether the gender_string input is a valid gender
    string (either "M", "F", or "NB").
    """
    result = re.match("^(M|F|NB)$", gender_string)
    if hero_dict["genero"] == gender_string and result:
        return True
    else:
        return False
    
# 2.2 Crear la función 'stark_guardar_heroe_genero' la cual recibira por
# parámetro la lista de héroes y un string el cual representará el género
# a evaluar (puede ser M o F). Deberá imprimir solamente los héroes o heroínas que coincidan con el 
# género pasado por parámetro y además, deberá guardar dichos nombres en un archivo con extensión 
# csv (cada nombre deberá ir separado por una coma)
# Reutilizar las funciones 'es_genero', 'obtener_nombre_capitalizado', 'imprimir_dato' y 'guardar_archivo'.
# En el caso de 'guardar_archivo', cuando se llame a esta función el
# nombre de archivo a guardar deberá respetar el formato:
# heroes_M.csv, heroes_F.csv o heroes_NB según corresponda.
# La función retornará True si pudo guardar el archivo, False caso
# contrario.

def stark_guardar_heroe_genero(hero_list, gender_string):
    """
    The function takes a list of heroes and a gender string, filters the heroes based on the gender,
    capitalizes their names, saves them to a CSV file based on the gender, and returns True if the file
    was successfully saved.
    
    :param hero_list: a list of dictionaries, where each dictionary represents a hero and contains
    information such as their name, gender, and powers
    :param gender_string: A string representing the gender of the heroes to be saved. It can be "M" for
    male, "F" for female, or "NB" for non-binary
    :return: a boolean value indicating whether the file was successfully saved or not. It returns True
    if the file was saved and False if it was not.
    """
    capitalized_heroes_list = []
    for hero in hero_list:
        if es_genero(hero, gender_string) == True:
            if hero["genero"] == gender_string and gender_string == "M":
                imprimir_dato(obtener_nombre_capitalizado(hero))
                capitalized_heroes_list.append(obtener_nombre_capitalizado(hero))
            if hero["genero"] == gender_string and gender_string == "F":
                imprimir_dato(obtener_nombre_capitalizado(hero))
                capitalized_heroes_list.append(obtener_nombre_capitalizado(hero))
            if hero["genero"] == gender_string and gender_string == "NB":
                imprimir_dato(obtener_nombre_capitalizado(hero))
                capitalized_heroes_list.append(obtener_nombre_capitalizado(hero))
    full_gender_hero_name_string = ",".join(capitalized_heroes_list)
    match gender_string:
        case "M":
            guardar_archivo("heroes_M.csv", full_gender_hero_name_string)
            print(capitalized_heroes_list)

            if os.path.isfile("heroes_M.csv"):
                return True
            else:
                return False
        case "F":
            guardar_archivo("heroes_F.csv", full_gender_hero_name_string)
            if os.path.isfile("heroes_F.csv"):
                return True
            else:
                return False
        case "NB":
            guardar_archivo("heroes_NB.csv", full_gender_hero_name_string)
            if os.path.isfile("heroes_NB.csv"):
                return True
            else:
                return False

# 3.1 Basandote en la función 'calcular_min', crear la función 'calcular_min_genero' la cual recibirá 
# como parámetro extra un string que representa el género de la heroína/héroe a buscar. modificar un
# poco la lógica para que dentro no se traiga por defecto al primer héroe de la lista sino que mediante 
# un flag, se traiga el primer héroe que COINCIDA con el género pasado por parámetro. A partir de allí, podrá
# empezar a comparar entre héroes o heroínas que coincidan con el género pasado por parámetro. 
# La función retornará el héroe o heroína que cumpla la condición de tener el mínimo (peso, altura u otro dato)

def calcular_min_genero(superhero_list, superhero_key, superhero_gender):
    """
    This function calculates the superhero with the minimum value of a given feature and a specified
    gender from a list of superheroes.
    
    :param superhero_list: a list of dictionaries containing information about superheroes
    :param superhero_key: The key or attribute of the superhero dictionary that we want to find the
    minimum value of
    :param superhero_gender: The gender of the superhero that we want to find the minimum value for the
    specified superhero_key
    :return: the name of the superhero with the minimum value for the specified feature (superhero_key)
    and gender (superhero_gender) from the given list of superheroes (superhero_list).
    """
    flag = True
    for superhero in superhero_list:
        if superhero["genero"] == superhero_gender:
            if flag == True:
                min_feature = float(superhero[superhero_key])
                superhero_min_name = superhero["nombre"]
                flag = False
            elif float(superhero[superhero_key]) < min_feature:
                min_feature = float(superhero[superhero_key])
                superhero_min_name = superhero["nombre"]
    return superhero_min_name

# 3.2 Basandote en la función 'calcular_max', crear la función
# 'calcular_max_genero' la cual recibirá como parámetro extra un string
# que representará el género de la heroína/héroe a buscar. modificar un
# poco la lógica para que dentro no se traiga por defecto al primer héroe
# de la lista sino que mediante un flag, se traiga el primer héroe que
# COINCIDA con el género pasado por parámetro. A partir de allí, podrá
# empezar a comparar entre héroes o heroínas que coincidan con el
# género pasado por parámetro. La función retornará el héroe o heroína
# que cumpla la condición de tener el máximo (peso, altura u otro dato)

def calcular_max_genero(superhero_list, superhero_key, superhero_gender):
    """
    The function calculates the superhero with the highest value for a given key and gender.
    
    :param superhero_list: a list of dictionaries containing information about superheroes
    :param superhero_key: The key or attribute of the superhero dictionary that we want to find the
    maximum value of
    :param superhero_gender: The gender of the superhero that we want to find the maximum value for
    :return: the name of the superhero with the highest value for a given feature (specified by
    superhero_key) and a given gender (specified by superhero_gender) from a list of superheroes
    (specified by superhero_list).
    """
    flag = True
    for superhero in superhero_list:
        if superhero["genero"] == superhero_gender:
            if flag == True:
                max_feature = float(superhero[superhero_key])
                superhero_max_name = superhero["nombre"]
                flag = False
            elif float(superhero[superhero_key]) > max_feature:
                max_feature = float(superhero[superhero_key])
                superhero_max_name = superhero["nombre"]
    return superhero_max_name

# 3.3 Basandote en la funcion 'calcular_max_min_dato', crear una funcion
# con la misma lógica la cual reciba un parámetro string que
# representará el género del héroe/heroína a buscar y renombrarla a
# 'calcular_max_min_dato_genero'. La estructura será similar a la ya
# antes creada, salvo que dentro de ella deberá llamar a
# 'calcular_max_genero' y 'calcular_min_genero', pasandoles el nuevo
# parámetro. Esta función retornará el héroe o heroína que cumpla con
# las condiciones pasados por parámetro. Por ejemplo, si se le pasa 'F' y
# 'minimo', retornará la heroína que tenga el mínimo (altura, peso u otro dato)

def calcular_max_min_dato_genero(superhero_list, max_min, superhero_key, hero_gender):
    """
    This function calculates either the maximum or minimum value of a specific key for a given gender in
    a list of superheroes.
    
    :param superhero_list: a list of dictionaries containing information about superheroes
    :param max_min: a string indicating whether to calculate the maximum or minimum value of the
    specified superhero key for the given gender
    :param superhero_key: This parameter refers to the specific attribute of a superhero that we want to
    calculate the maximum or minimum value for. For example, if we want to calculate the maximum or
    minimum height of superheroes, the superhero_key would be "height"
    :param hero_gender: The gender of the superhero, which is used as a filter to calculate either the
    maximum or minimum value of a specific attribute (superhero_key) in the superhero_list
    :return: the result of either the "calcular_max_genero" or "calcular_min_genero" function, depending
    on the value of the "max_min" parameter.
    """
    if max_min == "maximo":
        return calcular_max_genero(superhero_list, superhero_key, hero_gender)
    else:
        return calcular_min_genero(superhero_list, superhero_key, hero_gender)

# 3.4 Basandote en la función 'stark_calcular_imprimir_heroe' crear la función ‘stark_calcular_imprimir_guardar_heroe_genero’ 
# que además reciba un string el cual representará el género a evaluar. El formato de mensaje a imprimir deberá ser estilo:
# Mayor Altura: Nombre: Gamora | Altura: 183.65
# Además la función deberá guardar en un archivo csv el resultado obtenido.
# Reutilizar: 'calcular_max_min_dato_genero', 'obtener_nombre_y_dato',
# 'imprimir_dato' y 'guardar_archivo'.
# En el caso de 'guardar_archivo' el nombre del archivo debe respetar el formato:
# heroes_calculo_key_genero.csv
# Donde:
# -cálculo: representará el string máximo o mínimo
# -key: representará cual es la key la cual se tiene que hacer el cálculo
# -genero: representará el género a calcular.
# Ejemplo: para calcular el héroe más alto femenino, el archivo se deberá llamar:
# heroes_maximo_altura_F.csv
# Esta función retornará True si pudo guardar el archivo, False caso contrario

def stark_calcular_imprimir_guardar_heroe_genero(superhero_list, max_min, superhero_key, hero_gender):
    """
    This function calculates, prints, and saves the superhero with the maximum or minimum value for a
    given key and gender from a list of superheroes.
    
    :param superhero_list: A list of dictionaries containing information about superheroes
    :param max_min: A string indicating whether to calculate the maximum or minimum value for the given
    superhero_key
    :param superhero_key: It is a string representing the key of the superhero dictionary that we want
    to calculate the maximum or minimum value for. For example, it could be "altura" (height) or "peso"
    (weight)
    :param hero_gender: The gender of the superhero, which is used to filter the list of superheroes
    :return: either True or False depending on whether the file was successfully saved or not. If the
    file was saved, it returns True. If the file was not saved, it returns False.
    """
    if not superhero_list:
        return -1
    else:
        if max_min == "maximo":
            string_in_print = "mayor"
        else:
            string_in_print = "menor"
        
        final_string = f"{string_in_print} {superhero_key}: "
        for superhero in superhero_list:
            if superhero["nombre"] == calcular_max_min_dato_genero(superhero_list, max_min, superhero_key, hero_gender):
                superhero_index = superhero_list.index(superhero)
        chosen_superhero_dict = superhero_list[superhero_index]
        print(final_string)
        imprimir_dato(obtener_nombre_y_dato(chosen_superhero_dict, superhero_key))
        
        file_name = f"heroes_{string_in_print}_{superhero_key}_{hero_gender}.csv"
        guardar_archivo(file_name, obtener_nombre_y_dato(chosen_superhero_dict, superhero_key))
        if os.path.isfile(file_name):
                return True
        else:
                return False

# 4.1 Basandote en la función 'sumar_dato_heroe', crear la función llamada 'sumar_dato_heroe_genero' la cual deberá tener un 
# parámetro extra del tipo string que representará el género con el que se va a trabajar. 
# Esta función antes de realizar la suma en su variable sumadora, deberá validar lo siguiente:
# A. El tipo de dato del héroe debe ser diccionario.
# B. El héroe actual de la iteración no debe estar vacío (ser
# diccionario vacío)
# C. El género del héroe debe coincidir con el pasado por
# parámetro.
# Una vez que cumpla con las condiciones, podrá realizar la suma. La función deberá retornar la suma del valor de 
# la key de los héroes o heroínas que cumplan las condiciones o -1 en caso de que no se cumplan las validaciones

def sumar_dato_heroe_genero(superhero_list, superhero_key, hero_gender):
    """
    This function calculates the sum of a specific key's value for all superheroes in a list that match
    a given gender.
    
    :param superhero_list: a list of dictionaries, where each dictionary represents a superhero and
    contains information about them such as their name, gender, and various attributes (such as
    strength, intelligence, etc.)
    :param superhero_key: This parameter is a string that represents the key of the value we want to sum
    up for each superhero in the list. For example, if we want to sum up the "intelligence" values of
    each superhero, then superhero_key would be "intelligence"
    :param hero_gender: The gender of the superhero that we want to filter by. It could be "male",
    "female", "non-binary", or any other gender identity
    :return: the sum of the values of the specified key ("superhero_key") for all the superheroes in the
    input list ("superhero_list") that have the specified gender ("hero_gender"). If any of the
    superheroes in the list is not a dictionary or has no values for the specified key, the function
    returns -1.
    """
    accumulator = 0
    for superhero in superhero_list:
        if superhero["genero"] == hero_gender:
            if type(superhero) == dict and len(superhero) > 0:
                accumulator = accumulator + float(superhero[superhero_key])
            else:
                return -1
    return accumulator

# 4.2 Crear la función 'cantidad_heroes_genero' la cual recibirá por
# parámetro la lista de héroes y un string que representará el género a buscar. 
# La función deberá iterar y sumar la cantidad de héroes o heroínas que cumplan con la condición de género pasada por
# parámetro, retornará dicha suma.

def cantidad_heroes_genero(superhero_list, hero_gender):
    """
    The function counts the number of heroes in a list with a specific gender.
    
    :param superhero_list: a list of dictionaries, where each dictionary represents a superhero and
    contains information about their name, gender, powers, etc
    :param hero_gender: The gender of the heroes to be counted. It could be "male", "female",
    "non-binary", or any other gender category specified in the superhero_list
    :return: The function `cantidad_heroes_genero` returns the number of heroes in the `superhero_list`
    that match the specified `hero_gender`.
    """
    counter = 0
    for hero in superhero_list:
        if hero["genero"] == hero_gender:
            counter += 1
    return counter

# 4.3 Basandote en la función 'calcular_promedio', crear la función 'calcular_promedio_genero' 
# la cual tendrá como parámetro extra un string que representará el género a buscar. 
# la lógica es similar a la función anteriormente mencionada en el enunciado. Reutilizar las
# funciones: 'sumar_dato_heroe_genero', 'cantidad_heroes_genero' y 'dividir'.retornará el promedio obtenido, 
# según la key y género pasado por parámetro.

def calcular_promedio_genero(superhero_list, superhero_key, hero_gender):
    """
    This function calculates the average value of a specific key for all superheroes of a given gender
    in a list.
    
    :param superhero_list: a list of dictionaries containing information about superheroes
    :param superhero_key: The key or attribute of the superhero object that we want to use to calculate
    the average. For example, if we want to calculate the average height of superheroes, the
    superhero_key would be "height"
    :param hero_gender: The gender of the heroes for which we want to calculate the average. It could be
    "Male", "Female", "Non-Binary", or any other gender category present in the superhero_list
    :return: the average value of a specific superhero attribute (specified by the superhero_key
    parameter) for all superheroes of a given gender (specified by the hero_gender parameter) in a given
    superhero list (specified by the superhero_list parameter).
    """
    gender_average = sumar_dato_heroe_genero(superhero_list, superhero_key, hero_gender) / cantidad_heroes_genero(superhero_list, hero_gender)
    return gender_average

# 4.4 Basandote en la función ‘stark_calcular_imprimir_promedio_altura', desarrollar la función 
# 'stark_calcular_imprimir_guardar_ promedio_altura_genero' la cual tendrá como parámetro extra un string
# que representará el género de los héroes a buscar. La función antes de hacer nada, deberá validar que la lista no esté
# vacía. En caso de no estar vacía: calculará el promedio y lo imprimirá formateado al estilo:
# Altura promedio género F: 178.45
# En caso de estar vacía, imprimirá como mensaje:
# Error: Lista de héroes vacía.
# Luego de imprimir la función deberá guardar en un archivo los mismos datos. El nombre del archivo debe 
# tener el siguiente formato:
# heroes_promedio_altura_genero.csv
# Donde:
# -genero: será el género de los héroes a calcular, siendo M y F únicas opciones posibles.
# Ejemplos:
# heroes_promedio_altura_F.csv
# heroes_promedio_altura_M.csv
# Reutilizar las funciones: 'calcular_promedio_genero', 'imprimir_dato' y
# 'guardar_archivo'. Esta función retornará True si pudo la lista tiene algún elemento y pudo
# guardar el archivo, False en caso de que esté vacía o no haya podido guardar el archivo.

def stark_calcular_imprimir_guardar_promedio_altura_genero(superhero_list, hero_gender):
    """
    This function calculates and prints the average height of superheroes based on their gender, and
    saves the result to a CSV file.
    
    :param superhero_list: A list of dictionaries containing information about superheroes, including
    their height
    :param hero_gender: The gender of the heroes for which we want to calculate and save the average
    height. It can be "male", "female", or "genderless"
    :return: a boolean value, either True or False, depending on whether the file was successfully saved
    or not.
    """
    if not superhero_list:
        print("Error: Lista de heroes vacia")
        return False
    else:
        average_height = calcular_promedio_genero(superhero_list, "altura", hero_gender)
        print(f"Altura promedio genero {hero_gender}: {average_height}")
        file_adress = f"heroes_promedio_altura_{hero_gender}.csv"
        guardar_archivo(file_adress, average_height)
        if os.path.isfile(file_adress):
                return True
        else:
                return False

# 5.1 Crear la función 'calcular_cantidad_tipo' la cual recibirá por parámetro
# la lista de héroes y un string que representará el tipo de dato/key a buscar (color_ojos, color_pelo, etc)
# Antes de hacer nada, deberá validar que la lista no esté vacía. En caso
# de estarlo devolver un diccionario con la siguiente estructura:
# {
# "Error": “La lista se encuentra vacía”
# }
# La función deberá retornar un diccionario con los distintos valores del
# tipo de dato pasada por parámetro y la cantidad de cada uno (crear un diccionario clave valor).
# Por ejemplo, si el tipo de dato fuese color_ojos, devolverá un diccionario de la siguiente manera:
# {
# "Celeste": 4,
# "Verde": 8,
# "Marron": 6
# }
# Reutilizar la función 'capitalizar_palabras' para capitalizar los valores de las keys.

def calcular_cantidad_tipo(superhero_list, superhero_key):
    """
    This function calculates the amount of a specific feature in a list of superheroes and returns a
    dictionary with the count of each feature, with the option to capitalize the feature names.
    
    :param superhero_list: A list of dictionaries containing information about superheroes
    :param superhero_key: The superhero_key parameter is a string that represents the key or attribute
    of the superhero dictionary that we want to count the occurrences of
    :return: a dictionary with the count of occurrences of a specific feature (specified by the
    superhero_key parameter) in a list of superheroes (specified by the superhero_list parameter). If
    the list is empty, it returns an error dictionary. The keys of the returned dictionary are the
    capitalized feature names and the values are the count of occurrences.
    """
    if not superhero_list:
        empty_list_error_dict = {"Error": "La lista se encuentra vacia"}
        return empty_list_error_dict
    else:
        amount_of_features = {}
        for hero in superhero_list:
            if hero[superhero_key] == "":
                    if "No tiene" not in amount_of_features.keys():
                        amount_of_features["No tiene"] = 1
                    else:
                        amount_of_features["No tiene"] = amount_of_features["No tiene"] + 1
            else:
                if hero[superhero_key] not in amount_of_features.keys():
                    amount_of_features[hero[superhero_key]] = 1
                else:
                    for key, value in amount_of_features.items():
                        if key == hero[superhero_key]:
                            amount_of_features[key] = value + 1 
        amount_of_features_capitalized = {}
        for item in amount_of_features.keys():
            amount_of_features_capitalized[capitalizar_palabras(item)] = amount_of_features[item]
        return amount_of_features_capitalized

# 5.2 Crear la función 'guardar_cantidad_heroes_tipo' la cual recibirá como parámetro un diccionario que 
# representará las distintas variedades del tipo de dato (distintos colores de ojos, pelo, etc) como clave con sus
# respectivas cantidades como valor. Como segundo parámetro recibirá el dato (color_pelo, color_ojos, etc) 
# el cual tendrás que usarlo únicamente en el mensaje final formateado. Esta función deberá iterar
# cada key del diccionario y variabilizar dicha key con su valor para luego formatearlos en un mensaje el 
# cual deberá guardar en archivo. Por ejemplo:
# "Caracteristica: color_ojos Blue - Cantidad de heroes: 9"
# Reutilizar la función 'guardar_archivo'. El nombre del archivo final deberá respetar el formato:
# heroes_cantidad_tipoDato.csv
# Donde:
# tipoDato: representará el nombre de la key la cual se está evaluando la cantidad de héroes.
# Ejemplo:
# heroes_cantidad_color_pelo.csv
# heroes_cantidad_color_ojos.csv
# La función retornará True si salió todo bien, False caso contrario.

def guardar_cantidad_heroes_tipo(features_dict, superhero_key):
    """
    This function saves the quantity of heroes for each feature of a superhero in a CSV file.
    
    :param features_dict: A dictionary containing the features of superheroes and their corresponding
    quantities
    :param superhero_key: a string representing the type of superhero (e.g. "Marvel", "DC", "Anime")
    :return: a boolean value indicating whether the file was successfully saved or not. True is returned
    if the file exists, and False is returned if it does not exist.
    """
    features_aux_list = []
    for key in features_dict.keys():
        varieties = f"Caracteristica: {superhero_key} {key} - Cantidad de heroes {features_dict[key]}"
        features_aux_list.append(varieties)
    features_string = "\n".join(features_aux_list)
    file_name = f"heroes_cantidad_{superhero_key}.csv"
    guardar_archivo(file_name, features_string)
    if os.path.isfile(file_name):
        return True
    else:
        return False

# 5.3 Crear la función 'stark_calcular_cantidad_por_tipo' la cual recibirá por parámetro la lista de héroes 
# y un string que representará el tipo de dato/key a buscar (color_ojos, color_pelo, etc). Dentro deberás
# reutilizar 'calcular_cantidad_tipo' y 'guardar_cantidad_heroes_tipo' con la lógica que cada una de 
# esas funciones manejan. Esta función retornará True si pudo guardar el archivo, False caso contrario.

def stark_calcular_cantidad_por_tipo(superhero_list, superhero_key):
    """
    This function calculates the quantity of superheroes by a given type and saves the result.
    
    :param superhero_list: a list of dictionaries containing information about superheroes
    :param superhero_key: The superhero_key parameter is a string that represents the type of superhero
    that we want to calculate the quantity for. For example, if we want to calculate the quantity of all
    the superheroes that are of type "Avenger", then we would pass "Avenger" as the superhero_key
    parameter
    :return: The function `stark_calcular_cantidad_por_tipo` is returning the result of calling two
    other functions: `calcular_cantidad_tipo` and `guardar_cantidad_heroes_tipo`. The input parameters
    for `calcular_cantidad_tipo` are `superhero_list` and `superhero_key`, and the output of this
    function is passed as input to `guardar_cantidad_heroes
    """
    return guardar_cantidad_heroes_tipo(calcular_cantidad_tipo(superhero_list, superhero_key), superhero_key)

# 6.1 Crear la función 'obtener_lista_de_tipos' la cual recibirá por parámetro la lista de héroes y un string 
# que representará el tipo de dato/key a buscar (color_ojos, color_pelo, etc).
# Esta función deberá iterar la lista de héroes guardando en una lista las variedades del tipo de dato pasado 
# por parámetro (sus valores). En caso de encontrar una key sin valor (o string vacío), deberás
# hardcodear con el valor 'N/A' y luego agregarlo a la lista donde irás guardando todos los valores encontrados, 
# si el valor del héroe no tiene errores, guardarlo tal cual viene.
# Finalmente deberás eliminar los duplicados de esa lista y retornarla como un set.
# Reutilizar 'capitalizar_palabras' para guardar cada uno de los datos con la primera letra mayúscula.

def obtener_lista_de_tipos(superhero_list, superhero_key):
    """
    This function takes a list of superheroes and a key, and returns a set of the different types of
    values associated with that key in the list.
    
    :param superhero_list: a list of dictionaries, where each dictionary represents a superhero and
    their attributes
    :param superhero_key: The parameter superhero_key is a string that represents the key or attribute
    of the superhero dictionary that we want to extract and create a set of unique values from
    :return: a set of unique values obtained from the values of a specific key in a list of
    dictionaries. The values are capitalized using the "capitalizar_palabras" function, and if a value
    is empty, "N/A" is added to the set.
    """
    aux_list_features = []
    for hero in superhero_list:
        if len(hero[superhero_key]) == 0:
            aux_list_features.append("N/A")
        else:
            aux_list_features.append(capitalizar_palabras(hero[superhero_key]))
    features_set = set(aux_list_features)
    return features_set

# 6.2 Crear la función 'normalizar_dato' la cual recibirá por parámetro un
# dato de héroe (el valor de una de sus keys, por ejemplo si la key fuese
# color_ojos y su valor fuese Verde, recibira este ultimo) y tambien una
# variable como string la cual representará el valor por defecto a colocar
# en caso de que el valor está vacío. Deberá validar que el dato no esté
# vacío, en caso de estarlo lo reemplazará con el valor default pasado
# por parámetro y lo retornará, caso contrario lo retornará sin
# modificaciones.

def normalizar_dato(superhero_feature, default_string):
    """
    The function normalizes a superhero feature by replacing an empty string with a default string.
    
    :param superhero_feature: This is a variable that represents a feature or attribute of a superhero,
    such as their name, power, or origin story
    :param default_string: The default value to be used if the superhero_feature is empty
    :return: If the length of the `superhero_feature` is 0, then the function will return
    `default_string` after assigning it to `superhero_feature`. Otherwise, it will return
    `superhero_feature`.
    """
    if len(superhero_feature) == 0:
        superhero_feature = default_string
        return superhero_feature
    else:
        return superhero_feature

# 6.3 Crear la función 'normalizar_heroe' la cual recibirá dos parámetros: El primero será un diccionario 
# que representará un solo héroe, el segundo parámetro será el nombre de la key de dicho diccionario la cual debe ser 
# normalizada. 
# La función deberá capitalizar las palabras que tenga dicha key como valor, luego deberá normalizar 
# el dato (ya que si viene vacío, habrá que setearlo con N/A).
# Finalmente deberá capitalizar todas las palabras del nombre del héroe y deberá retornar al Hero con cada 
# palabra de su nombre capitalizados, cada palabra del valor de la key capitalizadas y normalizadas 
# (con N/A en caso de que estuviesen vacías por defecto). Reutilizar: 'capitalizar_palabras' y 'normalizar_dato'

def normalizar_heroe(superhero_dict, superhero_key): 
    """
    The function normalizes and capitalizes the values of a specific key in a dictionary of superhero
    attributes.
    
    :param superhero_dict: a dictionary containing information about a superhero, including their name
    and other features
    :param superhero_key: The key of the value in the superhero_dict dictionary that needs to be
    normalized
    :return: the updated superhero_dict after normalizing the values of the specified superhero_key and
    capitalizing the words in the "nombre" key.
    """
    list_of_words = superhero_dict[superhero_key].split(" ")
    list_of_capitalized_words = []
    for word in list_of_words:
        if word == "N/A":
            list_of_capitalized_words.append(word)
        else:
            list_of_capitalized_words.append(capitalizar_palabras(word))
    
    capitalized_words_feature = " ".join(list_of_capitalized_words)
    normalized_features = normalizar_dato(capitalized_words_feature, "N/A")
    superhero_dict[superhero_key] = normalized_features
    
    value_words_names_list = superhero_dict["nombre"].split(" ")
    capitalized_words_name_aux_list =[]
    for word in value_words_names_list:
        capitalized_words_name_aux_list.append(capitalizar_palabras(word))
    capitalized_words_names = " ".join(capitalized_words_name_aux_list)
    superhero_dict["nombre"] = capitalized_words_names
    return superhero_dict

# 6.4 Crear la funcion 'obtener_heroes_por_tipo' el cual recibira por parámetro:
# A. La lista de héroes
# B. Un set de tipos/variedades (colores de ojos, de pelo, etc)
# C. El tipo de dato a evaluar (la key en cuestion, color_ojos, color_pelo, etc)
# PRESTAR ATENCIÓN:
# A. Deberá iterar el set de tipos/variedades y por cada tipo tendrá que evaluar si ese tipo existe como key en un 
# diccionario el cual deberás armar. (contendrá cada variedad como key y una lista de nombres de héroes
# como valor de cada una de ellas).
# B. En caso de no existir dicha key en el diccionario, agregarla con una lista vacía como valor.
# C. Dentro de la iteración de variedades, iterar la lista de héroes (for anidado) 'normalizando' el posible valor 
# que tenga la key evaluada, ya que podría venir vacía (qué función usarias aca? guiño guiño)
# D. Una vez normalizado el dato, evaluar si dicho dato coincide con el tipo pasado por parámetro.
# E. En caso de que coincida, agregarlo a la lista (inicialmente vacía) de la variedad iterada en el primer bucle. Esta 
# función retornará un diccionario con cada variedad como key y una lista de nombres como valor.
# Por ejemplo:
# {
# "Celestes": ["Capitan America", "Tony Stark"],
# "Verdes": ["Hulk", "Viuda Negra"]
# ....
# }

def obtener_heroes_por_tipo(superheros_list, feature_set, superhero_key):
    """
    The function obtains a dictionary of heroes grouped by their type from a list of superheroes using a
    given feature set and superhero key.
    
    :param superheros_list: a list of dictionaries, where each dictionary represents a superhero and
    contains information about them such as their name, powers, and type
    :param feature_set: A set of features that we want to filter the superheroes by. For example, if we
    want to filter by superhero type, the feature set could be {"hero", "villain", "anti-hero"}
    :param superhero_key: This parameter is not defined in the given function. It is likely defined in
    another part of the code or documentation
    :return: a dictionary where the keys are the items in the feature_set list and the values are lists
    of superhero names that have the corresponding feature in their superhero_key attribute.
    """
    features_and_names_dict = {}
    for item in feature_set:
        if item not in features_and_names_dict.keys():
            features_and_names_dict[item] = []
        for hero in superheros_list:
            normalized_hero = normalizar_heroe(hero, superhero_key)
            if normalized_hero[superhero_key] == item:
                features_and_names_dict[item].append(hero["nombre"])
                if normalized_hero[superhero_key] == "N/A":
                    pass
    return features_and_names_dict

# 6.5 Crear la funcion 'guardar_heroes_por_tipo' la cual recibira por parámetro un diccionario que representará 
# los distintos tipos como clave y una lista de nombres como valor (Lo retorna la función anterior)
# y además como segundo parámetro tendrá un string el cual representará el tipo de dato a evaluar (color_pelo, color_ojos, etc).
# Deberá recorrer cada key y cada valor (lista) que esta contenga para finalmente crear un string el cual será 
# un mensaje que deberás imprimir formateado.
# Por ejemplo:
# "color_ojos Green: Black Widow | Hulk"
# Reutilizar la función 'guardar_archivo'. El archivo final deberá respetar el formato:
# heroes_segun_TipoDato.csv
# Donde:
# ● TipoDato: es la key la cual indicará qué cosas se deben guardar en el archivo.
# Ejemplo:
# heroes_segun_color_pelo.csv (Agrupados por color de pelo)
# heroes_segun_color_ojos.csv (Agrupados por color de ojos)
# Esta función retorna True si salió todo bien, False caso contrario.        

def guardar_heroes_por_tipo(types_and_names_dict, superhero_key):
    """
    This function takes a dictionary of superhero types and names, and saves them to a CSV file with a
    filename based on a given superhero key.
    
    :param types_and_names_dict: A dictionary where the keys are superhero types (e.g. "Avengers",
    "X-Men") and the values are lists of superhero names belonging to that type
    :param superhero_key: The superhero_key parameter is a string that represents the type of superhero
    (e.g. "Avengers", "X-Men", "Justice League") that will be used to group and save the heroes in the
    types_and_names_dict dictionary
    :return: a boolean value. It returns True if the file was successfully saved and False if it was
    not.
    """
    key_types_name_list = [] 
    for key, value in types_and_names_dict.items():
        concatenated_heroes = " | ".join(value)
        final_message_to_save =f"{superhero_key} {key}: {concatenated_heroes}"
        key_types_name_list.append(final_message_to_save)
    key_types_name_string = ", ".join(key_types_name_list)
    file_name = f"heroes_segun_{superhero_key}.csv"
    guardar_archivo(file_name, key_types_name_string)
    if os.path.isfile(file_name):
        return True
    else:
        return False

# 6.6 Crear la función 'stark_listar_heroes_por_dato' la cual recibirá por parámetro la lista de héroes y un string 
# que representará el tipo de dato a evaluar (color_pelo, color_ojos, etc). Dentro deberás reutilizar las funciones:
# A. 'obtener_lista_de_tipos'
# B. 'obtener_heroes_por_tipo'
# C. 'guardar_heroes_por_tipo'
# Pasando por parámetro lo que corresponda según la lógica de las funciones usadas.
# Esta función retornará True si pudo guardar el archivo, False caso contrario.

def stark_listar_heroes_por_dato(superhero_list, superhero_key):
    """
    This function lists superheroes based on a specific data key.
    
    :param superhero_list: a list of dictionaries containing information about superheroes
    :param superhero_key: The superhero_key parameter is a string that represents the specific attribute
    or property of a superhero that we want to use as a filter or sorting criteria. For example, if we
    want to list all superheroes by their "name" attribute, we would pass "name" as the superhero_key
    parameter
    :return: The function `stark_listar_heroes_por_dato` is returning the result of calling two other
    functions: `obtener_lista_de_tipos` and `obtener_heroes_por_tipo`, and then passing the result of
    those calls to `guardar_heroes_por_tipo`. The final result is a list of superheroes grouped by a
    specific key.
    """
    return guardar_heroes_por_tipo(obtener_heroes_por_tipo(superhero_list, obtener_lista_de_tipos(superhero_list, superhero_key), superhero_key), superhero_key)

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

# 1.3 Crear la función 'stark_marvel_app_5' la cual recibirá por parámetro la
# lista de héroes y se encargará de la ejecución principal de nuestro
# programa. (usar if/elif o match según prefiera) Reutilizar las funciones
# con prefijo 'stark_' donde crea correspondiente.

def stark_marvel_app_5(hero_list):
    """
    This is a function that takes a list of heroes and presents a menu of options to the user, with each
    option corresponding to a letter of the alphabet.
    
    :param hero_list: The hero_list parameter is a list of heroes that will be used in the function.
    """
    while True:
        user_choice = stark_menu_principal_desafio_5()
        match user_choice:
            case "a":
                stark_guardar_heroe_genero(hero_list, "M")
            case "b":
                stark_guardar_heroe_genero(hero_list, "F")
            case "c":
                stark_calcular_imprimir_guardar_heroe_genero(hero_list, "maximo", "altura", "M")
            case "d":
                stark_calcular_imprimir_guardar_heroe_genero(hero_list, "maximo", "altura", "F")
            case "e":
                stark_calcular_imprimir_guardar_heroe_genero(hero_list, "minimo", "altura", "M")
            case "f":
                stark_calcular_imprimir_guardar_heroe_genero(hero_list, "minimo", "altura", "F")
            case "g":
                stark_calcular_imprimir_guardar_promedio_altura_genero(hero_list, "M")
            case "h":
                stark_calcular_imprimir_guardar_promedio_altura_genero(hero_list, "F")
            case "i":
                name_list = []
                with open(r"C:\Users\x\Documents\Programming\Programacion y Laboratorio 1\Ejercicios\PRACTICOS\heroes_mayor_altura_F.csv", "r") as i_file:
                    for linea in i_file:
                        result = re.findall("Nombre: ([a-zA-Z]+)", linea)
                        for name in result:
                            name_list.append(name)
                with open(r"C:\Users\x\Documents\Programming\Programacion y Laboratorio 1\Ejercicios\PRACTICOS\heroes_mayor_altura_M.csv", "r") as i_file:
                    for linea in i_file:
                        result = re.findall("Nombre: ([a-zA-Z]+)", linea)
                        for name in result:
                            name_list.append(name)
                with open(r"C:\Users\x\Documents\Programming\Programacion y Laboratorio 1\Ejercicios\PRACTICOS\heroes_menor_altura_F.csv", "r") as i_file:
                    for linea in i_file:
                        result = re.findall("Nombre: ([a-zA-Z]+)", linea)
                        for name in result:
                            name_list.append(name)
                with open(r"C:\Users\x\Documents\Programming\Programacion y Laboratorio 1\Ejercicios\PRACTICOS\heroes_menor_altura_M.csv", "r") as i_file:
                    for linea in i_file:
                        result = re.findall("Nombre: ([a-zA-Z]+)", linea)
                        for name in result:
                            name_list.append(name)
                names_string = "\n".join(name_list)
                print(names_string)
            case "j":
                stark_calcular_cantidad_por_tipo(hero_list, "color_ojos")
            case "k":
                stark_calcular_cantidad_por_tipo(hero_list, "color_pelo")
            case "l":
                stark_calcular_cantidad_por_tipo(hero_list, "inteligencia")
            case "m":
                stark_listar_heroes_por_dato(hero_list, "color_ojos")
            case "n":
                stark_listar_heroes_por_dato(hero_list, "color_pelo")
            case "o":
                stark_listar_heroes_por_dato(hero_list, "inteligencia")
            case "z":
                break
            case _:
                print("Ha ingresado una letra incorrecta")
        clear_console()

stark_marvel_app_5(leer_archivo(json_adress))