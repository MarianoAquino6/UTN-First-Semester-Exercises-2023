import re
import os

# 1. Crear una función llamada es_mayuscula que reciba un string y devuelva True
# en caso de que todas las letras sean mayúsculas o False en el caso contrario

def es_mayuscula (given_string):
    result = re.search("^[A-Z]+$",given_string)
    if result:
        return True
    else:
        return False

# 2. Crear una función llamada es_minuscula que reciba un string y devuelva True
# en caso de que todas las letras sean minusculas o False en el caso contrario

def es_minuscula (given_string):
    result = re.search("^[a-z]+$",given_string)
    if result:
        return True
    else:
        return False

# 3. Crear una función llamada es_entero que reciba un string y devuelva True en
# caso de que se trate de un número entero y False en caso contrario.

def es_entero (given_string):
    result = re.search("^[0-9]+$",given_string)
    if result:
        return True
    else:
        return False

# 4. Crear una función llamada es_solo_texto que reciba un string y devuelva True
# en caso de que trate solo de caracteres alfabéticos y el espacio y False en el
# caso contrario

def es_solo_texto (given_string):
    result = re.search("^[a-zA-Z ]+$",given_string)
    if result:
        return True
    else:
        return False

# 5. Crear una función llamada es_decimal que reciba dos strings: el primero
# representa la expresión a evaluar y el segundo el separador decimal (puede
# ser punto . o coma ,). Debe devolver True en caso que se trate de un número
# decimal y False en el caso contrario.

def es_decimal (number_to_evaluate, pattern_dot_coma):
    result = re.search(f"^[0-9]+{pattern_dot_coma}[0-9]+$", number_to_evaluate)
    if result:
        return True
    else:
        return False

# 6. Crear una función llamada es_alfanumerico que devuelva True en caso de 
# tratarse de solo letras y números y False en el caso contrario 
# (es decir que contenga caracteres especiales) 

def es_alfanumerico (given_string):
    result = re.search("^[a-zA-z0-9 ]+$" ,given_string)
    if result:
        return True
    else:
        return False

# 7. Crear una función llamada es_binario que devuelva True en caso de un
# número binario válido (solo ceros y unos) o False en el caso contrario

def es_binario (given_string):
    result = re.search("^[0-1]+$" ,given_string)
    if result:
        return True
    else:
        return False

# 8. Crear una función que reciba una lista de palabras y devuelva otra lista con
# # las palabras que comienzan con la letra ‘U’

def create_list_of_words_containing_u (word_list):
    u_list = []
    for word in word_list:
        result = re.findall("^U[a-zA-Z]+", word)
        if result:
            u_list.append(result)
    return u_list

# 9. Crear una función que reciba un texto y devuelva una lista con las palabras
# que contienen entre 3 y 6 caracteres de largo

def create_list_of_long_words (given_string):
    long_words = []
    words_in_string = given_string.split(" ")
    for word in words_in_string:
        result = re.findall("^[a-zA-Z]{3,6}$", word)
        if result:
            long_words.append(result)
    return long_words

# 10. Crear una función que reciba un texto y devuelva una lista de todas las
# palabras que terminan con ‘ción’.

def create_list_words_ending_in_cion (given_string):
    words_ending_in_cion = []
    words_in_text = given_string.split(" ")
    for word in words_in_text:
        result = re.findall("[a-zA-Z]+cion$", word)
        if result:
            words_ending_in_cion.append(result)
    return words_ending_in_cion

# 11. Crear una función que reciba un texto y devuelva una lista de palabras que 
# encuentra que comienzan con una vocal

def create_list_words_starting_with_vocal (given_string):
    words_starting_with_vocals = []
    words_in_text = given_string.split(" ")
    for word in words_in_text:
        result = re.findall("^[AEIOUaeiou][a-zA-Z]+", word)
        if result:
            words_starting_with_vocals.append(result)
    return words_starting_with_vocals

# 12. Crear una función llamada obtener_oraciones que reciba como parámetro un
# string y que devuelva una lista con las oraciones (delimitadores, ‘.’, ‘!’, ‘?’).

def create_list_of_sentences_from_string (given_string):
    result = re.split("\.|!|\?", given_string)
    return result

# 13. Crear una función que reciba un texto como parámetro y que corrija los
# errores de ortografía que no cumplan con la regla ortográfica que indica que
# antes de V se escribe N y que antes de B se escribe M.
# Por ejemplo, si el texto es: "Mi comvicción me hace sentir que es el momento
# de imvertir tiempo para finalmente envarcar en esta nueva aventura." La
# función debería devolver:
# “Mi convicción me hace sentir que es el momento de invertir tiempo para
# finalmente embarcar en esta nueva aventura."

def correct_errors_in_string (given_string):
    words_in_string = given_string.split(" ")
    corrected_string_list = []
    for word in words_in_string:
        result_mv = re.search("^[a-zA-Z]+mv[a-zA-Z]", word)
        result_nv = re.search("^[a-zA-Z]+nv[a-zA-Z]", word)
        if result_mv:
            corrected_mv_string = re.sub("mv", "nv", word)
            corrected_string_list.append(corrected_mv_string)
        elif result_nv:
            corrected_nv_string = re.sub("nv", "mb", word)
            corrected_string_list.append(corrected_nv_string)
        else:
            corrected_string_list.append(word)
    corrected_string = " ".join(corrected_string_list)
    return corrected_string

# 14. Crear la función es_fecha que reciba dos string, el primero representa la
# expresión a evaluar y el segundo el separador de la fecha (puede ser la barra /
# o el guión -) y que devuelva True en caso de tratarse de una fecha válida y
# False en el caso contrario. Los formatos admitidos son: ‘dd/mm/aaaa’ o
# ‘dd-mm-aaaa’

def es_fecha (string_to_evaluate, divider):
    result_dd_mm_aaaa = re.search(f"^(0[1-9]|[1-2][0-9]|3[0-1]){divider}(0[1-9]|1[0-2]){divider}[0-9][0-9][0-9][0-9]$", string_to_evaluate)
    if result_dd_mm_aaaa:
        return True
    else:
        return False

# 15. Crear la función es_hora que reciba un string y que devuelva True en caso de
# tratarse de una hora válida y False en el caso contrario. El formato admitido
# es ‘hh:mm:ss’

def es_hora (string_to_evaluate):
    result_hh_mm_ss = re.search("^([0-1][0-9]|2[0-4]):([0-5][0-9]):([0-5][0-9])$", string_to_evaluate)
    if result_hh_mm_ss:
        return True
    else:
        return False

#16. Crear la función validar_codigo_postal que reciba un string como parámetro y
# devuelva True en caso de tratarse de código postal válido o False en caso
# contrario

def validar_codigo_postal (string_to_evaluate):
    result_postal_code = re.search("^[A-Z][0-9]{4}[A-Z]{3}$", string_to_evaluate)
    if result_postal_code:
        return True
    else:
        return False

# 17. Crear la función validar_patente que reciba un string como parámetro y
# devuelva True en caso de tratarse de un número de patente válido o False en
# caso contrario. 

def validar_patente (string_to_evaluate):
    result_new_license_plate = re.search("^[A-Z]{2} [0-9]{3} [A-Z]{2}$", string_to_evaluate)
    result_old_license_plate = re.search("^[A-Z]{3} [0-9]{3}$", string_to_evaluate)
    if result_new_license_plate or result_old_license_plate:
        return True
    else:
        return False

# 18. Crear una función que se llame obtener_direcciones_email que reciba un texto
# y devuelva una lista con todas las direcciones de email válidas que
# encuentren en el mismo. 

def obtener_direcciones_email (given_string):
    email_list= re.findall("[a-z]+@[a-z]+\.[a-z]{3}", given_string)
    return email_list

# 19. Crear una función llamada validar_password que reciba un string y verifique si
# se trata de una contraseña cumple con los requisitos mínimos de seguridad:
# ○ Al menos 8 caracteres
# ○ Al menos una letra mayúscula y una letra minúscula
# ○ Un número
# ○ Un carácter especial
# En caso de no cumplir con alguno de los requisitos, imprimir un mensaje
# informando cual no se cumplio

def validar_password(password):
    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    
    if not re.search(r"[A-Z]", password):
        print("La contraseña debe contener al menos una letra mayúscula.")
        return False
    
    if not re.search(r"[a-z]", password):
        print("La contraseña debe contener al menos una letra minúscula.")
        return False
    
    if not re.search(r"[0-9]", password):
        print("La contraseña debe contener al menos un número.")
        return False
    
    if not re.search(r"[^0-9a-zA-Z]", password):
        print("La contraseña debe contener al menos un carácter especial.")
        return False
    
    print("La contraseña es válida.")
    return True

# 20. Crear una función llamada validar_ip que reciba un string como parámetro y
# verifique si se trata de una dirección IP v4 válida, en caso de serlo retornar
# True de lo contrario retornar False.
# Se considera una dirección IP válida si tiene el formato xxx.xxx.xxx.xxx, donde
# xxx es un número entero entre 0 y 255.

def validar_ip (given_string):
    regex = "(0[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
    result_ip_adress = re.search(f"^{regex}\.{regex}\.{regex}\.{regex}$", given_string)
    if result_ip_adress:
        return True
    else:
        return False

def show_menu_offer_user_choice():
    print("Bienvenido a los ejercicios de REGEX. A continuacion, el menu: \n \
    0. Salir \n \
    1. Ejercicio 1 \n \
    2. Ejercicio 2 \n \
    3. Ejercicio 3 \n \
    4. Ejercicio 4 \n \
    5. Ejercicio 5 \n \
    6. Ejercicio 6 \n \
    7. Ejercicio 7 \n \
    8. Ejercicio 8 \n \
    9. Ejercicio 9 \n \
    10. Ejercicio 10 \n \
    11. Ejercicio 11 \n \
    12. Ejercicio 12 \n \
    13. Ejercicio 13 \n \
    14. Ejercicio 14 \n \
    15. Ejercicio 15 \n \
    16. Ejercicio 16 \n \
    17. Ejercicio 17 \n \
    18. Ejercicio 18 \n \
    19. Ejercicio 19 \n \
    20. Ejercicio 20")
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

def regex_app():
    while True:
        user_choice_int = show_menu_offer_user_choice()
        match(user_choice_int):
            case 0:
                break
            case 1:
                user_input = input("Ingrese un texto: ")
                print(es_mayuscula(user_input))
            case 2:
                user_input = input("Ingrese un texto: ")
                print(es_minuscula(user_input))
            case 3:
                user_input = input("Ingrese un numero: ")
                print(es_entero(user_input))
            case 4:
                user_input = input("Ingrese un texto: ")
                print(es_solo_texto(user_input))
            case 5:
                user_input = input("Ingrese un numero: ")
                print(es_decimal(user_input, "\."))
            case 6:
                user_input = input("Ingrese un texto: ")
                print(es_alfanumerico(user_input))
            case 7:
                user_input = input("Ingrese un numero: ")
                print(es_binario(user_input))
            case 8:
                list_of_words =["Utah", "Humo", "Urqnell"]
                print(create_list_of_words_containing_u(list_of_words))
            case 9:
                user_input = input("Ingrese un texto: ")
                print(create_list_of_long_words(user_input))
            case 10:
                user_input = input("Ingrese un texto: ")
                print(create_list_words_ending_in_cion(user_input))
            case 11:
                user_input = input("Ingrese un texto: ")
                print(create_list_words_starting_with_vocal(user_input))
            case 12:
                user_input = input("Ingrese un texto: ")
                print(create_list_of_sentences_from_string(user_input))
            case 13:
                long_text_test_error ="Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente envarcar en esta nueva aventura."
                print(correct_errors_in_string(long_text_test_error))
            case 14:
                print(es_fecha("10-10-1992", "\-"))
            case 15:
                print(es_hora("21:15:12"))
            case 16:
                user_input = input("Ingrese un codigo postal: ")
                print(validar_codigo_postal(user_input))
            case 17:
                user_input = input("Ingrese su patente: ")
                print(validar_patente(user_input))
            case 18:
                datos = "<Alberto, Cervantes> acervantes@gmx.com <Ana, Jimenez> ajimenez@hotmail.com <Antonio, Castillo> acastillo@gmail.com <Armando, Vega>"
                print(obtener_direcciones_email(datos))
            case 19:
                user_input = input("Ingrese la contraseña: ")
                print(validar_password(user_input))
            case 20:
                user_input = input("Ingrese su IPv4: ")
                print(validar_ip(user_input))
            case _:
                print("Ha seleccionado una opcion incorrecta")
        clear_console()

regex_app()