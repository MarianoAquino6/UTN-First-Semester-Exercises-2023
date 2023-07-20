# Dado un número entero n, imprimir todos los números primos menores o
# iguales a n.

numero_txt = input("Ingrese un numero entero positivo")
numero_int = int(numero_txt)
contador = 0
contador_divisibles = 0
numero_descendente = numero_int

while (numero_int >= contador):  #Incluimos el 0
    numero_txt_2 = str(numero_descendente)  #casteamos el numero descendente para por concatenar en el print
    
    contador_2 = 0
    contador_divisibles = 0
    while (numero_descendente >= contador_2):
        contador_2 = contador_2 + 1
        if (numero_descendente % contador_2 == 0):
            contador_divisibles = contador_divisibles + 1

    if (contador_divisibles == 2):
        print("Numero primo: " + numero_txt_2)
    if (numero_descendente < numero_int):
        print("Numero menor: " + numero_txt_2)
    if (numero_descendente == numero_int):
        print("Numero igual: " + numero_txt_2)
    
    numero_descendente = numero_descendente - 1
    contador = contador + 1