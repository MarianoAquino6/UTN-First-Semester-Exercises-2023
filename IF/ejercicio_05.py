# Escribir un programa que le pida al usuario que ingrese su nombre, 
# y luego imprima "Hola [nombre]" si el nombre ingresado es "Juan", "María" o "Pedro", o "Hola desconocido" 
# si el nombre ingresado no es uno de esos tres.

nombre = input("Ingrese su nombre")

if (nombre == "Juan" or nombre == "Maria" or nombre == "Pedro" or nombre == "Hola desconocido"):
    print("Hola " + nombre)