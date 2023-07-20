# Escribir un programa que le pida al usuario que ingrese su nombre y su edad, 
# y luego imprima "Eres adolescente" si la edad está entre 13 y 17 inclusive, 
# "Eres adulto" si la edad está entre 18 y 64 inclusive, o "Eres adulto mayor" si la edad es mayor o igual a 65.

edad_txt = input("Ingrese su edad")
edad_int = int(edad_txt)

if (edad_int > 12 and edad_int < 18):
    print("Eres un adolescente")
elif (edad_int > 17 and edad_int < 65):
    print("Eres un adulto")
elif (edad_int > 64):
    print("Eres adulto mayor")