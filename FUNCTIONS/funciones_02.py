# Crear una función que calcule el área de un círculo. Recibe un parámetro
# (radio) y devuelve el área del círculo.
import math

def calculate_area (ratio):
    #Function calculates circle area
    #Takes entered radio as input
    #Returns the result of the calculation
    area_calculation = math.pi * (ratio**2)
    return area_calculation

ratio_txt = input("Ingrese el radio del circulo: ")
ratio_int = int(ratio_txt)

print(f"El area del circulo es {calculate_area(ratio_int)}")