import os

# 1. Escribir una función que reciba un string y devuelva el mismo string todo en
# mayúsculas.

def create_upper_case_str(txt):
    return txt.upper()

# 2. Escribir una función que reciba un string y devuelva el mismo string todo en
# minúsculas.

def create_lower_case_str(txt):
    return txt.lower()

# 3. Escribir una función que tome dos strings y devuelva un nuevo string que
# contenga ambos strings concatenados, separados por un espacio.

def concatenate_by_space(txt_1, txt_2):
    space_character = " "
    return space_character.join([txt_1, txt_2])

# 4. Escribir una función que tome un string y devuelva el número de caracteres
# que tiene el string.

def return_number_of_characters_in_str(txt_1):
    return len(txt_1)

# 5. Escribir una función que tome un string y un carácter y devuelva el número de
# veces que aparece ese carácter en el string.

def return_quantity_of_characters(txt_1, character):
    return txt_1.count(character)

# 6. Escribir una función que tome un string y un carácter y devuelva una lista con
# todas las palabras en el string que contienen ese carácter.

def create_list_with_words_cointaining_selected_character(txt_1, character):
    list_words_containing_selected_character = []
    individual_words = txt_1.split(" ")
    for word in individual_words:
        for letter in word:
            if (letter==character):
                list_words_containing_selected_character.append(word)
    return list_words_containing_selected_character

# 7. Escribir una función que tome un string y devuelva el mismo string con los
# espacios eliminados

def eliminate_spaces_in_str(txt_1):
    no_spaces_string = txt_1.strip()
    return no_spaces_string.replace(" ", "")

# 8. Escribir una función que reciba dos string (nombre y apellido) y devuelva un
# diccionario con el nombre y apellido, eliminando los espacios del comienzo y
# el final y colocando la primer letra en mayúscula

def create_dictionary_with_name_and_lastname_delete_spaces_and_capitalize(name, last_name):
    names_dictionary = {}
    names_dictionary[name.strip().capitalize()] = last_name.strip().capitalize()
    return names_dictionary

# 9. Escribir una función que tome una lista de nombres y los una en una sola
# cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"]
# -> "Juan\nMaría\nPedro".

def join_names_and_break_line(name_list):
    break_lines = "\n"
    return break_lines.join(name_list)

# 10. Escribir una función que tome un nombre y un apellido y devuelva un email en
# formato "inicial_nombre.apellido@utn-fra.com.ar".

def create_email_from_name(txt_1, txt_2):
    return f"{txt_1[0]}_{txt_1}.{txt_2}@utn-fra.com.ar"

# 11. Escribir una función que tome una lista de palabras y devuelva un string que
# contenga todas las palabras concatenadas con comas y "y" antes de la última
# palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el
# string resultante debería ser "manzanas, naranjas y bananas"..

def concatenate_words_using_space_and_y(word_list):
    #Takes list of words as input
    #Concatenates them using coma. Concatenates the last one using "y"
    #Returns concatenated string
    if (len(word_list) == 0):
        concatenated_str_by_coma_and_y = "Error"
    if (len(word_list) == 1):
        concatenated_str_by_coma_and_y = word_list[0]
    if (len(word_list) == 2):
        concatenated_str_by_coma_and_y = ", ".join(word_list)
    if (len(word_list) > 2):
        concatenated_str_by_coma = ", ".join(word_list[:-1])
        concatenated_str_by_coma_and_y = " y ".join([concatenated_str_by_coma, word_list[-1]])
    return concatenated_str_by_coma_and_y

# 12. Escribir una función que tome un número de tarjeta de crédito como input,
# verificar que todos los caracteres sean numéricos y devolver los últimos
# cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** ****
# **** 1234".

def verify_numbers_return_hidden_number(number):
    if number.isdigit() == True:
        no_spaces_number = number.replace(" ", "")

        hidden_part = "**** **** **** "
        last_four_digits = no_spaces_number[-4:]
        hidden_final_number = hidden_part + last_four_digits

        return hidden_final_number

# 13.Escribir una función que tome un correo electrónico y elimine cualquier
# carácter después del símbolo @, por ejemplo: "usuario@gmail.com" ->
# "usuario".

def delete_after_at_sign(txt_1):
    str_before_at_sign_list = []
    for character in txt_1:
        if character != "@":
            str_before_at_sign_list.append(character)
        else:
            break
    str_before_at_sign_str = "".join(str_before_at_sign_list)
    return str_before_at_sign_str

# 14.Escribir una función que tome una URL y devuelva solo el nombre de dominio,
# por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..

def get_domain(txt_1):
    email_segments_list = txt_1.split(".")
    return email_segments_list[1]

# 15. Escribir una función que tome una cadena de texto y devuelva solo los
# caracteres alfabéticos, eliminando cualquier número o símbolo, por ejemplo:
# "H0l4, m4nd0!" -> "Hl, mnd.

def get_only_alf(txt_1):
    characters_list = []
    for character in txt_1:
        if character.isalpha() == True or character == " ":
            characters_list.append(character)
    only_alf_string = "".join(characters_list)
    return only_alf_string

# 16. Escribir una función que tome una cadena de texto y la convierta en un
# acrónimo, tomando la primera letra de cada palabra, por ejemplo:
# "Universidad Tecnológica Nacional Facultad Regional Avellaneda" ->
# "UTNFRA”.

def get_acronym(txt_1):
    upper_letters_list = []
    for letter in txt_1:
        if letter.isupper() == True:
            upper_letters_list.append(letter)
    acronym = "".join(upper_letters_list)
    return acronym

# 17. Escribir una función que tome un número binario y lo convierta en una cadena
# de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo:
# "101" -> "00000101".

def transform_binary_to_8_bits(txt_1):
    if len(txt_1) < 8:
        eight_bits_bin = txt_1.zfill(8)
    else:
        eight_bits_bin = txt_1
    return eight_bits_bin

# 18. Escribir una función que tome una cadena de caracteres y reemplace todas
# las letras mayúsculas por letras minúsculas y todas las letras minúsculas por
# letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"

def invert_cases(txt_1):
    inverted_case_list = []
    for letter in txt_1:
        if letter.isupper() == True:
            inverted_case_list.append(letter.lower())
        else:
            inverted_case_list.append(letter.upper())
    inverted_case_str = "".join(inverted_case_list)
    return inverted_case_str

# 19.Escribir una función que tome una cadena de caracteres y cuente la cantidad
# de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.

def count_digits(txt_1):
    counter = 0
    for character in txt_1:
        if character.isdigit():
            counter += 1
    return f"Contiene {counter} digitos"

# 20. Escribir una función que tome una lista de direcciones de correo electrónico y
# las una en una sola cadena separada por punto y coma, por ejemplo:
# ["juan@gmail.com", "maria@hotmail.com"] ->
# "juan@gmail.com;maria@hotmail.com".

def join_email_adresses(email_list):
    return ";".join(email_list)

# 21. Crear una función que reciba como parámetro un string y devuelva un
# diccionario donde cada clave es una palabra y cada valor es un entero que
# indica cuántas veces aparece esa palabra dentro del string.

def create_dictionary_with_coincidences_counter(txt_1):
    #Takes string as an input
    #Creates a dictionary with words as keys and the amount of thime this word appears as value
    #Returns dictionary
    dictionary_with_counter = {}
    separate_words = txt_1.split(" ")
    for word in separate_words:
        dictionary_with_counter[word] = txt_1.count(word)
    return dictionary_with_counter

def show_menu_offer_user_choice():
    print("MENU: \n \
    0. Salir \n \
    1. Obtener string en mayusculas \n \
    2. Obtener string en minusculas \n \
    3. Obtener string separado por espacios \n \
    4. Obtener numero de caracteres en string \n \
    5. Obtener numero de veces que aparece un caracter en el string \n \
    6. Obtener lista de caracteres que contienen el string \n \
    7. Obtener string sin espacios \n \
    8. Obtener diccionario con nombre y apellido, sin espacios en principio en final el final y con primer letra en mayúscula \n \
    9. Obtener lista con nombres separados en salto de linea \n \
    10. Obtener direccion de email en formato 'inicial_nombre.apellido@utn-fra.com.ar' \n \
    11. Obtener lista con palabras concatenadas con comas e 'y' \n \
    12. Obtener direccion de email oculta con solo los primeros 4 numeros visibles \n \
    13. Obtener direccion de email sin dominio \n \
    14. Obtener dominio de direccion web \n \
    15. Obtener solo caracteres alfabeticos \n \
    16. Obtener acronimo \n \
    17. Obtener cadena de 8 bits a partir de un numero binario \n \
    18. Obtener string con mayusculas y minusculas invertidas \n \
    19. Obtener cantidad de digitos en el string \n \
    20. Separar direcciones email mediante punto y coma \n \
    21. Obtener diccionario con contador de palabras a partir de una cadena de texto")
    user_choice_txt = input("Elija su opcion: ")
    user_choice_int = int(user_choice_txt)
    return user_choice_int

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

def string_app():
    while True:
        user_choice_int = show_menu_offer_user_choice()
        match(user_choice_int):
            case 0:
                break
            case 1:
                user_input_txt_1 = input("Ingrese el string: ")
                print(create_upper_case_str(user_input_txt_1))
            case 2:
                user_input_txt_1 = input("Ingrese el string: ")
                print(create_lower_case_str(user_input_txt_1))
            case 3:
                user_input_txt_1 = input("Ingrese el string: ")
                user_input_txt_2 = input("Ingrese el segundo string: ")
                print(concatenate_by_space(user_input_txt_1, user_input_txt_2))
            case 4:
                user_input_txt_1 = input("Ingrese el string: ")
                print(return_number_of_characters_in_str(user_input_txt_1))
            case 5:
                user_input_txt_1 = input("Ingrese el string: ")
                user_input_txt_2 = input("Ingrese el segundo string: ")
                print(return_quantity_of_characters(user_input_txt_1, user_input_txt_2))
            case 6:
                user_input_txt_1 = input("Ingrese el string: ")
                user_input_txt_2 = input("Ingrese el segundo string: ")
                print(create_list_with_words_cointaining_selected_character(user_input_txt_1, user_input_txt_2))
            case 7:
                user_input_txt_1 = input("Ingrese el string: ")
                print(eliminate_spaces_in_str(user_input_txt_1))
            case 8:
                user_input_txt_1 = input("Ingrese el string: ")
                user_input_txt_2 = input("Ingrese el segundo string: ")
                print(create_dictionary_with_name_and_lastname_delete_spaces_and_capitalize(user_input_txt_1, user_input_txt_2))
            case 9:
                user_input_txt_1 = input("Ingrese el string: ")
                user_input_txt_2 = input("Ingrese el segundo string: ")
                list_of_names = []
                list_of_names.append(user_input_txt_1)
                list_of_names.append(user_input_txt_2)
                print(join_names_and_break_line(list_of_names))
            case 10:
                user_input_txt_1 = input("Ingrese el string: ")
                user_input_txt_2 = input("Ingrese el segundo string: ")
                print(create_email_from_name(user_input_txt_1, user_input_txt_2))
            case 11:
                user_input_txt_1 = input("Ingrese el string: ")
                user_input_txt_2 = input("Ingrese el segundo string: ")
                user_input_txt_3 = input("Ingrese el tercer string: ")
                list_from_user_input = [user_input_txt_1, user_input_txt_2, user_input_txt_3]
                print(concatenate_words_using_space_and_y(list_from_user_input))
            case 12:
                user_input_txt_1 = input("Ingrese el string: ")
                print(verify_numbers_return_hidden_number(user_input_txt_1))
            case 13:
                user_input_txt_1 = input("Ingrese el string: ")
                print(delete_after_at_sign(user_input_txt_1))
            case 14:
                user_input_txt_1 = input("Ingrese el string: ")
                print(get_domain(user_input_txt_1))
            case 15:
                user_input_txt_1 = input("Ingrese el string: ")
                print(get_only_alf(user_input_txt_1))
            case 16:
                user_input_txt_1 = input("Ingrese el string: ")
                print(get_acronym(user_input_txt_1))
            case 17:
                user_input_txt_1 = input("Ingrese el string: ")
                print(transform_binary_to_8_bits(user_input_txt_1))
            case 18:
                user_input_txt_1 = input("Ingrese el string: ")
                print(invert_cases(user_input_txt_1))
            case 19:
                user_input_txt_1 = input("Ingrese el string: ")
                print(count_digits(user_input_txt_1))
            case 20:
                user_input_txt_1 = input("Ingrese el string: ")
                user_input_txt_2 = input("Ingrese el segundo string: ")
                user_input_txt_3 = input("Ingrese el tercer string: ")
                list_of_emails = [user_input_txt_1, user_input_txt_2, user_input_txt_3]
                print(join_email_adresses(list_of_emails))
            case 21:
                user_input_txt_1 = input("Ingrese el string: ")
                print(create_dictionary_with_coincidences_counter(user_input_txt_1))
            case _:
                print("Ha seleccionado una opcion incorrecta")
        clear_console()

string_app()