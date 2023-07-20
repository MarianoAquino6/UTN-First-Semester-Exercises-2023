# Dada una cadena de texto, imprimir la cadena al revés.

string = input("Ingrese una cadena de texto")
longitud_string = len(string)

contador = 0
contador_2 = longitud_string - 1  
#Necesitamos partir desde el ultimo caracter del string. El cual es equivalente a el len del string menos 1
# (Ya que el indice comienza a contar desde el numero 0). Veamos un ejemplo:
#En caso del string "hola", el len es 4, pero si se usa este len como indice ([]) buscara el 4to caracter
#de la siguiente manera H(0), O(1), L(2), A(3). El 4to caracter no existe. Por lo tanto se usa len - 1

while (longitud_string > contador):
    print(string[contador_2])
    contador_2 = contador_2 - 1
    contador = contador + 1
