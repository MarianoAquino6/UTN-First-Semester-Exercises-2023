# Crear una función que recibe una lista de palabras y devuelve un diccionario
# con las palabras como llaves y su longitud como valores.

def create_dictionary_from_list (list1):
    #Function creates a dictionary from list that cointains words as keys and their lenght as value
    #Takes list as input
    #Returns a new dictionary containing these elements
    dictionary = {}
    for word in list1:
        dictionary[word] = len(word)
    return dictionary

user_list = []

while True:
    user_input_txt = input("Ingrese palabras para añadir a la lista. Cuando termine ingrese BYE: ")
    if (user_input_txt == "BYE"):
        break

    user_list.append(user_input_txt)

print(create_dictionary_from_list(user_list))