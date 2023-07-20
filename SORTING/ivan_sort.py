
import random
import time

#IVAN SORT

def ivan_sort_B(lista:list,flag_orden:bool):
    rango_a = len(lista) - 1
    flag_swap = True

    while(flag_swap):
        flag_swap = False

        for indice_A in range(rango_a):
            if  flag_orden == False and lista[indice_A] < lista[indice_A+1] \
             or flag_orden == True and lista[indice_A] > lista[indice_A+1]:
                lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                flag_swap = True

#QUICK SORT

def quick_sort(lista_original:list,flag_orden:bool)->list:
    lista_de = []
    lista_iz = []
    if(len(lista_original)<=1):
        return lista_original
    else:
        pivot = lista_original[0]
        for elemento in lista_original[1:]:
            if(elemento > pivot):
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)
    lista_iz = quick_sort(lista_iz,True)
    lista_iz.append(pivot) 
    lista_de = quick_sort(lista_de,True)
    lista_iz.extend(lista_de) 
    return lista_iz