# Recibe un número como parámetro y devuelve True si es par o False si es
# impar.

def calculate_even_or_odd_number (entered_number):
    #Funcion calculates if number is even or odd
    #Takes entered number as input
    #Returns True or False according to the condition
    even_or_odd_calculation = entered_number % 2
    if even_or_odd_calculation == 0:
        true_or_false = True
    else:
        true_or_false = False
    return true_or_false

number_txt = input("Ingrese el numero: ")
number_int = int(number_txt)

print(calculate_even_or_odd_number(number_int))