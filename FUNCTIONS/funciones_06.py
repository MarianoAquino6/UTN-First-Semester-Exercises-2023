# Crear una función que calcule el área de un triángulo. Recibe dos parámetros
# (base y altura) y devuelve el área.

def calculate_triangle_area (base, height):
    #Function calculates triangle area
    #Takes base and height as input
    #Returns the result of the calculation
    triangle_area_calculation = (base * height) / 2
    return triangle_area_calculation

base_txt = input("Ingrese la base del triangulo: ")
base_float = float(base_txt)
height_txt = input("Ingrese la altura del triangulo: ")
height_float = float(height_txt)

print(f"El area del triangulo es {calculate_triangle_area(base_float, height_float)}")