# Un gimnasio desea llevar el control de sus miembros. Cada miembro tiene un número de identificación, 
# nombre, edad y tipo de membresía (por ejemplo, mensual o anual). La información se encuentra almacenada 
# en una lista de listas, donde cada sublista representa a un miembro y contiene los siguientes elementos: 
# número de identificación, nombre, edad y tipo de membresía.

continue_user = True

general_list = [ {"ID" : 1, "Nombre" : "Marian", "Edad" : 26, "Membresia" : "Mensual"},
                {"ID" : 2, "Nombre" : "Antonio", "Edad" : 41, "Membresia" : "Anual"},
                {"ID" : 3, "Nombre" : "Sandra", "Edad" : 22, "Membresia" : "Mensual"},
                {"ID" : 4, "Nombre" : "Gabriel", "Edad" : 22, "Membresia" : "Mensual"},
                {"ID" : 5, "Nombre" : "Pablo", "Edad" : 34, "Membresia" : "Anual"}]

while (continue_user == True):
    print("Menu de opciones:")
    print("1. Agregar nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresia de un miembro")
    print("4. Buscar informacion de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar al miembro mas joven y el mas viejo")
    print("0. Salir del programa")
    
    user_choice = input("Ingrese la opcion deseada")

    match user_choice:
        case "0":
            continue_user = False
        case "1":
            #Agregar un nuevo miembro: el programa debe pedir al usuario que ingrese el número de identificación, 
            #nombre, edad y tipo de membresía del nuevo miembro. La información debe ser agregada a las listas paralelas.
            
            new_id = input("Ingrese el nuevo numero de identificacion")
            new_name = input("Ingrese el nuevo nombre")
            new_age_txt = input("Ingrese la nueva edad")
            new_age_int = int(new_age_txt)
            new_membership = input("Ingrese el tipo de membresia (Mensual o Anual)")

            new_list = {"ID" : new_id, "Nombre" : new_name, "Edad" : new_age_int, "Membresia" : new_membership}

            general_list.append(new_list)

            print(f"La nueva lista es: {general_list}")

        case "2":
            #Mostrar toda la información de todos los miembros (número de identificación, nombre, edad y 
            # tipo de membresía).
            
            for item in general_list:
                for key, value in item.items():
                    print(f"La clave es {key} y el valor es {value}")

        case "3":
            #Actualizar el tipo de membresía de un miembro: el programa debe pedir al usuario que ingrese el 
            # número de identificación del miembro y el nuevo tipo de membresía. El programa debe buscar el 
            # miembro en la lista de listas y actualizar el tipo de membresía correspondiente.

            check_id_txt = input("Ingrese el numero de identificacion")
            check_id_int = int(check_id_txt)
            check_membership = input("Ingrese el tipo de membresia (Mensual o Anual)")
            
            for item in general_list:
                for key, value in item.items():
                    if (key == "ID" and value == check_id_int):
                        item["Membresia"] = check_membership
                        number_of_dictionary = item
            
            print(f"La nueva lista es: {number_of_dictionary}")

        case "4":
            #Buscar información de un miembro: el programa debe pedir al usuario que ingrese el 
            # número de identificación del miembro. El programa debe buscar el miembro en la lista de listas 
            # y mostrar su nombre, edad y tipo de membresía.
            
            check_id_txt = input("Ingrese el numero de identificacion")
            check_id_int = int(check_id_txt)

            for item in general_list:
                for key, value in item.items():
                    if (key == "ID" and value == check_id_int):
                        print(f"El nombre correspondiente es: {item['Nombre']}, La edad correspondiente es: {item['Edad']}, El tipo de membresia es: {item['Membresia']}")

        case "5":
            #Calcular el promedio de edad de los miembros: el programa debe recorrer la lista de 
            # edades y calcular el promedio de edad de los miembros.
            
            counter = 0
            accumulator = 0
            
            for item in general_list:
                counter += 1
                for key, value in item.items():
                    if (key == "Edad"):
                        accumulator = accumulator + value

            age_average = accumulator / counter

            print(f"El promedio es de: {age_average}")

        case "6":
            # Buscar el miembro más joven y el más viejo: el programa debe buscar la edad máxima y 
            # mínima en la lista de edades y mostrar el nombre y número de identificación correspondientes 
            # en las listas de nombres y números de identificación.
            
            age_flag = True
            
            for item in general_list:
                for key, value in item.items():
                    if (key == "Edad"):
                        if (age_flag == True):
                            max_age = value
                            min_age = value
                            name_youngest = item["Nombre"]
                            name_oldest = item["Nombre"]
                            id_youngest = item["ID"]
                            id_oldest = item ["ID"]
                            age_flag = False
                        elif (value > max_age):
                            max_age = value
                            name_oldest = item["Nombre"]
                            id_oldest = item["ID"]
                        elif (value < min_age):
                            min_age = value
                            name_youngest = item["Nombre"]
                            id_youngest = item["ID"]
                
            print(f"El miembro mas viejo es {name_oldest}, tiene {max_age} años y su ID es {id_oldest}")
            print(f"El miembro mas joven es {name_youngest}, tiene {min_age} y su ID es {id_youngest}")
                