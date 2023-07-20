# Crea una lista vacía y pide al usuario que ingrese números enteros hasta que
# ingrese un número negativo. Luego, muestra la suma de todos los números
# ingresados.

lista = []

acumulador = 0
flag = True

while (flag == True):
    ingresar_nuevo_numero_txt = input("Ingrese su nuevo numero entero")
    ingresar_nuevo_numero_int = int(ingresar_nuevo_numero_txt)

    if (ingresar_nuevo_numero_int >= 0):
        lista.append(ingresar_nuevo_numero_int)
        acumulador = acumulador + ingresar_nuevo_numero_int
    else:
        flag = False

print(acumulador)
print(lista)