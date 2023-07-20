import re
import json
import os

json_adress = "data_stark_json_5.json"

#---------------------------Importo funciones usadas en previos desafios---------------------------------------
def imprimir_dato(given_string):
    #Takes a string as input
    #Prints the string
    print(given_string)

def imprimir_menu():
    # Prints the menu
    menu_desafio_6 =\
    """
    Bienvenido al SIMULACRO CLASE 10. A continuacion, el menu de opciones:
    1. Listar cierto numero de superheroes
    2. Ordenar superheroes por altura
    3. Ordenar superheroes por fuerza
    4. Clasificar superheroes segun promedio de una determinada caracteristica
    5. Clasificar superheroes segun inteligencia
    6. Crear CSV a partir de la opcion elegida anteriormente (Solo valido tras elegir primero opcion 1, 2, 3 o 4)
    _________________________________________________________________________________________________________________
    """
    imprimir_dato(menu_desafio_6)

def menu_principal():
    """
    The function "menu_principal" displays a menu and prompts the user to input an option, returning the
    integer value of the option or -1 if the input is invalid.
    :return: The function `menu_principal()` returns an integer value representing the user's selected
    option from a menu. If the user's input is a valid integer between 0 and 6, the function returns
    that integer. Otherwise, it returns -1.
    """
    imprimir_menu()
    user_input_str = input("Ingrese su opcion: ")
    result = re.match("^[0-6]$", user_input_str)
    if result:
        return int(user_input_str)
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

def normalizar_datos(superhero_list):
    """
    This function normalizes the data of a list of superheroes by converting their height, weight, and
    strength values to integers or floats.
    
    :param superhero_list: a list of dictionaries containing information about superheroes, including
    their height, weight, and strength
    :return: a message indicating whether the data in the input list of superheroes has been
    successfully normalized or not. The message will be "Datos normalizados" if the normalization is
    successful, or "Error: Lista de héroes vacía" if the input list is empty.
    """
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

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

#----------------------------Funciones correspondientes a los enunciados--------------------------------------------

# 1. Listar los primeros N héroes. El valor de N será ingresado por el usuario
# (Validar que no supere max. de lista)

def listar_n_heroes(superhero_list, amount_of_heroes):
    """
    This function takes a list of superheroes and a number as input, and returns a new list with the
    specified number of superheroes from the original list.
    
    :param superhero_list: a list of superheroes
    :param amount_of_heroes: The number of heroes that the user wants to select from the superhero_list
    :return: a list of superheroes from the input `superhero_list` based on the input
    `amount_of_heroes`. If `amount_of_heroes` is less than or equal to the length of `superhero_list`,
    then the function returns a sublist of `superhero_list` containing the first `amount_of_heroes`
    elements. Otherwise, the function prints an error message and does not
    """
    if amount_of_heroes <= len(superhero_list):
        selected_superhero_list = superhero_list[:amount_of_heroes]
        return selected_superhero_list
    else:
        print("Ingresaste un numero mayor al numero de superheroes disponibles. Por favor ingresa un numero mas chico")

# 2. Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de
# manera ascendente (‘asc’) o descendente (‘desc’)

def sort_superheroes_by_height(superhero_list, order):
    """
    This function sorts a list of superheroes by their height in ascending or descending order.
    
    :param superhero_list: a list of dictionaries, where each dictionary represents a superhero and
    contains information about their name, height, and other attributes
    :param order: The order parameter specifies whether the superhero_list should be sorted in ascending
    or descending order based on their height. If order is "asc", the list will be sorted in ascending
    order, and if order is "desc", the list will be sorted in descending order
    :return: The function `sort_superheroes_by_height` is returning a sorted list of superheroes based
    on their height, either in ascending or descending order depending on the value of the `order`
    parameter.
    """
    flag_swap = True
    while(flag_swap):
        flag_swap = False

        for indice_A in range(len(superhero_list) - 1):
            if order == "asc":
                if superhero_list[indice_A]["altura"] > superhero_list[indice_A+1]["altura"]:
                    superhero_list[indice_A],superhero_list[indice_A+1] = superhero_list[indice_A+1],superhero_list[indice_A]
                    flag_swap = True
            else:
                if superhero_list[indice_A]["altura"] < superhero_list[indice_A+1]["altura"]:
                    superhero_list[indice_A],superhero_list[indice_A+1] = superhero_list[indice_A+1],superhero_list[indice_A]
                    flag_swap = True
    return superhero_list

# 3. Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar
# de manera ascendente (‘asc’) o descendente (‘desc’)

def sort_superheroes_by_strength(superhero_list, order):
    """
    This function sorts a list of superheroes by their strength in ascending or descending order.
    
    :param superhero_list: a list of dictionaries, where each dictionary represents a superhero and
    contains information about their strength (among other attributes)
    :param order: The order parameter specifies whether the superhero_list should be sorted in ascending
    or descending order based on their strength. If order is "asc", the list will be sorted in ascending
    order, and if order is "desc", the list will be sorted in descending order
    :return: The function `sort_superheroes_by_strength` is returning a sorted list of superheroes based
    on their strength, either in ascending or descending order depending on the `order` parameter.
    """
    flag_swap = True
    while(flag_swap):
        flag_swap = False

        for indice_A in range(len(superhero_list) - 1):
            if order == "asc":
                if superhero_list[indice_A]["fuerza"] > superhero_list[indice_A+1]["fuerza"]:
                    superhero_list[indice_A],superhero_list[indice_A+1] = superhero_list[indice_A+1],superhero_list[indice_A]
                    flag_swap = True
            else:
                if superhero_list[indice_A]["fuerza"] < superhero_list[indice_A+1]["fuerza"]:
                    superhero_list[indice_A],superhero_list[indice_A+1] = superhero_list[indice_A+1],superhero_list[indice_A]
                    flag_swap = True
    return superhero_list

# 4. Calcular promedio de cualquier key numérica, filtrar los que cumplan con la
# condición de superar o no el promedio (preguntar al usuario la condición:
# ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con ser
# mayores o menores según corresponda.

def calcular_promedio_de_key(superhero_list, superhero_key, below_above):
    """
    This function calculates the average value of a specified key in a list of dictionaries and returns
    a list of dictionaries that have values either above or below the average based on a given
    parameter.
    
    :param superhero_list: a list of dictionaries, where each dictionary represents a superhero and
    contains information about them such as name, powers, and stats
    :param superhero_key: The key in the dictionary of each superhero that we will use to calculate the
    average and determine which superheroes are above or below the average
    :param below_above: A string parameter that determines whether to return the list of superheroes
    with values below or above the calculated average. If the value is "menor", the function will return
    the list of superheroes with values below the average. If the value is anything else, the function
    will return the list of superheroes with values
    :return: The function `calcular_promedio_de_key` returns either the list of superheroes whose value
    for the specified key is below the average or the list of superheroes whose value for the specified
    key is above the average, depending on the value of the `below_above` parameter.
    """
    accumulator = 0
    for superhero in superhero_list:
        accumulator = accumulator + superhero[superhero_key]
    average_calculation = accumulator / len(superhero_list)
    
    below_average_list = []
    above_average_list = []

    for superhero in superhero_list:
        if superhero[superhero_key] > average_calculation:
            above_average_list.append(superhero)
        else:
            below_average_list.append(superhero)
    
    if below_above == "menor":
        return below_average_list
    else:
        return above_average_list

# 5. Buscar héroes por inteligencia [good, average, high] y listar en consola los
# que cumplan dicha búsqueda. (Usando RegEx)

def categorize_heroes_by_intelligence(superhero_list, good_average_high):
    """
    This function categorizes superheroes based on their intelligence level and returns a list of
    superheroes with good, average, or high intelligence.
    
    :param superhero_list: a list of dictionaries, where each dictionary represents a superhero and
    contains information such as their name and intelligence level
    :param good_average_high: This parameter is a string that specifies the level of intelligence that
    the user wants to categorize the superheroes by. It can have one of three values: "good", "average",
    or "high"
    :return: a list of superheroes that match the specified intelligence level ("good", "average", or
    "high") based on the input superhero_list. The format of the returned list depends on the
    intelligence level: 
    - For "good" and "average", the function returns a list of dictionaries containing information about
    the matching superheroes.
    - For "high", the function returns a list of strings containing the
    """
    match good_average_high:
        case "good":
            good_intelligence_list = []
            for superhero in superhero_list:
                result_good = re.search("^good$", superhero["inteligencia"])
                if result_good:
                    good_intelligence_list.append(superhero)
            return good_intelligence_list

        case "average":
            average_intelligence_list = []
            for superhero in superhero_list:
                result_average = re.search("^average$", superhero["inteligencia"])
                if result_average:
                    average_intelligence_list.append(superhero)
            return average_intelligence_list

        case "high":
            high_intelligence_list = []
            for superhero in superhero_list:
                result_high = re.search("^high$", superhero["inteligencia"])
                if result_high:
                    high_intelligence_list.append(superhero["nombre"])
            return high_intelligence_list

# 6. Exportar a CSV la lista de héroes ordenada según opción elegida
# anteriormente [1-4]

def exportar_a_csv(chosen_option= 0, superhero_list= 0, amount_of_heroes= 0, order_flag= 0, superhero_key= 0, below_above= 0):
    """
    This function exports a list of superheroes to a CSV file based on different options such as sorting
    by height or strength, calculating the average of a specific key, and specifying whether the value
    should be below or above the average.
    
    :param chosen_option: An integer representing the user's chosen option for exporting data to a CSV
    file, defaults to 0 (optional)
    :param superhero_list: a list of dictionaries containing information about superheroes, defaults to
    0 (optional)
    :param amount_of_heroes: The number of heroes to be listed or exported to CSV file, defaults to 0
    (optional)
    :param order_flag: A flag that determines the order in which the superheroes will be sorted
    (ascending or descending), defaults to 0 (optional)
    :param superhero_key: The key (attribute) of the superhero dictionary that will be used to calculate
    the average in case of option 4 in the function, defaults to 0 (optional)
    :param below_above: The below_above parameter is used in the function calcular_promedio_de_key() to
    determine whether to calculate the average of superhero attributes that are below or above a certain
    value. It can take the values "below" or "above", defaults to 0 (optional)
    """
    match chosen_option:
        case 1:
            option_1_list = listar_n_heroes(superhero_list, amount_of_heroes)
            
            with open("simulacro_parcial.csv", "w") as file:
                keys_list= []
                for item in option_1_list[1].keys():
                    keys_list.append(item)
                keys_string = ",".join(keys_list)
                file.write(f"{keys_string}")
                file.write("\n")
                for item in option_1_list:
                    file.write(f"{item['nombre']},{item['identidad']},{item['empresa']},{item['altura']},{item['peso']},{item['genero']},{item['color_ojos']},{item['color_pelo']},{item['fuerza']},{item['inteligencia']} \n")
            
            if os.path.isfile("simulacro_parcial.csv"):
                imprimir_dato(f"Se creó el archivo 'simulacro_parcial.csv'")
            else:
                imprimir_dato(f"Error al crear el archivo 'simulacro_parcial.csv'")
        case 2:
            option_2_list = sort_superheroes_by_height(superhero_list, order_flag)
            
            with open("simulacro_parcial.csv", "w") as file:
                keys_list= []
                for item in option_2_list[1].keys():
                    keys_list.append(item)
                keys_string = ",".join(keys_list)
                file.write(f"{keys_string}")
                file.write("\n")
                for item in option_2_list:
                    file.write(f"{item['nombre']},{item['identidad']},{item['empresa']},{item['altura']},{item['peso']},{item['genero']},{item['color_ojos']},{item['color_pelo']},{item['fuerza']},{item['inteligencia']} \n")
            
            if os.path.isfile("simulacro_parcial.csv"):
                imprimir_dato(f"Se creó el archivo 'simulacro_parcial.csv'")
            else:
                imprimir_dato(f"Error al crear el archivo 'simulacro_parcial.csv'")
        case 3:
            option_3_list = sort_superheroes_by_strength(superhero_list, order_flag)
            
            with open("simulacro_parcial.csv", "w") as file:
                keys_list= []
                for item in option_3_list[1].keys():
                    keys_list.append(item)
                keys_string = ",".join(keys_list)
                file.write(f"{keys_string}")
                file.write("\n")
                for item in option_3_list:
                    file.write(f"{item['nombre']},{item['identidad']},{item['empresa']},{item['altura']},{item['peso']},{item['genero']},{item['color_ojos']},{item['color_pelo']},{item['fuerza']},{item['inteligencia']} \n")
            
            if os.path.isfile("simulacro_parcial.csv"):
                imprimir_dato(f"Se creó el archivo 'simulacro_parcial.csv'")
            else:
                imprimir_dato(f"Error al crear el archivo 'simulacro_parcial.csv'")
        case 4:
            option_4_list = calcular_promedio_de_key(superhero_list, superhero_key, below_above)
            
            with open("simulacro_parcial.csv", "w") as file:
                keys_list= []
                for item in option_4_list[1].keys():
                    keys_list.append(item)
                keys_string = ",".join(keys_list)
                file.write(f"{keys_string}")
                file.write("\n")
                for item in option_4_list:
                    file.write(f"{item['nombre']},{item['identidad']},{item['empresa']},{item['altura']},{item['peso']},{item['genero']},{item['color_ojos']},{item['color_pelo']},{item['fuerza']},{item['inteligencia']} \n")
            
            if os.path.isfile("simulacro_parcial.csv"):
                imprimir_dato(f"Se creó el archivo 'simulacro_parcial.csv'")
            else:
                imprimir_dato(f"Error al crear el archivo 'simulacro_parcial.csv'")

#----------------------------------------------Menu--------------------------------------------------------------
def marvel_app(hero_list):
    """
    This is a Python function that takes a list of superheroes and allows the user to perform various
    operations on the list, such as sorting and filtering, and export the results to a CSV file.
    
    :param hero_list: A list of dictionaries containing information about superheroes
    """
    hero_list_duplicate = hero_list[:]
    print(normalizar_datos(hero_list_duplicate))
    flag_enable_csv = False
    while True:
        user_choice = menu_principal()
        if flag_enable_csv == True and user_choice == 6:
            match valid_user_choice:
                case 1:
                    exportar_a_csv(chosen_option=valid_user_choice, superhero_list=hero_list_duplicate, amount_of_heroes=user_choice_amount_heroes_int)
                case 2:
                    exportar_a_csv(chosen_option=valid_user_choice, superhero_list=hero_list_duplicate, order_flag=user_choice_order)
                case 3:
                    exportar_a_csv(chosen_option=valid_user_choice, superhero_list=hero_list_duplicate, order_flag=user_choice_order)
                case 4:
                    exportar_a_csv(chosen_option=valid_user_choice, superhero_list=hero_list_duplicate, superhero_key=user_choice_superhero_key, below_above=user_choice_below_above)
        elif user_choice == 1 or user_choice == 2 or user_choice == 3 or user_choice == 4:
            match user_choice:
                case 1:
                    user_choice_amount_heroes = input("Ingrese la cantidad de superheroes: ") 

                    result = re.search("^[0-9]+$", user_choice_amount_heroes)
                    if result:
                        user_choice_amount_heroes_int = int(user_choice_amount_heroes)
                        print(listar_n_heroes(hero_list_duplicate, user_choice_amount_heroes_int))
                        valid_user_choice = 1
                    else:
                        print("Debe ingresar un numero")
                case 2:
                    user_choice_order = input("Ingrese el orden: 'asc' o 'desc': ")
                    if user_choice_order == "asc" or user_choice_order == "desc":
                        print(sort_superheroes_by_height(hero_list_duplicate, user_choice_order))
                        valid_user_choice = 2
                    else:
                        print("Debe ingresar 'asc' o 'desc'")
                case 3:
                    user_choice_order = input("Ingrese el orden: 'asc' o 'desc': ")
                    if user_choice_order == "asc" or user_choice_order == "desc":
                        print(sort_superheroes_by_strength(hero_list_duplicate, user_choice_order))
                        valid_user_choice = 3
                    else:
                        print("Debe ingresar 'asc' o 'desc'")
                case 4:
                    user_choice_superhero_key = input("Ingrese la caracteristica: 'altura', 'peso' o 'fuerza': ")
                    if user_choice_superhero_key == "altura" or user_choice_superhero_key == "peso" or user_choice_superhero_key == "fuerza":
                        user_choice_below_above = input("Ingrese si quiere los menores o mayores: 'menor' o 'mayor': ")
                        if user_choice_below_above == "menor" or user_choice_below_above == "mayor":
                            print(calcular_promedio_de_key(hero_list_duplicate, user_choice_superhero_key, user_choice_below_above))
                            valid_user_choice = 4
                        else:
                            print("Debe ingresar 'menor' o 'mayor'")
                    else:
                        print("Debe ingresar 'altura', 'peso' o 'fuerza'")
            flag_enable_csv = True
        elif(user_choice == 5):
            user_choice_intelligence_type = input("Ingrese el tipo de inteligencia: 'good', 'average' o 'high': ")
            if user_choice_intelligence_type == "good" or user_choice_intelligence_type == "average" or user_choice_intelligence_type == "high":
                print(categorize_heroes_by_intelligence(hero_list_duplicate, user_choice_intelligence_type))
            else:
                print("Debe ingresar 'good', 'average' o 'high'")
        elif(flag_enable_csv == False and user_choice == 6):
            print("Para seleccionar la opcion 6, primero debe seleccionar la opcion 1, 2, 3 o 4")
        else:
            print("Ha ingresado una opcion incorrecta")
        clear_console()

marvel_app(leer_archivo(json_adress))