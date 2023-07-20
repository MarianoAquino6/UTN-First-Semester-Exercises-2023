# Crea una función que reciba como parámetro una cadena de texto y devuelva
# la cantidad de vocales que tiene.

def count_vocals_in_string (entered_string):
    #Function counts vocals in a string
    #Takes the string as input
    #Returns the amount of vocals in the string
    counter = 0
    for letter in entered_string:
        if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
            counter += 1
    return counter

user_input_txt = input("Ingrese una cadena de texto: ")

print(f"La cantidad de vocales en el string es {count_vocals_in_string(user_input_txt)}")