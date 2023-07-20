# Dada una lista de palabras, imprimir la palabra más larga de la lista.

strings = ["pedro", "homero", "esternocleidomastoideo"]
max_longitud = len(strings[0])

for palabra in strings:
    longitud_palabra = len(palabra)
    if (longitud_palabra > max_longitud):
        max_longitud = longitud_palabra
        palabra_mas_larga = palabra

print(palabra_mas_larga)