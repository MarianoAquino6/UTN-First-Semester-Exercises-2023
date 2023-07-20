# Crear una función que determine si un número es primo o no. Recibe un
# parámetro (número) y devuelve True si es primo y False si no lo es.

def calculate_prime_number (entered_number):
    #Function calculates if number is prime or not
    #Takes entered number as input
    #Returns the TRUE or FALSE according to the condition
    counter = 0
    divisible_counter = 0
    while (entered_number > counter):
        counter = counter + 1
        if (entered_number % counter == 0):
            divisible_counter = divisible_counter + 1
    
    if (divisible_counter == 2):
        returned_value = True
    else:
        returned_value = False
    
    return returned_value

number_txt = input("Ingrese un numero entero positivo: ")
number_int = int(number_txt)

print(f"El numero ingresado {number_int} es primo? {calculate_prime_number(number_int)}")