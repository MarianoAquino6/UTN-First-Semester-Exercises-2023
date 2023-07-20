from data_stark import lista_personajes

# 1.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# 2.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
# 3.Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
# 4.Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
# 5.Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
# 6.Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
# 7.Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
# 8.Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
# 9.Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# 10.Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# 11.Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
# 12.Listar todos los superhéroes agrupados por color de ojos.
# 13.Listar todos los superhéroes agrupados por color de pelo.
# 14.Listar todos los superhéroes agrupados por tipo de inteligencia

menu = " 0. Salir del sistema\n \
1. Obtener los nombres de los superheroes de genero M\n \
2. Obtener los nombres de los superheroes de genero F\n \
3. Obtener superheroe mas alto de genero M\n \
4. Obtener superheroe mas alto de genero F\n \
5. Obtener superheroe mas bajo de genero M\n \
6. Obtener superheroe mas bajo de genero F\n \
7. Obtener altura promedio de superheroes de genero M\n \
8. Obtener altura promedio de superheroes de genero F\n \
9. Obtener cantidad de tipos de color de ojos de superheroes\n \
10. Obtener cantidad de tipos de pelo de ojos de superheroes\n \
11. Obtener cantidad de tipos de inteligencia de superheroes\n \
12. Obtener lista de superheroes agrupados por color de ojos\n \
13. Obtener lista de superheroes agrupados por color de pelo\n \
14. Obtener lista de superheroes agrupados por tipo de inteligencia"

print(menu)
user_choice_txt = input("Que opcion desea elegir?: ")
user_choice_int = int(user_choice_txt)

def obtain_name_by_sex (sex):
    #Function obtains superheroes's names by sex
    #Takes sex as input
    #Returns a list containing superheroes names according to sex
    superhero_name_list = []
    
    for superhero in lista_personajes:
        if (superhero["genero"] == sex):
            superhero_name_list.append(superhero["nombre"])  
    return superhero_name_list
        
def obtain_tallest_by_sex (sex):
    #Function obtains tallest superhero by sex
    #Takes sex as input
    #Returns tallest superhero's name
    flag_height = True
    
    for superhero in lista_personajes:
        if (superhero["genero"] == sex):
            if (flag_height == True):
                max_height = float(superhero["altura"])
                tallest_superhero = superhero["nombre"]
                flag_height = False
            elif (float(superhero["altura"]) > max_height):
                max_height = float(superhero["altura"])
                tallest_superhero = superhero["nombre"]
    return tallest_superhero

def obtain_shortest_by_sex (sex):
    #Function obtains shortest superhero by sex
    #Takes sex as input
    #Returns shortest superhero's name
    flag_height = True
    
    for superhero in lista_personajes:
        if (superhero["genero"] == sex):
            if (flag_height == True):
                min_height = float(superhero["altura"])
                shortest_superhero = superhero["nombre"]
                flag_height = False
            elif (float(superhero["altura"]) < min_height):
                min_height = float(superhero["altura"])
                shortest_superhero = superhero["nombre"]
    return shortest_superhero

def obtain_height_average_by_sex (sex):
    #Function calculates an obtains superheroes's height average by sex
    #Takes sex as input
    #Returns height average
    counter = 0
    accumulator = 0
    
    for superhero in lista_personajes:
        if (superhero["genero"] == sex):
            counter += 1
            accumulator = accumulator + float(superhero["altura"])
    height_average = accumulator / counter
    return height_average

def obtain_eye_color_dict_name_or_counter (list_heroes, request):
    #Function obtains a dict with the amount of eye color types and a dict with superheroes sorted by their eye color
    #Takes the list and user's request as input
    #Returns the eye color counter dict or the superheroes sorted by eye color dict depending on what is being requested
    eye_color_dict_counter = {"Brown": 0, "Blue":0, "Green":0, "Yellow":0, "Hazel":0, "Silver":0, "Red":0}
    eye_color_dict_names = {"Brown": [], "Blue":[], "Green":[], "Yellow":[], "Hazel":[], "Silver":[], "Red":[]}
    for superhero in list_heroes:
        match superhero["color_ojos"]:
            case "Brown":
                eye_color_dict_counter["Brown"]+=1
                eye_color_dict_names["Brown"].append(superhero["nombre"])
            case "Blue":
                eye_color_dict_counter["Blue"]+=1
                eye_color_dict_names["Blue"].append(superhero["nombre"])
            case "Green":
                eye_color_dict_counter["Green"]+=1
                eye_color_dict_names["Green"].append(superhero["nombre"])
            case "Yellow":
                eye_color_dict_counter["Yellow"]+=1
                eye_color_dict_names["Yellow"].append(superhero["nombre"])
            case "Hazel":
                eye_color_dict_counter["Hazel"]+=1
                eye_color_dict_names["Hazel"].append(superhero["nombre"])
            case "Silver":
                eye_color_dict_counter["Silver"]+=1
                eye_color_dict_names["Silver"].append(superhero["nombre"])
            case "Red":
                eye_color_dict_counter["Red"]+=1
                eye_color_dict_names["Red"].append(superhero["nombre"])

    if (request == "Counter"):
        return eye_color_dict_counter
    else:
        return eye_color_dict_names

def obtain_hair_color_dict_name_or_counter (list_heroes, request):
    #Function obtains a dict with the amount of hair color types and a dict with superheroes sorted by their hair color
    #Takes the list and user's request as input
    #Returns the hair color counter dict or the superheroes sorted by hair color dict depending on what is being requested
    hair_color_dict_counter = {"Yellow": 0, "Brown":0, "Black":0, "Auburn":0, "Red":0, "White":0, "No Hair":0, "Blond":0, "Green":0, "Mix":0}
    hair_color_dict_names = {"Yellow": [], "Brown":[], "Black":[], "Auburn":[], "Red":[], "White":[], "No Hair":[], "Blond":[], "Green":[], "Mix":[]}
    for superhero in list_heroes:
        match superhero["color_pelo"]:
            case "Yellow":
                hair_color_dict_counter["Yellow"]+=1
                hair_color_dict_names["Yellow"].append(superhero["nombre"])
            case "Brown":
                hair_color_dict_counter["Brown"]+=1
                hair_color_dict_names["Brown"].append(superhero["nombre"])
            case "Black":
                hair_color_dict_counter["Black"]+=1
                hair_color_dict_names["Black"].append(superhero["nombre"])
            case "Auburn":
                hair_color_dict_counter["Auburn"]+=1
                hair_color_dict_names["Auburn"].append(superhero["nombre"])
            case "Red":
                hair_color_dict_counter["Red"]+=1
                hair_color_dict_names["Red"].append(superhero["nombre"])
            case "White":
                hair_color_dict_counter["Whie"]+=1
                hair_color_dict_names["White"].append(superhero["nombre"])
            case "No Hair":
                hair_color_dict_counter["No Hair"]+=1
                hair_color_dict_names["No Hair"].append(superhero["nombre"])
            case "Blond":
                hair_color_dict_counter["Blond"]+=1
                hair_color_dict_names["Blond"].append(superhero["nombre"])
            case "Green":
                hair_color_dict_counter["Green"]+=1
                hair_color_dict_names["Green"].append(superhero["nombre"])
            case "Brown / White":
                hair_color_dict_counter["Mix"]+=1
                hair_color_dict_names["Mix"].append(superhero["nombre"])
            case "Red / Orange":
                hair_color_dict_counter["Mix"]+=1
                hair_color_dict_names["Mix"].append(superhero["nombre"])
    
    if (request == "Counter"):
        return hair_color_dict_counter
    else:
        return hair_color_dict_names

def obtain_intelligence_dict_name_or_counter (list_heroes, request):
    #Function obtains a dict with the amount of intelligence types and a dict with superheroes sorted by their intelligence
    #Takes the list and user's request as input
    #Returns the intelligence counter dict or the superheroes sorted by intelligence dict depending on what is being requested
    intelligence_dict_counter = {"No tiene": "No tiene", "Average":0, "Good":0, "High":0}
    intelligence_dict_names = {"No tiene":[], "Average":[], "Good":[], "High":[]}
    for superhero in list_heroes:
        match superhero["inteligencia"]:
            case "":
                intelligence_dict_names["No tiene"].append(superhero["nombre"])
            case "average":
                intelligence_dict_counter["Average"]+=1
                intelligence_dict_names["Average"].append(superhero["nombre"])
            case "good":
                intelligence_dict_counter["Good"]+=1
                intelligence_dict_names["Good"].append(superhero["nombre"])
            case "high":
                intelligence_dict_counter["High"]+=1
                intelligence_dict_names["High"].append(superhero["nombre"])
    
    if (request == "Counter"):
        return intelligence_dict_counter
    else:
        return intelligence_dict_names

def show_menu_and_offer_new_choice():
    #Function shows menu and offers the user a new choice
    #Doesn't have an input
    #Returns user's choice
    print(menu)
    user_choice_txt = input("Que opcion desea elegir a continuacion? ")
    user_choice_int = int(user_choice_txt)
    return user_choice_int

while True:
    match user_choice_int:
        case 0:         
            break
        case 1:
            print(obtain_name_by_sex("M"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 2:
            print(obtain_name_by_sex("F"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 3:
            print(obtain_tallest_by_sex("M"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 4:
            print(obtain_tallest_by_sex("F"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 5:
            print(obtain_shortest_by_sex("M"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 6:
            print(obtain_shortest_by_sex("F"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 7:
            print(obtain_height_average_by_sex("M"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 8:
            print(obtain_height_average_by_sex("F"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 9:
            print(obtain_eye_color_dict_name_or_counter(lista_personajes, "Counter"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 10:
            print(obtain_hair_color_dict_name_or_counter(lista_personajes, "Counter"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 11:
            print(obtain_intelligence_dict_name_or_counter(lista_personajes, "Counter"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 12:
            print(obtain_eye_color_dict_name_or_counter(lista_personajes, "Name"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 13:
            print(obtain_hair_color_dict_name_or_counter(lista_personajes, "Name"))
            user_choice_int = show_menu_and_offer_new_choice()
        case 14:
            print(obtain_intelligence_dict_name_or_counter(lista_personajes, "Name"))
            user_choice_int = show_menu_and_offer_new_choice()