# Crea una función que reciba dos listas de nombres, y devuelva una lista con
# los nombres que aparecen en ambas listas

def join_lists (list_1, list_2):
    #Function joins lists
    #Takes the two list as input
    #Returns a new list which contains both lists joined together
    new_list = list_1 + list_2
    return new_list

list_user_1 = []
list_user_2 = []

while True:
    user_input_txt = input("Ingrese nombres para la primera lista. Cuando termine ingrese BYE: ")
    if (user_input_txt == "BYE"):
        break

    list_user_1.append(user_input_txt)

while True:
    user_input_txt = input("Ingrese nombres para la segunda lista. Cuando termine ingrese BYE: ")
    if (user_input_txt == "BYE"):
        break

    list_user_2.append(user_input_txt)

print(join_lists(list_user_1, list_user_2))