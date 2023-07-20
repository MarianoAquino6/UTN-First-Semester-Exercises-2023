# Dada una lista de palabras, imprimir las palabras que comienzan y terminan
# con la misma letra.

#Version Chat GPT:
lista_palabras = ["ozzy", "dio", "avantasia", "almohada"]

for palabra in lista_palabras:
    if palabra[0] == palabra[-1]:
        print(palabra)

#Version mia:
# lista_palabras = ["ozzy", "dio", "avantasia", "almohada"]

# for palabra in lista_palabras:
#     longitud_palabra = len(palabra)
#     contador = 0
#     flag_primera_letra = 0
#     for letras in palabra:
#         if (flag_primera_letra == 0):
#             primera_letra = letras
#             flag_primera_letra = 1
#         contador += 1
#         if (contador == longitud_palabra):
#             if (primera_letra == letras):
#                 print(palabra)