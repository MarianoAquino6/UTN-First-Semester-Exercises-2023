# Solicitar al usuario números enteros hasta que ingrese el 0. Almacenar los
# números en una lista y luego imprimir el mayor (sin utilizar la función max())

lista = []

flag = True
flag_numero_mayor = True

while (flag == True):
    nuevo_numero_txt = input("Ingrese un nuevo numero entero")
    nuevo_numero_int = int(nuevo_numero_txt)
    if (nuevo_numero_int == 0):
        flag = False
    else:
        lista.append(nuevo_numero_int)
        if (flag_numero_mayor == True):
            numero_maximo = nuevo_numero_int
            flag_numero_mayor = False
        elif (nuevo_numero_int > numero_maximo):
            numero_maximo = nuevo_numero_int

print(f"El numero maximo es {numero_maximo}")