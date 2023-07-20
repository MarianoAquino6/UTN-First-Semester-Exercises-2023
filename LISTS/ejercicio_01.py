# Crea una lista con los números del 1 al 10 e imprime solo los números
# impares.

lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista_numeros:
    calculo_par = numero % 2
    if (calculo_par != 0):
        print(numero)