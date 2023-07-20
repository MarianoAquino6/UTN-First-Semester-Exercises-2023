# Un gimnasio desea llevar el control de sus miembros. 
# Cada miembro tiene un número de identificación, nombre, edad y tipo de membresía (por ejemplo, mensual o anual). 
# La información se encuentra almacenada en cuatro listas paralelas: una lista con los números de identificación, 
# otra lista con los nombres, una lista con las edades y una lista con los tipos de membresía.

continue_user = True

id_list = [1, 2, 3, 4, 5]
name_list = ["Marian", "Antonio", "Sandra", "Gabriel", "Pablo"]
age_list = [26, 41, 22, 22, 34]
membership_list = ["Mensual", "Anual", "Mensual", "Mensual", "Anual"]

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

            id_list.append(new_id)
            name_list.append(new_name)
            age_list.append(new_age_int)
            membership_list.append(new_membership)

            print(f"La nueva lista de id es: {id_list}")
            print(f"La nueva lista de nombres es: {name_list}")
            print(f"La nueva lista de edad es: {age_list}")
            print(f"La nueva lista de miembros es: {membership_list}")

        case "2":
            #Mostrar toda la información de todos los miembros (número de identificación, nombre, edad y 
            # tipo de membresía).

            print(id_list)
            print(name_list)
            print(age_list)
            print(membership_list)

        case "3":
            #Actualizar el tipo de membresía de un miembro: el programa debe pedir al usuario que 
            # ingrese el número de identificación del miembro y el nuevo tipo de membresía. 
            # El programa debe buscar el número de identificación en la lista de números de identificación 
            # y actualizar el tipo de membresía correspondiente en la lista de tipos de membresía. 
            # En caso de no encontrar al miembro informar con un mensaje de que el mismo no se encontró

            check_id_txt = input("Ingrese el numero de identificacion")
            check_id_int = int(check_id_txt)
            check_membership = input("Ingrese el tipo de membresia (Mensual o Anual)")
            
            for index in range(len(id_list)):
                if (check_id_int == index):
                    membership_list[index] = check_membership
                    # item_index = id_list.index(id)
                else:
                    print("No se encontro el miembro informado")
            
            print(f"La nueva lista de membresia es: {membership_list}")

        case "4":
            #Buscar información de un miembro: el programa debe pedir al usuario que ingrese el número de 
            # identificación del miembro. El programa debe buscar el número de identificación en la lista de 
            # números de identificación y mostrar el nombre, edad y tipo de membresía correspondientes en las 
            # listas de nombres, edades y tipos de membresía.

            check_id_txt = input("Ingrese el numero de identificacion")
            check_id_int = int(check_id_txt)

            for index in range(len(id_list)):
                if (check_id_int == index):
                    print(f"El nombre correspondiente es: {name_list[index]}")
                    print(f"La edad correspondiente es: {age_list[index]}")
                    print(f"La membresia correspondiente es: {membership_list[index]}")

        case "5":
            #Calcular el promedio de edad de los miembros: el programa debe recorrer la lista de 
            # edades y calcular el promedio de edad de los miembros.

            counter = 0
            accumulator = 0
            for age in age_list:
                counter += 1
                accumulator = accumulator + age
            age_average = accumulator / counter

            print(f"El promedio es de: {age_average}")

        case "6":
            # Buscar el miembro más joven y el más viejo: el programa debe buscar la edad máxima y 
            # mínima en la lista de edades y mostrar el nombre y número de identificación correspondientes 
            # en las listas de nombres y números de identificación.

            age_flag = True
            
            for index in range(len(age_list)):
                if (age_flag == True):
                    max_age = age
                    min_age = age
                    name_youngest = name_list[0]
                    name_oldest = name_list[0]
                    id_youngest = id_list[0]
                    id_oldest = id_list[0]
                    age_flag = False
                elif (age > max_age):
                    max_age = age
                    name_oldest = name_list[index]
                    id_oldest = id_list[index]
                elif (age < min_age):
                    min_age = age
                    name_youngest = name_list[index]
                    id_youngest = id_list[index]
                
            print(f"El miembro mas viejo es {name_oldest}, tiene {max_age} años y su ID es {id_oldest}")
            print(f"El miembro mas joven es {name_youngest}, tiene {min_age} y su ID es {id_youngest}")
                