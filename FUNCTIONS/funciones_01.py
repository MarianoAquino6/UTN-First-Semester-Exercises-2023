# Crear una función que convierta grados Celsius a grados Fahrenheit. Recibe
# un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.

def convert_celsius_to_fahrenheit (celsius):
    #Function converts celsius to farehnheit
    #Takes entered celsius as input
    #Returns the result of the conversion
    conversion_to_fahrenheit = (celsius*1.8) + 32
    return conversion_to_fahrenheit

celsius_txt = input("Ingrese los grados celsius a convertir: ")
celsius_float = float(celsius_txt)

print(f"El equivalente es {convert_celsius_to_fahrenheit(celsius_float)} grados Fahrenheit")