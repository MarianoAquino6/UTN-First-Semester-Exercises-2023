# Crear una función que recibe una lista de diccionarios con información de
# películas (título, género, director) y devuelve un diccionario con la cantidad de
# películas por género.

def create_dictionary_from_list (list1):
    #Function creates a dictionary that will contain the amount of movies by genre
    #Function receives a list that contains user's entered dictionaries containing information about movies
    #Function returns the dictionary containing the amount of movies by genre
    horror_counter = 0
    action_counter = 0
    drama_counter = 0
    genre_dictionary = {}
    for dictionary in list1:
        if (dictionary["Genero"] == "Horror"):
            horror_counter += 1
        elif (dictionary["Genero"] == "Accion"):
            action_counter += 1
        elif (dictionary["Genero"] == "Drama"):
            drama_counter += 1
    genre_dictionary["Peliculas de horror"] = horror_counter
    genre_dictionary["Peliculas de accion"] = action_counter
    genre_dictionary["Peliculas de drama"] = drama_counter
    return genre_dictionary

user_list = []

while True:
    movie_title_input = input("Ingrese el titulo de la pelicula: ")
    movie_genre_input = input("Ingrese el genero de la pelicula: ")
    movie_director_input = input("Ingrese el director de la pelicula: ")
    
    dictionary = {}
    
    dictionary["Titulo"] = movie_director_input
    dictionary["Genero"] = movie_genre_input
    dictionary["Director"] = movie_director_input

    user_list.append(dictionary)

    user_choice_continue = input("Desea ingresar otro diccionario? Si es asi ingrese SI de lo contrario ingrese NO: ")
    if (user_choice_continue == "NO"):
        break

print(create_dictionary_from_list(user_list))