# Dado un número entero n, imprimir todos los números impares menores o
# iguales a n.

numero_txt = input("Ingrese un numero")
numero_int = int(numero_txt)

numero_descendente = numero_int
contador = 0

while (numero_int >= contador):  #Incluimos el 0
    calculo_impar = numero_descendente % 2
    numero_txt_2 = str(numero_descendente)  #casteamos el numero descendente para por concatenar en el print

    if (calculo_impar != 0):
        print("Numero impar: " + numero_txt_2)
    if (numero_descendente < numero_int):
        print("Numero menor: " + numero_txt_2)
    if (numero_descendente == numero_int):
        print("Numero igual: " + numero_txt_2)
    
    numero_descendente = numero_descendente - 1
    contador = contador + 1
