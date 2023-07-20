# Crear una función que cuente la cantidad de veces que aparece un elemento
# en una lista. Recibe una lista y un elemento como parámetros y devuelve la
# cantidad de veces que aparece en la lista.

def count_how_many_times_item_appears_in_list (list_1, item_to_count):
    #Function counts how many times an item exists on a list
    #Takes list and entered item as input
    #Returns the times it appears in the list
    counter = 0
    for item in list_1:
        if (item == item_to_count):
            counter += 1
    return counter

list_user = []

while True:
    user_input_txt = input("Ingrese distintos elementosCuando termine ingrese BYE: ")
    if (user_input_txt == "BYE"):
        break

    list_user.append(user_input_txt)

print(f"La cantidad de veces que aparece este elemento es {count_how_many_times_item_appears_in_list(list_user, 'Ozzy')}")