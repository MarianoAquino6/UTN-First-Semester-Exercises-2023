# Crea una función que reciba como parámetros una lista de palabras y
# devuelva la palabra más larga.

def identify_longest_word_from_list (list_1):
    #Function idenfity the longest word from the list
    #Takes a list as input
    #Returns the largest word found
    flag = True
    for item in list_1:
        if (flag == True):
            max_lenght = len(item)
            largest_word = item
            flag = False
        elif (len(item) > max_lenght):
            max_lenght = len(item)
            largest_word = item
    return largest_word

list_user = []

while True:
    user_input_txt = input("Ingrese palabras. Cuando termine ingrese BYE: ")
    if (user_input_txt == "BYE"):
        break

    list_user.append(user_input_txt)

print(f"La palabra mas larga es {identify_longest_word_from_list(list_user)}")
