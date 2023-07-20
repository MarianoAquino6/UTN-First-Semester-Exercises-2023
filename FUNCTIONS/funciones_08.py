# Crear una función que verifique si un número es par o impar.

def calculate_even_or_odd_number (entered_number):
    #Function calculates if number is even or odd
    #Takes entered number as input
    #Returns the rest of the entered number module 2
    even_or_odd_calculation = entered_number % 2
    return even_or_odd_calculation

number_txt = input("Ingrese el numero: ")
number_int = int(number_txt)

if (calculate_even_or_odd_number(number_int) == 0):
    print("El numero es par")
else:
    print("El numero es impar")