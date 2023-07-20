from data_stark import lista_personajes

# 1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# 2. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
# 3. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# 4. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# 5. Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
# 6. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
# 7. Calcular e informar cual es el superhéroe más y menos pesado.

menu = " 0. Salir del sistema\n \
1. Obtener los nombres de todos los superheroes\n \
2. Obtener los nombres y altura de todos los superheroes\n \
3. Obtener superheroe mas alto\n \
4. Obtener superheroe mas bajo\n \
5. Obtener altura promedio de los superheroes\n \
6. Obtener los nombres del superheroe mas alto y el mas bajo\n \
7. Obtener los nombres de los superheroes mas y menos pesados"

print(menu)
user_choice_txt = input("Que opcion desea elegir? ")
user_choice_int = int(user_choice_txt)

def show_all_superheroes():
    for superheroe in lista_personajes:
        print(superheroe["nombre"])

def show_name_and_height():
    for superheroe in lista_personajes:
        print(f"El nombre es del superheroe es {superheroe['nombre']} y su altura es {superheroe['altura']}")

def show_tallest():
    for indice in range(len(lista_personajes)):
        altura_actual = float(lista_personajes[indice]["altura"])
        nombre_actual = lista_personajes[indice]["nombre"]
        if indice == 0 or altura_actual > altura_maxima:
            altura_maxima = altura_actual
            tallest_superhero = nombre_actual

    print(f"El superheroe mas alto es {tallest_superhero}")

def show_shortest():
    for superheroe in lista_personajes:
        if (lista_personajes.index(superheroe) == 0):
            min_height_txt = superheroe["altura"]
            min_height_float = float(min_height_txt)
            shortest_superhero = superheroe["nombre"]
        elif (float(superheroe["altura"]) < min_height_float):
            min_height_float = float(superheroe["altura"])
            shortest_superhero = superheroe["nombre"]
    print(f"El superheroe mas bajo es {shortest_superhero}")


def show_height_average():
    counter = 0
    accumulator = 0
    for superheroe in lista_personajes:
        counter += 1
        superhero_height_txt = superheroe["altura"]
        superhero_height_float = float(superhero_height_txt)
        accumulator = accumulator + superhero_height_float
    height_average = accumulator / counter
    print(f"La altura promedio es {height_average}")

def show_shortest_and_tallest():
    for superheroe in lista_personajes:
        if (lista_personajes.index(superheroe) == 0):
            max_height_txt = superheroe["altura"]
            max_height_float = float(max_height_txt)
            tallest_superhero = superheroe["nombre"]
            min_height_txt = superheroe["altura"]
            min_height_float = float(min_height_txt)
            shortest_superhero = superheroe["nombre"]
        elif (float(superheroe["altura"]) > max_height_float):
            max_height_float = float(superheroe["altura"])
            tallest_superhero = superheroe["nombre"]
        elif (float(superheroe["altura"]) < min_height_float):
            min_height_float = float(superheroe["altura"])
            shortest_superhero = superheroe["nombre"]
    print(f"El superheroe mas alto es {tallest_superhero} y el mas bajo es {shortest_superhero}")
        
def show_heaviest_and_lightest():
    for superheroe in lista_personajes:
        if (lista_personajes.index(superheroe) == 0):
            max_weight_txt = superheroe["peso"]
            max_weight_float = float(max_weight_txt)
            heaviest_superhero = superheroe["nombre"]
            min_weight_txt = superheroe["peso"]
            min_weight_float = float(min_weight_txt)
            lightest_superhero = superheroe["nombre"]
        elif (float(superheroe["peso"]) > max_weight_float):
            max_weight_float = float(superheroe["peso"])
            heaviest_superhero = superheroe["nombre"]
        elif (float(superheroe["peso"]) < min_weight_float):
            min_weight_float = float(superheroe["peso"])
            lightest_superhero = superheroe["nombre"]
    print(f"El superheroe mas pesado es {heaviest_superhero} y el mas liviano es {lightest_superhero}")

while True:
    match user_choice_int:
        case 0:         
            break
        case 1:
            show_all_superheroes()
            print(menu)
            user_choice_txt = input("Que opcion desea elegir a continuacion? ")
            user_choice_int = int(user_choice_txt)
        case 2:
            show_name_and_height()
            print(menu)
            user_choice_txt = input("Que opcion desea elegir a continuacion? ")
            user_choice_int = int(user_choice_txt)
        case 3:
            show_tallest()
            print(menu)
            user_choice_txt = input("Que opcion desea elegir a continuacion? ")
            user_choice_int = int(user_choice_txt)
        case 4:
            show_shortest()
            print(menu)
            user_choice_txt = input("Que opcion desea elegir a continuacion? ")
            user_choice_int = int(user_choice_txt)
        case 5:
            show_height_average()
            print(menu)
            user_choice_txt = input("Que opcion desea elegir a continuacion? ")
            user_choice_int = int(user_choice_txt)
        case 6:
            show_shortest_and_tallest()
            print(menu)
            user_choice_txt = input("Que opcion desea elegir a continuacion? ")
            user_choice_int = int(user_choice_txt)
        case 7:
            show_heaviest_and_lightest()
            print(menu)
            user_choice_txt = input("Que opcion desea elegir a continuacion? ")
            user_choice_int = int(user_choice_txt)