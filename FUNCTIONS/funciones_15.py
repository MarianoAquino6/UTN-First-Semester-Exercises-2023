# Crear una función que recibe una lista de números y devuelve un diccionario
# con el valor mínimo, el valor máximo y el promedio de los números en la lista.

def create_dictionary_from_list_and_calculate_max_min_and_average (list1):
    #Function creates a dictionary from a list and calculates min, max and average from it's items
    #Takes a list as input
    #Returns the dictionary
    dictionary = {}
    counter = 0
    accumulator = 0
    flag = True
    for number in list1:
        counter += 1
        accumulator = accumulator + number
        if (flag == True):
            max_value = number
            min_value = number
            flag = False
        elif (number > max_value):
            max_value = number
        elif (number < min_value):
            min_value = number
        
        average = accumulator / counter

        dictionary["Valor minimo"] = min_value
        dictionary["Valor maximo"] = max_value
        dictionary["Promedio"] = average
    return dictionary

user_list = []

while True:
    user_input_txt = input("Ingrese numeros para añadir a la lista. Cuando termine ingrese BYE: ")
    if (user_input_txt == "BYE"):
        break
    
    user_input_float = float(user_input_txt)
    user_list.append(user_input_float)

print(create_dictionary_from_list_and_calculate_max_min_and_average(user_list))