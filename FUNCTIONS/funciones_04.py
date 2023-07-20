# Crear una función que calcule el promedio de edad de un grupo de personas.
# Recibe una lista de edades y devuelve el promedio.

age_list = []

def calculate_age_average (age_list):
    #Function calculates age average
    #Takes the age list as input
    #Returns the the result of the average calculation
    counter = 0
    accumulator = 0
    for age in age_list:
        counter = counter + 1
        accumulator = accumulator + age
    
    age_average_calculation = accumulator / counter
    return age_average_calculation

while True:
    user_age_input_txt = input("Ingrese la edad. Cuando termine ingrese BYE: ")
    if (user_age_input_txt == "BYE"):
        break
    user_age_input_int = int(user_age_input_txt)

    age_list.append(user_age_input_int)

print(f"El promedio de las edades ingresadas es de {calculate_age_average(age_list)} años")
