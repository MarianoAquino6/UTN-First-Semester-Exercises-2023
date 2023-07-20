# Escribir un programa que le pida al usuario que ingrese su edad, y luego
# imprima "Eres mayor de edad" si la edad es mayor o igual a 18, "Eres
# adolescente" si la edad está entre 13 y 17 inclusive, o "Eres menor de edad" si
# la edad es menor que 13

edad_txt = input("Ingresar la edad")
edad_int = int(edad_txt)

if (edad_int < 13):
    print("Eres menor de edad")
elif (edad_int < 18):
    print("Eres adolescente")
else:
    print("Eres mayor de edad")